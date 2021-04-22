from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from github import Github


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repos.db'
app.secret_key = 'v3ry_53cr3t_5tr1ng'

db = SQLAlchemy(app)
g = Github()


class ReposModel(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    repo_username = db.Column(db.String(100), nullable=False)
    repo_name = db.Column(db.String(100), nullable=False)
    repo_starcount = db.Column(db.Integer, default=0)

    def __init__(self, repo_username, repo_name, repo_starcount):
        self.repo_username = repo_username
        self.repo_name = repo_name
        self.repo_starcount = repo_starcount

    def __repr__(self):
        return '<Repo %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if not 'first_session' in session:
        ReposModel.query.delete()
        db.session.commit()
        session['first_session'] = True

    if request.method == 'POST':
        ReposModel.query.delete()
        db.session.commit()
        uname = request.form['username']

        try:
            for repository in g.get_user(uname).get_repos():
                new_repo = ReposModel(repo_username=uname, repo_name=repository.name, repo_starcount=repository.stargazers_count)
                db.session.add(new_repo)
            db.session.commit()
            return redirect('/')
        except:
            return render_template('index.html', error=True)

    else:
        repos_all = ReposModel.query.all()
        star_sum = ReposModel.query.with_entities(func.sum(ReposModel.repo_starcount)).scalar()
        return render_template('index.html', repos=repos_all, stars=star_sum)


@app.route('/sort/<int:col>', methods=['GET'])
def sort(col):
    if not 'sort_order' in session:
        session['sort_order'] = 1

    if col == 1:
        if session['sort_order'] != 2:
            repos_all = ReposModel.query.order_by(func.lower(ReposModel.repo_name).desc()).all()
            session['sort_order'] = 2
        else:
            repos_all = ReposModel.query.order_by(func.lower(ReposModel.repo_name).asc()).all()
            session['sort_order'] = 1
    else:
        if session['sort_order'] != 4:
            repos_all = ReposModel.query.order_by(ReposModel.repo_starcount.desc()).all()
            session['sort_order'] = 4
        else:
            repos_all = ReposModel.query.order_by(ReposModel.repo_starcount.asc()).all()
            session['sort_order'] = 3
    
    star_sum = ReposModel.query.with_entities(func.sum(ReposModel.repo_starcount)).scalar()
    return render_template('index.html', repos=repos_all, stars=star_sum)

if __name__ == '__main__':
    db.create_all()
    app.run()
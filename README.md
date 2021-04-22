# github-search-engine
Simple search engine, that enables searching GitHub repositories of selected users. Done using Python, Flask, HTML, CSS, JavaScript and REST API.

### Features
- searching repositories of a given GitHub user and listing them in a table along with corresponding star count
- filtering the table by *Repo Name*
- sorting the table by *Repo Name* or *Star Count*

### TODO
- [ ] expand searching options
- [ ] upgrade session side of the app
- [ ] allow users to authenticate and make changes to their repos (comment, commit etc.)
- [ ] make it look prettier

### Installation guide for Windows
1. Make sure you have Python version 3.x installed. To do so open Command Prompt and type ```python --version```. If no Python version is installed download and install [newest version](https://www.python.org/downloads/).
2. Download and install [Git](https://git-scm.com/downloads).
3. Install virtualenv by typing in the Command Prompt ```pip3 install virtualenv```.
4. Get the project repository from GitHub ```git clone https://github.com/MaciPaci/github-search-engine```.
5. Navigate to the project directory ```cd github-search-engine```.
6. Create new virtual enviroment ```py -m venv env```.
7. Activate created virtual enviroment ```.\env\Scripts\activate.bat```
8. Install required packages ```pip install -r requirements.txt```.
9. Run the app ```app.py```.
10. Go to http://127.0.0.1:5000/.

# Organization api
Minimalistic organization management app

## Installation
### Python requirements installation
Clone this repository to your local repository:<br/> 
```
https://github.com/ivanhumenyuk/organizations-back.git
```
First of all you have to install virtual environment, go to project root via cmd and execute:
```
python3.9 -m venv env
```
then
```
source env/bin/activate
```
then you have to install all dependencies. Just write 
in your console:
```
pip install requirements.txt
```

To allow and run alembic migrations type and run in a console:
```
alembic upgrade head
```
### Postgres installation
First go to https://www.postgresql.org/download/ and install postgresql >= 13.0 version. Change the user to postgres:
```
su - postgres
```
Then "organization" database:
```
createdb organizations
```
## Run api server
To run uvicorn server open the project folder path and run in console:
```
python main.py
```

## Usage
After all preparations can go to you browser and test it via Swagger UI interface.
Just put your uvicorn:
```
"http://your_host:your_port/docs"
```
example:
```
http://192.168.1.183:8000/docs
```
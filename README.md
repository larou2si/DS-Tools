# DS-Tools
Creating a Django application to include most of the tools needed in data science project. 

## Create a Virtual python3 Environment
```
make sure you have python3 installed in your operating system ?!
In lunix:
Sudo apt-get install python-virtualenv
virtualenv venv
. venv/bin/activate

In windows:
pip3 install ventualenv
virtualenv venv
venv\Scripts\activate.bat
```

## Installing Requirements
```
pip3 install -r requirements.txt

- use this command to put all python libraries used in our project
    pip3 freeze > requirements.txt
```

## Sync and Running application
```
# "python3 manage.py name_of_command"
cd data-management-solution
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
## Support
For any issue with the application, drop a message via mohamed.laroussi.1@esprit.tn

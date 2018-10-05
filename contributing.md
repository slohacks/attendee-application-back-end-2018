# SLO Hacks Attendee Application Backend Contributing Guide

**Welcome** to the attendee backend contributing guide. 

**Interested** in contributing to the backend of the attendee application

Keep reading and by the end you will know how you can contribute! 

# Our Tech

Here's what you'll need to know before contributing:

* [Django](https://www.djangoproject.com/)
* [Django REST Framework](http://www.django-rest-framework.org/)
* [PostgreSQL](https://www.postgresql.org/)

# Getting Started

So you've decided that you know our tech,

![pewds](https://media1.tenor.com/images/74bf4ac311b1965465a56473ac7682fe/tenor.gif?itemid=11698627)

1. Fork the repository and clone it to your local machine

2. Create a virtual environment in the repository's directory and activate the virtual environment

``` 
virtualenv venv

source venv/bin/activate
```
3. Install the dependencies
```
pip install -r requirements.txt
# You can also use the pip3 command to insure that you get the python3 variants of the packages
```

4. Install PostgreSQL onto your machine and setup your database. 

*For Mac users*:

 Install homebrew if it's not already installed. Then run these commands.

```
brew install postgresql
brew services start postgresql
createdb <username>
psql
```

Then follow the Digital Ocean [guide](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04#create-a-database-and-database-user) from this point on in the guide.

*For Ubuntu Users*:
 
 Follow the Digital Ocean [guide](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04#create-a-database-and-database-user) from the start.  
5. Open the activate script and set your environment variables in the the virtual environment
```
#opening the activate script
vim venv/bin/activate

#Activate Script
#find the deactivate function 
deactivate() {
    ...
    #Unset variables
    unset SECRET_KEY
    unset DB_NAME
    unset DB_USER
    unset DB_PASS
    unset DB_HOST
}
# go to the end of the activate script and set the environment variable
export SECRET_KEY = 'Please contact someone within the organization for the secret key'
export DB_NAME = 'Your db name'
export DB_USER = 'Your db username'
export DB_PASS = 'Your db password'
export DB_HOST = 'Your db host name'
```
6. Deactivate and reactivate the virtual environment so the environment variables will work
```
deactivate 
source att-app/bin/activate
```
7. Make sure to migrate the database so you have the proper endpoints
``` 
# Again you can use the python3 command to guarantee that the python3 interpreter is selected, but not necessary
python manage.py makemigrations application
python manage.py migrate
# Run the server
python manage.py runserver
```
8. Add your virtual environment directory to the bottom of the .gitignore file
```
/venv
```
9. Create a Pull Request with your changes
10. Congratulations, you contributed! 

![celebrate](https://media1.tenor.com/images/3198fe150595834238623b4da262a3eb/tenor.gif?itemid=5106342)

# Standards

Everybody has them, and here are ours: 

## Code

* Python Style Guide
    * *to be determined*

## Commits and Pull Requests

* [conventional changelog](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines)
* *Recommended:* use [commitizen](https://github.com/commitizen/cz-cli) through `git cz` when committing
    * Our repository is preconfigured to be commitizen-friendly

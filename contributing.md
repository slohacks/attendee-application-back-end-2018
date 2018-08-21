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
venv attendee-application

source attendee-application/bin/activate
```
3. Install the dependencies
```
pip install django
pip install djangorestframework
pip install psycopg2
# You can also use the pip3 command to insure that you get the python3 variants of the packages
```
4. Open the activate script of your virtual environment
```
cd attendee_application
cd bin
# Don't have to use vim to edit it, but you can use any editor to edit this script
vim activate
```
5. Set your environment variables in the activate script of the virtual environment
```
#find the deactivate function 
deactivate() {
    ...
    #Unset variables
    unset ENV_VARIABLE
}
# go to the end of the activate script and set the environment variable
export ENV_VARIABLE = 'Please use environment variables for API keys and keys in general'
```
6. Deactivate and reactivate the virtual environment so the environment variables will work
```
deactivate 
source attendee-application/bin/activate
```
7. Make sure to migrate the database so you have the proper endpoints
``` 
# Again you can use the python3 command to guarantee that the python3 interpreter is selected, but not necessary
python manage.py makemigrations application
python manage.py migrate
# Run the server
python manage.py runserver
```
8. Create a Pull Request with your changes
9. Congratulations, you contributed! 

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

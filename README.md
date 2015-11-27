# Django Bucketlist App [![Build Status](https://travis-ci.org/andela-ashuaib/django-bucketlist.svg?branch=master)](https://travis-ci.org/andela-ashuaib/django-bucketlist) [![Coverage Status](https://coveralls.io/repos/andela-ashuaib/django-bucketlist/badge.svg?branch=master&service=github)](https://coveralls.io/github/andela-ashuaib/django-bucketlist?branch=master)


This app is to keep track of the list of awesome things you would like to do before kicking the bucket


###Features
It comes with the following features:
  - Full tests
  - Responsive Design
  - Exposed API endpoints



### Technology used

Bucketlist Tracker uses a number of open source projects to work properly:

* [Django] - Django makes it easier to build better Web apps more quickly and with less code
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [Bower] - A front end javascript  manager for the web
* [Django Rest Framework] - Django REST framework is a powerful and flexible toolkit for building Web APIs
* [jQuery] - jQuery is a fast, small, and feature-rich JavaScript library


### Installation
You can go to the website here and signup for an [here](http://django-bucketlist.herokuapp.com/)

if you wish to run it locally donwload python environment from [here](https://www.python.org/downloads/)

After you're done installing python, run these following command in your terminal.
```bash
$ git clone [git@github.com:andela-ashuaib/django-bucketlist.git] bucketlist
$ cd bucketlist
$ pip install -r requirements.txt
```

Next, setup environment your secret key
```bash
$ touch .env.yml
$ echo 'SECRET_KEY="whatever-you-wish-this-to-be"'
```

Finally, run your build
```bash
$ python django_bucketlist/manage.py runserver --settings=settings.development

To run the test
```bash
$ python django_bucketlist/manage.py test django_bucketlist


### API Documentation
Django REST framework with swagger was used to document the API which can be viewed [here](http://django-bucketlist.herokuapp.com/api/v1/docs/)
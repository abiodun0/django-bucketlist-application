# Django Bucketlist App [![Build Status](https://travis-ci.org/andela-ashuaib/django-bucketlist-application.svg?branch=master)](https://travis-ci.org/andela-ashuaib/django-bucketlist-application) [![Coverage Status](https://coveralls.io/repos/andela-ashuaib/django-bucketlist-application/badge.svg?branch=master&service=github)](https://coveralls.io/github/andela-ashuaib/django-bucketlist-application?branch=master)


This app is to keep track of the list of awesome things you would like to do before kicking the bucket


###Features
It comes with the following features:
  - [Full tests](https://coveralls.io/github/andela-ashuaib/django-bucketlist-application?branch=master)
  - [Responsive Design](https://django-bucketlist.herokuapp.com)
  - [Exposed API endpoints](http://django-bucketlist.herokuapp.com/api/v1/docs/)
  - Pagination
  - Search
  - User can edit profile information



### Technology used

Bucketlist Tracker uses a number of open source projects to work properly:

* [Django](https://www.djangoproject.com/) - Django makes it easier to build better Web apps more quickly and with less code
* [Twitter Bootstrap](http://getbootstrap.com/) - great UI boilerplate for modern web apps
* [Bower](http://bower.io/) - A front end javascript  manager for the web
* [Django Rest Framework](http://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs
* [jQuery](https://jquery.com/) - jQuery is a fast, small, and feature-rich JavaScript library

### API Documentation
Django REST framework with swagger was used to document the API which can be viewed [here](http://django-bucketlist.herokuapp.com/api/v1/docs/)


### Installation
You can go to the website and signup for an accout [here](http://django-bucketlist.herokuapp.com/)

If you wish to run it locally donwload python environment from [Python official website](https://www.python.org/downloads/)

After you're done installing Python, run these following command in your terminal.
```bash
$ git clone [git@github.com:andela-ashuaib/django-bucketlist.git] bucketlist
$ cd bucketlist
$ pip install -r requirements.txt
```

Next, setup environment your secret key
```bash
$ touch .env.yml
$ echo 'SECRET_KEY="your secret keey"' > .env.yml
```

Finally, run your build
```bash
$ python django_bucketlist/manage.py runserver --settings=settings.development
```

To run the test
```bash
$ python django_bucketlist/manage.py test django_bucketlist
```



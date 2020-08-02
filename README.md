# MALICE HUNTER

![malice_hunter](https://raw.githubusercontent.com/visionarysec/RK305_BRAHMASTRA/master/Malice_Hunter.png?token=AK2HFTHILVJL3VFYH7CHYWK7FYMMY)

> This Project is the implementation of the Idea that was proposed by Bureau of Police Research and Development during the period of [SIH](https://sih.gov.in).

## Installation Guide:

- ### Prerequisite :

## Requirements

- Django v >=2.1, Python v >=3.6

# Procedure

Clone this repository and then

### First install a virtual environment to test this, using command:

```sh
    $ pip install pipenv
    $ pipenv shell
    $ pipenv lock
    $ pipenv sync
```

### Just do migration for the app from project root.

```sh
    $ python manage.py migrate
```

_Note_ - Make sure you have installed Djnago and required modules like requests or unshortenit in your virtual environment,before migrating.
If not ,then:

```sh
    $ pip install django
    $ pip install requests
    $ pip install unshortenit
```

- And you would be up and running at http://localhost:8000/

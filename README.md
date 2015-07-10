# alc-product-2

ALC Learning Management System using Django Web Framework.

## Installation (Ubuntu)
1. Install MongoDB and ensure it is running (on 127.0.0.1:27017)
2. Run `sudo apt-get install python-dev libmysqlclient-dev`
3. Run `sudo apt-get install pip` 
4. Run `pip install django mongoengine`
5. Run `python manage.py runserver` in the project root directory

## Database configurations
See alc/mongoconf.py

## Directory Structure
This is not mandatory, but this directory is based on traveloka repository architecture with some simplifications.
- `app` : front-end code: urls (routes in laravel) and views (controllers in laravel). It consist of:
  - `templates` : html template
  - use-case based folders, each consists of:
    - `views`: function to handle url request (controller)
    - `urls` : routing
- `main` : bootstrapper for django (file configurations, etc)
- other directories are domain-based name. It consists of:
  - `daos` : Data Access Object, for querying (and maybe cache) the database. Daos cannot be called from front-end.
  - `services` : function to be called from front-end. Services can call daos.
  - `models` : Object Database Mapper representation (eloquent in laravel, but this is not relational)


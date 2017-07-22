# Item Catalog

This application provides a list of items within a variety of categories as well as provides a user registration and authentication system. Registered users will have the ability to post, edit and delete their own categories and items.

Used technologies: Flask, SQLAlchemy, Google+ Authentication, Bootstrap for responsive design


# Application Usage
-----------------------
1. Navigate to project folder:

`cd /vagrant/catalog`

2. Create your own virtual environment and install dependencies from requirements.txt

```
virtualenv catalog-project
pip install -r requirements.txt
source catalog-project/bin/activate
```

3. Run database_setup.py in order to set database:

`python database_setup.py`

4. Populate database

`python catalog_populator.py`

5. Run

`python webserver.py`

6. Go to: http://localhost:8080

7. Api endpoint are:
	7.1 http://localhost:8080/all/JSON => For listing all categories
	7.2 http://localhost:8080/1/JSON => For getting all items of category with categoryid as 1
	7.3 http://localhost:8080/1/item/2/JSON  => For getting details of item with categoryid as 1 itemid as 2

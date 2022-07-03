# Django application with GraphQL API
A django application demonstrating how GraphQL APIs can be implemented in Django.

## Setup

Clone the repository
```
git clone https://github.com/ldtalent/bijitakc-graphql-multipart-postman.git
```

Create a virtual environment and activate it.
```
python -m venv env
env\scripts\activate
```

Switch to the project directory and install the requirements
```
cd bijitakc-graphql-multipart-postman
pip install -r requirements.txt
```

Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

Run the development server
```
python manage.py runserver
```
The application should be available at http://localhost:8000/graphql/

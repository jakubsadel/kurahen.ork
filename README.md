# kurahen.ork
Meme website created with Django/Django REST Framework on backend and React on frontend

## Installation

### Pre Required

- Python 3.8
- Node 14.15
- Npm 6.14.8


### 1. Clone the repository
  
  `git clone https://github.com/sondisonda/kurahen.ork`
  
### 2. Backend

Create and/or activate your Python virtual environment and install project dependencies.
To do it go to the `backend` directory via terminal with active venv and execute `pip install -r requirements.txt`.
After that you check if evrything is correct with database, execute `python manage.py makemigrations`, and next command
`python manage.py migrate`. If there is no errors you can start server with `python manage.py runserver`

### 3. Frontend

Work in proggres ...

## Use application

At this point only server is ready, but Django Rest Framework has great tool to test API.

`admin/` - Django Admin panel.

`api/memes/` - List of all memes.

`api/meme/<int:pk>/` - Meme detail, Author can also edit or delete his post.

`api/create/` - Create new meme.

`api/meme/admin/<int:pk>/` - 'Meme detail for user with admin permission to view, edite or delete post.

`api/user/register/` - New user registration.

`api/user/logout/blacklist/` - Black list endpoint.

`api-auth/login` - Login.

`api-auth/logout` - Logout.

`api/token/` - Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.

`api/token/refresh/` - Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.
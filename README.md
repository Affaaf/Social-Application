# Social-Application

Before running the app assuming that Python 3.10.8 is installed on development machine

1. Create virtual environment with Python 3.10.8
```shell
pip install virtualenv
Python 3.10.8 virtualenv env
```

2. Activate the virtual environment
```shell
 env\scripts\activate
```

3. Install required packages:
```shell
pip install -r .\requirements.txt
```

4. Run the migrations to reflect the django models to database (sqlite for test)
```shell
python manage.py makemigrations
python manage.py migrate
```

5. Run Server Locally
```shell
python manage.py runserver
```

6. Create Superuser for Admin-panel
```shell
python manage.py createsuperuser
```


7. API Documentation:

```shell

http://localhost:8000/auth/signup/ (POST) (Add New User)
http://localhost:8000/auth/login/ (POST) (Login)
http://localhost:8000/post/posttext/ (POST) (Create New Post)
http://localhost:8000/post/posttext/ (GET) (Get Post Against Login User)
http://localhost:8000/post/getallpost/ (GET) (Get all Posts)
http://localhost:8000/post/updatepost/1/ (PUT) (Update a Post Against a Login User And Send PK Of Post)
http://localhost:8000/post/deletepost/1/ (DELETE) (Delete a Post Against Login User)
http://localhost:8000/post/likepost/ (POST) (like a post)
http://localhost:8000/post/dislikepost/ (POSt) (Dislike a post)
```

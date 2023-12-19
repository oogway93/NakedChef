# NakedChef

### *__NakedChef__* is a restaurant with lots of various and delicious food.

#### Basic starting

1. Firstly, you need to make a local environment and activate it.
   ```python
   python -m venv venv
   source venv/bin/activate
2. Install packages.
   ```python
   pip install -r requirements.txt
3. Create a ".env" file at the root of the directory with params.
   ```python
   DEBUG=True or False
   SECRET_KEY='see in the Internet'
   
   # ALL SETTINGS FOR !POSTGRESQL!
   DB_USER='your postgres user'
   DB_PASS='your password for user'
   DB_NAME='your name of db'
   DB_HOST='127.0.0.1' or 'localhost'
   DB_PORT='5432'

   REDIS_HOST='127.0.0.1'
   REDIS_PORT='6379'
3. After that, do migrate to your DB.
   ```python
   python manage.py migrate
4. Finally, you can start the project with third-party tools due commands.
    ```
    python manage.py runserver or gunicorn main.wsgi --reload
    celery -A main.celery:app worker -l INFO 
    celery -A main.celery:app flower -l INFO 

> As well as, you can start tests in the project

  ```
  python manage.py test <'name_folder'> ( without (),<> and '' )
  ```

#### Docker starting

1. Create a ".env" file at the root of the directory with params.
   ```python
   DEBUG=False
   SECRET_KEY='see in the Internet'
   
   # ALL SETTINGS FOR !POSTGRESQL!
   DB_USER='your postgres user'
   DB_PASS='your password for user'
   DB_NAME='your name of db'
   DB_HOST='db'
   DB_PORT='5432'

   REDIS_HOST='redis'
   REDIS_PORT='6379'
2. Do command.
    ```
   docker compose up -d --build
3. Let's check site's pages...

> Some pictures
>
> 1. Main page
     > ![main page](https://i.imgur.com/Bcc5QXI.png)
>
> 2. Menu
     > ![menu](https://i.imgur.com/Ubl0QEM.png)
>
> 3. Registration form
     > ![registration](https://i.imgur.com/qbsVe85.png)
>
> 4. Login
>
> ![login](https://i.imgur.com/koL61oT.png)
>
> 5. Profile
>
> ![profile](https://i.imgur.com/sgE3xT5.png)
>
> 6. Shopping basket
>
> ![ordering](https://i.imgur.com/X74DzFV.png)
>
> 7. Ordering form
>
> ![ordering form](https://i.imgur.com/YFkL6vV.png)
>
> 8. Orders
>
> ![orders](https://i.imgur.com/18tIgov.png)
>
> 9. Details of order
>
> ![details](https://i.imgur.com/VuZGqLF.png)


Docker services for development
=========

The main docker-compose file has all the services to run at development

```
    docker-compose up --build
    # To build project
    
    docker-compose run --rm django python manage.py run_all_commands
    # To fill db (Country, City, Airport)
    
    docker-compose run --rm django python manage.py delete_db_models
    # Delete db (delete all countries, cities, airports)
```

Secondary commands if it necessary

```
    docker-compose run --rm django python manage.py createsuperuser
    # create django super user
    docker-compose run --rm django python manage.py migrate
    # command to run migrate
    docker-compose run --rm django python manage.py makemigrations
``` 

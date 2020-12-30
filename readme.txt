export FLASK_APP=main.py

# We start by initializing the database and enabling migrations. The generated migrations are just scripts that define the operations to be undertaken on our database. Since this is the first time, the script will just generate the DailyAgg2019 table with columns as specified in our model.
The flask db upgrade command executes the migration and creates our table.

# Pushing migrations to database.
flask db init

# Pushing migrations to database.
flask db migrate

# Pushing schema changes to database
flask db upgrade

sudo docker-compose build
sudo docker-compose run app ./run.sh
sudo docker-compose up

https://realpython.com/dockerizing-flask-with-compose-and-machine-from-localhost-to-the-cloud/
https://levelup.gitconnected.com/dockerizing-a-flask-application-with-a-postgres-database-b5e5bfc24848
https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/
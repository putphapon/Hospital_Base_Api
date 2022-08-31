# Build
```console
docker-compose build
```

# Up
``` console
docker-compose up
```
# Register init Admin username
[http://localhost:8000/init/register-admin](http://localhost:8000/api/register-admin)

# Link API
[http://localhost:8000/docs](http://localhost:8000/docs)

# Database
``` console
docker-compose exec db psql --username=postgres --dbname=postgres

\c postgres
```
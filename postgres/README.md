# postgres

## Pg in Podman
Setup
```
brew install --cask podman-desktop
python3 -m pip install --upgrade pip
python3 -m pip install podman-compose
podman machine start
```

compose.yaml
```
version: "3"
volumes:
  data:
  export:
services:
  postgres-sql-eval:
    image: docker.io/postgres:14-alpine
    container_name: postgres-sql-eval
    ports:
      - 5432:5432
    environment:
      - POSTGRES_PASSWORD=postgres
    volumes:
      - data:/var/lib/postgresql/data 
      - export:/export
```

Create volumes
```
podman volume create data
podman volume create export
podman volume ls
```

Run Pg in Podman
```
podman-compose -f ./compose.yaml up
```

### psql
Install psql
```
brew doctor
brew update
brew install libpq
brew link --force libpq
psql --version
```

Access the database
```
export POSTGRES_USERNAME=postgres
export POSTGRES_PASSWORD=postgres
export HOSTNAME=localhost
export PORT=5432
export DATABASENAME=postgres
psql postgres://${POSTGRES_USERNAME}:${POSTGRES_PASSWORD}@${HOSTNAME}:${PORT}/${DATABASENAME}
```

In psql:
```
postgres-# \dt *.*

```
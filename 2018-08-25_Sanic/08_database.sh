docker run --rm -d \
  -p 5432:5432 \
  -e POSTGRES_USER=flask \
  -e POSTGRES_PASSWORD=conf \
  -e POSTGRES_DB=sanic \
  --name pgdb \
  postgres

export PGSQL_URL=postgres://flask:conf@localhost:5432/sanic

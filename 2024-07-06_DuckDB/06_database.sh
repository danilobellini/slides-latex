docker run --rm -d \
  -p 5432:5432 \
  -e POSTGRES_USER=ducky \
  -e POSTGRES_PASSWORD=sanca \
  -e POSTGRES_DB=pyse \
  --name pgdb \
  postgres:16

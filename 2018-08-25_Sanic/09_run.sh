time sh -c ' \
  seq 10 \
  | xargs -n1 -P5 curl -sXGET "localhost:1337?input=flaskconf" -d \
  | jq -c'

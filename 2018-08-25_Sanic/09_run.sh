command='curl -s "localhost:1337?input=flaskconf"'
time sh -c "seq 10 | sed 'c $command' | xargs -d'\n' -n1 -P5 sh -c | jq -c"

#Humming bot monitor


To start the server:
```
docker-compose up --detach grafana
```

To test api:
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"hummingbot1","trades":"12"}' \
  http://localhost:5000/
```

To run client python environment
```
docker-compose run --rm client
```

To run client and parse the sqlite db
```
python client.py db.sqlite http://grafana.url bot_name
```

Crontab entry
```
*/5 * * * * /bin/python3 /root/client.py db.sqlite http://grafana.url bot_name 
```
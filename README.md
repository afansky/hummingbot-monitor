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

#!/bin/bash
#API_HOST="http://172.29.0.4:8777/"
API_HOST="http://localhost:8100/"

get=$(curl -s ${API_HOST}raw/refresco/)
for id in $(echo $get | jq -r '.[].id')
do
    echo "Deleting $id"
    curl -X DELETE ${API_HOST}raw/refresco/$id/
done


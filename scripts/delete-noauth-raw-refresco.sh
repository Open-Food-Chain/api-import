#!/bin/bash
source discord_url.txt
#API_HOST="http://172.29.0.4:8777/"
#API_HOST="http://localhost:8100/"
#API_HOST="https://austria-juice.import-api.gcp.staging.thenewfork.com/"
API_HOST="https://refresco.import-api.gcp.staging.thenewfork.com/"
ORG="R"
GREETING="**PURGING DATA**"

get=$(curl -s ${API_HOST}raw/refresco/)
for id in $(echo $get | jq -r '.[].id')
do
    echo "Deleting $id"
    curl -i -H "Accept: application/json" -H "Content-Type:application/json" -X POST --data "{\"content\": \"${GREETING}\n(id) ${id} ${ORG}\nDELETE ${API_HOST}raw/refresco/${id}\"}" ${discord_url}

    curl -X DELETE ${API_HOST}raw/refresco/$id/
done


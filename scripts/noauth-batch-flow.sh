#!/bin/bash
BATCH_ID_1=$(curl -X POST -H "Content-Type: application/json" http://localhost:8777/batch/ -d '{ "anfp": "1","dfp": "1","bnfp": "1","pds": "2020-08-05","pde": "2020-08-28","jds": 5,"jde": 28,"bbd": "2020-10-28","pc": "1","pl": "1","rmn": "1","pon": "1","pop": "1"}' | jq -r '.id')

echo $BATCH_ID_1
sleep 1


# length 34 RINVALID+26random
RANDOM_INTEGRITY_ADDRESS=RINVALID$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 26 | head -n 1)

INTEGRITY_ID_1=$(curl -X POST -H "Content-Type: application/json" http://localhost:8777/integrity/ -d "{\"integrity_address\": \"${RANDOM_INTEGRITY_ADDRESS}\", \"batch\": \"${BATCH_ID_1}\"}" | jq -r '.id')

echo $INTEGRITY_ID_1

sleep 11

RANDOM_INTEGRITY_PRE_TX=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 64 | head -n 1)

curl -X PUT -H "Content-Type: application/json" http://localhost:8777/integrity/${INTEGRITY_ID_1}/ -d "{\"integrity_address\": \"${RANDOM_INTEGRITY_ADDRESS}\", \"integrity_pre_tx\": \"${RANDOM_INTEGRITY_PRE_TX}\" }"

sleep 11

RANDOM_INTEGRITY_POST_TX=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 64 | head -n 1)

curl -X PUT -H "Content-Type: application/json" http://localhost:8777/integrity/${INTEGRITY_ID_1}/ -d "{\"integrity_address\": \"${RANDOM_INTEGRITY_ADDRESS}\", \"integrity_post_tx\": \"${RANDOM_INTEGRITY_POST_TX}\" }"

echo Done

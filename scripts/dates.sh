#!/bin/bash
PROD_RANDOM_START_DAY=$(cat /dev/urandom | tr -dc '1-2' | fold -w 2 | head -n 1)
RANDOM_1=$(cat /dev/urandom | tr -dc '1-8' | fold -w 1 | head -n 1)
PROD_END_DAY=$((PROD_RANDOM_START_DAY + RANDOM_1))
PROD_MONTH="01"
PROD_YEAR="2020"
BBD="${PROD_END_DAY}/03/2020"

echo $PROD_RANDOM_START_DAY
echo $BBD

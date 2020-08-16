#!/bin/bash
# run multiple requests

for i in $(seq $3); do
    curl localhost:8000/$1?t=$i&s=$2 &
done

# examples
# ./multirun.sh busy 5 10
# ./multirun.sh asleep 5 10
#!/bin/bash
# check status code and print body
var=$(curl -s -o /dev/null -w "%{http_code}" $1)
if [[ $var  == 200 ]]; then
        curl $1
fi

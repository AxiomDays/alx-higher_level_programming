#!/bin/bash
#prints the content length of a url
curl -s -I $1 | grep -Fi Content-Length | awk '{print $2}'

#!/bin/bash
#checking headers allow
curl -sI $1 | grep -Fi "Allow" | cut -d' ' -f 2-

#!/bin/bash

MYHOST="http://18.234.132.52:5000/systemdetail"
if curl -v $MYHOST  2>&1 | grep -w "200\|301\|302\|308" > /dev/null
then
echo "server is up"
else
/usr/bin/python3 /task/send.py
echo "server is down"
fi

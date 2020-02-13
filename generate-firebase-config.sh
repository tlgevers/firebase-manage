#!/usr/bin/env bash

echo Please enter a project ID:
read PROJECT_ID

if [ -z "$PROJECT_ID" ]
then
    echo "Please enter a project ID"
    exit 1
else
    echo "Using " $PROJECT_ID
fi

export PROJECT_ID=$PROJECT_ID

python main.py --action=getConfig

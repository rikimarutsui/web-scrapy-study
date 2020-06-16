#!/usr/bin/env bash
echo "Creating mongo users..."
mongo << EOF
use webscrapy
db.createUser({user: 'webscrapy', pwd: 'WebScrapy123', roles:[{role:'readWrite',db:'webscrapy'}]})
EOF
echo "Mongo users created."

#!/bin/bash

echo "Creating mongo users, db and collection..."
mongo < /workdir/init-mongo.js
echo "Completed."

docker-compose build
docker-compose up -d

# Install Virtual Environment
docker exec web-scrapy bash -c "cd /workdir && pipenv --python 3.7"
docker exec web-scrapy bash -c "cd /workdir && pipenv install requests beautifulsoup4 lxml pymongo"

# Install start up mongo script
#docker exec mongo-scrapy bash -c "mongo < /home/init-mongo.js"
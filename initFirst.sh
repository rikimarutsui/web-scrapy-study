
# Install Virtual Environment
docker exec web-scrapy bash -c "cd /workdir && pipenv --python 3.7"
docker exec web-scrapy bash -c "cd /workdir && pipenv install requests beautifulsoup4 lxml pymongo"
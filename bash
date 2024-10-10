docker stop flask-rss-app
docker rm flask-rss-app
docker rmi flask-rss-app

docker build -t flask-rss-app https://github.com/observatorioempleo/observatorio/
docker run -p 8080:8080 flask-rss-app

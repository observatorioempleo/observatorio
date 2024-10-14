docker stop flask-rss-app
docker rm flask-rss-app
docker rmi flask-rss-app
pip install Werkzeug==3.0.3
gunicorn wsgi:app --bind 0.0.0.0:8000
docker build -t flask-rss-app https://github.com/observatorioempleo/observatorio/
docker run -p 8080:8080 flask-rss-app

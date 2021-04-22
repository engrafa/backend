# backend
## Development
Run the server in a development environment:
  - Make sure all requirements are installed or install them with:
```
pip install -r requirements.txt
```
  - Run the server in a developement environment:
```
python server.py
```
The default developement port is *8000*.
## Dockerized
Run the server in a docker container:
```
docker build . -t yaguide-backend
docker run -p 80:80 yaguide-backend
```
## Production (without docker)
Run the server in a production environment:
  - Make sure all requirements are installed or install them with:
```
pip install -r requirements.txt
```
  - Run the server in a production environment with gunicorn:
```
gunicorn --bind 0.0.0.0:80 server:app
```
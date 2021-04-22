FROM python:3.9
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY server.py .
EXPOSE 80
CMD ["gunicorn", "--bind", "0.0.0:80", "server:app"]

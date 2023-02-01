FROM python:alpine
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY pages ./pages
COPY app.py .
CMD ["gunicorn", "--access-logfile=-", "--log-level=info", "--log-file=-", "-b", "0.0.0.0:8080", "app:app"]

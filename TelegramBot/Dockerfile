FROM python:latest

WORKDIR /app

COPY /requirements.txt .
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python3", "app.py" ]

FROM python:latest

WORKDIR /app

COPY requirements.txt .

COPY . .
EXPOSE 3421

RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT [ "python3", "manage.py","runserver","0.0.0.0:3421" ]
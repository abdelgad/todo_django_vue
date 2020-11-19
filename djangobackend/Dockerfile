FROM python:3.8
ENV PYTHONUNBUFFERED 1

WORKDIR /backend
COPY requirements.txt /backend/
# EXPOSE 8000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /backend/
# RUN python manage.py makemigrations
RUN python manage.py migrate

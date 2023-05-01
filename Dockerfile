FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_django
WORKDIR /web_django
COPY requirements.txt /web_django/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /web_django/

ENTRYPOINT ["python","manage.py","runserver","127.0.0.1:8000"]

FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

RUN apt-get update \
    && apt-get install -y lsof

RUN echo 'alias ll="ls -la --color=auto"' >> ~/.bashrc
RUN echo 'alias runserver="python manage.py runserver 0.0.0.0:8000"' >> ~/.bashrc
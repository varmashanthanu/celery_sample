FROM python:3
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install celery
RUN pip3 install redis
COPY . /app
EXPOSE 8000
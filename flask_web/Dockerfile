FROM python:3.8.3-slim-buster
RUN apt update 
RUN apt install -y procps 
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
EXPOSE 3000
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "pytho" ]


# FROM python base image
FROM python:2-alpine
MAINTAINER Practical DevSecOps

# COPY startup script
COPY . /app

WORKDIR /app

RUN apk update 
RUN apk add gcc musl-dev python-dev libffi-dev openssl-dev
RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE port 5000 for communication to/from server
EXPOSE 5000

CMD [ "python", "api/api.py" ]

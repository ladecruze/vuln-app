# FROM python base image
FROM python:3-alpine
MAINTAINER Practical DevSecOps

# COPY startup script
COPY . /app

WORKDIR /app

RUN apk update 
RUN apk add gcc musl-dev libffi-dev openssl-dev
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN python api/create-sqlite-db.py 

# EXPOSE port 5000 for communication to/from server
EXPOSE 5000

CMD [ "python", "api/api-sqlite.py" ]

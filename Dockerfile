FROM python:3.9-slim
RUN apt-get update && apt-get -y install --no-install-recommends \
    default-libmysqlclient-dev build-essential \
    python3-lxml libxml2-dev libxslt-dev \
    python3-dev \
    nginx \
  && rm -rf /var/lib/apt/lists/*

COPY requirements_prod.txt requirements_prod.txt

# variables receiving build argument values
ARG SECRET_KEY
ARG FRIBYTE_DOCKER_PASSWORD
ARG DIGAS_DB_PASSWORD
ARG PROGRAMINFO_DB_PASSWORD

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# secret keys and passwords from github action secrets
# variables with $-sign is the build argument variables
ENV SECRET_KEY=$SECRET_KEY
ENV FRIBYTE_DOCKER_PASSWORD=$FRIBYTE_DOCKER_PASSWORD
ENV DIGAS_DB_PASSWORD=$DIGAS_DB_PASSWORD
ENV PROGRAMINFO_DB_PASSWORD=$PROGRAMINFO_DB_PASSWORD

RUN pip install -r requirements_prod.txt

COPY . .

COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir /media & mkdir /media/podcast # Mount the NAS media files to this folder

EXPOSE 80
CMD ["bash", "./start.sh"]


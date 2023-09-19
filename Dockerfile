FROM python:3.9-slim
RUN apt-get update && apt-get -y install --no-install-recommends \
    default-libmysqlclient-dev build-essential \
    python3-lxml libxml2-dev libxslt-dev \
    python3-dev \
    nginx \
  && rm -rf /var/lib/apt/lists/*

COPY requirements_prod.txt requirements_prod.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements_prod.txt

COPY . .

COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir /media & mkdir /media/podcast # Mount the NAS media files to this folder

EXPOSE 80
CMD ["bash", "./start.sh"]


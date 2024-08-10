FROM python:3.12-slim

RUN apt-get update && apt-get -y install --no-install-recommends \
    default-libmysqlclient-dev \
    build-essential \
    libxml2-dev \
    libxslt-dev \
    nginx \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Create and set the working directory
WORKDIR /app

# Copy only the requirements file first to leverage Docker cache
COPY requirements_prod.txt .

# Set build arguments
ARG ENVIRONMENT

# Set environment variables
ENV ENVIRON=$ENVIRONMENT
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements_prod.txt

# Copy the rest of the application code
COPY . .

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Create media directories
RUN mkdir -p /media/podcast

# Expose port 80
EXPOSE 80

# Start the application
CMD ["bash", "./start.sh"]
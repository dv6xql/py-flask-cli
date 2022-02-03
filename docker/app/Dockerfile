FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

# Set working directory
WORKDIR /usr/src/app

# Copy project files to working directory
COPY app /usr/src/app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --editable .

CMD gunicorn -c "python:config.gunicorn" "src.app:create_app()"

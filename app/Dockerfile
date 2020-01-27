FROM python:3-alpine

WORKDIR /code

RUN apk update && apk add --no-cache \
  gcc \
  musl-dev \
  libffi-dev \
  python3-dev \
  postgresql-dev \
  linux-headers

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py", "--config-file=app.conf"]

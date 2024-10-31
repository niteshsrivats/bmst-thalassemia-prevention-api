FROM python:3.12-slim

WORKDIR /code

RUN apt-get update && \
  apt-get install -y procps wget && \
  apt-get purge -y --auto-remove && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8080"]

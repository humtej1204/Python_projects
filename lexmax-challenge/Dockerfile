FROM python:3.8.10

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip --no-cache-dir install -r package-py.txt

ENTRYPOINT python app.py

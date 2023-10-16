#FROM ubuntu:20.04
FROM python:3.11

RUN DEBIAN_FRONTEND=noninteractive

COPY requirements.txt /app/

RUN apt-get update && \
  apt-get install -y libaio1 libaio-dev curl unzip vim git less && \
  apt-get install -y pip && \
  pip install --upgrade pip && \
  pip install -r /app/requirements.txt

RUN mkdir -p ~/lib
RUN curl https://download.oracle.com/otn_software/linux/instantclient/1919000/instantclient-basiclite-linux.x64-19.19.0.0.0dbru.el9.zip -o ~/lib/instantclient-19.19.0.0.zip

RUN unzip ~/lib/instantclient-19.19.0.0.zip -d ~/lib/

WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:src"
ENTRYPOINT ["/usr/local/bin/python3", "src/ocfl_rehydration/main.py"]
#CMD ["sh", "-c", "cd /app && bash"]

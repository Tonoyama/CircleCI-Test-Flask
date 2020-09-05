FROM python:stretch

ADD requirements.txt /

RUN pip3 install --upgrade pip --no-cache-dir \
    && pip3 install -r requirements.txt --no-cache-dir

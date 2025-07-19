FROM ubuntu:22.04

RUN /bin/bash -c "apt -y update" && \
    apt -y install python3 python3-pip python3-venv \
        imagemagick-6.q16 libxml2-dev libxslt-dev vim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN cd /app && pip3 install -r requirements.txt

COPY . .

RUN sed -i 's/policy domain="coder".* pattern="PDF"/policy domain="coder" rights="read | write" pattern="PDF"/' /etc/ImageMagick-6/policy.xml

ENTRYPOINT ["/app/ctr-runner.sh"]

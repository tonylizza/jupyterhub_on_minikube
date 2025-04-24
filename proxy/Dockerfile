FROM amazonlinux:2023

RUN dnf install -y nodejs npm && \
    npm install -g configurable-http-proxy

ENTRYPOINT ["configurable-http-proxy"]

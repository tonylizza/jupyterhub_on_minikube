FROM amazonlinux:2023

RUN dnf install -y python3 git && \
    python3 -m ensurepip && \
    pip3 install --no-cache-dir jupyterhub==4.0.0 kubernetes_asyncio pycurl jupyterhub-idle-culler \
    git+https://github.com/jupyterhub/kubespawner.git && \
    useradd -m jupyter && \
    mkdir -p /srv/jupyterhub

COPY jupyterhub_config.py /srv/jupyterhub/

WORKDIR /srv/jupyterhub

CMD ["jupyterhub"]
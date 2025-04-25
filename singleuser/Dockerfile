FROM amazonlinux:2023

RUN dnf install -y \
    python3 \
    python3-pip \
    python3-devel \
    gcc \
    g++ \
    make \
    libcurl-devel \
    sqlite-devel \
    openssl-devel \
    shadow-utils && \
    python3 -m ensurepip && \
    pip3 install --no-cache-dir --upgrade pip --ignore-installed

# Copy and install dependencies

# Copy unpinned requirements and prepare pip-tools
COPY requirements.txt ./requirements.in

# Install pip-tools to resolve & lock dependencies
RUN pip3 install --no-cache-dir pip-tools && \
    pip-compile --generate-hashes requirements.in

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt --timeout 360 --retries 5 --prefer-binary

# Create a non-root user
RUN useradd -m -s /bin/bash jupyteruser

USER jupyteruser
WORKDIR /home/jupyteruser

CMD ["jupyter-lab", "--ip=0.0.0.0", "--no-browser"]
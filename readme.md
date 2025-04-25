# JupyterHub on Minikube: A Simple Example

A simple example for implementing JupyterHub in Kubernetes locally using Minikube. It uses Helm Charts from Zero to Kubernetes. There is a cheat sheet of commands to make this work in jupyter-kub-reference.md. It features dummy authentication for the moment but can be modified to use SSO.

It uses Amazon Linux 2023 as a base image, but this can be modified to use other base images. The AL2023 base images uses Python 3.9, but if an updated version is desired, it could be built and installed on the hub and singleuser docker images.

To get the modules and libraries, we are using pip-tools to take an unpinned requirements.txt and resolve and lock and dependencies.

I have implemented a self-signed certificate via Ingress, so it is possible to connect to JupyterHub https. 
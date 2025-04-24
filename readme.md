# JupyterHub on Minikube: A Simple Example

A simple example for implementing JupyterHub in Kubernetes locally using Minikube. It uses Helm Charts from Zero to Kubernetes. There is a cheat sheet of commands to make this work in jupyter-kub-reference.md. It features dummy authentication for the moment but can be modified to use SSO.

I have implemented a self-signed certificate via Ingress, so it is possible to connect to JupyterHub https. 
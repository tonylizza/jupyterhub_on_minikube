# JupyterHub on Minikube: Command Reference

A concise reference guide for working with your custom JupyterHub deployment on Minikube.

---

## 🚪 Accessing JupyterHub

**Get the login URL:**
```bash
minikube service proxy-public -n jhub --url
```
Paste the output URL into your browser to open JupyterHub.

---

## 📦 Helm Operations

**Add Helm repo for Zero to JupyterHub**
```bash
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
helm repo update
```

**Install or modify JupyterHub using the Zero to JupyterHub Helm Chart:**
```bash
helm upgrade --install jhub jupyterhub/jupyterhub \
  --namespace jhub --create-namespace -f config.yaml
```

**Uninstall JupyterHub and remove the namespace:**
```bash
helm uninstall jhub -n jhub
kubectl delete namespace jhub
```

---

## 🐳 Minikube Docker Environment

**Switch Docker to use Minikube’s internal Docker engine:**
```bash
eval $(minikube docker-env)
```

**Revert back to the host Docker engine:**
```bash
eval $(minikube docker-env -u)
```

---

## 🏗️ Building Docker Images Inside Minikube

**Build your images inside Minikube:**
```bash
docker build -t jupyterhub/jupyterhub:dev hub/
docker build -t jupyterhub/jupyter-proxy:dev proxy/
docker build -t jupyterhub/jupyter-singleuser:dev singleuser/
```

Note: You can use any names for the above docker images as long as those names are referenced in config.yaml.

> Make sure to run `eval $(minikube docker-env)` before building.

---

## 📋 Pod Management

**Check the status of all pods:**
```bash
kubectl get pods -n jhub
```

**Delete the Hub pod (to apply changes):**
```bash
kubectl delete pod -l component=hub -n jhub
```

**List all user pods:**
```bash
kubectl get pods -n jhub | grep jupyter
```

---

## 🔍 Logs & Debugging

**View logs for a specific pod:**
```bash
kubectl logs <pod-name> -n jhub
```

**Describe a pod for detailed info:**
```bash
kubectl describe pod <pod-name> -n jhub
```

---

## 🔁 Full Rebuild & Redeploy Workflow

```bash
eval $(minikube docker-env)
docker build -t jupyterhub/jupyterhub:dev hub/
helm upgrade --install jhub jupyterhub/jupyterhub \
  --namespace jhub --create-namespace -f config.yaml
kubectl delete pod -l component=hub -n jhub
```



# Ansible — Local Kubernetes Cluster
## Kind · Argo CD

Provision a local Kubernetes cluster and install Argo CD with a single Ansible command.

---

## 🏗 What this does

| Step | Role | Description |
|------|------|-------------|
| 1 | `prereqs` | Installs **kind**, **helm**, **kubectl** via Homebrew |
| 2 | `kind_cluster` | Creates a **Kind** cluster (1 control-plane + 2 workers) |
| 3 | `argocd` | Installs **Argo CD** via Helm |

---

## 🚀 Quick Start

```bash
# 1. Install Ansible collections
ansible-galaxy collection install -r requirements.yml

# 2. Run the playbook
ansible-playbook site.yml
```

---

## 🌐 Accessing Argo CD

After the playbook finishes, start a port-forward:

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:80
```

*   **URL**: http://localhost:8080
*   **Username**: `admin`
*   **Password**: printed at the end of the playbook run

---

## 🧹 Tear Down

To delete the cluster and all resources:
```bash
ansible-playbook teardown.yml
```

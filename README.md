# Ansible — Local Kubernetes Cluster
## Kind · Argo CD · Prometheus · Grafana

> Provision a fully-featured local Kubernetes cluster with a single Ansible command.

---

## 🏗 What this does

| Step | Role | Description |
|------|------|-------------|
| 1 | `prereqs` | Installs **kind**, **helm**, **kubectl** via Homebrew; waits for Docker daemon |
| 2 | `kind_cluster` | Creates a **Kind** cluster (1 control-plane + 2 workers) |
| 3 | `argocd` | Installs **Argo CD** via Helm (NodePort) and waits for all pods |
| 4 | `monitoring` | Installs **kube-prometheus-stack** (Prometheus + Grafana + Alertmanager) via Helm |

---

## 📋 Prerequisites

| Tool | Install |
|------|---------|
| macOS + [Homebrew](https://brew.sh) | Required |
| Ansible ≥ 2.14 | `brew install ansible` |
| Docker Desktop | [Download](https://www.docker.com/products/docker-desktop) — must be **running** |

---

## 🚀 Quick Start

```bash
# 1. Install Ansible collections
ansible-galaxy collection install -r requirements.yml

# 2. Run the full playbook (~10–15 min)
ansible-playbook site.yml
```

### Run individual roles with tags

```bash
ansible-playbook site.yml --tags prereqs
ansible-playbook site.yml --tags cluster
ansible-playbook site.yml --tags argocd
ansible-playbook site.yml --tags monitoring
```

---

## 🌐 Accessing Services

### Argo CD — port-forward to plain HTTP
```bash
kubectl port-forward svc/argocd-server -n argocd 8080:80
```
→ **http://localhost:8080** (no certificate warning)

| | |
|--|--|
| Username | `admin` |
| Password | printed at end of playbook run |


### Grafana
```bash
kubectl port-forward svc/kube-prometheus-stack-grafana -n monitoring 3000:80
```
→ **http://localhost:3000** · `admin` / `admin123`

### Prometheus
```bash
kubectl port-forward svc/kube-prometheus-stack-prometheus -n monitoring 9090:9090
```
→ **http://localhost:9090**

### Alertmanager
```bash
kubectl port-forward svc/kube-prometheus-stack-alertmanager -n monitoring 9093:9093
```
→ **http://localhost:9093**

---

## ⚙️ Configuration

Edit [`group_vars/all.yml`](group_vars/all.yml) to customise:

| Variable | Default | Description |
|----------|---------|-------------|
| `kind_cluster_name` | `local-k8s` | Name of the Kind cluster |
| `kind_k8s_image` | `kindest/node:v1.29.2` | Kubernetes version |
| `argocd_namespace` | `argocd` | ArgoCD namespace |
| `argocd_chart_version` | `7.1.3` | Argo CD Helm chart version |
| `monitoring_namespace` | `monitoring` | Prometheus + Grafana namespace |
| `kube_prometheus_stack_version` | `58.7.2` | kube-prometheus-stack chart version (K8s 1.29 compatible) |

---

## 🗂 Project Structure

```
ansible_kubernetes/
├── ansible.cfg
├── site.yml                               # Master playbook
├── requirements.yml                       # Ansible Galaxy collections
├── inventory/localhost.yml
├── group_vars/all.yml                     # All variables
└── roles/
    ├── prereqs/tasks/main.yml             # Install tools + wait for Docker
    ├── kind_cluster/
    │   ├── tasks/main.yml                 # Create Kind cluster
    │   └── templates/kind-config.yaml.j2
    ├── argocd/tasks/main.yml              # Install Argo CD
    └── monitoring/tasks/main.yml          # Install Prometheus + Grafana
```

---

## 🧹 Tear Down

```bash
kind delete cluster --name local-k8s
```

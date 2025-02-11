# 📄 Costa Epshtein - Resume

![GitHub Repo stars](https://img.shields.io/github/stars/CostaEp/resume?style=social)
![GitHub forks](https://img.shields.io/github/forks/CostaEp/resume?style=social)

## 🌍 About Me
🚀 **WMS PMO & DevOps Engineer** based in **Israel**

Passionate DevOps Engineer with experience in cloud infrastructure, automation, CI/CD pipelines, and cloud-native technologies. Enthusiastic about Kubernetes, Docker, Terraform, and modern DevOps practices. Adept at leading projects, optimizing workflows, and implementing scalable solutions for enterprise environments.

## 📜 Resume Format
This repository contains my resume in **YAML format**, making it easy to version control and automate updates.

📂 **Files:**
- [`resume.yaml`](resume.yaml) - Resume data
- [`template.md`](template.md) - Markdown template for resume
- [`convert.py`](convert.py) - Python script to convert YAML to Markdown
- [`.github/workflows/build-resume.yml`](.github/workflows/build-resume.yml) - GitHub Action to generate PDF

## 📥 How to Use
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/CostaEp/resume.git
cd resume
```

### 2️⃣ Convert YAML to Markdown
```sh
python3 convert.py
```
This will generate `resume.md` from `resume.yaml` using `template.md`.

### 3️⃣ Generate PDF with Pandoc
```sh
pandoc resume.md -o resume.pdf --pdf-engine=xelatex
```
This creates a PDF version of the resume.

## 🚀 Automating with GitHub Actions
This repository is integrated with **GitHub Actions**, which automatically generates `resume.pdf` when `resume.yaml` is updated.

### How It Works:
1. **On every push to `main` (or manual trigger), GitHub Action runs**
2. It **converts `resume.yaml` → `resume.md`** using Python
3. It **generates `resume.pdf`** using Pandoc
4. The PDF is **uploaded as an artifact**
5. The latest PDF version is **released in GitHub Releases**

### Manually Trigger the Workflow
You can manually trigger the workflow from GitHub Actions:
1. Go to the **"Actions"** tab in this repository.
2. Select **"Build Resume PDF"**.
3. Click **"Run workflow"**.

## 📌 Technologies & Tools
- **DevOps & Cloud:** Docker, Kubernetes, AWS, Terraform, Ansible, ArgoCD, Grafana, Jenkins, Linux
- **Programming & Scripting:** Bash, Python, Node.js, REST API, CSS, HTML, React
- **Databases:** MSSQL, MySQL, MongoDB
- **Tools:** Git, GitHub, GitLab, Postman

## 🎯 Goals
- 📜 **AWS Certified Solutions Architect (Planned for 2025)**

## 🔗 Connect with Me
- **📧 Email:** [costadevop@gmail.com](mailto:costadevop@gmail.com)
- **🔗 LinkedIn:** [linkedin.com/in/costa-epshtein-33271131](https://www.linkedin.com/in/costa-epshtein-33271131/)
- **💻 GitHub:** [github.com/CostaEp](https://github.com/CostaEp)
- **🌐 Portfolio:** [CostaEp.github.io](https://CostaEp.github.io)

---

🚀 **Feel free to fork, star ⭐, and use this template for your own DevOps resume!**

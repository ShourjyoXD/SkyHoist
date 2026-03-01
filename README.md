# ☁️ SkyHoist
**The Cloud IAM Escalation & Pathfinding Engine**

![Build Status](https://github.com/ShourjyoXD/skyhoist/actions/workflows/test.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

SkyHoist is an offensive security tool designed to identify **Identity and Access Management (IAM)** privilege escalation paths in cloud environments. It maps complex permission relationships to discover how a low-privileged user can "hoist" themselves to Administrative control.

---

## 🚀 Key Features
* **Pathfinding Engine:** Correlates multiple permissions (e.g., `iam:PassRole` + `ec2:RunInstances`) to identify attack vectors.
* **Multi-Cloud Architecture:** Designed for modular expansion (AWS supported, Azure/GCP roadmap).
* **CI/CD Integrated:** Built with automated testing and linting for reliable security operations.

## 🛠️ Installation
```bash
git clone [https://github.com/ShourjyoXD/skyhoist.git](https://github.com/ShourjyoXD/skyhoist.git)
cd skyhoist
pip install -r requirements.txt
💻 Usage
Set your environment variables and run a scan:

Bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
python -m skyhoist.cli scan --provider aws
🧠 Security Methodology
SkyHoist uses a Rules-Based Engine to look for known misconfigurations:

EC2 Role Injection: Detecting the ability to pass high-privilege roles to new compute instances.

Policy Attachment: Identifying users who can modify their own permission boundaries.

Disclaimer: This tool is for authorized security testing and educational purposes only.



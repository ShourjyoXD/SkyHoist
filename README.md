Markdown
# ☁️ SkyHoist
**The Cloud IAM Escalation & Pathfinding Engine**

![Build Status](https://github.com/ShourjyoXD/skyhoist/actions/workflows/test.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Security](https://img.shields.io/badge/IAM-Security-red.svg)

SkyHoist is an offensive security tool designed to identify **Identity and Access Management (IAM)** privilege escalation paths in cloud environments. It maps complex permission relationships to discover how a low-privileged user can "hoist" themselves to Administrative control.



---

## 🚀 Key Features
* **Modular Pathfinding Engine:** Correlates multiple permissions (e.g., `iam:PassRole` + `ec2:RunInstances`) to identify high-risk attack vectors.
* **Professional Terminal UI:** Built with `Rich` for clean, color-coded security reporting and tables.
* **Enterprise Architecture:** Separated Scanner (Data), Engine (Logic), and Output (Reporting) layers for high scalability.
* **CI/CD Integrated:** Automated testing via GitHub Actions ensures code reliability on every push.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShourjyoXD/skyhoist.git
   cd skyhoist
Install dependencies:

Bash
pip install -r requirements.txt
Install as a local package (Optional):

Bash
pip install .
💻 Usage Quick Start
Set your environment variables and run a scan against an AWS environment:

Bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1

python -m skyhoist.cli scan --provider aws
For detailed command options and authentication methods, see the Full Usage Guide.

🧠 Security Methodology
SkyHoist focuses on identifying "chains" of permissions that lead to Full Admin access. Current supported paths include:

EC2 Role Injection: Abusing iam:PassRole to inject roles into compute instances.

Self-Attachment: Identifying users with iam:AttachUserPolicy capabilities.

Version Reversion: Detecting iam:SetDefaultPolicyVersion risks.

Read more about our detection logic in the Methodology Documentation.

🧪 Development
Running tests to verify the engine:

Bash
pytest -v
⚖️ Disclaimer
SkyHoist is intended for authorized security testing, research, and educational purposes only. Unauthorized scanning of cloud infrastructure is illegal.

Maintained by [Shourjyo Chakraborty]

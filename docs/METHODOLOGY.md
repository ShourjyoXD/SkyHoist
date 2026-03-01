# SkyHoist Security Methodology

This document outlines the specific IAM privilege escalation paths that SkyHoist identifies.

## 1. EC2 Role Injection (iam:PassRole + ec2:RunInstances)
This is a common "Critical" finding. If a user has `iam:PassRole`, they can assign an existing IAM Role to a new EC2 instance. 
* **The Attack:** An attacker launches a new instance, attaches a powerful 'Administrator' role to it, and then uses SSH or Instance Connect to log in and execute commands as that Administrator.

## 2. Policy Attachment (iam:AttachUserPolicy)
If a user has the permission to attach policies to themselves, they can effectively grant themselves `AdministratorAccess`.
* **The Attack:** The attacker identifies the ARN for the managed `AdministratorAccess` policy and calls `iam.attach_user_policy()` on their own username.

## 3. Future Roadmap: Logic Expansion
Upcoming versions of SkyHoist will include:
- **GCP Service Account Impersonation**
- **Azure Service Principal Contributor abuse**
- **Visual Graphing of attack paths via Graphviz**
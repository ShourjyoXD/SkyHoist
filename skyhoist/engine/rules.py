# skyhoist/engine/rules.py

AWS_ESCALATION_RULES = [
    {
        "name": "EC2 Role Injection",
        "required_perms": ["iam:PassRole", "ec2:RunInstances"],
        "description": "User can create an EC2 instance with an Admin role attached via iam:PassRole."
    },
    {
        "name": "User Policy Attachment",
        "required_perms": ["iam:AttachUserPolicy"],
        "description": "User can attach the AdministratorAccess policy directly to their own identity."
    },
    {
        "name": "Policy Version Flip",
        "required_perms": ["iam:SetDefaultPolicyVersion"],
        "description": "User can revert to a previous, more permissive version of an IAM policy."
    }
]
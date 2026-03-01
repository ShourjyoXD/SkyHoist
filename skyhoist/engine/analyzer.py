class PathAnalyzer:
    def __init__(self):
        # These represent "Dangerous Combinations" in AWS
        self.escalation_rules = [
            {
                "name": "EC2 Role Injection",
                "required_perms": ["iam:PassRole", "ec2:RunInstances"],
                "description": "User can create an EC2 instance with an Admin role attached."
            },
            {
                "name": "User Policy Attachment",
                "required_perms": ["iam:AttachUserPolicy"],
                "description": "User can attach the AdministratorAccess policy to themselves."
            }
        ]

    def analyze(self, found_permissions):
        """Check if found permissions match any known escalation paths."""
        findings = []
        for rule in self.escalation_rules:
            # Check if all required permissions for a rule are in our found list
            if all(perm in found_permissions for perm in rule["required_perms"]):
                findings.append(rule)
        return findings
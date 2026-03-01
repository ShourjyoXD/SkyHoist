from skyhoist.engine.rules import AWS_ESCALATION_RULES

class PathAnalyzer:
    def __init__(self):
        # We load the rules from our dedicated rules file
        self.escalation_rules = AWS_ESCALATION_RULES

    def analyze(self, found_permissions):
        """
        Check if found permissions match any known escalation paths.
        Logic: Iterates through defined rules and checks for 100% permission match.
        """
        findings = []
        if not found_permissions:
            return findings

        for rule in self.escalation_rules:
            # Check if every permission required by the rule exists in found_permissions
            if all(perm in found_permissions for perm in rule["required_perms"]):
                findings.append(rule)
        
        return findings
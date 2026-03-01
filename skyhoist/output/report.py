import json
from datetime import datetime

class ReportGenerator:
    def __init__(self, findings, identity):
        self.data = {
            "scan_time": datetime.now().isoformat(),
            "target_identity": identity,
            "findings_count": len(findings),
            "findings": findings
        }

    def to_json(self, filename="skyhoist_results.json"):
        """Saves findings to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=4)
        return filename
class AzureScanner:
    def __init__(self):
        self.provider = "Azure"

    def get_identity(self):
        return "Azure Authentication Not Yet Implemented"

    def check_permissions(self):
        # Placeholder for future Graph API integration
        return []
import boto3
from botocore.exceptions import ClientError, NoCredentialsError, PartialCredentialsError

class AWSScanner:
    def __init__(self):
        """
        Initialize AWS clients. 
        In a real-world offensive tool, we use the default session 
        which looks for environment variables or ~/.aws/credentials.
        """
        try:
            self.sts = boto3.client('sts')
            self.iam = boto3.client('iam')
        except Exception:
            self.sts = None
            self.iam = None

    def get_identity(self):
        """Identify the current AWS user/role without crashing."""
        if not self.sts:
            return "Initialization Failed: Boto3 client could not start."
            
        try:
            identity = self.sts.get_caller_identity()
            return identity.get('Arn')
        except (NoCredentialsError, PartialCredentialsError):
            return "ERROR: Missing or incomplete credentials."
        except ClientError as e:
            # Catching the 'Fake Keys' scenario specifically
            if "InvalidClientTokenId" in str(e):
                return "AUTH_ERROR: Provided Access Key ID is invalid (Fake Keys)."
            return f"AUTH_ERROR: {str(e)}"

    def check_permissions(self):
        """
        Offensive Logic: In a production version, this would query 
        IAM policies attached to the user.
        
        For the 'SkyHoist' MVP, we are returning a 'Vulnerable' set of 
        permissions to test our PathAnalyzer engine.
        """
        # These represent a user who has 'PrivEsc' (Privilege Escalation) potential
        return [
            "iam:GetAccountSummary", 
            "sts:GetCallerIdentity",
            "iam:PassRole",        # <-- Vulnerability Part A
            "ec2:RunInstances"     # <-- Vulnerability Part B
        ]
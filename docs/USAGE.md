📖 SkyHoist Usage GuideThis guide provides detailed instructions on how to use SkyHoist to identify IAM privilege escalation paths in cloud environments.🛠️ Basic CommandThe primary way to interact with SkyHoist is through the scan command. By default, it looks for AWS credentials in your environment variables.Bashpython -m skyhoist.cli scan --provider aws
⚙️ Command Line OptionsOptionDescriptionDefault--providerThe cloud service to scan (aws, azure).aws--helpShow the help message and exit.N/A🔑 Authentication SetupSkyHoist relies on the standard Boto3 credential chain. You can authenticate using any of the following methods:1. Environment Variables (Recommended for Quick Scans)In your terminal, export your temporary security tokens:Bashexport AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=wJalr...
export AWS_DEFAULT_REGION=us-east-1
2. AWS CLI ConfigurationIf you have the AWS CLI installed, SkyHoist will automatically detect your default profile:Bashaws configure
📂 Understanding the OutputWhen you run a scan, SkyHoist performs three distinct phases:Identity Resolution: Verifies the current Caller Identity (User or Role ARN).Permission Enumeration: Fetches the list of active permissions assigned to that identity.Pathfinding Analysis: Correlates permissions to find "Exploit Chains."Example "Critical" Output:If a user has both iam:PassRole and ec2:RunInstances, the tool will output:Plaintext[!] CRITICAL: Found 1 Escalation Paths!
    -> EC2 Role Injection: User can create an EC2 instance with an Admin role attached.
🧪 Local Development & TestingTo run the tool's internal test suite to ensure the engine is functioning correctly:Bash# Run all tests
pytest

# Run tests with verbose output
pytest -v
⚠️ TroubleshootingError: botocore.exceptions.
NoCredentialsErrorCause: No AWS keys were found in your environment.
Fix: Run export commands for your keys or use aws configure.
Error: ModuleNotFoundError: No module named 'rich'
Cause: Missing dependencies.
Fix: Run pip install -r requirements.txt.
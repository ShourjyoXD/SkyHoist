import click
import sys
from skyhoist.scanner.aws_client import AWSScanner
from skyhoist.engine.analyzer import PathAnalyzer
from skyhoist.output.visualizer import SkyVisualizer

@click.group()
def cli():
    """SkyHoist: Cloud IAM Escalation & Pathfinding Engine"""
    # This ensures the banner prints only once at the start of any command
    SkyVisualizer.print_banner()

@cli.command()
@click.option('--provider', default='aws', help='Cloud provider to scan (default: aws)')
def scan(provider):
    """Scan the target cloud environment for privilege escalation paths."""
    
    if provider.lower() == 'aws':
        scanner = AWSScanner()
        analyzer = PathAnalyzer()
        
        # 1. Identity Check
        identity = scanner.get_identity()
        click.echo(f"[*] Current Identity: {identity}")
        
        # 2. Permission Retrieval
        perms = scanner.check_permissions()
        click.echo(f"[*] Analyzing {len(perms)} permissions against known attack patterns...")
        
        # 3. Pathfinding Analysis
        findings = analyzer.analyze(perms)
        
        # 4. Result Visualization
        SkyVisualizer.display_findings(findings)
        
    elif provider.lower() == 'azure':
        click.echo("[!] Azure support is currently in development (Roadmap v0.2.0).")
    else:
        click.echo(f"[!] Error: {provider} is an unsupported cloud provider.")
        sys.exit(1)

if __name__ == '__main__':
    cli()
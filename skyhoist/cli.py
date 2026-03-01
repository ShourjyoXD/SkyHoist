import click
from skyhoist.scanner.aws_client import AWSScanner
from skyhoist.engine.analyzer import PathAnalyzer
from skyhoist.output.visualizer import SkyVisualizer 

@click.group()
def cli():
    """SkyHoist: Cloud IAM Escalation & Pathfinding Engine"""
    SkyVisualizer.print_banner() 

@cli.command()
@click.option('--provider', default='aws')
def scan(provider):
    if provider == 'aws':
        scanner = AWSScanner()
        analyzer = PathAnalyzer()
        
        click.echo(f"[*] Authenticated as: {scanner.get_identity()}")
        
        perms = scanner.check_permissions()
        click.echo(f"[*] Analyzing {len(perms)} permissions...")
        
        findings = analyzer.analyze(perms)
        
        # Use the visualizer instead of raw text
        SkyVisualizer.display_findings(findings)
    else:
        click.echo(f"[!] {provider} is not yet supported.")

if __name__ == '__main__':
    cli()
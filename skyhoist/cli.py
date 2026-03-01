import click
from skyhoist.scanner.aws_client import AWSScanner
from skyhoist.engine.analyzer import PathAnalyzer

@click.group()
def cli():
    """SkyHoist: Cloud IAM Escalation & Pathfinding Engine"""
    pass

@cli.command()
@click.option('--provider', default='aws')
def scan(provider):
    if provider == 'aws':
        scanner = AWSScanner()
        analyzer = PathAnalyzer()
        
        click.echo(f"[*] Authenticated as: {scanner.get_identity()}")
        
        # 1. Get permissions
        perms = scanner.check_permissions()
        click.echo(f"[*] Analyzing {len(perms)} permissions...")
        
        # 2. Run the Exploit Engine
        findings = analyzer.analyze(perms)
        
        if not findings:
            click.echo("[+] No immediate escalation paths found.")
        else:
            click.echo(f"[!] CRITICAL: Found {len(findings)} Escalation Paths!")
            for f in findings:
                click.secho(f"    -> {f['name']}: {f['description']}", fg='red', bold=True)

if __name__ == '__main__':
    cli()
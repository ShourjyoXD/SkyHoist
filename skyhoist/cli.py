import click
from skyhoist.scanner.aws_client import AWSScanner

@click.group()
def cli():
    """SkyHoist: Cloud IAM Escalation & Pathfinding Engine"""
    pass

@cli.command()
@click.option('--provider', default='aws', help='Cloud provider (aws/azure)')
def scan(provider):
    """Scan the target cloud environment."""
    if provider == 'aws':
        scanner = AWSScanner()
        click.echo(f"[*] Authenticated as: {scanner.get_identity()}")
        
        perms = scanner.check_permissions()
        click.echo(f"[*] Found {len(perms)} base permissions.")
    else:
        click.echo(f"[!] {provider} is not yet supported.")

if __name__ == '__main__':
    cli()
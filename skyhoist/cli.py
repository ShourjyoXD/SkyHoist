import click

@click.group()
def cli():
    """SkyHoist: Cloud IAM Escalation & Pathfinding Engine"""
    pass

@cli.command()
@click.option('--provider', type=click.Choice(['aws', 'azure']), help='Cloud provider to scan')
def scan(provider):
    """Scan the target cloud environment for misconfigurations."""
    click.echo(f"[*] Starting SkyHoist scan on {provider.upper()}...")
    # Logic for scanning will go here soon!
    click.echo("[+] Scan complete. No paths found (yet).")

if __name__ == '__main__':
    cli()
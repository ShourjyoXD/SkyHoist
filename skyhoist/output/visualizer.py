from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

class SkyVisualizer:
    @staticmethod
    def print_banner():
        """Prints a cool ASCII-style banner."""
        banner = Panel.fit(
            "[bold cyan]SKYHOIST[/bold cyan]\n[dim]Cloud IAM Pathfinding Engine[/dim]",
            border_style="bright_blue"
        )
        console.print(banner)

    @staticmethod
    def display_findings(findings):
        """Displays findings in a clean, professional table."""
        if not findings:
            console.print("[bold green]✔ No escalation paths detected.[/bold green]")
            return

        table = Table(title="Critical Security Findings", title_style="bold red")

        table.add_column("Path Name", style="cyan", no_wrap=True)
        table.add_column("Severity", style="bold red")
        table.add_column("Description", style="white")

        for f in findings:
            table.add_row(
                f['name'],
                "CRITICAL",
                f['description']
            )

        console.print(table)
import click

from src.logs.application_log import ApplicationLog

log = ApplicationLog()


@click.command()
def cli() -> None:
    """Example script."""
    log.info('A sample script has been executed')

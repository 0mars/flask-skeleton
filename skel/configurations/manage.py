import click
from flask.cli import FlaskGroup

from skel.configurations.app import create_app


def create_skel(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_skel)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Initialize the app
    """
    click.echo("initialized app")


if __name__ == "__main__":
    cli()

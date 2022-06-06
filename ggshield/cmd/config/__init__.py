import click

from .config_get import config_get_command
from .config_list import config_list_cmd
from .config_set import config_set_command
from .config_unset import config_unset_command
from .config_update import config_update_cmd


@click.group(
    commands={
        "list": config_list_cmd,
        "set": config_set_command,
        "unset": config_unset_command,
        "get": config_get_command,
        "update": config_update_cmd,
    }
)
def config_group() -> None:
    """Commands to manage configuration."""

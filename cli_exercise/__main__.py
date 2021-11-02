"""CLI Exercise - Main script."""
import argparse
import sys

from cli_exercise.user import get_user_info
from cli_exercise.namespace import list_namespaces
from cli_exercise.repository import list_repositories
from cli_exercise.package import list_packages

COMMANDS = {
    'get_user_info': {
        'function': get_user_info,
        'args': []
    },
    'list_namespaces': {
        'function': list_namespaces,
        'args': []
    },
    'list_repositories': {
        'function': list_repositories,
        'args': [],
    },
    'list_packages': {
        'function': list_packages,
        'args': []
    }
}

parser = argparse.ArgumentParser(description="Interact with the Cloudsmith API.")
parser.add_argument('command', type=str, nargs='?', help='The command you wish to run.', default=None)

def main():
    args = parser.parse_args()
    function = COMMANDS.get(args.command, {}).get('function')
    if function is None:
        print(f"Please enter a valid command: {', '.join(COMMANDS)}")
        return 1

    function()

    return 0


if __name__ == "__main__":
    sys.exit(main())

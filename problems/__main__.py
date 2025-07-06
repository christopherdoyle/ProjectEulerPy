"""Main entry point for 'python -m problems' command which
dynamically imports the specified problem module and executes
its main function via the CLI interface.
"""

import argparse
from problems.lib import cli


parser = argparse.ArgumentParser(
    description="Project Euler Problem Solutions",
    epilog="For more information, visit https://projecteuler.net/",
)
parser.add_argument(
    "problem", type=int, help="Problem number to solve (e.g., 1, 2, 3, ...)"
)

parsed_args = parser.parse_args()
problem_number = parsed_args.problem

module_name = f"problems.problem{problem_number}"
__import__(module_name, fromlist=["main"])
cli(module_name)

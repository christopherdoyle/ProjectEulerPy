"""Main entry point for 'python -m problems' command which
dynamically imports the specified problem module and executes
its main function via the CLI interface.
"""

import argparse
import logging
from problems.lib import cli


parser = argparse.ArgumentParser(
    description="Project Euler Problem Solutions",
    epilog="For more information, visit https://projecteuler.net/",
)
parser.add_argument(
    "problem", type=int, help="Problem number to solve (e.g., 1, 2, 3, ...)"
)
parser.add_argument("-v", "--verbose", action="store_true")

parsed_args = parser.parse_args()
problem_number: int = parsed_args.problem
verbose: bool = parsed_args.verbose

module_name = f"problems.problem{problem_number:04d}"
__import__(module_name, fromlist=["main"])

# the verbose flag modulates the verbosity of just the imported
# module, because that is what I want
if verbose:
    logging.getLogger(module_name).setLevel(logging.DEBUG)
else:
    logging.getLogger(module_name).setLevel(logging.INFO)

cli(module_name)

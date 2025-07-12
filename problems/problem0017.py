import logging

from problems.lib import cli, main_wrapper, num_format

logger = logging.getLogger(__name__)


@main_wrapper
def main():
    total_length = 0
    for n in range(1, 1000 + 1):
        human_n = num_format.number_to_human_words(n)
        logger.info("Converted %d to '%s'", n, human_n)
        # discard spaces and hyphens from the count
        human_n = human_n.replace(" ", "").replace("-", "")
        total_length += len(human_n)
    return total_length


if __name__ == "__main__":
    cli()

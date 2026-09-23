import logging


def setup_logging() -> None:
    """
    Configure application-wide logging.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a logger for a specific module.
    """

    return logging.getLogger(name)
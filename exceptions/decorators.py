import logging


def logged(exception, mode, file='file.txt'):
    """
    Decorator that logs exceptions.

    Args:
        exception (Exception): The specific exception to catch and log.
        mode (str): The logging mode, either 'console' or 'file'.
        file (str): The name of the file to which exceptions will be logged (only used when mode is 'file').
                    Defaults to 'file.txt'.

    Returns:
        function: The decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == 'console':
                    logging.basicConfig(level=logging.INFO)
                elif mode == 'file':
                    logging.basicConfig(filename=file, filemode='a', level=logging.INFO)
                logging.exception(e)

        return wrapper

    return decorator

import logging

class Logger:
    """
    Class to manage logging configuration and provide logger instances.
    """
    _logger = None

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        """
        Create and configure a logger instance with a given name.
        Logs will include the timestamp, log level, logger name, and message.
        
        :param name: Name of the logger (typically module or function name)
        :return: logger instance
        """
        if cls._logger is None:
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s \t %(levelname)s \t %(name)s \t %(message)s",
                handlers=[
                    logging.StreamHandler(),
                ]
            )
            cls._logger = logging.getLogger('Root')

        logger = logging.getLogger(name)
        return logger

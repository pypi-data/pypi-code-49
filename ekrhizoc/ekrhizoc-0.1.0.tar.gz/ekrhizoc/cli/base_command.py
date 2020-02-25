from argparse import ArgumentParser, Namespace

from ekrhizoc.logging import logger


class BaseCommand:
    def __init__(self):
        self._name = ""

    @property
    def name(self) -> str:
        """Getter for name attribute.

        If no name is set, use the module's name.

        Returns:
            The value of the name attribute.
        """
        if "".__eq__(self._name):
            return self.__module__.split(".")[-1].replace("_", "-")
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Setter for name attribute.

        Args:
            value: The value to set the name attribute.
        """
        self._name = value

    def run(self, args: Namespace) -> None:
        """Entrypoint for a CLI command.

        Args:
            args: The Namespace object for the subcommand.
        """
        logger.debug(f"Validate arguments: {args}")
        self.validate_args(args)
        logger.debug(f"Execute command with arguments: {args}")
        self._execute(args)

    def add_args(self, parser: ArgumentParser) -> None:
        """Add custom subcommand arguments to the parser.

        Args:
            parser: The ArgumentParser object of the subcommand.

        Raises:
            NotImplementedError: If this method is used but not
                defined in the subcommand class.
        """
        raise NotImplementedError(
            f"Method: add_args is undefined for command {self.name}"
        )

    def validate_args(self, args: Namespace) -> None:
        """Validate the provided arguments to the parser.

        Args:
            args: The Namespace object for the subcommand.

        Raises:
            NotImplementedError: If this method is used but not
                defined in the subcommand class.
        """
        raise NotImplementedError(
            f"Method: validate_args is undefined for command {self.name}"
        )

    def _execute(self, args: Namespace) -> None:
        """Internal function to run command's execute safely.
        
        Args:
            args: The Namespace object for the subcommand.

        Raises:
            Exception: If any exception is raised.
        """
        try:
            self.execute(args)
        except Exception as e:
            logger.critical(e)
            raise SystemError(e)

    def execute(self, args: Namespace) -> None:
        """Logic of CLI command.

        Args:
            args: The Namespace object for the subcommand.
        
        Raises:
            NotImplementedError: If this method is used but not
                defined in the subcommand class.
        """
        raise NotImplementedError(
            f"Method: execute is undefined for command {self.name}"
        )

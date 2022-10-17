"""The Greeting Generator."""


def greeting(name: str) -> str:
    """
    Give the text of greeting.

    Args:
        name (str): The name of the user.

    Returns:
        return_greeting (str): The text of the greeting.
    """
    return 'Привет, {0}'.format(name.title())

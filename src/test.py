def say_message(message: str = "Hello, World!") -> str:
    """
    Function to print a message.
    Args:
        message (str): The message to print. Defaults to "Hello, World!".
    Returns:
        str: The message that was printed.
    """
    # Print the message
    print(message)
    return message


if __name__ == "__main__":
    say_message()

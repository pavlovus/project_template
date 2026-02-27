def output_to_console(message: str) -> None:
    """
    Print a message to the console.
    Args: message (str): Text to print.
    Returns: None
    """
    print(message)

def output_to_file(message: str, path: str) -> None:
    """
    Write a message to a file.
    Args: message (str): Text to write, path (str): Path to the output file.
    Returns: None
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(message)
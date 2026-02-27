import pandas as pd

def input_from_console(message: str) -> str:
    """
    Read input from the console.
    Args:message (str): Prompt message displayed to the user.
    Returns: str: User input as a string.
    """
    return input(message)

def input_from_file(path: str) -> str:
    """
    Read the entire contents of a text file.
    Args: path (str): Path to the file.
    Returns: str: Full file content as a single string.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def input_from_file_with_pandas (path: str) -> str:
    """
    Read the entire contents of a text file using pandas.
    Args: path (str): Path to the file.
    Returns: str: Full file content reconstructed as a single string.
    """
    df = pd.read_csv(path, header=None)
    return "\n".join(df[0].astype(str))
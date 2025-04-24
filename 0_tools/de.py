def replace_multiple(text, char_map):
    """
    Replace multiple characters in a string based on a character mapping.

    This function performs multiple character substitutions on a text at the same time.

    Args:
        text (str): The input string to perform substitutions on.
        char_map (dict): A dictionary mapping characters to their replacements.
                         Keys are characters to replace, values are their replacements.

    Returns:
        str: A new string with all specified substitutions applied.

    Example:
        >>> text = "Hello, World!"
        >>> mapping = {'H': 'J', 'o': '0', 'l': '1'}
        >>> replace_multiple(text, mapping)
        'Je110, W0r1d!'
    """
    table = str.maketrans(char_map)
    return text.translate(table)

#some tools here:
#1.return char mod 26
def idx(char):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return alpha.index(char)

#2.handle with the original input
def handle(text):
    text = text.lower()
    text = text.replace(" ","")
    return text
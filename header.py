"""
This package will help you print nifty console application headers.
It is inspired by TalkPython.fm Python Jumpstart Course.

Usage:
import header

print(header.header())

Defaults values:
    - text = "APPLICATION HEADER",
    - text_color = "none",
    - text_background_color = "none",
    - width = 32,
    - height = 3,
    - decorative_pattern = "-",
    - decorative_pattern_color = "none",
    - decorative_pattern_background_color = "none",
    - align = "center",
text
    - Must be a valid string
text_color
    - Can be "black", "red", "green", "yellow", "blue", "magenta", "cyan",  "white"
text_background_color
    - Can be "black", "red", "green", "yellow", "blue", "magenta", "cyan",  "white"
width
    - Must be an integer larger than the length of the text string
    - Minimum value: length of text string + 2 characters for padding
    - Maximum value: None enforced, 132 characters suggested
height
    - Ideally an odd integer to have the text centered vertically
    - Minimum value: 1
    - Maximum value: 9
decorative_pattern
    - Can be a single character or a sequence ofcharacters
    - If sequence is lesser than the width, it will be repeated to span the width
    - If the sequence is longer than the width it will be truncated at the width
decorative_pattern_color
    - Can be "black", "red", "green", "yellow", "blue", "magenta", "cyan",  "white"
decorative_pattern_background_color
    - Can be "black", "red", "green", "yellow", "blue", "magenta", "cyan",  "white"
align
    - Can be "left", "center", "right"

"""


from platform import system

if system() == "Windows":
    from colorama import init

    init()


def header(
    text: str = "APPLICATION HEADER",
    *,
    text_color: str = "none",
    text_background_color: str = "none",
    width: int = 32,
    height: int = 3,
    decorative_pattern: str = "-",
    decorative_pattern_color: str = "none",
    decorative_pattern_background_color: str = "none",
    align: str = "center",
) -> str:

    """
    CLI application header formatter.

    Defaults values:
        - text = "APPLICATION HEADER",
        - text_color = "none",
        - text_background_color = "none",
        - width = 32,
        - height = 3,
        - decorative_pattern = "-",
        - decorative_pattern_color = "none",
        - decorative_pattern_background_color = "none",
        - align = "center",
    text
        - Must be a valid string
    text_color
        - Can be "black", "red", "green", "yellow", "blue", "magenta", "cyan",  "white"
    text_background_color
        - Can be "black", "red", "green", "yellow", "blue", "magenta", "cyan",  "white"
    width
        - Must be an integer larger than the length of the text string
        - Minimum value: length of text string + 2 characters for padding
        - Maximum value: None enforced, 132 characters suggested
    height
        - Ideally an odd integer to have the text centered vertically
        - Minimum value: 1
        - Maximum value: 9
    decorative_pattern
        - Can be a single character or a sequence ofcharacters
        - If sequence is lesser than the width, it will be repeated to span the width
        - If the sequence is longer than the width it will be truncated at the width
    decorative_pattern_color
        - Can be "black", "red", "green", "yellow", "blue", "magenta", "cyan",  "white"
    decorative_pattern_background_color
        - Can be "black", "red", "green", "yellow", "blue", "magenta", "cyan",  "white"
    align
        - Can be "left", "center", "right"
    """

    # To match color to escape code
    color_table = {
        "none": "",
        "black": "\033[30",
        "red": "\033[31",
        "green": "\033[32",
        "yellow": "\033[33",
        "blue": "\033[34",
        "magenta": "\033[35",
        "cyan": "\033[36",
        "white": "\033[37",
        "reset": "\033[39",
    }

    background_color_table = {
        "none": "",
        "black": ";40m",
        "red": ";41m",
        "green": ";42m",
        "yellow": ";43m",
        "blue": ";44m",
        "magenta": ";45m",
        "cyan": ";46m",
        "white": ";47m",
        "reset": ";49m",
    }

    # TODO - Validate input - with try except blocks?
    # To set default and enforce limits
    text = str(text)
    text_color = color_table[str.lower(text_color)]
    text_background_color = background_color_table[str.lower(text_background_color)]
    width = int(width)
    height = int(height)
    decorative_pattern = str(decorative_pattern)
    decorative_pattern_color = color_table[str.lower(decorative_pattern_color)]
    decorative_pattern_background_color = background_color_table[
        str.lower(decorative_pattern_background_color)
    ]
    align = str.lower(align)

    # To match the width to the length of the text string plus 2 characters of padding
    if (width + 2) < len(text):
        width = len(text) + 2

    # To cap height at 9 and to remove the center line which will hold the text
    height = max(1, min(height, 9)) - 1

    # To center text vertically and to place single line at bottom
    top = round(height / 2)
    bottom = height - round(height / 2)

    # To default to "center"
    valid_alignements = "left", " center", "right"
    if align not in valid_alignements:
        align = "center"

    # To trim the string to the proper width
    decorative_string = int(width / len(decorative_pattern)) * decorative_pattern

    if 2 * int(width / len(decorative_pattern)) < width:
        decorative_string = (decorative_string + decorative_pattern)[0:width]

    # To add color theme to string
    decorative_string = (
        decorative_pattern_color
        + decorative_pattern_background_color
        + decorative_string
        + color_table["reset"]
        + background_color_table["reset"]
    )

    # To align text
    aligned_text = text_color + text_background_color

    if align == "left":
        aligned_text += " " + text + (width - 1 - len(text)) * " "
    if align == "center":
        aligned_text += text.center(width, " ")
    if align == "right":
        aligned_text += (width - 1 - len(text)) * " " + text + " "

    # To reset the colors, otherwise the entire line is colored
    aligned_text += color_table["reset"] + background_color_table["reset"]

    # On with the show!
    return (
        top * (decorative_string + "\n")
        + aligned_text
        + "\n"
        + bottom * (decorative_string + "\n")
    )


def main():

    # Print header with default values
    print(header())

    # Print a custom header to show off some of the features
    print(
        header(
            "PYTHON.ORG",
            text_color="green",
            text_background_color="black",
            width=48,
            decorative_pattern="-=",
            decorative_pattern_color="black",
            decorative_pattern_background_color="green",
            align="left",
        )
    )

    # Print the ultimate show off demo scene style header!
    print(
        header(
            "░TALKPYTHON.FM░",
            text_color="blue",
            text_background_color="yellow",
            width=64,
            height=5,
            decorative_pattern="   ░░▒▒▓▓███▓▓▒▒░░   ",
            decorative_pattern_color="magenta",
            decorative_pattern_background_color="blue",
            align="center",
        )
    )


if __name__ == "__main__":
    main()

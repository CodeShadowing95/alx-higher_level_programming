#!/usr/bin/python3
"""
doctest_text_indentation

Print a text with 2 new lines after each of these characters: . and ? and :

>>> text_indentation("Lorem ipsum. Dolor sit amet")
Lorem ipsum

Dolor sit amet
"""


def text_indentation(text):
    """Return a text with 2 new lines after the characters ., ? and :

    Params:
        text: string

    Raises:
        TypeError if text is not a string
    """
    c = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in ".?:":
            print(i, end="")
            c = 1
        elif c == 1 and i == " ":
            print("\n")
            c = 0
        else:
            print(i, end="")

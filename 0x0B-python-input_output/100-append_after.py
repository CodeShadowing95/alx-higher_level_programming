#!/usr/bin/python3
"""Definition of the function append_after()"""


def append_after(filename="", search_string="", new_string=""):
    """insert a line of text to a file, after each line containing
    a specific string

    Args:
        filename: file to operate on
        search_string: string to search in the lines of the file
        new_string: string to add after the first occurrence of search_string
    """
    with open(filename, 'r', encoding='UTF-8') as f:
        datas = f.readlines()

    new_datas = []
    for i in range(len(datas)):
        if search_string in datas[i]:
            new_datas.append(datas[i])
            new_datas.append(new_string)
        else:
            new_datas.append(datas[i])

    with open(filename, 'w', encoding='UTF-8') as f:
        f.writelines(new_datas)

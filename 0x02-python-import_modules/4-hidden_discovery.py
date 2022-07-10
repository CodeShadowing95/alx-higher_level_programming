#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    tab = dir(hidden_4)
    for module in tab:
        if module[0] + module[1] != "__":
            print(module)

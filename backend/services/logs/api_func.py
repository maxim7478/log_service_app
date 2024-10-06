def tail_file(file_path, lines):
    with open(file_path, 'r', encoding='UTF-8') as file:
        arr = file.readlines()[-lines:]
        return arr[::-1]
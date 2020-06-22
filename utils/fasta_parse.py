def parse(filename: str) -> dict:
    # taken from src/gc.py
    lines = []
    parsed = dict()
    with open(filename, "r") as f:
        lines = [i.strip() for i in f.readlines()]
    identifier = ""
    content = ""
    for line in lines:
        if line[0] == '>':
            if identifier:
                parsed[identifier] = content
            content = ""
            identifier = line[1:]
        else:
            content += line
    parsed[identifier] = content
    return parsed

print(parse("utils/test.txt"))
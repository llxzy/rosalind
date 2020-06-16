def gc_content(s: str) -> float:
    return ((s.count('C') + s.count('G')) / len(s)) * 100


def parse(filename: str):
    # requires file input
    lines = []
    parsed = dict()
    with open(filename, "r") as f:
        lines = [i.strip() for i in f.readlines()]
    identifier = ""
    content = ""
    for line in lines:
        if line[0] == '>':
            if identifier:
                parsed[identifier] = gc_content(content)
            content = ""
            identifier = line[1:]
        else:
            content += line
    parsed[identifier] = gc_content(content)
    max_val = max(parsed.values())
    for k, v in parsed.items():
        if v == max_val:
            return f"{k}\n{v}"




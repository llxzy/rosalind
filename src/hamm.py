def identical_tuple(tpl):
    if (len(tpl) != 2):
        raise ValueError("Wrong sized tuple")
    return tpl[0] == tpl[1]

def hamming(strone: str, strtwo: str) -> int:
    return len([x for x in zip(strone, strtwo) if not identical_tuple(x)])

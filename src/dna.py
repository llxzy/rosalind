# simple function to count the number of occurences for each strand
# raises value error if another char is present in the string

def count_nucleotides(s : str):
    strain_count = {'A': 0, 'G': 0, 'C': 0, 'T': 0}
    for c in s:
        if c not in ['A', 'C', 'G', 'T']:
            raise ValueError("Wrong characters in input string")
        strain_count[c] += 1
    return f"{strain_count['A']} {strain_count['C']} {strain_count['G']} {strain_count['T']}"

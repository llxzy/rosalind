STOPS = ["UAA", "UAG", "UGA"]
CODON_TABLE = {
    "UUU" : 'F',
    "UUC" : 'F',
    "UUA" : 'L',
    "UUG" : 'L',
    "UCU" : 'S',
    "UCC" : 'S',
    "UCA" : 'S',
    "UCG" : 'S',
    "UAU" : 'Y',
    "UAC" : 'Y',
    "UGU" : 'C',
    "UGC" : 'C',
    "UGG" : 'W',
    "CUU" : 'L',
    "CUC" : 'L',
    "CUA" : 'L',
    "CUG" : 'L',
    "CCU" : 'P',
    "CCC" : 'P',
    "CCA" : 'P',
    "CCG" : 'P',
    "CAU" : 'H',
    "CAC" : 'H',
    "CAA" : 'Q',
    "CAG" : 'Q',
    "CGU" : 'R',
    "CGC" : 'R',
    "CGA" : 'R',
    "CGG" : 'R',
    "AUU" : 'I',
    "AUC" : 'I',
    "AUA" : 'I',
    "AUG" : 'M',
    "ACU" : 'T',
    "ACC" : 'T',
    "ACA" : 'T',
    "ACG" : 'T',
    "AAU" : 'N',
    "AAC" : 'N',
    "AAA" : 'K',
    "AAG" : 'K',
    "AGU" : 'S',
    "AGC" : 'S',
    "AGA" : 'R',
    "AGG" : 'R',
    "GUU" : 'V',
    "GUC" : 'V',
    "GUA" : 'V',
    "GUG" : 'V',
    "GCU" : 'A',
    "GCC" : 'A',
    "GCA" : 'A',
    "GCG" : 'A',
    "GAU" : 'D',
    "GAC" : 'D',
    "GAA" : 'E',
    "GAG" : 'E',
    "GGU" : 'G',
    "GGC" : 'G',
    "GGA" : 'G',
    "GGG" : 'G'
}

# takes an RNA string, returns protein
# RNA string corresponds to a strand of mRNA
def rna_to_protein(rna_string : str) -> str:
    protein_str = substr = ""
    for i in range(len(rna_string)):
        if i % 3 == 0 and i != 0:
            if substr in STOPS:
                return protein_str
            else:
                protein_str += CODON_TABLE[substr]
                substr = rna_string[i]
        else:
            substr += rna_string[i]
    return protein_str

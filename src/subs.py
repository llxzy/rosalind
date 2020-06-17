def dna_substring(s: str, t: str) -> [int]:
    # i + 1 because of indexing
    return [i+1 for i in range(len(s)) if s[i:i+len(t)] == t]

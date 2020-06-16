-- DNA to RNA conversion is done by replacing 'T' by 'U' symbols in the DNA string

replace :: Char -> Char
replace 'T' = 'U'
replace  x  =  x

dna_to_rna :: String -> String
dna_to_rna = map replace

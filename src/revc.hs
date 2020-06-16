-- 'A' and 'T' are complements, so are 'G' and 'C'
-- creating a reverse complement of a DNA string is done by
-- reversing the string and then replacing every symbol by its complement

complement :: Char -> Char
complement 'A' = 'T'
complement 'T' = 'A'
complement 'C' = 'G'
complement 'G' = 'C'
complement  x  =  x

complement_strand :: String -> String
complement_strand = (map complement) . reverse
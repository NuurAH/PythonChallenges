codon_table = {
    "F" : ("TTT","TTC"),
    "L" : ("TTA", "TTG", "CTT", "CTA", "CTG" ),
    "I" : ("ATT", "ATC", "ATA"),
    "M" : "ATG",
    "V" : ("GTT", "GTC", "GTG"),
    "S" : ("TCT", "TCC", "TCA", "TCG", "AGT", "AGC"),
    "P" : ("CCT", "CCC", "CCA", "CCG"),
    "T" : ("ACT", "ACC", "ACA", "ACG"),
    "A" : ("GCT", "GCC", "GCA", "GCG"),
    "Y" : ("TAT", "TAC"),
    "*" : ("TAA", "TAG", "TGA"),
    "H" : ("CAT", "CAC"),
    "Q" : ("CAA", "CAG"),
    "N" : ("AAT", "AAC"),
    "K" : ("AAA", "AAG"),
    "D" : ("GAT", "GAC"),
    "E" : ("GAA", "GAG"),
    "C" : ("TGT", "TGC"),
    "W" : "TGG",
    "R" : ("CGT", "CGC", "CGA", "CGG", "AGA", "AGG" ),
    "G" : ("GGT", "GGC", "GGA", "GGG" )
}
#variables (the usual suspects)
dna = "aggagtaagcccttgcaactggaaatacacccattg"
dna_length = len(dna)
block_size = 3
blocking = 3
start = 0
dna_list = []

while start < dna_length :
   dna_list.append(dna[start:blocking]) 
   start += block_size
   blocking += block_size

split_dna = ""
for _ in dna_list:
   split_dna += (" " + (_) + " ") 
#printing
formatted_dna = split_dna.strip()
print(formatted_dna)

#need to convert split dna into values


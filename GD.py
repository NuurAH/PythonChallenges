#variable list
dna = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
dna_length = len(dna)
block_size = 10
blocking = 10
start = 0
print (dna_length)
dna_list = []
#loops
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

dna = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGXGGGTTTCTCAGATAACTGGGCCXCCTGCGCTCAGGAGGCCTTCACCCTCXTGCTCTGGGTAAAGTTCAXTTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"

reverse_dna = dna[::-1]
dna_length = len(dna)
c_list = list(dna)
start = 0
dna_list = []
complement_list = []
complement = 0
complement_table = {
    "a" : "t",
    "t" : "a",
    "g" : "c",
    "c" : "g",
    "A" : "T",
    "T" : "A",
    "G" : "C",
    "C" : "G"
}

#repurposing the function to look through the last string value in the DNA to look through the complement table
def reverse_complement(nucleotide):
    if nucleotide in complement_table:
        return nucleotide
    else:
        print("This is not a base" + " " + nucleotide)
        return ""

#remade the while loop so that it is more efficient, went from outputting 8x the wrong value (dummy nucleotides not in the dictionary) to outputting the exact amount
while start < dna_length:
    dna_list.append(dna[start])
    complement = reverse_complement(dna_list[-1])
    for key, value in complement_table.items():
        if complement in value :
            complement_list.append(key)
    start+=1
 #Reversing the string   
    complement_output = ""
for x in complement_list:
    complement_output += x


print(complement_output[::-1])


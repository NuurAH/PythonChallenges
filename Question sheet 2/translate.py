codon_table = {
    "F" : "TTT",
    "F" : "TTC",
    "L" : "TTA",
    "L" : "TTG", 
    "L" : "CTT", 
    "L" : "CTA",
    "L" : "CTG" ,
    "I" : "ATT",
    "I" : "ATC",
    "I" : "ATA",
    "M" : "ATG",
    "V" : "GTT",
    "V" : "GTC",
    "V" : "GTG",
    "S" : "TCT",
    "S" : "TCC", 
    "S" : "TCA",
    "S" : "TCG",
    "S" : "AGT",
    "S" : "AGC",
    "P" : "CCT", 
    "P" : "CCC",
    "P" : "CCA",
    "P" : "CCG",
    "T" : "ACT",
    "T" : "ACC",
    "T" : "ACA",
    "T" : "ACG",
    "A" : "GCT", 
    "A" : "GCC",
    "A" : "GCA",
    "A" : "GCG",
    "Y" : "TAT",
    "Y" : "TAC",
    "*" : "TAA", 
    "*" : "TAG", 
    "*" : "TGA",
    "H" : "CAT",
    "H" : "CAC",
    "Q" : "CAA", 
    "Q" : "CAG",
    "N" : "AAT",
    "N" : "AAC",
    "K" : "AAA", 
    "K" : "AAG",
    "D" : "GAT", 
    "D" : "GAC",
    "E" : "GAA",
    "E" : "GAG",
    "C" : "TGT",
    "C" : "TGC",
    "W" : "TGG",
    "R" : "CGT",
    "R" : "CGC",
    "R" : "CGA",
    "R" : "CGG",
    "R" : "AGA",
    "R" : "AGG",
    "G" : "GGT", 
    "G" : "GGC",
    "G" : "GGA",
    "G" : "GGG" 
}
#variables (the usual suspects)
dna = "aggagtaagcccttgcaactggaaatacacccattg"
dna_length = len(dna)
block_size = 3
blocking = 3
start = 0
dna_list = [ ]
extracted_codons = [ ]
protein = 0
dna_upper = dna.upper()
split_dna_list = []

#function   
print(dna_upper)
def find():
    for key, value in codon_table.items():
        if value in dna_list:
            extracted_codons.append(key)


#need to find a way to make the find function not return all of the previous values in the loop. So make it jump by 3
while start < dna_length :
   dna_list.append(dna_upper[start:blocking]) 
   start += block_size
   blocking += block_size
   protein += 1
   if (protein+1) %3 == 0:
       find()
#splitting dna
split_dna = ""
for _ in dna_list:
   split_dna += (" " + (_) + " ")


#need to convert split dna into values so if 
#For split on the list, it needs to be converted into the right key

#printing the new list
print(extracted_codons)
protein_list = ""
for x in extracted_codons:
    protein_list += x


print(protein_list)

#make the left side a key with the key value being on the right
#always keep multiple values in an array per key 
codon_table = {
    "F" : ["TTT","TTC"],
    "L" : ["TTA", "TTG", "CTT", "CTA", "CTG" ],
    "I" : ["ATT", "ATC", "ATA"],
    "M" : ["ATG"],
    "V" : ["GTT", "GTC", "GTG"],
    "S" : ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
    "P" : ["CCT", "CCC", "CCA", "CCG"],
    "T" : ["ACT", "ACC", "ACA", "ACG"],
    "A" : ["GCT", "GCC", "GCA", "GCG"],
    "Y" : ["TAT", "TAC"],
    "*" : ["TAA", "TAG", "TGA"],
    "H" : ["CAT", "CAC"],
    "Q" : ["CAA", "CAG"],
    "N" : ["AAT", "AAC"],
    "K" : ["AAA", "AAG"],
    "D" : ["GAT", "GAC"],
    "E" : ["GAA", "GAG"],
    "C" : ["TGT", "TGC"],
    "W" : ["TGG"],
    "R" : ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG" ],
    "G" : ["GGT", "GGC", "GGA", "GGG" ]
}
#variables (the usual suspects)
dna = "aggagtaagcccttgcaactggaaatacacccattg"
dna_length = len(dna)
block_size = 3
start = 0
dna_list = [ ]
extracted_codons = [ ]
protein = 0
dna_upper = dna.upper()
split_dna_list = []

#function   
def find():
    print(dna_list[-1])
    for key, value in codon_table.items():
        if dna_list[-1] in value:
            #print(value)
            extracted_codons.append(key)



#loop

while start < dna_length :
    dna_list.append(dna_upper[start:(start+block_size)]) 
    #print(dna_list[-1])
    find()
    start += block_size
   
# #splitting dna
# split_dna = ""
# for _ in dna_list:
#    split_dna += (" " + (_) + " ")


# #need to convert split dna into values so if 
# #For split on the list, it needs to be converted into the right key

# #printing the new list

protein_list = ""
for x in extracted_codons:
    protein_list += x


print(protein_list)
#ctrl forward slash comments sections and can uncomment

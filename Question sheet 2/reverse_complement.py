dna = "aggagtaagcccttgcaactggaaatacacccattg"
reverse_dna = dna[::-1]
dna_length = len(dna)
start = 0
dna_list = []
complement_list = []

complement_table = {
    "a" : ["t"],
    "t" : ["a"],
    "g" : ["c"],
    "c" : ["g"] 
}
#repurposing the function to look through the last string value in the DNA to look through the complement table
def reverse_complement():
    for key, value in complement_table.items():
        if dna_list[-1] in value:
            complement_list.append(key)

#same kind of logic as translating I think
while start < dna_length :
    dna_list.append(dna[start])
    reverse_complement()
    start += 1


#very easy to reverse the string so I saved it till the end rather than mess with a reversed DNA string
complement_output = ""
for x in complement_list:
    complement_output += x

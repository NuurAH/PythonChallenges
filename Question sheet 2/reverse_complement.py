dna = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"

reverse_dna = dna[::-1]
dna_length = len(dna)
c_list = list(dna)
start = 0
dna_list = []
complement_list = []

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
def reverse_complement(x):

    else:
        print("This is not a base" + " " + x)
        return ""


while start < dna_length:
    dna_list.append(dna[start])


    start +=1




# def base_scan():
#     for value in complement_table.items():
#         if dna_list[-1] not in value:
#             print("this is not a value")
# different function?

    
#same kind of logic as translating I think
# while start < dna_length :
#   if c_list[start] == "A":
#       c_list[start] == "T"
#   elif c_list[start] == "T":
#       c_list[start] == "A"
#   elif c_list[start] == "G":
#       c_list[start] == "C"
#   elif c_list[start] == "C":
#     c_list[start] == "G"
#   else:
#     print("This is not a base")
# complement_list.append(c_list(start))
# start += 1



#very easy to reverse the string so I saved it till the end rather than mess with a reversed DNA string
complement_output = ""
for x in complement_list:
    complement_output += x


print(complement_output[::-1])

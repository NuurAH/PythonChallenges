''' In this code, I am finding the length of the DNA sequence, then I am making my block size which is 3 in this case. I have start_string = 0 
A list is then made, I append the first value and then add blocking which is the same value as block size however
this value will always be greater than the first value by the block size.  I need them to be stored separately so that I can add block size to both start_string and blocking so that
both values increase by block size. This causes my while loop, which evaluates the length of dna_length, to loop and break up the string by my block size and
add it to the list. The second loop coverts the list back into a string and finally the whitespace at the front is removed using the strip function '''
#variable list
dna = "aggagtaagcccttgcaactggaaatacacccattg"
dna_length = len(dna)
block_size = 3
blocking = 3
start_string = 0
dna_list = []
#loops
while start_string < dna_length :
   dna_list.append(dna[start_string:blocking]) 
   start_string += block_size
   blocking += block_size

split_dna = ""
for _ in dna_list:
   split_dna += (" " + (_) + " ") 
#printing
formatted_dna = split_dna.strip()
print(formatted_dna)


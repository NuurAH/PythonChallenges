''' In this code, I am finding the length of the DNA sequence, then I am making my block size which is 3 in this case. I have z = 0 
this is because it is the start of the string. A list is then made, I append the first value and then add blocking which is the same value as block size however
this value will always be greater than the first value by the block size.  I need them to be stored separately so that I can add block size to both z and blocking so that
both values increase by block size. This causes my while loop, which evaluates the length of x, to loop until z reaches x and break up the string by my block size and
add it to the list. The second loop coverts the list back into a string and finally the whitespace at the front is removed using the strip function '''
#variable list
DNA = "aggagtaagcccttgcaactggaaatacacccattg"
x = len(DNA)
block_size = 3
blocking = 3
z = 0
my_list = []
#loops
while z < x :
   my_list.append(DNA[z:blocking]) 
   z += block_size
   blocking += block_size

split_dna = ""
for _ in my_list:
   split_dna += (" " + (_) + " ") 
#printing
formatted_dna = split_dna.strip()
print(formatted_dna)


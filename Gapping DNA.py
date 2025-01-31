DNA = "aggagtaagcccttgcaactggaaatacacccattg"
x = len(DNA)
block_size = 3
blocking = 3
z = 0

my_list = []
while z < x :
   my_list.append(DNA[z:blocking]) 
   z += block_size
   blocking += block_size

split_dna = ""
for _ in my_list:
   split_dna += (" " + (_) + " ") 

print (split_dna)

#challenge
#GCTGAGACTT  CCTGGACGGG  GGACAGGCTG  TGGGGTTTCT  CAGATAACTG  GGCCCCTGCG  CTCAGGAGGC  CTTCACCCTC  TGCTCTGGGT  AAAGTTCATT  GGAACAGAAA  GAAATGGATT  TATCTGCTCT  TCGCGTTGAA  GAAGTACAAA  ATGTCATTAA  TGCTATGCAG  AAAATCTTAG  AGTGTCCCAT  CTGTCTGGAG  TTGATCAAGG  AACCTGTCTC  CACAAAGTGT  GACCACATAT  TTTGCAAATT  TTGCATGCTG  AAACTTCTCA  ACCAGAAGAA  AGGGCCTTCA  CAGTGTCCTT  TATGTAAGAA  TGATATAACC  AAAAGGAGCC  TACAAGAAAG  TACGAGATTT  GAT
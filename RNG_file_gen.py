import sys
import os
import random

lower_bound = sys.argv[1]
upper_bound = sys.argv[2]
ammount = sys.argv[3]
directory = sys.argv[4]
num_of_files = sys.argv[5]

for j in range(int(num_of_files)):
	f = open(directory+"/in"+str(j+1)+".txt", "a")
	for i in range(int(ammount)):
		f.write(str(random.randint(int(lower_bound), int(upper_bound))) + " ")
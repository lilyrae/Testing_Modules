# Fuzz Testing
# ------------
# Write a random fuzzer, based on Charlie Miller's example
# from Problem Set 4, for a text viewer application.
#
# For multiple iterations, the procedure, fuzzit, should take in the content
# of a text file, pass the content into a byte array, randomly modify bytes
# of the "file", and add the resulting byte array (as a String) to a list. 
# The return value of the fuzzit procedure should be a list of 
# byte-modified strings.


import random
import math

content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Phasellus sollicitudin condimentum libero,
sit amet ultrices lacus faucibus nec.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Cras nulla nisi, accumsan gravida commodo et,
venenatis dignissim quam. Mauris rutrum ullamcorper consectetur.
Nunc luctus dui eu libero fringilla tempor. Integer vitae libero purus.
Fusce est dui, suscipit mollis pellentesque vel, cursus sed sapien.
Duis quam nibh, dictum ut dictum eget, ultrices in tortor.
In hac habitasse platea dictumst. Morbi et leo enim.
Aenean ipsum ipsum, laoreet vel cursus a, tincidunt ultrices augue.
Aliquam ac erat eget nunc lacinia imperdiet vel id nulla."""

def fuzzit(content):
# Write a random fuzzer for a simulated text viewer application

	num_tests = 20
	FuzzFactor = 1

	fuzzed_content = []

	for i in range(num_tests):

		byte_content = bytearray(content)

		# code taken from talk by Charlie Miller
		# Baby sitting an army of monkeys
		# https://www.youtube.com/watch?v=Xnwodi2CBws

		# number of bytes to be modified
		numwrites = random.randrange(math.ceil((float(len(byte_content)) / FuzzFactor))) + 1

		for j in range(numwrites):
			rand_byte = random.randrange(125)
			rand_n = random.randrange(len(byte_content))
			byte_content[rand_n] = "%c"%(rand_byte)

		# end charlie miller code

		fuzzed_str = str(byte_content.decode())
        
		# add newly fuzzed content to list as a string
		fuzzed_content.append(fuzzed_str)

	return fuzzed_content

print fuzzit(content)

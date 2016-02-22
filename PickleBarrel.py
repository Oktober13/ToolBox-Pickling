from os.path import exists
import sys
import pickle
import os

def pickle_toolbox(file_name, reset = False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> pickle_toolbox('blah.txt',True)
	1
	>>> pickle_toolbox('blah.txt')
	2
	>>> pickle_toolbox('blah2.txt',True)
	1
	>>> pickle_toolbox('blah.txt')
	3
	>>> pickle_toolbox('blah2.txt')
	2
	"""

	if os.path.exists(file_name):
	    count_file = open(file_name, 'r')
	    counter = pickle.load(count_file)
	    if reset == True:
	    	counter = 1
	    else:
	    	counter = counter + 1
	    print counter

	    count_file = open(file_name, 'w')
	    pickle.dump(counter, count_file)
	    count_file.close()

	else:
	    count_file = open(file_name, 'w')
	    counter = 1
	    pickle.dump(counter, count_file)
	    count_file.close()
	return

if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))
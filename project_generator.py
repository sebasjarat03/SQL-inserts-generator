import random as rd

def generate_project(num):
	insert = ''

	for x in range(num):
		insert += ('INSERT INTO Project VALUES ('+
			str(x + 1)                        +', '+
			"'superCreativeName#" + str(x + 1)+"', "+
			str(rd.randint(1, num)) +');'+
			'\n')

	return insert
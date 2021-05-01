import random as rd

def generate_department(num):
	MANAGER_EMPLOYEES =  rd.sample(range(num), num) # n numbers in [0, n]
	insert = ''

	for x in range(num):
		insert += ('INSERT INTO Department VALUES ('+
			str(x + 1)                    +', '+
			"'deptName#" + str(x + 1)      +"', "+
			str(MANAGER_EMPLOYEES[x] + 1) +');'+
			'\n')

	return insert
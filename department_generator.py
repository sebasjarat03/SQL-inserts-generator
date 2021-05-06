import random as rd


MANAGER_EMPLOYEES = list()

def generate_department(num):
	global MANAGER_EMPLOYEES
	MANAGER_EMPLOYEES =  rd.sample(range(num), num) # n numbers in [0, n]
	insert = ''

	for x in range(6):
		insert += ('INSERT INTO Department VALUES ('+
			str(x + 1)                    +', '+
			"'deptName#" + str(x + 1)      +"',"+
			str(MANAGER_EMPLOYEES[x] + 1) +');'+
			'\n')

	return insert
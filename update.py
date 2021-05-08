import employee_generator
import department_generator
import random as rd


def generate_emp(num):
	empNo = rd.randint(1, num)
	return empNo

def generate_updates(num):
	update = ''
	emplN = department_generator.MANAGER_EMPLOYEES
	
	for x in range(6):
		update += ('UPDATE employee SET deptNo ='+ 
            str(x+1)   + ' WHERE empNo = ' 
            + str(emplN[x]+1)
			 +';'+
			'\n')
	

	for x in range(6,30):
		update += ('UPDATE employee SET deptNo ='+ 
            str(employee_generator.generate_deptNo(6)) + ' WHERE empNo = ' 
            + str(emplN[x] + 1) +';'+
			'\n')

	return update
import employee_generator


emplN = employee_generator.return_empl()

def generate_updates(num):
	update = ''

	for x in range(num):
		update += ('UPDATE department SET mgrEmpNo ='+ 
            str(x+1)   + ' WHERE deptNo = ' 
            + str(emplN[x])
			 +';'+
			'\n')

	return update
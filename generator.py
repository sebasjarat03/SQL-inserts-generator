import sys;
import employee_generator
import department_generator
import project_generator
import worksOn_generator

print ('Enter the number of inserts that you want: ')

NUM_ROWS = int(input())

employees_insert = employee_generator.generate_employees(NUM_ROWS)
department_insert = department_generator.generate_department(NUM_ROWS)
project_insert = project_generator.generate_project(NUM_ROWS);
worksOn_insert = worksOn_generator.generate_worksOn(NUM_ROWS)

inserts_file = open('inserts.SQL', 'w');

inserts_file.writelines('DELETE FROM DEPARTMENT;' + '\n')
inserts_file.writelines('DELETE FROM EMPLOYEE;' + '\n')
inserts_file.writelines('DELETE FROM PROJECT;' + '\n')
inserts_file.writelines('DELETE FROM WORKSON;' + '\n')
inserts_file.writelines(employees_insert + '\n')
inserts_file.writelines(department_insert + '\n')
inserts_file.writelines(project_insert + '\n')
inserts_file.writelines(worksOn_insert)

inserts_file.close()
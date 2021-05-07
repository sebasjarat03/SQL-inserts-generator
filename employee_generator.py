import sys;
import csv;
import random as rd
import datetime

names_list = list(csv.reader(open('data/names.csv','r')))
surnames_list = list(csv.reader(open('data/surnames.csv','r')))

NAMES_LEN = len(names_list) - 1
SURNAMES_LEN = len(surnames_list) - 1

emplN = []

def generate_name():
	#Random between 0 and the number of names
	return "'" + names_list[rd.randint(0, NAMES_LEN)][0] + "'"

def generate_surname():
	return "'" +surnames_list[rd.randint(0, SURNAMES_LEN)][0].capitalize() + "'"

def generate_DOB():
	#Generates a random date between two given
	
	end_date = datetime.date(2002, 1, 1)
	start_date = datetime.date(1940, 2, 1)

	time_between_dates = end_date - start_date
	days_between_dates = time_between_dates.days
	random_number_of_days = rd.randrange(days_between_dates)
	random_date = start_date + datetime.timedelta(days=random_number_of_days)

	return "'" + str(random_date)+ "'"

def generate_gender():
	gender = ['M', 'F']
	return "'" + gender[rd.randint(0, 1)] + "'"

def generate_deptNo(num):
	deptNo = rd.randint(1, num)
	return deptNo

def return_empl():
	return emplN

def generate_address():
	opt = ['CLL', 'CRA']
	return "'" + opt[rd.randint(0,1)] + " " + str(rd.randint(1,125)) + " N° " + str(rd.randint(1,150)) + "-" + str(rd.randint(1,150))



def generate_employees(num):
	insert = ''

	for x in range(num):
		insert += ('INSERT INTO Employee (empNo, fName, lName, address, DOB, sex, position) VALUES ('+
			str(x + 1)                    +', '+
			generate_name()               +', '+
			generate_surname()            +', '+
			generate_address()      +"', "+
			generate_DOB()                +', '+
			generate_gender()             +', '+
			"'position#" + str(x + 1)     +"');"+
			'\n')

	return insert
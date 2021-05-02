import sys;
import csv;
import random as rd
import time

names_list = list(csv.reader(open('data/names.csv','r')))
surnames_list = list(csv.reader(open('data/surnames.csv','r')))

NAMES_LEN = len(names_list) - 1
SURNAMES_LEN = len(surnames_list) - 1

MAX_DATE = '01/01/2002'
MIN_DATE = '01/01/1970'
DATE_FORMAT = '%d/%m/%Y'
emplN = []

def generate_name():
	#Random between 0 and the number of names
	return "'" + names_list[rd.randint(0, NAMES_LEN)][0] + "'"

def generate_surname():
	return "'" +surnames_list[rd.randint(0, SURNAMES_LEN)][0].capitalize() + "'"

def generate_DOB():
	#Generates a random date between two given

    min_time = time.mktime(time.strptime(MIN_DATE, DATE_FORMAT))
    max_time = time.mktime(time.strptime(MAX_DATE, DATE_FORMAT))

    ptime = min_time + rd.random() * (max_time - min_time)

    return "'" + time.strftime(DATE_FORMAT, time.localtime(ptime))+ "'"

def generate_gender():
	gender = ['M', 'F']
	return "'" + gender[rd.randint(0, 1)] + "'"

def generate_deptNo(num, x):
	deptNo = rd.randint(1, num)
	emplN.insert(x, deptNo) 
	return deptNo

def return_empl():
	return emplN

def generate_employees(num):
	insert = ''

	for x in range(num):
		insert += ('INSERT INTO Employee VALUES ('+
			str(x + 1)                    +', '+
			generate_name()               +', '+
			generate_surname()            +', '+
			"'adress#" + str(x + 1)       +"', "+
			generate_DOB()                +', '+
			generate_gender()             +', '+
			"'position#" + str(x + 1)     +"', "+
			str(generate_deptNo((num), x)) +');'+
			'\n')

	return insert
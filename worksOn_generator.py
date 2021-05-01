import time
import random as rd

MAX_DATE = '01/01/2002'
MIN_DATE = '01/01/1970'
DATE_FORMAT = '%d/%m/%Y'

def generate_DW():
	#Generates a random date between two given

    min_time = time.mktime(time.strptime(MIN_DATE, DATE_FORMAT))
    max_time = time.mktime(time.strptime(MAX_DATE, DATE_FORMAT))

    ptime = min_time + rd.random() * (max_time - min_time)

    return "'" + time.strftime(DATE_FORMAT, time.localtime(ptime)) + "'"

def generate_worksOn(num):
	insert = ''

	for x in range(num):
		insert += ('INSERT INTO WorksOn VALUES ('+
			str(rd.randint(1, num))  +', '+
			str(rd.randint(1, num))  +', '+
			generate_DW()            +', '+
			str(rd.randint(1, 500))  +');'+
			'\n')

	return insert
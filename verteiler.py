#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from datetime import datetime
from calendar import monthrange
import sys

#functions
def splitter(personList=[], maxTasksPerPerson=3):
    persons = personList[:]
    output = []
    while len(persons) > 0 and maxTasksPerPerson > 0:
        output.append(random.choice(persons))
        for index, value in enumerate(persons):
            if output.count(value) == maxTasksPerPerson:
                del persons[index]
    return output

def split_work(persons=[], taskcount=3):
    leftover = taskcount % len(persons)
    taskcount = taskcount // len(persons)
    output = splitter(persons, taskcount)
    output += splitter(persons, 1)[:leftover]
    return output

#settings
persons = ["Shinji", "Misato", "Gendo"]
weekdays = ["Mo.", "Di.", "Mi.", "Do.", "Fr.", "Sa.", "So."]
today = datetime.now()

if len(sys.argv) > 1:
	persons = []
	for arg in sys.argv[1:]:
		persons.append(arg)
	month = ""
	while not month.isnumeric():
		month = input("Berechnen für Monat(default="+ str(today.month) + "): ")
		if month == "":
			month = str(today.month)		
	year = ""
	while not year.isnumeric():
		year =  input("Berechnen für Jahr(default="+str(today.year) +"): ")
		if year == "":
			year = str(today.year)
	
	month = int(month)
	year = int(year)		
	today = today.replace(day=1, month=month, year=year)

#time calculations
calendarWeek = today.replace(day=1).isocalendar()[1]
firstWeekdayOfMonth = monthrange(today.year, today.month)[0]
lastDayOfMonth = monthrange(today.year, today.month)[1]
tasks = lastDayOfMonth
print("Berechne für Monat:", str(today.month).zfill(2), "-", today.year)

#excecution
worklist = split_work(persons, tasks)

#review
print("Aufgaben:", tasks)
print("---")

for person in persons:
    print(person + ":", worklist.count(person))

print("---")

startDay = firstWeekdayOfMonth
output = "KW" + str(calendarWeek).zfill(2) + ":\t" +   "\t\t\t" * startDay
for x in range(1, tasks+1):
	if startDay == 7:
		startDay = 0
		calendarWeek += 1
		if calendarWeek == 53:
			calendarWeek = 1
		output += "\n" + "KW" + str(calendarWeek).zfill(2) + ":\t"
	output += weekdays[startDay] + " " + str(x).zfill(2) + "." +  str(today.month).zfill(2) + "." + str(today.year)[-2:] + ": " + worklist.pop(0) + "\t"
	startDay+=1

print(output)

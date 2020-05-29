import datetime 
import sys
import os

months = {
	"January": 1,
	"February": 2,
	"March": 3,
	"April": 4,
	"May": 5,
	"June": 6,
	"July": 7,
	"August": 8,
	"September": 9,
	"October": 10,
	"November": 11,
	"December": 12
}

ev_list = []

def load():
	file = open("/Users/andsa/.scripts/todo/.todo.txt", "r")
	for line in file:
		spl = line.split(" on ")
		ev_list.append((spl[0], spl[1]))
	file.close()

def store():
	file = open("/Users/andsa/.scripts/todo/.todo.txt", "w")
	for ev in ev_list:
		file.write("{} on {}".format(ev[0], ev[1]))
	file.close()

def newev(ev_name, ev_date):
	load()
	# Sort by date
	index = 0 
	while index < len(ev_list) and ev_date > datetime.date(int(ev_list[index][1][0:4]), int(ev_list[index][1][5:7]), int(ev_list[index][1][8:])):
		index = index + 1
	ev_list.insert(index, (ev_name, ev_date.isoformat() + "\n"))

	store()

def listev():
	file = open("/Users/andsa/.scripts/todo/.todo.txt", "r")
	print("\n*** [TODO] ***")
	for line in file:
		print(line, end="\r")
	print()
	file.close()

def delev(ev_name):
	load()
	rem = False
	for ev in ev_list:
		if ev[0] == ev_name:
			ev_list.remove(ev)
			rem = True
			store()
			break

def clear():
	file = open("/Users/andsa/.scripts/todo/.todo.txt", "w")
	file.close()

def ctrl(): 
	args = sys.argv
	if args[1] == "newev":
		ev_name = args[2]
		spl = args[3].replace(",", "").split()
		try:
			ev_date = datetime.date(int(spl[2]), months[spl[0]], int(spl[1]))
			newev(ev_name, ev_date)
		except ValueError:
			print("Invalid date.")
	elif args[1] == "delev":
		ev_name = args[2]
		delev(ev_name)
	elif args[1] == "listev":
		listev()
	elif args[1] == "clear":
		clear()
	else:
		print("Invalid command.")

ctrl()



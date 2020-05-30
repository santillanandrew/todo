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

list = []

def load():
	file = open("/Users/andsa/.scripts/todo/.todo.txt", "r")
	for line in file:
		spl = line.split(" : ")
		list.append((spl[0], spl[1]))
	file.close()

def store():
	file = open("/Users/andsa/.scripts/todo/.todo.txt", "w")
	for ev in list:
		file.write("{} : {}".format(ev[0], ev[1]))
	file.close()

def newev(name, date):
	load()
	# Sort by date
	index = 0 
	while index < len(list) and date > datetime.date(int(list[index][1][0:4]), int(list[index][1][5:7]), int(list[index][1][8:])):
		index = index + 1
	list.insert(index, (name, date.isoformat() + "\n"))

	store()

def newit(name):
	load()

	list.insert(0, (name, "N/A\n"))

	store()

def show():
	file = open("/Users/andsa/.scripts/todo/.todo.txt", "r")
	print("\n*** [TODO] ***")
	for line in file:
		print(line, end="\r")
	print()
	file.close()

def delev(name):
	load()
	rem = False
	for ev in list:
		if ev[0] == name:
			list.remove(ev)
			rem = True
			store()
			break

def delit(name):
	delev(name)

def clear():
	file = open("/Users/andsa/.scripts/todo/.todo.txt", "w")
	file.close()

def ctrl(): 
	args = sys.argv
	if args[1] == "newev":
		name = args[2]
		spl = args[3].replace(",", "").split()
		try:
			date = datetime.date(int(spl[2]), months[spl[0]], int(spl[1]))
			newev(name, date)
		except ValueError:
			print("Invalid date.")
	elif args[1] == "del":
		name = args[2]
		delev(name)
	elif args[1] == "show":
		show()
	elif args[1] == "clear":
		clear()
	elif args[1] == "newit":
		name = args[2]
		newit(name)
	else:
		print("Invalid command.")

ctrl()



#!/bin/bash

function todo() {
	arg1="$1"
	arg2="$2"
	arg3="$3"
	arg4="$4"
	arg5="$5"
	if [ "$arg1" = "newev" ]; then
		if [ "$arg2" != "" -a "$arg3" = "on" -a "$arg4" != "" -a "$arg5" = "" ]; then
			python3 /Users/andsa/.scripts/todo/.todo.py "$arg1" "$arg2" "$arg4"
		else
			echo "Command should be of the form: todo newev [NAME] on [DATE]"
		fi
	elif [ "$arg1" = "del" ]; then 
		if [ "$arg2" != "" -a "$arg3" = "" ]; then
			python3 /Users/andsa/.scripts/todo/.todo.py "$arg1" "$arg2"
		else
			echo "Command should be of the form: todo del [NAME]"
		fi
	elif [ "$arg1" = "show" ]; then
		if [ "$arg2" = "" ]; then
			python3 /Users/andsa/.scripts/todo/.todo.py "$arg1"
		else
			echo "Command should be of the form: todo show"
		fi
	elif [ "$arg1" = "clear" ]; then
		if [ "$arg2" =  "" ]; then
			python3 /Users/andsa/.scripts/todo/.todo.py "$arg1"
		else 
			echo "Command should be of the form: todo clear"
		fi
	elif [ "$arg1" = "newit" ]; then
		if [ "$arg2" != "" -a "$arg3" = "" ]; then
			python3 /Users/andsa/.scripts/todo/.todo.py "$arg1" "$arg2"
		else 
			echo "Command should be of the form: todo newit [NAME]"
		fi
	else
		echo "Invalid todo operation"
	fi
}
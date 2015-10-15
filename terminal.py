import os
import sys
import readline

class MyCompleter(object):  # Custom completer

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options 
                                    if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try: 
            return self.matches[state]
        except IndexError:
            return None

def execute(command):
	allowed_commands=["clr","cd","echo","pause","help","quit","environ","dir","pwd"]
	pwd=os.getcwd()
	for a in pwd:
		if a in allowed_commands:
			allowed_commands.remove(a)
	list_of_files=os.listdir(pwd)
	allowed_commands=allowed_commands+list_of_files
	completer = MyCompleter(allowed_commands)
	readline.set_completer(completer.complete)
	readline.parse_and_bind('tab: complete')
	SHELL=pwd + "terminal.py"
	if not command:
		return
	if command[0] not in allowed_commands:
			print "Command does not exist"
	elif command[0]=="environ":
		if len(command) > 1:
			print "environ takes no arguements"
		else:
			print "PWD = ",pwd
			print "SHELL = ",SHELL
	elif command[0]=="pwd":
		print pwd	
	elif command[0]=="pause":
		if len(command) > 1:
			print "pause takes no arguements"
		else:	
			print "System Paused"
			raw_input("Press Enter to unpause")	
	elif command[0]=="echo":
		statement=""
		for string in command:
			if string!="echo":
				statement=statement+string+' '
		print statement
	elif command[0]=="clr":
		if len(command) > 1:
			print "clr takes no arguements"
		else:
			os.system('clear')
	elif command[0]=="dir":
		if len(command)==2:
			ls_files=os.listdir(command[1])
			for l in ls_files:
				print l
		elif len(command) > 2:
			print "invalid path"
		else:
			for l in list_of_files:
				print l			
	elif command[0]=="cd":
		if len(command) > 2:
			print "cd takes only one arguement"
		else:
			path=command[1]
			if os.path.isdir(path):
				os.chdir(path)
				pwd=os.getcwd()
				SHELL=pwd + '/terminal'
				list_of_files=os.listdir(pwd)
			else:
				print "No such directory path exists"
	elif command[0]=="help":
		if len(command)==1:
			fileopen=open('help.txt')
			for f in fileopen:
				print f
		elif len(command)>2:
			print "help takes only one arguement"	
		else:
			if command[1]=="dir":
				print "dir [list files and directories in the current directory] [takes no arguements]"
			elif command[1]=="cd":
				print "cd [change to a directory] [takes a path as input to change to it]"
			elif command[1]=="quit":
				print "quit [break out of the system] [takes no arguements]"
			elif command[1]=="clr":
				print "clr [clear the screen] [takes no arguements]"
			elif command[1]=="echo":
				print "echo [print to screen] [takes a statement as input]"
			elif command[1]=="pause":
				print "pause [pauses the system untill enter is pressed] [takes no arguements]"
			elif command[1]=="environ":
				print "environ [lists the environment variables] [takes no arguements]"
			elif command[1]=="pwd":
				print "pwd [present working directory] [takes no arguements]"
			else:
				print "No such command exists"	
	elif command[0]=="quit":
		exit(0)

if len(sys.argv)==1:
	while 1:
		pwd=os.getcwd()
		comm=raw_input("terminal@" + pwd + ':- ' + '$').split()
		execute(comm)			
else:
	if os.path.exists(sys.argv[1]):
		fileopen=open(sys.argv[1])
		for f in fileopen:
			comm=f.split()
			execute(comm)
	else:
		print "input file does not exist"		
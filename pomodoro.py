import time
import os
import re

# complete total work cycle
# announce breaks and work sprints
def pomodori(work_len, break_len, iterations):
	# convert work_len to seconds
	work_len_sec =  work_len * 60
	break_len_sec = break_len * 60

	for i in range(iterations):
		print("You are on pomodoro number " + str(i+1))
		# start work period
		print("Start working for " + str(work_len) + " minutes!")
		# TODO add minute count
		time.sleep(work_len_sec)
		os.system('say "your work sprint has finished, take a break"')

		# don't announce break if total work period finished
		if (i + 1) < iterations:
			# start break period
			print("Take a break for " + str(break_len) + " minutes!")
			# TODO add minute count
			time.sleep(break_len_sec)
			os.system('say "your break is done, back to work"')
		else:
			break

	# finish total work period
	print("Pomodori complete!")
	os.system('say "you are done, please close the computer and throw it out a window"')


# capture user input on work length, break length and numbers of cycles
def user_input():
	# TODO add a user introduction to the program
	work_len = clean_input(raw_input("How long do you want to work for (in minutes): "))
	break_len = clean_input(raw_input("How long do you want your breaks to be (in minutes): "))
	iterations = clean_input(raw_input("How many work/break cycles do you want to complete: "))

	print "Ok, you will work for " + str(work_len) + " mins then take a " + str(break_len) + " min break, " + str(iterations) + " times."

	# TODO add a "ready to start? prompt"
	raw_input("How long do you want your breaks to be (in minutes): ")
	pomodori(int(work_len), int(break_len), int(iterations))

# only allow numbers
def clean_input(raw_work_len):
	work_len = re.sub('[^0-9]','', raw_work_len)
	return work_len

user_input()


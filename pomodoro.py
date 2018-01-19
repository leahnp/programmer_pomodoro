import time
import os

def pomodoro(work_len, break_len, iterations):
	# convert work_len to seconds
	work_len_sec =  work_len * 60
	break_len_sec = break_len * 60

	for i in range(iterations):
		print(i)
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

	os.system('say "you are done, please close the computer and throw it out a window"')

# pomodoro(10, 5, 2)


#!/usr/bin/python3
#Zipeng Wang
#3909934
#hw5 problem 5                                          - first digit
#my intepretation: 16 bit:0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#                         |               | |     | ----- Channel number
#						  |	              | -------       Time
#						  -----------------               Pulse height


def decod_info(num):
	'''assume num is of type int, decode information'''
	pulse_h = num>>7
	num_time_channel = num-(pulse_h<<7) #only contains info about time and channel
	time = num_time_channel>>3  
	num_channel = num_time_channel - (time<<3)
	channel = num_channel
	return pulse_h,time,channel


while True:
	input_num = input("plese enter a 16 bit number: ")
	try: 
		num = int(input_num)
		if num >=0 and num <=65535:
			break
		else:
			print("Your number is not 16 bit.")
			print("It needs to be an integer between 0 and 65535.")
	except ValueError:
		print("This is not a integer. try again.")
pulse, time, chan = decod_info(num)
print('\nchannel is',chan,'\ntime is',time,'\npulse height is',pulse)
	

import time

#decorator
def calculate_time(func):
	def wrapper():
		start_time=time.time()
		func()
		end_time=time.time()
		total_time=end_time-start_time
		print(f"Total time {total_time}")
	return wrapper

@calculate_time
def time_sleep():
	time.sleep(2)

time_sleep=calculate_time(time_sleep)


def calculate_apr(principal, interest_rate, years):
	"""Calculates the amount of money after a number of years given an interest
	rate.""" 
	isvalid= isinstance(principal, int) and isinstance(interest_rate,float)\
	and isinstance(years, int) and principal>=0 and interest_rate>=0\
	 and years >=0 

	if not isvalid:
		return isvalid

	value=principal
	for i in range (1,years+1):
		print(f"interest rate:{interest_rate}")
		value=principal*(1+interest_rate)**i
		print(f"Total {value}")

	print(float(value))
	return float(value)
def main():
	#calculate_apr(500,0.03, 65)
	#calculate_apr(100,0.06,1)
	calculate_apr(100,-0.05,3)
main()

def calculate_apr(principal, interest_rate, years):
	
	isvalid= isinstance(principal, int) and isinstance(interest_rate,float)	and isinstance(years, int)
	if not isvalid:
		return isvalid

	value=principal
	for i in range (1,years):
		print(f"Total {value}")
		print(f"interest:{principal*interest_rate*i}")
		value=(principal*(1+interest_rate)*i)

	print(float(value))
	return float(value)
def main():
	calculate_apr(500,0.03, 65)

main()

import math

#attempt to personalize pi's decimal places
# def CalculatePi():
# 	Round_Digit = int(input('Enter the number of digits you want after the decimal for Pi: \n'))
# 	somepi = round(math.pi,Round_Digit)
    
# 	return somepi

# somepi = CalculatePi()
# try:
# 	print(f'Roundest Pi to your choice {somepi}')
# except:
# 	print("You did not enter an correctly");



# def CalculatePi():
# 	Round_Digit = int(input('Enter the number of digits you want after the decimal for Pi: \n'))
# 	somepi = round(math.pi,Round_Digit)
# 	print(f'Roundest Pi to your choice {somepi}')
	
# CalculatePi()

def CalculatePi():
	Round_Digit = int(input('Enter the number of digits you want after the decimal for Pi: \n'))
	somepi = round(math.pi,Round_Digit)
	return somepi 
	
somepi = CalculatePi()
print(f'Roundest Pi to your choice {somepi}')
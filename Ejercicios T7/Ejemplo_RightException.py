def ask_values():
	print('Please enter dividend: ')
	value1 = input()
	print('Please enter divisor: ')
	value2 = input()
	return (value1, value2)

def convert_to_numbers(value1, value2):
	number1 = float(value1)
	number2 = float(value2)
	return (number1, number2)

def divide(x, y):
	return x / y

dividend_as_text, divisor_as_text = ask_values()
try:
	dividend, divisor = convert_to_numbers(dividend_as_text, divisor_as_text)
except ValueError:
	print('Invalid values: only numeric values must be used')
else:
	try:
		result = divide(dividend, divisor)
	except ZeroDivisionError:
		print('Division by zero not allowed')
	else:
		print('Result: ', result)
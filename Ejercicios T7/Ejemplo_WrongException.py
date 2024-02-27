'''
def ask_numbers_and_divide():
	print('Please enter dividend: ')
	try:
		number1 = input()
		number1 = int(number1)
		print('Please enter divisor: ')
		number2 = input()
		number2 = int(number2)
	except ValueError:
		print('Invalid values: only numeric values must be used')
	else:
		try:
			result = divide(number1, number2)
		except ZeroDivisionError:
			print('Division by zero is not allowed.')
			print('Values: ', number1, ', ', number2)
		else:
			print('The result is: ', result)
'''

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


try:
        dividend_as_text, divisor_as_text = ask_values()
        dividend, divisor = convert_to_numbers(dividend_as_text, divisor_as_text)
        result = divide(dividend, divisor)
        print('El resultado es:', result)
except BaseException: #La excepción está mal porque es muy general y no concreta dónde está el error.
        print('Error con los valores proporcionados:',
              dividend_as_text, divisor_as_text)
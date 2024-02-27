from Ej_3_9_2 import calculate_seconds, convert_seconds_to_time
import sys


"""hour1 = input("Please enter number of hour: ")
minutes1 = input("Please enter numer of minutes: ")
seconds1 = input("Please enter number of seconds: ")"""

"""hour2 = input("Please enter number of hour: ")
minutes2 = input("Please enter numer of minutes: ")
seconds2 = input("Please enter number of seconds: ")"""

if len(sys.argv) < 7:
    print("The number of parameters is incorrect")
    exit()

hour1 = int(sys.argv[1])
minutes1 = int(sys.argv[2])
seconds1 = int(sys.argv[3])

hour2 = int(sys.argv[4])
minutes2 = int(sys.argv[5])
seconds2 = int(sys.argv[6])

total_seconds1 = calculate_seconds(hour1, minutes1, seconds1)
total_seconds2 = calculate_seconds(hour2, minutes2, seconds2)

result_hours, result_minutes, result_seconds = convert_seconds_to_time(total_seconds1 + total_seconds2)
print("This is the result in hours, minutes and seconds", result_hours, result_minutes, result_seconds)

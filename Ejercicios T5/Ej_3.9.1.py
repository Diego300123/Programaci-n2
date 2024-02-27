def calculate_seconds(hours, minuts, seconds):
    total_seconds = (hours * 3600) + (minuts * 60) + seconds
    return total_seconds

time = calculate_seconds(7, 50, 1)
print (time)



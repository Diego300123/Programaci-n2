def calculate_time(seconds):
    hours = (seconds // 3600)
    minutes = (seconds // 60) - (hours * 60)


    return (hours, minutes, seconds)

seconds = calculate_time(28201)
print (seconds)


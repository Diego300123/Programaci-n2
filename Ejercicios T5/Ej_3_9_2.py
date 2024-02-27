SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
def calculate_seconds(hours = 0, minutes = 0, seconds = 0): 
    """Calculate the total time in seconds.
    hours: (int) number of hours
    minutes: (int) number of minutes
    seconds: (int) number of seconds
    output: (int) total number of seconds"""
    total_seconds = (hours * SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE) + seconds

    return total_seconds

def convert_seconds_to_time(seconds):
    """Calculate the total time in hours, minutes and seconds.
    seconds: (int) number of seconds
    output: (int) total number of hours, minutes and seconds"""
    hours = (seconds // SECONDS_PER_HOUR)
    #minutes = (seconds // SECONDS_PER_MINUTE) - (hours * SECONDS_PER_MINUTE)
    minutes = (seconds % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE
    #secs = (seconds) - ((hours // SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE))
    secs = (seconds % SECONDS_PER_MINUTE)
    return (hours, minutes, secs)



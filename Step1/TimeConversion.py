timegiven = "12:00:00AM"
ampm = timegiven[-2:]
print(ampm)

# Extract the hour, minute, and second from the input string
hour = int(timegiven[:2])  # Get the hour as an integer
minute = timegiven[3:5]  # Get the minute as a string
second = timegiven[6:8]  # Get the second as a string

if ampm == "AM":
        if hour == 12:
            hour = 0
        else:  # PM case
            if hour != 12:
                hour += 12

hour_24 = f"{hour:02}"
print(f"{hour_24}:{minute}:{second}")
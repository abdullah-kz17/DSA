def timeConversion(s : str) -> str:
    period = s[-2:]
    hour = int(s[:2])
    min = s[3:5]
    sec = s[6:8]

    if hour > 12:
        return "Invalid hour value. Hour must be between 01 and 12."

    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    military_time = f"{hour:02}:{minute}:{second}"
    return military_time

print(timeConversion("07:05:45PM")) 








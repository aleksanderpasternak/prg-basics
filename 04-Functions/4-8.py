def time_string(hours,minutes,time_format):
    if hours < 10:
        hours = str(f"0{hours}")
    if  minutes < 10:
        minutes = str(f"0{minutes}")
    if time_format == '24':
        hours = hours
        result = str(f"{hours}:{minutes}")
    elif time_format == '12':
        if int(hours) > 12:
            hours -= 12
            result = str(f"{hours}:{minutes}pm")
        elif int(hours) <= 12:
            hours = hours
            result = str(f"{hours}:{minutes}am")
    return result

print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12') )
print(time_string(19, 2, '12'))
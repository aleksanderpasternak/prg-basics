def avg_speed(distance,hours,minutes):
    r = round(distance/(hours+minutes/60),2)
    return r
distance = float(input('Enter distance in km: '))
hours = int(input('Enter number of travel hours: '))
minutes = int(input('Enter number of travel minutes: '))
print('Average speed: ',avg_speed(distance,hours,minutes))
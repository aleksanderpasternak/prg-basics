time24 = input("Enter time (24-hour format): ")
hour24 = int(time24[0:2])
minute24 = int(time24[3:5])
if 0 <= hour24 < 12:
    suffix = "am"
    hour12 = hour24
elif hour24 < 24:
    suffix = "pm"
    hour12 = hour24 - 12



print(f"Time in 12-hour format: {hour12}:{minute24}{suffix}")
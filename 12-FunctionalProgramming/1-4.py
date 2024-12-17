ms = input('Speed in m/s: ')
ms_to_kmh = lambda x: float(x)*3.6
result = ms_to_kmh(ms)
print(f'{ms} m/s = {result} km/h')

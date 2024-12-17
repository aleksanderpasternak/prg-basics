def ms_to_kmh(x):
    return float(x)*3.6
ms = input('Speed in m/s: ')
result = ms_to_kmh(ms)
print(f'{ms} m/s = {result} km/h')
def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_in(n):
    return n*0.39

def ft_to_cm(n):
    return n/0.39*12

def in_to_cm(n):
    return n/0.39

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'123cm = {cm_to_in(123)}in')
    print(f'6 feet = {ft_to_cm(6)}cm')
    print(f'123in = {in_to_cm(123)}cm')


import tv

def main():
    tl = tv.TV()

    tl.turn_on()
    tl.set_channel(3)
    tl.show_status()
    tl.increse_volume()

if __name__ == "__main__":
    main()
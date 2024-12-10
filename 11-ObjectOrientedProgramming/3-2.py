class Music():
    def __init__(self,performer,title,album,year):
        self.performer = performer
        self.title = title
        self.album = album
        self.year = year
    
    def __str__(self):
        print(f'Performer: {self.performer}')
        print(f'Title: {self.title}')
        print(f'Album: {self.album}')
        print(f'Year: {self.year}')
        print('')

def main():
    song1 = Music('Ed Sheeran','Hearts Don\'t Break Around Here','Divide','2017')
    song2 = Music('Queen','Bohemian Rhapsody','A Night at the Opera','1975')
    song1.__str__()
    song2.__str__()

if __name__ == '__main__':
    main()
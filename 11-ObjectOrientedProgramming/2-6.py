class Phone():
    def __init__(self):
        self.brand = 'Apple'
        self.memory = 64
        self.color = 'black'
        self.contacts = []
        self.battery = 50
        self.alarm = ''

    def addContact(self,name,number):
        self.contacts.append(f"{name}: {number}")

    def charge(self,n):
        self.battery += n
    
    def setAlarm(self,hour):
        self.alarm = hour

    def display(self):
        print(f'Contacts: {self.contacts}')
        print(f'Battery: {self.battery}%')
        print(f'Alarm: {self.alarm}')
    
def main():
    phone = Phone()
    phone.addContact('John','123456789')
    phone.addContact('Joe','456987321')
    phone.charge(43)
    phone.setAlarm('7:30')
    phone.display()

if __name__== "__main__":
    main()


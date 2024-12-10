class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels_list = ['TVP1','TVP2','Polsat','TVN','Filmbox','Discovery']
        self.volume = 5
    
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
    
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no

    def volume_increase(self):
        if self.volume < 10:
            self.volume += 1
        else:
            
    
    def volume_decrease(self):
        if self.volume > 0:
            self.volume -= 1
        else:


    def show_status(self):
        if self.is_on == True:
            print(f'TV is on, channel {self.channel_no} ({self.channels_list[self.channel_no-1]}), volume {self.volume}')
        else:
            print('TV is off')

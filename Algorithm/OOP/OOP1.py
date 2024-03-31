class Battery: #membuat class battery
    
    # construktor untuk menginisialisasi atribut-atribut objek battery
    def __init__(self, name, power_percent, play_game, coding, browsing, play_audio, charge_rate):
        self.name = name
        self.power = power_percent
        self.game = play_game
        self.coding = coding
        self.browsing = browsing
        self.audio = play_audio
        self.charge = charge_rate
        
    def playinggame(self, time):
        if "hour" in time:
            split_time = time.split()
            minute = int(split_time[0]) * 60
            type_time = "jam"
        elif "minute" in time:
            split_time = time.split()
            minute = int(split_time[0])
            type_time = "menit"
        minus = self.game * minute/10
        self.power -= minus
        if self.power < 0:
            self.power = 0
        print(f"{self.name} bermain game selama {split_time[0]} {type_time}")
        print(f"Daya berkurang sebanyak {minus} %")
        print(f"Daya tersisa {self.power} %")
    
    def getcoding(self, time):
        if "hour" in time:
            split_time = time.split()
            minute = int(split_time[0]) * 60
            type_time = "jam"
        elif "minute" in time:
            split_time = time.split()
            minute = int(split_time[0])
            type_time = "menit"
        minus = self.coding * minute/10
        self.power -= minus
        if self.power < 0:
            self.power = 0
        print(f"{self.name} melakukan coding selama {split_time[0]} {type_time}")
        print(f"Daya berkurang sebanyak {minus} %")
        print(f"Daya tersisa {self.power} %")
        
    def getbrowsing(self, time):
        if "hour" in time:
            split_time = time.split()
            minute = int(split_time[0]) * 60
            type_time = "jam"
        elif "minute" in time:
            split_time = time.split()
            minute = int(split_time[0])
            type_time = "menit"
        minus = self.browsing * minute/10
        self.power -= minus
        if self.power < 0:
            self.power = 0
        print(f"{self.name} melakukan browsing selama {split_time[0]} {type_time}")
        print(f"Daya berkurang sebanyak {minus} %")
        print(f"Daya tersisa {self.power} %")

    def playingaudio(self, time):
        if "hour" in time:
            split_time = time.split()
            minute = int(split_time[0]) * 60
            type_time = "jam"
        elif "minute" in time:
            split_time = time.split()
            minute = int(split_time[0])
            type_time = "menit"
        minus = self.audio * minute/10
        self.power -= minus
        if self.power < 0:
            self.power = 0
        print(f"{self.name} memainkan audio selama {split_time[0]} {type_time}")
        print(f"Daya berkurang sebanyak {minus} %")
        print(f"Daya tersisa {self.power} %")
        
    def getcharge(self, time):
        if "hour" in time:
            split_time = time.split()
            minute = int(split_time[0]) * 60
            type_time = "jam"
        elif "minute" in time:
            split_time = time.split()
            minute = int(split_time[0])
            type_time = "menit"
        powerup = self.charge * minute/10
        self.power += powerup
        if self.power > 100:
            self.power = 100
        print(f"{self.name} mengisi daya selama {split_time[0]} {type_time}")
        print(f"Daya bertambah sebanyak {powerup} %")
        print(f"Daya tersisa {self.power} %")
        
    
Laptop = Battery("Laptop", 0, 10, 1, 2, 5, 10)

Laptop.getcharge("2 hours")
print("\n")
Laptop.playinggame("1 hour")
print("\n")
Laptop.getbrowsing("1 hour")
print("\n")
Laptop.getcharge("20 minutes")
print("\n")
Laptop.getcoding("2 hours")
print("\n")
Laptop.playingaudio("2 hours")


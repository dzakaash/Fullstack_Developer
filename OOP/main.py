class Hero: # Deklarasi kelas Hero sebagai blueprint untuk objek Hero
    pass

# Membuat tiga objek Hero menggunakan kelas Hero
hero1 = Hero() # Membuat objek hero1
hero2 = Hero() # Membuat objek hero2
hero3 = Hero() # Membuat objek hero3

# Menetapkan atribut untuk setiap objek Hero
hero1.name = "sniper" # Menetapkan nama "sniper" untuk hero1
hero1.health = 100    # Menetapkan kesehatan 100 untuk hero1

hero2.name = "sven"   # Menetapkan nama "sven" untuk hero2
hero2.health = 200    # Menetapkan kesehatan 200 untuk hero2

hero3.name = "ucup"   # Menetapkan nama "ucup" untuk hero3
hero3.health = 1000   # Menetapkan kesehatan 1000 untuk hero3

# Mencetak informasi tentang objek hero1
print(hero1)          # Mencetak representasi objek hero1
print(hero1.__dict__) # Mencetak atribut dan nilai objek hero1 dalam bentuk kamus
print(hero1.name)     # Mencetak nama hero1

##################

class Hero: # Template untuk membuat objek Hero
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Metode khusus yang dipanggil saat objek Hero dibuat
        # Menerima inputName, inputHealth, inputPower, dan inputArmor
        # dan menetapkan nilainya ke instance variable objek
        self.name = inputName     # Menetapkan nama Hero
        self.health = inputHealth # Menetapkan kesehatan Hero
        self.power = inputPower   # Menetapkan kekuatan Hero
        self.armor = inputArmor   # Menetapkan armor Hero

# Membuat instance objek Hero dengan menggunakan constructor (__init__)
# hero1 dengan nama "sniper", kesehatan 100, kekuatan 10, dan armor 4
hero1 = Hero("sniper", 100, 10, 4)
# hero2 dengan nama "mirana", kesehatan 100, kekuatan 15, dan armor 1
hero2 = Hero("mirana", 100, 15, 1)
# hero3 dengan nama "ucup", kesehatan 1000, kekuatan 100, dan armor 0
hero3 = Hero("ucup", 1000, 100, 0)

# Mencetak atribut name dari hero1
print(hero1.name)
# Mencetak atribut health dari hero2
print(hero2.health)
# Mencetak atribut armor dari hero3
print(hero3.armor)

# Mencetak kamus yang berisi semua atribut dan nilainya dari hero1
print(hero1.__dict__)
# Mencetak kamus yang berisi semua atribut dan nilainya dari hero2
print(hero2.__dict__)
# Mencetak kamus yang berisi semua atribut dan nilainya dari hero3
print(hero3.__dict__)

# Mencetak kamus yang berisi semua atribut dan nilai dari kelas Hero itu sendiri
# Termasuk metode dan atribut yang terkait dengan kelas Hero secara keseluruhan
print(Hero.__dict__)

##################

class Hero: # Template untuk membuat objek Hero
    jumlah = 0 # Variabel kelas, variabel statik
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Variabel instance
        self.name = inputName      # Menetapkan nama Hero
        self.health = inputHealth  # Menetapkan kesehatan Hero
        self.power = inputPower    # Menetapkan kekuatan Hero
        self.armor = inputArmor    # Menetapkan armor Hero
        Hero.jumlah += 1           # Menambahkan 1 ke variabel kelas jumlah
        print("membuat Hero dengan nama " + inputName) # Pesan pembuatan Hero

# Membuat instance objek Hero dengan menggunakan constructor (__init__)
hero1 = Hero("sniper", 100, 10, 4) # Membuat objek hero1
print(Hero.jumlah) # Mencetak jumlah objek Hero saat ini (1)
hero2 = Hero("mirana", 100, 15, 1) # Membuat objek hero2
print(Hero.jumlah) # Mencetak jumlah objek Hero saat ini (2)
hero3 = Hero("ucup", 1000, 100, 0) # Membuat objek hero3
print(Hero.jumlah) # Mencetak jumlah objek Hero saat ini (3)

#################################
class Hero:
    # Variabel kelas
    jumlah_hero = 0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Variabel instance
        self.name = inputName    # Menetapkan nama Hero
        self.health = inputHealth   # Menetapkan kesehatan Hero
        self.power = inputPower    # Menetapkan kekuatan Hero
        self.armor = inputArmor    # Menetapkan armor Hero
        Hero.jumlah_hero += 1    # Menambahkan 1 ke jumlah_hero saat objek Hero dibuat
        
    # Metode tanpa argumen dan return (void function)
    def siapa(self):
        print("Namaku adalah " + self.name)
        
    # Metode dengan argumen, tanpa return
    def healthUp(self, up):
        self.health += up   # Menambahkan nilai kesehatan dengan nilai up
        
    # Metode dengan return
    def getHealth(self):
        return self.health   # Mengembalikan nilai kesehatan
        
# Membuat instance objek Hero menggunakan constructor (__init__)
hero1 = Hero('sniper', 100, 10, 5)   # Membuat objek hero1
hero2 = Hero('mario bros', 90, 5, 10)   # Membuat objek hero2

hero1.siapa()   # Memanggil metode siapa() dari objek hero1
hero1.healthUp(10)   # Memanggil metode healthUp() dari objek hero1 dengan nilai 10
print(hero1.health)   # Mencetak kesehatan hero1 setelah ditambah 10
print(hero1.getHealth())   # Memanggil metode getHealth() dari objek hero1 dan mencetak nilai kesehatannya

########################

class Hero:
    
    def __init__(self, name, health, attackPower, armorNumber):
        # Constructor untuk menginisialisasi atribut-atribut objek Hero
        self.name = name                # Nama Hero
        self.health = health            # Kesehatan Hero
        self.attackPower = attackPower  # Kekuatan serangan Hero
        self.armorNumber = armorNumber  # Angka armor Hero
        
    def serang(self, lawan):
        # Metode untuk menyerang lawan
        print(self.name + ' menyerang ' + lawan.name)  # Mencetak pesan serangan
        lawan.diserang(self, self.attackPower)         # Memanggil metode diserang() lawan dengan attackPower sendiri
        
    def diserang(self, lawan, attackPower_lawan):
        # Metode untuk menanggapi serangan dari lawan
        print(self.name + ' diserang ' + lawan.name)  # Mencetak pesan diserang
        attack_diterima = attackPower_lawan / self.armorNumber  # Menghitung serangan yang diterima
        print('Serangan terasa : ' + str(attack_diterima))       # Mencetak serangan yang diterima
        self.health -= attack_diterima    # Mengurangi kesehatan berdasarkan serangan yang diterima
        print('Darah ' + self.name + ' tersisa ' + str(self.health))  # Mencetak sisa kesehatan
        
# Membuat objek Hero
sniper = Hero('sniper', 100, 10, 5)      # Membuat objek Hero dengan nama "sniper"
rikimaru = Hero('rikimaru', 100, 20, 10)  # Membuat objek Hero dengan nama "rikimaru"

# Sniper menyerang Rikimaru
sniper.serang(rikimaru)
print("\n")
# Rikimaru menyerang Sniper
rikimaru.serang(sniper)

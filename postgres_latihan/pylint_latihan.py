"""My Perfect Code Example

This should eventually get 10/10 points
"""
# Sembunyikan peringatan jika tidak sesuai sehingga masalah lain tidak disembunyikan.
#pylint: disable=trailing-whitespace
#pylint: disable=missing-final-newline
# Peringatan masing-masing diidentifikasi dengan nama simbolis ( empty-docstring) Peringatan khusus Google dimulai dengan g-.

class MyPerson:
    """
    Person class
    """
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.AskedForName = False #pylint: disable=invalid-name
        
    def get_name(self):
        """
        Returns the name of the person

        :returns: the name
        """
        self.AskedForName = True
        return self.name
    
    def get_age(self):
        """
        Returns the age of the person

        :returns: the age
        """
        return self.age
    
mike = MyPerson("Mike", 20, "m")
print(mike.get_name())
print(mike.get_age())
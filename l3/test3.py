class Cat:
    def __init__(self, _name, age):
        self.__name = _name
        self.age = age

    name = property() # Создание свойства name без методов контроля

    @name.getter
    def name(self):
        print("call get name")
        return self.__name

    @name.setter
    def name(self, name_value):
        print("call set name")
        self.__name = name_value

    @name.deleter
    def name(self):
        print("call remove name")
        del self.__name

iter

cat = Cat('Barsik', 3)
print(cat.name)
cat.name =  "Devil"
del cat.name
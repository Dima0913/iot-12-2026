from enum import Enum
 
 
class ClothingType(Enum):
    SHIRT = "сорочка"
    JEANS = "джинси"
    JACKET = "куртка"
    SWEATER = "светр"
    HAT = "шапка"
 
 
class Clothing:
    def __init__(self, name="Невідомо", description="Невідомо",
                 location="Невідомо", colour="Невідомо", size=0,
                 clothing_type=ClothingType.SHIRT):
        self.__name = name
        self.__description = description
        self.__location = location
        self.__colour = colour
        self.__size = size
        self.__type = clothing_type
 
    @property
    def name(self):
        return self.__name
 
    @property
    def description(self):
        return self.__description
 
    @property
    def location(self):
        return self.__location
 
    @property
    def colour(self):
        return self.__colour
 
    @property
    def size(self):
        return self.__size
 
    @property
    def type(self):
        return self.__type
 
    def is_warm(self):
        return self.__type in (
            ClothingType.JACKET, ClothingType.SWEATER, ClothingType.HAT)
 
    def __str__(self):
        return (f"{self.__name} ({self.__type.value}), "
                f"{self.__description}, {self.__location}, "
                f"{self.__colour}, розмір {self.__size}")
 
    def __del__(self):
        print(f"Одяг видалено: {self.__name}")
 
 
class Wardrobe:
    def __init__(self, owner="Невідомо"):
        self.__owner = owner
        self.__items = []
 
    @property
    def owner(self):
        return self.__owner
 
    @property
    def items(self):
        return list(self.__items)
 
    def add(self, item):
        self.__items.append(item)
 
    def sort_by_size(self):
        self.__items.sort(key=lambda item: item.size)
 
    def print_items(self):
        print(f"Шафа: {self.__owner}")
        for number, item in enumerate(self.__items, start=1):
            print(f"  {number}. {item}")
 
    def __del__(self):
        print(f"Шафу видалено: {self.__owner}")
 
 
def are_go_out(clothes):
    count = len({item.type for item in clothes})
    answer = "так" if count > 3 else "ні"
    print(f"Типів одягу: {count}. Готовий вийти: {answer}")
 
 
def main():
    wardrobe = Wardrobe("Іван")
    wardrobe.add(Clothing("Zara", "бавовна", "шафа", "білий", 48))
    wardrobe.add(Clothing(
        "Levi's", "прямі", "полиця", "синій", 46, ClothingType.JEANS))
    wardrobe.add(Clothing(
        "Nike", "зимова", "вішалка", "чорний", 52, ClothingType.JACKET))
    wardrobe.add(Clothing(
        "H&M", "вовна", "полиця", "сірий", 50, ClothingType.SWEATER))
    wardrobe.add(Clothing())
 
    wardrobe.sort_by_size()
    wardrobe.print_items()
    are_go_out(wardrobe.items)
 
    for item in wardrobe.items:
        print(f"{item.name}: тепла річ - {item.is_warm()}")
 
    small = Wardrobe("Марія")
    small.add(Clothing("Mango", "літня", "шафа", "рожевий", 44))
    are_go_out(small.items)
 
 
if __name__ == "__main__":
    main()
 
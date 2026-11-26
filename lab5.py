from enum import Enum


class ClothingType(Enum):
    SHIRT = "сорочка"
    JEANS = "джинси"
    JACKET = "куртка"
    SWEATER = "светр"
    HAT = "шапка"


def _check_text(value, field):
    """Перевіряє, що значення - непорожній рядок."""
    if not isinstance(value, str):
        raise TypeError(f"{field} має бути рядком, отримано {type(value).__name__}")
    if not value.strip():
        raise ValueError(f"{field} не може бути порожнім")
    return value.strip()


class Clothing:
    def __init__(self, name="Невідомо", description="Невідомо",
                 location="Невідомо", colour="Невідомо", size=0,
                 clothing_type=ClothingType.SHIRT):
        # Валідація типів і значень
        self.__name = _check_text(name, "Назва")
        self.__description = _check_text(description, "Опис")
        self.__location = _check_text(location, "Місцезнаходження")
        self.__colour = _check_text(colour, "Колір")

        # bool є підкласом int, тому його виключаємо окремо
        if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError("Розмір має бути цілим числом")
        if size < 0:
            raise ValueError("Розмір не може бути від'ємним")
        self.__size = size

        if not isinstance(clothing_type, ClothingType):
            raise TypeError("Тип одягу має бути елементом ClothingType")
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

    @location.setter
    def location(self, value):
        # Дозволяє переміщувати річ після створення
        self.__location = _check_text(value, "Місцезнаходження")

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
        # Якщо __init__ впав до встановлення атрибута - не падаємо
        name = getattr(self, "_Clothing__name", "невідомо (не ініціалізовано)")
        print(f"Одяг видалено: {name}")


class Wardrobe:
    def __init__(self, owner="Невідомо"):
        self.__owner = _check_text(owner, "Власник")
        self.__items = []

    @property
    def owner(self):
        return self.__owner

    @property
    def items(self):
        return list(self.__items)

    def add(self, item):
        if not isinstance(item, Clothing):
            raise TypeError("До шафи можна додати лише об'єкт Clothing")
        self.__items.append(item)

    def sort_by_size(self):
        self.__items.sort(key=lambda item: item.size)

    def print_items(self):
        print(f"Шафа: {self.__owner}")
        for number, item in enumerate(self.__items, start=1):
            print(f"  {number}. {item}")

    def __del__(self):
        owner = getattr(self, "_Wardrobe__owner", "невідомо (не ініціалізовано)")
        print(f"Шафу видалено: {owner}")


def are_go_out(clothes):
    count = len({item.type for item in clothes})
    is_ready = count > 3
    answer = "так" if is_ready else "ні"
    print(f"Типів одягу: {count}. Готовий вийти: {answer}")
    return is_ready


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

    if are_go_out(wardrobe.items):
        print("Можна виходити!")

    for item in wardrobe.items:
        print(f"{item.name}: тепла річ - {item.is_warm()}")

    # Демонстрація сеттера: переміщуємо річ
    wardrobe.items[0].location = "валіза"

    small = Wardrobe("Марія")
    small.add(Clothing("Mango", "літня", "шафа", "рожевий", 44))
    are_go_out(small.items)


if __name__ == "__main__":
    main()
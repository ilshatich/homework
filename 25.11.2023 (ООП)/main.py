class Bowl:
    food_amount = 0

    def add_food(self, amount: int):
        self.food_amount += amount

    def remove_food(self, amount: int):
        self.food_amount -= amount

    def is_food_avialable(self, amount_to_be_ate):
        if self.food_amount < amount_to_be_ate:
            return False
        return True

class Cat:
    def __int__(self, name: str, cat_id: int, cat_type: str, energy: int, eat_amount: int):
        self.name = name
        self.__energy = energy
        self.__cat_id = cat_id
        self.__cat_type = cat_type
        self.__eat_amount = eat_amount
        self.__bowl = Bowl()

    def get_energy(self):
        return self.__energy

    def get_id(self):
        return self.__cat_id

    def get_cat_type(self):
        return self.__cat_type

#0 -- все ок, 1 -- покормили, 2 -- нужно покормить

    def get_status(self):
        if self.__energy >= 100:
            return 1
        elif self.__energy in range(5, 40):
            return 2
        else:
            return 0

    def meow(self):
        if self.get_status()==0:
            print('Meow!')
            self.__energy -= 1

    def eat(self):
        if not self.__bowl.is_food_available(self.__eat_amount):
            print('MEOW!!!!')
        else:
            if self.__energy + self.__eat_amount > 100:
                self.__energy == 100
            else:
                self.__energy += self.__eat_amount

            self.__bowl.remove_food(self.__eat_amount)

    def __str__(self):
        return f'{self.__cat_id} {self.name} {self.__energy} {self.__cat_type}'

    def __repr__(self):
        return (f"Cat(cat_id={self.__cat_id}, name = '{self.name}',"
                f"energy = {self.__energy}, cat_type = '{self.__cat_type}', eat_amount = {self.__eat_amount}")

cat = Cat( name = 'Barsik', cat_id = 1, cat_type='Персидская', eat_amount=20, energy=70)

print(cat.__str__())
print(cat.__repr__())
cat_1 = eval(cat.__repr__())
print(type(cat_1))


#Вторая пара


class Cat_Manager():
    def __int__(self):
        self.__cats = []

    def __getitem__(self, cat_id: int):
        for cat in self.__cats:
            if cat.get_id() == cat_id:
                return cat

        raise ValueError('No cat found')

    def __setitem__(self, key, value):
        if isinstance(key, int):
            if not self.__getitem__(key):
                self.__cats.append(value)
                print('New cat added successfully')
            else:
                index = self.__cats.index(value)
                self.__cats[index] == value
        else:
            raise ValueError('No such keys')

    def add_cat(self, cat: Cat):
        if cat.get_id() not in [added_cat.get_id() for added_cat in self.__cats]:
            self.__cats.append(cat)
        else:
            raise ValueError('Car is already added')

    def del_cat(self, cat: Cat):
        if cat.get_id() in [added_cat.get_id() for added_cat in self.__cats]:
            self.__cats.remove(cat)

    def get_cats_by_status(self, status: str):
        if status not in [0,1,2]:
            raise ValueError('Invalid status')

        return_list = []
        for cat in self.__cats:
            if cat.get_status() == status:
                return_list.append(cat)

    def __str__(self):
        return f"{self.__cats}"


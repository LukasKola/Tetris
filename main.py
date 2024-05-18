class Zoo :
    animals = []
    released = 0
    def __init__(self, initial_animals):
        self.animals = initial_animals
    
    def add_animal(self, animal):
        self.animals.append(animal)

    def release_animal(self, animal):
        user_input = animal
        def check_if_animal_in_zoo():
            if animal not in self.animals:
                print('We dont have this animal in our zoo, still want release animal? If yes choose one of these then {animals}, otherwise write "No".'.format(animals=','.join(self.animals)))
                animal_to_release = input()
                if animal_to_release.capitalize() == 'No':
                    return False
                if animal_to_release not in self.animals:
                    check_if_animal_in_zoo()
            return animal_to_release
        
        user_input = check_if_animal_in_zoo()
        if not user_input:
            return
        print(user_input)
        self.animals.remove(user_input)
        self.released += 1
        print('You released {} to wilderness.'.format(user_input))

    def feed_animal(self):
        picked_animal = False
        while not picked_animal:
            print('Which animal u want to feed, in our zoo we have these: {}.'.format(','.join(self.animals)))
            animal_from_input = input()
            if animal_from_input in self.animals:
                picked_animal = True
                print('Thank you for feeding our {}!'.format(animal_from_input))
            else:
                print('We dont have this animal in zoo, try again')
    def __repr__(self) -> str:
        if self.released < 1:
            return 'Welcome to our zoo, we have these awesome animals : {animals}.'.format(animals=','.join(self.animals))
        return 'Welcome to our zoo, we have these awesome animals : {animals} and we released {number} animals to wildernes.'.format(animals=','.join(self.animals), number=self.released)

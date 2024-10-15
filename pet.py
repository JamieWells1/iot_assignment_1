import random
import time
import threading

start_time = time.time()

activities = ['done a backflip!', 'eaten a caterpillar!', 'squashed a plant!', 'broken a lamp!']
exercises = ['Go for a walk', 'Play catch', 'Play hide and seek', 'Do a dance']
foods = ['Fruit salad', 'Cheese', 'Baguette', 'Spaghetti']

age_calculations = {}

age_amplifier = random.randint(0, 1)
if age_amplifier == 0:
    age_calculations = {'slower': 1 / random.randint(1, 100)}
else:
    age_calculations = {'faster': 1 * random.randint(1, 100)}

def check_age():
    while True:
        if time.time() - start_time > 5000:
            print('Your pet died of old age!')
            break
        time.sleep(2)

age_checker = threading.Thread(target=check_age)
age_checker.daemon = True
age_checker.start()

planet_prefixes_dict = {
    0: 'Zar',
    1: 'Lam',
    2: 'Sep',
    3: 'Rig',
    4: 'Ro',
    5: 'Tyn',
    6: 'Del',
    7: 'Gan',
    8: 'Jed'
}

planet_suffixes_dict = {
    0: 'dar',
    1: 'ith',
    2: 'arsk',
    3: 'hoff',
    4: 'heb',
    5: 'seep',
    6: 'raz',
    7: 'asant'
}

alien = """

     .-""-.
    / _  _ \\
    |  O O  |
    |   ∆   |
     \\_____/
     /     \\
    /_______\\

"""


class Pet:
    def __init__(self, pet_name, age_calculations):
        self.past_interactions = {}
        self.pet_hunger = random.randint(5, 10)
        self.pet_fitness = random.randint(5, 10)
        self.pet_energy = random.randint(5, 10)
        self.owner_fondness = random.randint(1, 10)
        self.pet_name = pet_name
        self.pet_planet = planet_prefixes_dict[random.randint(0, len(planet_prefixes_dict) - 1)]+planet_suffixes_dict[random.randint(0, len(planet_suffixes_dict) - 1)]
        self.age_calculations = age_calculations
        self.favourite_food = random.choice(foods)
        self.least_favourite_food = self.get_least_favourite_food()
        self.favourite_exercise = random.choice(exercises)
        self.least_favourite_exercise = self.get_least_favourite_exercise()

    def get_least_favourite_food(self):
        self.least_favourite_food = random.choice(foods)
        while self.least_favourite_food == self.favourite_food:
            self.least_favourite_food = random.choice(foods)
        return self.least_favourite_food

    def get_least_favourite_exercise(self):
        self.least_favourite_exercise = random.choice(exercises)
        while self.least_favourite_exercise == self.favourite_exercise:
            self.least_favourite_exercise = random.choice(exercises)
        return self.least_favourite_exercise

    def view_stats(self):
        print(alien)
        print(f"{self.pet_name}'s stats:\n")
        print(f'Hunger:')
        print('█ ' * self.pet_hunger + '- ' * (10 - self.pet_hunger))
        print(f'\nFitness:')
        print('█ ' * self.pet_fitness + '- ' * (10 - self.pet_fitness))
        print(f'\Energy:')
        print('█ ' * self.pet_energy + '- ' * (10 - self.pet_energy))
        print(f'\nOwner fondness:')
        print('█ ' * self.owner_fondness + '- ' * (10 - self.owner_fondness))
        self.check_stats()

    def check_stats(self):
        while self.pet_hunger < 8 or self.pet_fitness < 8 or self.pet_energy < 8 or self.owner_fondness < 5:
            if self.pet_hunger < 8:
                self.increase_stats('hunger')
            elif self.pet_fitness < 8:
                self.increase_stats('fitness')
            elif self.pet_energy < 8:
                self.increase_stats('energy')
            else:
                self.increase_stats('fondness')
        user_input = input(f'\n{self.pet_name} is ready to go! (i) View past interactions | (a) View age | (c) Continue ')
        if user_input == 'i':
            print(self.past_interactions)
            check_stats()
        elif user_input == 'a':
            if 'slower' in age_calculations:
                print(f"\n{self.pet_name} is from the planet {self.pet_planet} and ages", int(1 / age_calculations['slower']), f"times slower! They are {(time.time() - start_time) * age_calculations['slower']:.1f} seconds old.")
                check_stats()
            if 'faster' in age_calculations:
                print(f"\n{self.pet_name} is from the planet {self.pet_planet} and ages", age_calculations['faster'], f"times faster! They are {(time.time() - start_time) * age_calculations['faster']:.1f} seconds old.")
                check_stats()
        elif user_input == 'c':
            print('')
            # Do something
        else:
            print('Invalid input')
            check_stats()

    def increase_stats(self, stat):
        if stat == 'hunger':
            self.food()
        elif stat == 'fitness':
            self.exercise()
        elif stat == 'energy':
            self.sleep()
        elif stat == 'fondness':
            self.like()

    def food(self):
        print(f'\nYour pet has {self.pet_hunger} hunger points! Input one of the following to feed them:\n')
        choice = input(f'(f) {foods[0]} | (c) {foods[1]} | (b) {foods[2]} | (s) {foods[3]} ')
        food_choices = {
            'f': foods[0],
            'c': foods[1],
            'b': foods[2],
            's': foods[3]
        }
        food = food_choices.get(choice)

        if food == self.favourite_food:
            print(f"Yum, you picked {self.pet_name}'s favourite food! +3 hunger points")
            self.pet_hunger += 3
            self.past_interactions['feed'] = '+3'
        elif food == self.least_favourite_food:
            print(f"Ugh, you picked {self.pet_name}'s least favourite food! +1 hunger point")
            self.pet_hunger += 1
            self.past_interactions['feed'] = '-1'
        elif food in food_choices:
            print(f"You picked {food}. +2 hunger point")
            self.pet_hunger += 2
            self.past_interactions['feed'] = '+2'
        else:
            print('Invalid input')

    def exercise(self):
        print(f'\nYour pet has {self.pet_fitness} fitness points! Input one of the following to give them some exercise:\n')
        choice = input(f'(w) {exercises[0]} | (c) {exercises[1]} | (h) {exercises[2]} | (d) {exercises[3]} ')
        exercise_choices = {
            'w': exercises[0],
            'c': exercises[1],
            'h': exercises[2],
            'd': exercises[3]
        }
        exercise = exercise_choices.get(choice)

        if exercise == self.favourite_exercise:
            print(f"Nice, you picked {self.pet_name}'s favourite exercise! +3 fitness points")
            self.pet_fitness += 3
            self.past_interactions['exercise'] = '+3'
        elif exercise == self.least_favourite_exercise:
            print(f"Ugh, you picked {self.pet_name}'s least favourite exercise! +1 fitness point")
            self.pet_fitness += 1
            self.past_interactions['exercise'] = '-1'
        elif exercise in exercise_choices:
            print(f"You picked {exercise}. +2 fitness point")
            self.pet_fitness += 2
            self.past_interactions['exercise'] = '+2'
        else:
            print('Invalid input')

    def sleep(self):
        user_input = input(f'\nYour pet has {self.pet_energy} energy points and needs to sleep! Type (s) to put them to sleep or (w) to keep them awake: ')
        if user_input == 's':
            sleep_time = 5 * (10 - self.pet_energy)
            print(f'\n{self.pet_name} needs to sleep for {sleep_time} seconds! Let them rest 💤 or type (w) to wake them up')
            for i in range(int(sleep_time / 5)):
                time.sleep(2.5)
                print(f'{self.pet_name} is sleeping. Zzz')
                time.sleep(2.5)
                self.pet_energy += 1
                print(f"{self.pet_name}'s energy has gone up to {self.pet_energy}")


    def like(self):
        user_input = input(f'\nYour pet has {self.pet_energy} fitness points! Input one of the following to give them some sleep:\n')


# <------ Script start!!!! ------>

pet_name = input('Welcome your virtual pet to the world by giving them a name: ')
pet = Pet(pet_name, age_calculations)
pet.view_stats()
age_checker.join()
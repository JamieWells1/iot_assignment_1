import random

activities = ['done a backflip!', 'eaten a caterpillar!', 'squashed a plant!', 'broken a lamp!']
excercises = ['Go for a walk', 'Play catch', 'Play hide and seek', 'Do a dance']
foods = [
    'Fruit salad',
    'Cheese',
    'Baguette',
    'Spaghetti'
]
past_interactions = {}
pet_hunger = random.randint(5, 10)
pet_fitness = random.randint(5, 10)
pet_energy = random.randint(5, 10)
owner_fondness = random.randint(1, 10)
aging_multiplier = random.randint(0, 5)

favourite_food = foods[random.randint(0, 3)]
favourite_excercise = excercises[random.randint(0, 3)]

# <------------ functions ------------>

def view_stats():
    print(f"\n{pet_name}'s stats:\n")
    print(f'Hunger:')
    print('█ ' * pet_hunger, '- ' * (10 - pet_hunger))
    print(f'\nFitness:')
    print('█ ' * pet_fitness, '- ' * (10 - pet_fitness))
    print(f'\nTiredness:')
    print('█ ' * pet_energy, '- ' * (10 - pet_energy))
    print(f'\nOwner fondness:')
    print('█ ' * owner_fondness, '- ' * (10 - owner_fondness))
    check_stats(pet_hunger, pet_fitness, pet_energy, owner_fondness)

def check_stats(hunger, fitness, energy, fondness):
    while hunger < 8 or fitness < 8 or energy < 8 or fondness < 5:
        if hunger < 8:
            increase_stats('hunger', hunger)
        elif fitness < 8:
            increase_stats('fitness', fitness)
        elif tiredness < 8:
            increase_stats('energy', pet_energy)
        else:
            increase_stats('fondness', fondness)

def increase_stats(stat, current_value):
    if stat == 'hunger':
        feed(current_value)

def feed(current_value):
    print(f'\nYour pet has {current_value} hunger points!\n')
    choice = input(f'(f) {foods[0]} | (c) {foods[1]} | (b) {foods[2]} | (s) {foods[3]}')


# <------------ script start ------------>

pet_name = input('Welcome your virtual pet to the world by giving them a name: ')
view_stats()
print('1:')
for i in range(12, 25):
    print(i, end=' ')
print()

print('2:')
for i in range(7, 33, 2):
    print(i, end=' ')
print()

print('3:')
for i in range(10, 22, 2):
    print(i, end=' ')
print()

print('4:')
for i in range(1, 46):
    if i % 3 == 0:
        print(i, end=': Fizz ,')
    if i % 5 == 0:
        print(i, end=': Buzz ,')
    if i % 5 == 0 and i % 3 == 0:
        print(i, end=': FizzBuzz ,')
print()

print('5:')


def def_5(list5: list[int]):
    sum: int = 0
    for num in list5:
        sum += num
    return sum


print(def_5([1, 13, 22, 123, 49, 34, 5, 24, 57, 45]))

print('6,1:')


def remove(studentss: list[dict], key) -> None:
    for student in studentss:
        if key in student:
            del student[key]


students: list[dict] = [
    {'id': 111, 'name': 'tomer', 'last name': 'cohn', 'age': 21, 'country': 'Israel', 'city': 'Haifa'},
    {'id': 222, 'name': 'liel', 'last name': 'or', 'age': 34, 'country': 'Israel', 'city': 'Tel Aviv'},
    {'id': 333, 'name': 'ortal', 'last name': 'ist', 'age': 22, 'country': 'Israel', 'city': 'Netanya'},
]

remove(students, 'country')
print(students)

print('6.2:')


def prints(studentss: list[dict]):
    for student in studentss:
        print('student:')
        for key, value in enumerate(student):
            print(f'{key}:{value}')


prints(students)
print(students)

print('6.3:')
print(sorted(students, key=lambda p: p['age'], reverse=True))

print('7.1:')
our_pets = [{"animal_type": "cat",
             "names": [
                 "Meowzer",
                 "Fluffy",
                 "Kit-Cat"]},
            {"animal_type": "dog",
             "names": [
                 "Spot",
                 "Bowser",
                 "Frankie"]}]


def only_cats(animals):
    for animal in animals:
        if animal['animal_type'] == 'cat':
            print(animal)


only_cats(our_pets)

print('7.2:')


def animal_names(animals: list[dict], animal_type: str):
    for animal in animals:
        if animal["animal_type"] == animal_type:
            print(f'{animal_type}:')
            for name in animal["names"]:
                print(f'names: {name}')
            return
    print('not in the list')


animal_names(our_pets, "cat")

print('7,3:')


def if_name_exists(animals: list[dict], animal_name: str):
    for animal in animals:
        if animal_name in animal["names"]:
            print(f'the name:{animal_name} is already exists')
        else:
            animal["names"].append(animal_name)


if_name_exists(our_pets, "Fluffy")
print(our_pets)

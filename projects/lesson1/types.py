name = 'Evgeniy'
b = 'Привет,{}'.format(name)
print(b)
v = int(input('Введите числа от 1 до 10: '))
m = 10
n = v+m
print(n)
numbers=[3,5,7,9,10.5]
print(numbers[0])
planet = {
    "city": "Moscow",
    "temperature": 20
}
print(planet["city"])
planet["temperature"]= planet["temperature"]-5
print(planet["temperature"])
print(planet.get("country"))
planet.get("coutry","Russia")
print(planet["country"])
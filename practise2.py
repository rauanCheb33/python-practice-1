#variant B

name = input('Enter name: ')
destination = input('Enter destination: ')
distance = float(input('Enter distance: '))
fuel_cons = float(input('Enter fuel consumption (L/100km): '))
fuel_price = float(input('Enter fuel price (KZT/L): '))

litres_needed = distance*fuel_cons/100
fuel_cost = litres_needed*fuel_price
trip_cat = ''
if distance<100 :
    trip_cat = 'Sort trip'
elif distance >= 100 and distance<= 500 :
    trip_cat = 'Medium trip'
elif distance >= 500:
    trip_cat = 'Long trip'

print(' ')
print('='*30)
print('Driver: ', name)
print('Destination: ', destination)
print(f'Distance: {distance} km')
print(f'Fuel cost: {fuel_cost} KZT')
print(f'Category: {trip_cat}')
print('='*30)

for i in range(100, int(distance) +1, 100):
    
    total_cost = (fuel_cons*i/100)*fuel_price
    print(f'{i} km -> {total_cost} KZT')
upper_dest = destination.upper()
lower_dest = destination.lower()
count_a = lower_dest.count('a')

print('='*30)

print(f'Destination uppercase: {upper_dest}')
print(f'Destination lowercase: {lower_dest}')
print(f'Length {len(destination)}')
print(f'Letter "a" count: {count_a}')


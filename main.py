# variant B

driver  = input('Your name:  ')
distance  = float(input('Distance in km: '))
fuel_cons = float(input('Fuel consuption(per 100 km in litres): '))
fuel_price = float(input('Fuel price (per litre in KZT): '))

litres_needed = distance*fuel_cons/100
total__fuel_cost = fuel_price* litres_needed
cost_per_km = total__fuel_cost/distance 

print('==============================')
print(' ')
print('      ROAD TRIP SUMMARY')
print(' ')
print('==============================')
print(' ')
print(f'Driver: {driver}')
print(f'Distance: {distance} km')
print(f'Concuption {fuel_cons}/100')
print(f'Fuel price: {fuel_price} KZT/L')
print(' ')
print('------------------------------')
print(' ')
print(f'Litres needed: {litres_needed} L')
print(f'Fuel cost: {total__fuel_cost} KZT')
print(f'Cost per km: {cost_per_km} KZT')
print(' ')
print('==============================')

print('Trip longer than 300 km: ', distance>300 )
print('Fuel cost above 5000 KZT: ', total__fuel_cost>5000)



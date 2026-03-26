# name  = 'Rauan'
# age = 18
# print('My name is '+ name )
# print(f'My age is {age}'




original_price = float(input('Enter original price: '))
discount = original_price*0.2
sale_price = original_price-discount
print('The sale price is', sale_price)


sec = float(input ("Enter the number of seconds: "))
day = sec // (24 * 3600)
hour = (sec % (24 * 3600)) // 3600
min = ((sec % (24 * 3600)) % 3600) // 60
print ("The number of days, hours and minutes are: ", day, "days", hour, "hours", min, "minutes")


test1 = float(input("Enter a first result : "))
test2 = float(input("Enter a second result : "))
test3 = float(input("Enter a third result : "))
avg = (test1 + test2 + test3) / 3 
print("Average:", avg)


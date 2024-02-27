# even or odd:

a = int(input('Type a numeric value: '))

if a % 2 == 0:
    print(f'The value of a {a} is an even number')
else:
    print(f'The value of a {a} is an odd number')

# of legal age
age_of_an_adult = 18
age_of_person = int(input("Provide your age: "))

if age_of_person >= age_of_an_adult:
    print(f'The person with age {age_of_person} is an adult')
else:
    print(f'The person with age {age_of_person} is a minor')

# range
value = int(input('type the value: '))
minimum_value = 0
value_maximum = 5

within_Range = value >= minimum_value and value <= value_maximum

if within_Range:
    print(f'Value {value} is within range')
else:
    print(f'Value {value} is out of range')

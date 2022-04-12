number = -34132

revs_number = 0
counter = 0
result = ''

if number < 0:
    negative = True
    number *= -1

while number > 0:
    # Logic
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10
    counter += 1
    result += str(remainder)
    print('resutl',counter,'#',result)
    print(counter,'#')
    print('remainder=', remainder)
    print('revs=', revs_number)
    print('number=', number)
if negative:
    revs_number *= -1
result *= -1
print('resutls=',revs_number)
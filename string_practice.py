#print('This is a basic string')
name = 'Chokmaradmah'

#print('Hi, my name is', name, '.')
# extra space in the above
#it prints 3 seperate strings.
#strings by nature add etra space by default

#print('Hi, my name is '+ name + '.')
# this makes one string by concatenating

#print(f'Hi, my name is {name}.')
# this is a f string
# this is the  most powerful type of string
#it tells the comp that it is just one string

#print('hi, i\'m really excited to be here! (:'.upper())
# .upper() is a method that turns string upper case
#print('hi, i\'m really excited to be here! (:'.lower())
# .lower() is a method that turns string lower case

password_info = "DONT FORGET, password is 1234. remember, 1234. that's your password."
#print(password_info.replace(1234, "****"))
# the above will not work because 1234 is a number and not string
#print(password_info.replace("1234", "****"))

sentence = 'How many times does the letter "t" show up in this string'
#print(sentence.count('t'))
#count() will count the instance of the argument

#print("7", 7)
#they look the same
#print(type('7'), type(7), type(7.0))

#booleans

phone_num = '718 555 1234'
is_nyc = phone_num.startswith('718')

#print(phone_num)
#print(is_nyc)
#print(type(is_nyc))

#there is a endswith() as well

name = input("What is your name?")
print(f'Hello, {name}!')
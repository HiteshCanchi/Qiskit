message = 'Hello I like Your Lie In April'

print(message)
print(len(message)) #gives length of msg

print(message[15])
print(message[0:5]) #this prints all the words from 0 to 5 but not including 5. Index starts from 0. kinda like [0,5)
                    #this can also be written as print(message[:5]) if you wanna start from the beginning.
print(message[25:])

print(message.lower()) #converts everything to lowercase
print(message.upper())

print(message.count('l')) #number of times a char or string is.

print(message.find('Lie')) #Index at which "Lie" starts

message = message.replace('like', 'love')
print (message) #must use message = and not just message.replace

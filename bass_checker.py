number_of_basses = int(input('How many bass guitars do you have? '))

if number_of_basses > 50:
    print('Congrats you are a rock star with many bass guitars!')
elif number_of_basses > 0:
    print('You have at least 1 bass guitar')
else:
    print('You are not a rock star because you have no bass guitars')
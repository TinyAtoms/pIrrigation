user_input = 'random'
crop_list = [''] #import from db
growth_periods = ['early', 'developing', 'mature', 'late']

def menu_1():
    print('Hello and welcome to the menu of your irrigation system.')
    print('What would you like to do?')
    print('1. Add a new CG (crop group)')
    print('2. Edit information of a CG')
    print('3. View information of a CG ')
    print('[Exit]')

def select_crop():
    for crop in list:
        n = 0
        print(n,'.', crop)
        n = n + 1
    return input('>>> ')

    






while user_input != '4':
user_input = input('>>> ')
    if user_input == '1':
        print('What is the type of your crop?')
        crop = select_crop() 
        crop_name = 'something' #import from db based on index number
        print('What is the distance between individual crops?')
        d = input('>>> ')

        print('In what growth period is your crop?')
        print('Choose from')


        print('At what time should your crop be irrigated? [hh:mm] If no answer is supplied, the default time will be configured')
        user_input = input('>>> ')
        if user_input == '':
            time = '07:30'
        else time = user_input 

        print('In what slot would you like to assign your CG?')
        slot = input('>>> ')
        #now create object with given information, kc imported based on crop and growth stage 
        #duration calculated based on distance and kc, for future usage with et

        print('Success.')

    elif user_input == '2':
        print('Which slot would you like to edit? ')

    elif user_input == '3':

    elif user_input == 'Exit':
        print('Goodbye')
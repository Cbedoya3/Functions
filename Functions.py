# Defining a function
def greet_user():
    """Display a simple greeting"""
    print("hello")

greet_user()

# #Passing information to a function
# def greet_user(username):
#      """Display a simple greeting."""
#      print(f"hello, {username.title()}!")
#
# greet_user('jesse')
#
# #Arguments and parameters
# def describe_pet(animal_type,pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My pets name is {pet_name.title()}.")
#
# describe_pet('hamster','harry')
#
# #Multiple function calls is a more efficient way to code
# describe_pet('hamster','harry')
# describe_pet('dog','junior')

#with keyword arguments the order dont matter because python knows where each value should go
#describe_pet(animal_type='hamster',pet_name='harry')

#Default values
# def describe_pet(pet_name,animal_type = 'dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My pets name is {pet_name.title()}.")
#
# describe_pet(pet_name="willie")#same ting
# describe_pet("willie")

#Return values
# def get_formatted_name(first_name,last_name):
#     """Return a full name, neatly formated"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# musician = get_formatted_name('jimi','hendrix')
# print(musician)

#Making an argument optional
# def get_formatted_name(first_name,last_name,middle_name):
#     """Retun a full name, neatly formatted"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# musician = get_formatted_name('john','hooker','')
# print(musician)

#Returning a dictionary
# def build_person(first_name,last_name):
#     """Return a dictionary of information about a person"""
#     person = {'first':first_name,'last':last_name}
#     return person
# musician = build_person('jimi','hendrix')
# print(musician)

# def build_person(first_name,last_name,age=None):
#     """Return a dictionary of information about a person"""
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person
#
# musician = build_person('jimi','hendrix',age=27)
# print(musician)

#Using a function with a while loop
# def get_formatted_name(first_name,last_name):
#     """Return a full name, neatly formated"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# #This is an infinite loop:
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("first name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name,l_name)
#     print(f"\nHello, {formatted_name}!")

#Passing a list
# def greet_users(names):
#     """Print a simple greeting to each user in the list"""
#     for name in names:
#         msg = f"Hello,{name.title()}!"
#         print(msg)
#
# usernames = ['hannah','ty','margot']
# greet_users(usernames)

#Modifying a list in a function
#Start with some designs that need to be printed.
# unprinted_designs = ['phone case','robot pendant','dodecahedron']
# completed_models =[]

#Simulate printing each design, until none are left.
#move each design to completed_models after printing
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"printing model: {current_design}")
#     completed_models.append(current_design)
#
# #Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# unprinted_designs = ['phone case','robot pendant','dodecahedron']
# completed_models =[]
#
# def print_designs(unprinted_designs,completed_models):
#     """Printing each design untill none are left in unprinted designs, move to completed models"""
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"printing model: {current_design}")
#         completed_models.append(current_design)
#     return completed_models
#
# def summarize_prints(completed_models):
#     """printing summary of completed models"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# print_designs(unprinted_designs)
# summarize_prints(completed_models)

#Preventing a function from modifying a list:
#In the previous example we removed the content of the unprinted_designs
#and the empty list is the only version we have. the original is gone.
#we can address this issue by making a copy of the list in question like this
#function_name(list_name[:])
#The slice notation [:] makes a copy of the list to send to the function.
#if we didnt want to empty the lsit of unprinted _designs we could call
#print models like this.
#
# unprinted_designs = ['phone case','robot pendant','dodecahedron']
# completed_models =[]
#
# print_designs(unprinted_designs[:],completed_models)
# print(unprinted_designs)

#Passing an arbitrary Number of arguments
# def make_pizza(*toppings):
#     """print the list of toppings that have been requested"""
#     print(toppings)
#
# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')

#Same thing with a while loop
# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"-{topping}")
#
# make_pizza('pepperoni')
# make_pizza('mushroom','green pepper','extra cheese')

#mixing positional and arbitrary arguments
# def make_pizza(size, *toppings):
#     """summarize the pizza we are about to make"""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"-{topping}")
#
# make_pizza(16,'pepperoni')
# make_pizza(12,'mushroom','green pepper','extra cheese')

#USER_PROFILE
# def build_profile(first,last,**user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['firs_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
# user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')
# print(user_profile)

#NOTE:Youll often see the parameter name **kwargs used to collect non-specific keyword arguments

def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        #print(f"Sorry the file {filename} does not exist.") for this example we will pass
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


'''
For this task, you will be creating the beginning code for this project. You can think of it as a template for the chatbot you will be creating later on in Elite 101. 

Your chatbot template needs to have the following features:


Welcome the user
Collect the user’s name and age
Ask the user how it can help them
Allow the user to choose from a menu/list of options on how they can continue the conversation

Do not worry about the options on the list. For now, they can just be placeholders.

-Include one menu option for exiting the conversation. This option should display a goodbye message and end your program.
'''
#chatbot
#name variable
#age variable
#ask how it can help
#select from a list of options
#one option must end the program

# definition
def chatbot():
  print('Welcome!')
  user_name = input('What is your name?: ')
  user_age = int(input(f'Nice to meet you, {user_name}! What is your age?: '))
  print(f'{user_age}. Interesting! How may I help you?')
  print('Option 1')
  print('Option 2')
  print('Option 3')
  print('Option 4')
  print('Option 5: Exits the program.')
  user_help_input = int(input('Please enter a number from 1-5: '))
  if user_help_input == 1:
    print('Run option 1')
  if user_help_input == 2:
    print('Run option 2')
  if user_help_input == 3:
    print('Run option 3')
  if user_help_input == 4:
    print('Run option 4')
  if user_help_input == 5:
    print('Thank you for using our chatbot! Have a nice day.')
    pass

# body
chatbot()
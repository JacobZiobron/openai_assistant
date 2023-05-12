import keyboard
from prompt import write_query

is_running = True
request_count = 0
options = """Options:
    0 - Show Options Menu
    1 - Rewrite Formal
    2 - Summarize
    3 - Rewrite Informal
    4 - English to Spanish
    5 - Spanish to English
    6 - Exit"""

# show options initially
print(options)

while is_running == True:
    
    # take an input
    choice = input("Request Number " + str(request_count) + ": ")

    if choice == str(0):
        print(options)
    elif choice == str(1):
        write_query("Rewrite the section after the colon to be more formal: ")
    elif choice == str(2):
        write_query("Summarize the section after the colon: ")
    elif choice == str(3):
        write_query("Rewrite the section after the colon to be more informal: ")
    elif choice == str(4):
        write_query("Translate the section after the colon to Spanish: ")
    elif choice == str(5):
        write_query("Translate the section after the colon to English: ")
    elif choice == str(6):
        print("Stopping...")
        is_running = False
    else:
        is_running = False
    
    # increment to show request number
    request_count+=1

# Built in python print function only (by the way, this is a comment. It will not be processed.)
print("We are off to see the Wizard!")

# Print with variable
msg = "We are off to see the Wizard, the Wonderful Wizard of Oz!"
print(msg)

# a function! already? yes they are not so scary!

def msg():


print('lions, tigers, and bears, and functions, oh my!')
    msg()


# Main characters as variables
char_1 = 'Dorothy'
char_2 = 'Scarecrow'
char_3 = 'Tin Woodman'
char_4 = 'Cowardly Lion'
print(f"The main characters of the Wizard of Oz are {char_1}, {char_2}, {char_3}, and {char_4}.")

print("\nThe next bit of code will use the same variables, but will demonstrate the new line character")

# Printed as Markdown list:
print(f"\nThe main characters of the Wizard of Oz in Markdown format: \n\n* {char_1}\n* {char_2}\n* "
      f"{ char_3}\n* {char_4}\n")

# first line is a python list of the main characters and the second line is this list printed as a list:
print("this is a list:")
main_chars = ['Dorothy', 'Scarecrow', 'Tin Woodman', 'Cowardly Lion']
print(main_chars)

# get the first character
first_char = main_chars[0]  # this works but is verbose... not necessary.
print(f"the first character is {first_char} and this is the code that was used: ```main_chars[0]```")

# get the last character
print(f"the last character is {main_chars[-1]}")  # using the f string makes the code more efficient.

# here is the list as a simple loop
print('\nthe following output is the result of a "for" loop\n')
for char in main_chars:
    print(char)

print("\nLet's add the wizard to the main characters list:")
main_chars.append('The Wizard of Oz')
print(main_chars)

print("\nLet\'s \"slice\" the list:")
print(f"The first two Characters are {main_chars[:2]}")

print(f"\nLet\'s copy the list into a potential full cast list and print out this list with a new "
      f"list named \"all_chars\":")
all_chars = main_chars[:]
print(all_chars)

print(f"\nLet\'s add two characters to the copied list and print the char list followed by the original "
      f"main_char list:")
all_chars.append("Wicked Witch of the West")
all_chars.append("Toto")
all_chars.append("Glinda")
print(all_chars)
print(main_chars)
print(f"there are now two versions of the list. This can be beneficial  or create problems if not managed properly.\n")

print(f"Here is an example of how you can use variables a simple loop and "
      f"f strings build a basic webpage with Python:\n")
title = "Wizard of Oz Page"
h1 = "This html page was built with Python!"
lead_p = msg

print(f"<!doctype html>\n"
      f" <html lang=\"en\">\n"
      f"  <head>\n"
      f"   <meta charset=\"utf-8\">\n"
      f"   <title>{title}</title>\n" 
      f"  </head>\n"
      f"  <body>\n"
      f"   <h1>{h1}</h1>\n"
      f"   <p>{lead_p}</p>\n"
      f"   <p>The current list of all characters:</p>\n"
      f"   <ul>")
for char in all_chars:
    print(f"     <li>{char}</li>")
print(f"    </ul>\n"
      f"  </body>\n"
      f" </html>")

line_5 = '         line 5 is stored as a variable'


print('''         line 1
         line 2
         line 3
         line 4''')
print(line_5)

print('''         line 6
         line 7
         line 8''')

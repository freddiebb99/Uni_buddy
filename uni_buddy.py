
# This defines the greet function, which simply displays a message
def greet():
    print(""" 
Welcome to UniBuddy!    
      
Please enter your credentials to get started!      
      
""")

# This defines the user_info function, which will take inputs of name, age and favourite colour to be used later   
def user_info():
    """Prompt user for name, age, and favorite color."""
    name = input("What is your name: ").capitalize()
    while True:
        try:
            age = int(input("What is your age: "))
            if age < 0 or age > 120:
                print("Please enter a valid age.")
                continue
            break
        except ValueError:
            print("Please enter a valid age as a number.")
    fav_colour = input("What is your favorite color: ").lower()
    return name, age, fav_colour

# This defines the welcome responce to the users name, for personalisation
def respond(name):
    print(f"Nice to meet you, {name}!")

# This defines the age_responce function, using the user age, it will give a table of upcoming events, depenent on age, if 18 - fresher events, if over 18 - returner events
def age_responce(age):
    from tabulate import tabulate # This uses the tabulate function to create a table from given lists, using var 'col_names' as headings

    col_names = ["Event", "Location"]
    fresher_evs = {'Welcome Drinks': 'Student Union Bar', 'Sports Fair': 'Gym', 'Sports Day': 'Sports Field'}
    returner_evs = {'Returners Mixer': 'Student Union Bar', 'Fresher Help Desk': 'Ground Floor Student Union', 'Live Music': 'Student Union Bar (weekend)'}

    if age == 18:
        print("")
        print(tabulate(fresher_evs.items(), headers=col_names, tablefmt="grid"))

    elif age >= 19 and age <= 100:
        print("")
        print(tabulate(returner_evs.items(), headers=col_names, tablefmt="grid"))
  
# This defines the responce to the users favourite colour, which will give unique responces based on the users colour, includes 'else' function for colours outside of entered ones
def colour_responce(fav_colour):
    if fav_colour == 'blue':
        print("""
Here is a list of our Blue themed clubs:
          
1. Our fighting game club.
2. Our swimming club which includes activities such as : aqua aerobics, rowing etc.
3. Our blue themed art club
4. Our deep sea exploration club.
5. Our bird watching society.
""")
        
    elif fav_colour == 'red':
        print("""
Here is a list of our Red themed clubs:

1. Our red colour themed football club.
2. Our red themed art club.
3. Our vampire themed society.
4. Our twighlight themed club.
""")
        
    elif fav_colour == 'yellow':
        print("""
Here is a list of our Yellow themed clubs:              

1. Our werewolf soc.
2. Our hiking club.
3. Our mountain climbing club.
4. Our dance club.
5. Our suntan society.
""")
        
    elif fav_colour == 'green':
        print("""
Here is a list of our Green themed clubs:     

1. Our gardening society.
2. Our paintballing society.
3. Our painting club
""")

    else:
        print(f"""
Why not try these {fav_colour} themed clubs:       

1. Our {fav_colour} themed basketball club.
2. Our {fav_colour} themed debating club.
""")

# This function is for locating facilities, takes input for a facility user wants to locate, including a final 'else' clause to direct to university website
def facility_location():
    facility = input("\nWhich facility do you need to locate? (e.g. Library, Cafe, Gym, Student Services) : ").lower()

    if facility == 'library':
        print("\nThe library is located next to the Student Union building.")
    
    elif facility == 'gym':
        print("\nThe gym is located by the sports pitches.")
    
    elif facility == 'cafe':
        print("\nThere are cafes in the student union, library and gym.")
    
    elif facility == 'student services':
        print("\nStudent Services are located on the second floor of the student union.")
    
    elif facility == 'bar':
        print("\nThe main university bar is located on the ground floor of the student union, as well as in every halls of residence.")

    else:
        print(f"\nThe {facility} can be located on the campus map on our website.")

# This defines the main line of functions, and pulls on 'greet', 'respond', 'colour_responce'
def main():
    greet()
    name, age, fav_colour = user_info()
    print("")
    respond(name)
    print("")
    colour_responce(fav_colour)
    
    # This while loop gives the user options to search for multiple facilities
    while True:
        ask_facility = input("\nWould you like to know the location of a university facility? (yes/no): ").lower()
        if ask_facility == "yes":
            facility_location()
        else:
            print("\nOk, lets move on")
            break

    # This input gives the option of learning about upcoming events dependent on user age, and will run the 'age_responce' function 
    ask_events = input("\nWould you like to know about events in the upcoming week? (yes/no) : ").lower()
    if ask_events == 'yes':
        age_responce(age)
    else:
        print("\nOk! If you have any questions just ask!")


if __name__ == "__main__":
    main()
    

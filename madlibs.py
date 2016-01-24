story = """
We went to {} and we play {}.
After we played we ate {}  and we slept for {} hours.
After we woke up we ate {} and got dress to go to {}. """

def main():
#This what allows the user to input the information required
    location = raw_input("Enter a name of a place: ")
    game = raw_input("Enter a name of a game: ")
    food = raw_input("Enter a name of a food: ")
    hours = raw_input("Enter a number of hours: ")
    food = raw_input("Enter a name of a food again: ")
    place = raw_input("Enter a name of a place again: ")
#This is what tells the program how to format the words in order
    mad_lib = story.format(location,
                            game,
                            food,
                            hours,
                            food,
                            place,)

#This is what print the story after it made
    print(mad_lib)

main()

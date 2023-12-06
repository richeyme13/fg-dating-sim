# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "This is a test to see if this will display properly without having to include a character."

    "I definitely hate working at geeksquad"

    show eileen happy

    e "Hi! I heard that you hate your job!"

    e "So do I. Would you want to quit your job and come join me on an adventure?"

    menu:

        "Yes for the love of god":
            jump yes
        
        "No I think I would much rather suffer without the benefits":
            jump no

    label yes:

        e "Yes! You deserve so much more than working full time hours with part time benefits!"

        e "Let's go!!"
        
        jump end
    
    label no:
    
        e "Oh......................."

        e "Are you even human...?"

    # This ends the game.
    label end:
        return

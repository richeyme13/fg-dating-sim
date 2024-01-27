# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Esther") # Adrian's fg
define k = Character("Kat") # Adam's fg
define i = Character("Irene") # Cinderella's fg
define j = Character("Janelle") # Aurora's fg


# used for the drag and drop, subject to change location
init python:
    def drag_placed(drags,drop):
        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        return True

label start:

    # Global variables
    $ pc_background = "" # player character's background set to empty string to be changed later
    $ fg_points = dict() # dictionary of points PC earns with the FGs

    
    # for testing the mini games without having to go thru the story first
    call screen mix_ingredients

    "Please choose a background for your character. This is a test to see if the variable updates like I think it will"

    menu:

        "Tailor":
            python:
                pc_background = "Tailor"
                fg_points['Irene'] = 25
                fg_points['Janelle'] = 15
                fg_points['Esther'] = 10
                fg_points['Kat'] = 0
        "Chef":
            python:
                pc_background = "Chef"
                fg_points['Irene'] = 10
                fg_points['Janelle'] = 0
                fg_points['Esther'] = 25
                fg_points['Kat'] = 15
        "Writer":
            python:
                pc_background = "Writer"
                fg_points['Irene'] = 0
                fg_points['Janelle'] = 25
                fg_points['Esther'] = 15
                fg_points['Kat'] = 10
        "Courtier":
            python:
                pc_background = "Courtier"
                fg_points['Irene'] = 15
                fg_points['Janelle'] = 10
                fg_points['Esther'] = 0
                fg_points['Kat'] = 25

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


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
        
        jump adventure
    
    label no:
    
        e "Oh......................."

        e "Are you even human...?"

    label adventure:

        e "I've always wanted to visit the people that live in the clouds, just never had anyone skilled enough to help me out."

        e "Could you show me what kinds of skills you got?"
        

    # This ends the game.
    label end:
        return

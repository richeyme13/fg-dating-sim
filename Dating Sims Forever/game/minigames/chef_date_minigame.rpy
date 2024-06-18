""" This is code that initiates the chef date mini game
    Here the ingredients and bowl are created"""


init python:
    ############## MEMBER VARIABLES ###################

    ### Lists of all the recipes, should give player the option to choose before they start ###

    # NOTE: DO NOT CHANGE THESE. Make a copy to use in game for points
    easy_recipe = ["liquor", "bitters","citrus","ice","egg", "magic1"]
    med_recipe = ["flour", "sugar","egg", "icing","dye","magic1","magic2"]
    hard_recipe = ["flour",'salt',"butter","egg","spinach","magic1","magic2","magic3"]

    # This list will be the copy of the selected recipe chosen by the player
    goal = []


    cooking_dg = DragGroup()


    ############## FUNCTIONS #########################

    ### Function is used to remove ingredients from screen when dropped into bowl ###
    
    # TODO: Make this function automated in order to use it for all types of recipes
    def dragged_to_pot(dragged_items,dropped_item):
        if dropped_item is not None:
            if dragged_items[0].drag_name == "ing1" and dropped_item.drag_name == "bowl":
                cooking_dg.remove(ing1)
            elif dragged_items[0].drag_name == "ing2" and dropped_item.drag_name == "bowl":
                cooking_dg.remove(ing2)

    # TODO: Either create new function or use above to remove ing from goal list
    
    # TODO: Create a func that will create ing and add them to drag group
    def create_drag_group(g):

        
        # not sure if I want to add each of them, probably won't because m will get set in the actual script
        if g == easy_recipe:
            liquor = Drag(d = "liquor.png", drag_name = "liquor", dragged = dragged_to_pot, drag_raise = True, align = (0.5,0.2))
            bitters = Drag(d = "bitters.png", drag_name = "bitters", dragged = dragged_to_pot, drag_raise = True, align = (0.4,0.3))
            citrus = Drag(d = "citrus.png", drag_name = "citrus", dragged = dragged_to_pot, drag_raise = True, align = (0.6,0.3))
            ice = Drag(d = "ice.png", drag_name = "ice", dragged = dragged_to_pot, drag_raise = True, align = (0.7,0.4))
            egg = Drag(d = "egg.png", drag_name = "egg", dragged = dragged_to_pot, drag_raise = True, align = (0.55,0.25))
            cooking_dg.add(liquor)
            cooking_dg.add(bitters)
            cooking_dg.add(citrus)
            cooking_dg.add(ice)
            cooking_dg.add(egg)
        if g == med_recipe:
            print("entered")
            egg = Drag(d = "egg.png", drag_name = "egg", dragged = dragged_to_pot, drag_raise = True, align = (0.5,0.2))
            flour = Drag(d = "flour.png", drag_name = "flour", dragged = dragged_to_pot, drag_raise = True, align = (0.4,0.3))
            sugar = Drag(d = "icing.png", drag_name = "icing", dragged = dragged_to_pot, drag_raise = True, align = (0.6,0.3))
            dye = Drag(d = "food_dye.png", drag_name = "dye", dragged = dragged_to_pot, drag_raise = True, align = (0.7,0.4))
            cooking_dg.add(egg)
            cooking_dg.add(flour)
            cooking_dg.add(sugar)
            cooking_dg.add(dye)
        if g == hard_recipe:
            flour = Drag(d = "flour.png", drag_name = "flour", dragged = dragged_to_pot, drag_raise = True, align = (0.4,0.3))
            salt = Drag(d = "salt.png", drag_name = "salt", dragged = dragged_to_pot, drag_raise = True, align = (0.6,0.3))
            butter = Drag(d = "butter.png", drag_name = "butter", dragged = dragged_to_pot, drag_raise = True, align = (0.7,0.4))
            egg = Drag(d = "egg.png", drag_name = "egg", dragged = dragged_to_pot, drag_raise = True, align = (0.5,0.2))        
            spinach = Drag(d = "spinach.png", drag_name = "spinach", dragged = dragged_to_pot, drag_raise = True, align = (0.45,0.35))
            magic2 = Drag(d = "magic2.png", drag_name = "magic2", dragged = dragged_to_pot, drag_raise = True, align = (0.55,0.25))
            magic3 = Drag(d = "magic3.png", drag_name = "magic3", dragged = dragged_to_pot, drag_raise = True, align = (0.25,0.45))
            cooking_dg.add(flour)
            cooking_dg.add(salt)
            cooking_dg.add(butter)
            cooking_dg.add(egg)
            cooking_dg.add(spinach)
            cooking_dg.add(magic2)
            cooking_dg.add(magic3)
        # Once it is compared, these will always be added to the drag group
        # I may want to move this to the start of the function since they will all include it?
        bowl = Drag(d = "tray.png", drag_name = "bowl", dragged = dragged_to_pot,draggable = False, droppable = True, align = (0.5,0.99))
        magic1 = Drag(d = "magic1.png", drag_name = "magic1", dragged = dragged_to_pot, drag_raise = True, align = (0.3,0.4))
        cooking_dg.add(bowl)
        cooking_dg.add(magic1)

    #TODO: Create a func that calculates player score
 
screen mix_ingredients:    
    
    # displays the items on the screen
    add cooking_dg



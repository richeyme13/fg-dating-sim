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
    def create_drag_group(g, m):
        print("called init")
        # if goal == easy_recipe:
            #fill in later
        print(goal)
        if g == m:
            print("entered")
            egg = Drag(d = "egg.png", drag_name = "egg", dragged = dragged_to_pot, drag_raise = True, align = (0.5,0.2))
            flour = Drag(d = "flour.png", drag_name = "flour", dragged = dragged_to_pot, drag_raise = True, align = (0.4,0.3))
            sugar = Drag(d = "icing.png", drag_name = "icing", dragged = dragged_to_pot, drag_raise = True, align = (0.6,0.3))
            dye = Drag(d = "food_dye.png", drag_name = "dye", dragged = dragged_to_pot, drag_raise = True, align = (0.7,0.4))
            cooking_dg.add(egg)
            cooking_dg.add(flour)
            cooking_dg.add(sugar)
            cooking_dg.add(dye)
        # if goal == hard_recipe
            #fill in later
        
        # Once it is compared, these will always be added to the drag group
        bowl = Drag(d = "tray.png", drag_name = "bowl", dragged = dragged_to_pot,draggable = False, droppable = True, align = (0.5,0.99))
        magic1 = Drag(d = "magic1.png", drag_name = "magic1", dragged = dragged_to_pot, drag_raise = True, align = (0.3,0.4))
        cooking_dg.add(bowl)
        cooking_dg.add(magic1)

    #TODO: Create a func that calculates player score
 
screen mix_ingredients:    
    
    # displays the items on the screen
    add cooking_dg



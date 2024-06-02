""" This is code that initiates the chef date mini game
    Here the ingredients and bowl are created"""


init python:
    ############## MEMBER VARIABLES ###################

    ### Lists of all the recipes, should give player the option to choose before they start ###

    # NOTE: DO NOT CHANGE THESE. Make a copy to use in game for points
    easy_recipe = ["eggs", "flour","oil"]
    med_recipe = []
    hard_recipe = []

    # This list will be the copy of the selected recipe chosen by the player
    goal = []

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
    def create_drag_group(rec):
        for i in rec:

            cooking_dg.add(Drag(d = Solid("#ff9b94", xysize = (100,100)), drag_name = "ing", dragged = dragged_to_pot, drag_raise = True, align = (0.25,0.25)))

    #create_drag_group(goal)

    #TODO: Create a func that calculates player score

screen mix_ingredients:    
 
        # NOTE: May be easier to have the different difficulties share ingredients for drawing purposes

        # displays the items on the screen
    add cooking_dg

# hardcoded right now but these are just to test the dragged_to_pot func (cannot be under screen)
define ing1 = Drag(d = "egg.png", drag_name = "ing1", dragged = dragged_to_pot, drag_raise = True, align = (0.3,0.5))
define ing2 = Drag(d = Solid("#ff9b94", xysize = (100,100)), drag_name = "ing2", dragged = dragged_to_pot, drag_raise = True, align = (0.5,0.5))
define bowl = Drag(d = "tray.png", drag_name = "bowl", dragged = dragged_to_pot,draggable = False, droppable = True, align = (0.75,0.25))
define cooking_dg = DragGroup(ing1, ing2, bowl)

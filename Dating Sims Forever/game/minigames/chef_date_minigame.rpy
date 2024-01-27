""" This is code that initiates the chef date mini game
    Here the ingredients and bowl are created"""

""" This function makes the ingredients disappear when dragged to the pot

    ;param dragged_items: list of draggable items to cook
    ;param dropped_item: droppable item that ingredients are dragged to 

"""
init python:
    def dragged_to_pot(dragged_items,dropped_item):
        if dropped_item is not None:
            if dragged_items[0].drag_name == "ing1" and dropped_item.drag_name == "bowl":
                cooking_dg.remove(ing1)
            elif dragged_items[0].drag_name == "ing2" and dropped_item.drag_name == "bowl":
                cooking_dg.remove(ing2)

label chef_date:

    screen mix_ingredients:
        # draggroup:
        #     #ingredients
        #     drag:
        #         drag_name "ingredient1"
        #         xpos 0.25
        #         ypos 0.25
        #         drag_raise True
        #         dragged dragged_to_pot # calls the func that was made above
        #         frame:
        #             xpadding 20
        #             ypadding 20
        #             text "ingredient 1"

        #     drag:
        #         drag_name "ingredient2"
        #         xpos 0.5
        #         ypos 0.25
        #         drag_raise True
        #         dragged dragged_to_pot
        #         frame:
        #             xpadding 20
        #             ypadding 20
        #             text "ingredient 2"
            
        #     # The bowl
        #     drag:
        #         drag_name "bowl"
        #         xpos 0.45
        #         ypos 0.75
        #         drag_raise False
        #         draggable False
        #         droppable True
        #         frame:
        #             xpadding 45
        #             ypadding 45
        #             text "bowl"

        add cooking_dg

define ing1 = Drag(d = Solid("#ff9b94", xysize = (100,100)), drag_name = "ing1", dragged = dragged_to_pot, drag_raise = True, align = (0.3,0.5))
define ing2 = Drag(d = Solid("#ff9b94", xysize = (100,100)), drag_name = "ing2", dragged = dragged_to_pot, drag_raise = True, align = (0.5,0.5))
define bowl = Drag(d = Solid("#ade9ff", xysize = (100,100)), drag_name = "bowl", dragged = dragged_to_pot,draggable = False, droppable = True, align = (0.75,0.5))
define cooking_dg = DragGroup(ing1, ing2, bowl)


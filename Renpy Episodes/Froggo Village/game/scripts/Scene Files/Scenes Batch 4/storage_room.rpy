label storage_room:

    scene bg level_1_storage_room

    #SETTING THE DIOLOGUE BOX
    $ dialogue_yalign = 0.1


    show hoppo idle right:
        xalign 0.25
        yalign 0.85
        zoom 0.60

    show pebble idle right:
        xalign 0.25
        yalign 0.95
        zoom 0.65

    show chest_closed:
        xalign 0.80
        yalign 0.50
        zoom 4.0

    pause

    #HOPPO STARTS IN A IN THE MIDDLE OF THE ROOM WHILE
    #PEBBLE CATCHES UP

    #THEN HOPPO REMARKS HOW EMPTY THE ROOM LOOKS WHILE LOOKING AROUND

    #PEBBLE AGNOWLEDGES THE EMPTY ROOM THEN SAYS ATLEAST THERE ID THAT CHEST

    #HOPPO COMES UP TO IT OPENS IT

return
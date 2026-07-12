label storage_room:

    scene bg level_1_storage_room

    #SETTING THE DIOLOGUE BOX
    $ dialogue_yalign = 0.1


    show hoppo idle right:
        xalign 0.53
        yalign 0.55
        zoom 0.60

    show pebble idle right:
        xalign 0.25
        yalign 0.55
        zoom 0.65

    show chest_closed as chest1:
        xalign 0.78
        yalign 0.55
        zoom 0.6


    #HOPPO STARTS IN A IN THE MIDDLE OF THE ROOM WHILE
    #PEBBLE CATCHES UP

    pause 4.0

    #THEN HOPPO REMARKS HOW EMPTY THE ROOM LOOKS WHILE LOOKING AROUND
    hoppo neutral "So this is the place, huh?{w=1.5}{nw}"

    window hide

    #HOPPO LOOKS AROUND IN ALL FOUR DIRECTIONS

    show hoppo idle front

    pause 0.5

    show hoppo idle left

    pause 0.5

    hoppo thinking "Looks oddly empty for a storage room.{w=1.5}{nw}"
    #PEBBLE AGNOWLEDGES THE EMPTY ROOM THEN SAYS ATLEAST THERE ID THAT CHEST
    pebble neutral "When I came here the last time it wasn't as empty,{w=1.5}{nw}"
    pebble thinking "but I guess froggo miners have a tendency to just get their own gear from Gribble.{w=2.0}{nw}"
    pebble neutral "Maybe there is something in that chest?{w=1.5}{nw}"

    window hide

    #HOPPO TURNS TO THE CHEST 
    show hoppo idle back

    pause 0.5

    show hoppo idle right

    pause 0.5
    #HOPPO COMES UP TO IT OPENS IT
    show hoppo walk right:
        xalign 0.53 yalign 0.55
        linear 2.0 xalign 0.70

    pause 2.0

    show hoppo idle right

    pause 0.5

    show chest_open as chest1

    play sound chest_open

    pause 2.0

    #NARRATOR LIST A WORN OUT COPPER PICAXE AND A LIFT FLY HELMET
    narrator "Hoppo picked up {color=#FFFF00}Rusty Pickaxe{/color}\n Hoppo picked up {color=#FFFF00}Brittle Lightfly Helmet{/color}{w=2.5}{nw}"

    show chest_closed as chest1

    play sound chest_close

    pause 2.0

    show hoppo idle front

    pause 0.5

    show hoppo idle left 

    pause 0.5

    #HOPPO COMMENTS HOW THEY GOT SOME SUPPLIES AND IS HAPPY
    hoppo happy "See Pebble. We got some cool gear.{w=1.5}{nw}"
    hoppo happy "This rescue mission will be a breeze!{w=1.5}{nw}"

    play sound helmet_break

    pause 1.5

    narrator "Suddenly {color=#FFFF00}Brittle Lightfly Helmet{/color} randomly disentigrated in Hoppo's paw.{w=2.5}{nw}"

    hoppo sad "I guess we don't have a helmet anymore.{w=1.5}{nw}"
    hoppo neutral "Perhaps we can find another light source.{w=1.5}{nw}"

    pebble thinking "This village forgot about this storage room until now, apparently.{w=2.0}{nw}"
    pebble neutral "Alright lets get out of here.{w=1.5}{nw}"
    pebble neutral "I saw some toarches by the intersection up ahead.{w=1.5}{nw}"
    pebble thinking "I think we can take one for now.{w=1.5}{nw}"

    pause 4.0

return
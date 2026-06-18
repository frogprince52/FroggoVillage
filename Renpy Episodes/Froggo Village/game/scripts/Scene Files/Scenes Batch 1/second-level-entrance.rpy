label Second_level_entrance:

scene bg level_1_3

show torch_active as torch1:
    xalign 0.22
    yalign 0.65
    zoom 0.4

show torch_active as torch2:
    xalign 0.45
    yalign 0.65
    zoom 0.4


show hoppo idle right:
    xalign 0.15
    yalign 0.75
    zoom 0.60

show pebble idle right:
    xalign 0.035
    yalign 0.8
    zoom 0.65

pause 2.0

#HOPPO MOVES TO THE CORNER, TURNS
#HOPPS FORWARD A BIT

show hoppo walk right:
    xalign 0.15
    yalign 0.75
    linear 3.5 xalign 0.6

show pebble walk right:
    xalign 0.035
    yalign 0.8
    linear 3.6 xalign 0.6


pause 3.6

show hoppo idle right

show pebble idle right

pause 0.5

show hoppo idle back 

show pebble idle back 

pause 0.5

show hoppo walk back:
    xalign 0.6
    yalign 0.75
    linear 2.0 yalign 0.5

show pebble walk back:
    xalign 0.6
    yalign 0.8
    linear 2.0 yalign 0.6

pause 2.0

show hoppo idle back

show pebble idle back

pebble neutral "Alright Hoppo, the path gets really dark from here. {w=2.0}{nw}"

pebble neutral "Just use your torch and we will be fine. {w=2.0}{nw}"

hoppo neutral "We will save you lost froggo! {w=1.8}{nw}"

window hide

pause 4.0

return
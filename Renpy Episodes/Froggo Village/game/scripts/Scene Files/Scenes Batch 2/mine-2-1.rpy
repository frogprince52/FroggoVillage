label level_2_1:

    scene bg level_2_1

    #SETTING THE DIOLOGUE BOX
    $ dialogue_yalign = 0.1

    #Display the froggo rune
    show froggo_rune:
        xalign 0.05
        yalign 0.9
        zoom 1.65

    show hoppo idle back:
        xalign 0.49
        yalign 0.9
        zoom 0.5

    show pebble idle back:
        xalign 0.49
        yalign 0.99
        zoom 0.55

    #Characters walk to the intersection, hoppo stops again
    #asks a question, pebble answers, they hrey turn and walk front

    show hoppo walk back:
        xalign 0.49 yalign 0.9
        linear 3.0 yalign 0.55

    show pebble walk back:
        xalign 0.49 yalign 0.99
        linear 3.0 yalign 0.63

pause 3.0

#They both stop

show hoppo idle back

show pebble idle back

#Insert Diologue Here
show hoppo idle left 

pause 0.5

show hoppo idle back

pause 0.5

show hoppo idle right

pause 0.5

show hoppo idle front

hoppo thinking "Hmmm, it's an interection. Pebble where do we need to go exactly? {w=3.0}{nw}"

pebble thinking "I don't remember for sure, but the next room is supposed to have three tunnels that lead us deeper into the cave system.{w=4.0}{nw}"

#Make the froggo rune slowly fade out
hide froggo_rune with dissolve

pebble neutral "The lost froggo couldn't get too far without assistance and supplies anyway. {w=3.0}{nw}"

hoppo neutral "So, the path in front of us then ? {w=2.0}{nw}"

pebble neutral "I think so. {w=1.5}{nw}"

window hide

show hoppo idle back

pause 0.5

show hoppo walk back:
        xalign 0.49 yalign 0.55
        linear 3.0 yalign 0.25

show pebble walk back:
    xalign 0.49 yalign 0.63
    linear 3.0 yalign 0.33

pause 3.0

return

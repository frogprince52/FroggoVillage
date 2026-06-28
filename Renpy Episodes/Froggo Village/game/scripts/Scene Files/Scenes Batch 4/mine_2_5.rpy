label mine_2_5:

    scene bg level_2_5

    #SETTING THE DIOLOGUE BOX
    $ dialogue_yalign = 0.1


    show hoppo idle back:
        xalign 0.25
        yalign 0.85
        zoom 0.60

    show pebble idle back:
        xalign 0.25
        yalign 0.95
        zoom 0.65

    # PUT TORCHES UP
    show torch_off as torch1:
        xalign 0.38
        yalign 0.55
        zoom 0.4

    show torch_off as torch2:
        xalign 0.5
        yalign 0.55
        zoom 0.4

    narrator "Another distressed croaking echoed in the distance. {w=2.0}{nw}"

    hoppo happy "See Pebble? The call this time is much closer, and it sounds like it came from the tunnel in front of us.{w=3.0}{nw}"

    window hide

    pause 0.5

    #HOPPO RUSHES TO THE CAVE THEN DISAPEARS INTO THE OPENING
    
    show hoppo walk back:
        xalign 0.25
        yalign 0.85
        linear 4.0 yalign 0.40

    pause 4.0

    show hoppo idle back

    pause 0.5

    hide hoppo with dissolve

    pause 1.0

    play sound slide

    pause 1.0

    narrator "A fast, wet slipping sound was heard as Hoppo vanished into the cave.{w=2.0}{nw}"

    pebble neutral "Hey! Don't just run off on your own!{w=1.5}{nw}"

    pebble neutral "Well, that didn't sound good.{w=1.5}{nw}"

    pebble thinking "Please let them be alright...{w=1.5}{nw}"

    show pebble walk back:
        xalign 0.25
        yalign 0.95
        linear 4.0 yalign 0.40

    pause 4.0

    show pebble idle back

    pause 3.0

    return
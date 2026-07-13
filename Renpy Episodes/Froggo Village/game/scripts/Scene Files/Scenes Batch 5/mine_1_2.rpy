label mine_1_2:

    scene bg level_1_2 

    $ dialogue_yalign = 0.9


    show hoppo idle back:
        xalign 0.55
        yalign 0.85
        zoom 0.60

    show pebble idle back:
        xalign 0.4
        yalign 0.95
        zoom 0.65

    #TOARCHES
    show torch_active as torch1:
        xalign 0.25
        yalign 0.19
        zoom 0.4

    show torch_active as torch2:
        xalign 0.45
        yalign 0.19
        zoom 0.4

    #SPECIAL TOARCH
    show torch_active as torch3:
        xalign 0.65
        yalign 0.19
        zoom 0.4

    show torch_active as torch4:
        xalign 0.85
        yalign 0.19
        zoom 0.4


    pause

    #FIRST BOTH HOPPO AND PEBBLE MOVE TO THE CROSSROADS
    show hoppo walk back:
        xalign 0.55 yalign 0.85
        linear 3.0 yalign 0.35

    show pebble walk back:
        xalign 0.48 yalign 0.95
        linear 3.0 yalign 0.35

    pause 3.0

    show hoppo idle back

    show pebble idle back

    pause 0.5

    show hoppo idle left

    show pebble idle right

    pause 0.5
    

    #THEN HOPPO TURNS AROUND LEFT AND RIGHT AND ASKS WHAT HAPPANED TO THAT TUNNEL

    #PEBBLE RESPONDS BY SAYING THAT IT WAS A TUNNEL COLLAPSE DUE TO SOFT SEDIMENT

    #THEN REMARKS THAT SINCE THEY REALLY WANT TO PLAY CAVE ADVENTURES HOPPO
    #JUST NEEDS TO GRAB THAT TOARCH

    #HOPPO HOPS TO IT AND TAKES IT

    #AFTER THEY ASSEMBLE THEY BOTH HOP OFF SCREEN


    pause 4.0

    return
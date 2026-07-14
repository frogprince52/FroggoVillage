label mine_1_2:

    scene bg level_1_2 

    $ dialogue_yalign = 0.9


    show hoppo idle back:
        xalign 0.56
        yalign 0.85
        zoom 0.60

    show pebble idle back:
        xalign 0.45
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

    #FIRST BOTH HOPPO AND PEBBLE MOVE TO THE CROSSROADS
    show hoppo walk back:
        xalign 0.55 yalign 0.85
        linear 3.0 yalign 0.32

    show pebble walk back:
        xalign 0.45 yalign 0.95
        linear 3.0 yalign 0.32

    pause 3.0

    show hoppo idle back

    show pebble idle back

    pause 0.5

    show hoppo idle left

    show pebble idle right

    pause 0.5
    
    #THEN HOPPO TURNS AROUND LEFT AND RIGHT AND ASKS WHAT HAPPANED TO THAT TUNNEL
    hoppo neutral "Hey Pebble, I saw that pile of rubble over on the left. What's the story there?{w=2.0}{nw}"

    window hide
    #PEBBLE TURNS IN THE DIRECTION OF THE COLLAPSED TUNNEL
    show pebble idle left

    pause 0.5

    #PEBBLE RESPONDS BY SAYING THAT IT WAS A TUNNEL COLLAPSE DUE TO SOFT SEDIMENT
    pebble neutral "Ah, that tunnel.{w=1.5}{nw}"

    pebble neutral "A long time ago, some professional froggo miners tried carving out a shortcut to the deeper layers.{w=2.0}{nw}"

    pebble neutral "Unfortunately, the soil up here was too soft, and the whole thing caved in.{w=2.0}{nw}"

    pebble neutral "Thankfully, it collapsed in the middle of the night while the village was asleep, so nobody got hurt.{w=2.0}{nw}"

    #THEN REMARKS THAT SINCE THEY REALLY WANT TO PLAY CAVE ADVENTURES HOPPO
    pebble thinking "Since you're so eager to play froggo rescuers,{w=1.5}{nw}"

    #PEBBLE TURNS AROUND
    show pebble idle right

    pause 0.5

    pebble neutral "Hoppo, I'll need you to grab that torch behind you.{w=1.5}{nw}"
    #JUST NEEDS TO GRAB THAT TOARCH
    hoppo happy "You got it, Pebble!{w=1.5}{nw}"
    #HOPPO HOPS TO IT AND TAKES IT

    show hoppo idle right

    pause 1.0

    show hoppo walk right:
        xalign 0.55 yalign 0.32
        linear 2.0 xalign 0.65

    pause 2.0

    show hoppo idle right

    pause 0.5

    show hoppo idle back

    pause 1.0

    hide torch3

    pause 1.0

    narrator "Hoppo acquired the {color=#FFFF00}Cave Torch{/color}.{w=2.0}{nw}"

    show hoppo idle left

    pause 1.0

    #REMOVE TORCH FROM THE SCENE

    hoppo happy "All set!{w=1.5}{nw}"

    pebble neutral "Perfect. We're fully equipped now.{w=1.5}{nw}"

    pebble neutral "Hoppo... are you absolutely sure you want to keep going?{w=2.0}{nw}"

    pebble neutral "It's not too late to turn back.{w=1.5}{nw}"

    hoppo thinking "Pebble, how could I abandon the froggos who welcomed me with open paws?{w=2.0}{nw}"

    hoppo happy "They gave me a home, and I've made so many amazing friends here.{w=2.0}{nw}"

    hoppo happy "Especially you, Pebble.{w=1.8}{nw}"

    pebble sad "...{w=1.7}{nw}"

    pebble happy "I suppose you're right.{w=1.5}{nw}"

    pebble neutral "Come on, let's get moving.{w=1.5}{nw}"

    window hide

    #AFTER THEY ASSEMBLE THEY BOTH HOP OFF SCREEN

    show hoppo idle right

    show pebble idle right

    pause 0.5

    show hoppo walk right:
        xalign 0.65 yalign 0.32
        linear 4.0 xalign 1.2

    show pebble walk right:
        xalign 0.45 yalign 0.32
        linear 6.0 xalign 1.20

    pause 10.0

    return
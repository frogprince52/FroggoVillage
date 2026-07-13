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


    pause

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
    hoppo neutral "Hey Pebble, I saw that pile of rubble over on the left. What's the story there?"

    window hide
    #PEBBLE TURNS IN THE DIRECTION OF THE COLLAPSED TUNNEL
    show pebble idle left

    pause 0.5

    #PEBBLE RESPONDS BY SAYING THAT IT WAS A TUNNEL COLLAPSE DUE TO SOFT SEDIMENT
    pebble neutral "Ah, that tunnel."

    pebble neutral "A long time ago, some professional froggo miners tried carving out a shortcut to the deeper levels."

    pebble neutral "Unfortunately, the soil up here was too soft, and the whole thing caved in."

    pebble neutral "Thankfully, it collapsed in the middle of the night while the village was asleep, so nobody got hurt."

    #THEN REMARKS THAT SINCE THEY REALLY WANT TO PLAY CAVE ADVENTURES HOPPO
    pebble thinking "Since you're so eager to play froggo rescuers,"

    #PEBBLE TURNS AROUND
    show pebble idle right

    pause 0.5

    pebble neutral "Hoppo, I'll need you to grab that torch behind you."
    #JUST NEEDS TO GRAB THAT TOARCH
    hoppo happy "You got it, Pebble!"
    #HOPPO HOPS TO IT AND TAKES IT

    show hoppo walk back:
        xalign 0.55 yalign 0.32
        linear 2.0 xalign 0.65

    pause 2.0

    show hoppo idle back

    pause 0.5

    show hoppo idle left

    pause 0.5

    hide torch3

    narrator "Hoppo acquired the {color=#FFFF00}Cave Torch{/color}."

    #HOPPO TURNS BACK TO PEBBLE

    show hoppo idle left

    pause 0.5

    #REMOVE TORCH FROM THE SCENE

    hoppo happy "All set!"

    pebble neutral "Perfect. We're fully equipped now."

    pebble neutral "Hoppo... are you absolutely sure you want to keep going?"

    pebble neutral "It's not too late to turn back."

    hoppo thinking "Pebble, how could I abandon the froggos who welcomed me with open arms?"

    hoppo happy "They gave me a home, and I've made so many amazing friends here."

    hoppo happy "Especially you, Pebble."

    pebble sad "..."

    pebble happy "I suppose you're right."

    pebble neutral "Come on, let's get moving."

    window hide

    #AFTER THEY ASSEMBLE THEY BOTH HOP OFF SCREEN


    pause 4.0

    return
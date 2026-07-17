label geode_room:

    scene bg level_2_3

    $ dialogue_yalign = 0.9

    show hoppo idle right:
        xalign 0.16
        yalign 0.30
        zoom 0.60

    show pebble idle right:
        xalign 0.05
        yalign 0.30
        zoom 0.65

    show nuggy_geode_full as geode_main:
        xalign 0.8
        yalign 0.35
        zoom 0.75

    show nuggy_geode_depleted as geode_2:
        xalign 0.55
        yalign 0.65
        zoom 0.75

    show nuggy_geode_depleted as geode_3:
        xalign 0.85
        yalign 0.7
        zoom 0.75

    show nuggy_geode_depleted as geode_4:
        xalign 0.9
        yalign 0.25
        zoom 0.75

    #BOTH PEBBLE AND HOPPO HOP TO AN OPENING THEN STOP
    show hoppo walk right:
        xalign 0.16 yalign 0.30
        linear 3.5 xalign 0.80

    show pebble walk right:
        xalign 0.05 yalign 0.30
        linear 4.0 xalign 0.70

    pause 4.0 

    show hoppo idle front

    show pebble idle front

    pause 1.0

    #SAY THEIR LINE AKA WE CAN MINE THESE NUGGIES
    pebble neutral "Hoppo, look!{w=1.5}{nw}"

    pebble neutral "There's a Dino Nuggy Ore right in front of us.{w=2.0}{nw}"

    pebble thinking "It looks partially mined, but we can still get a few dino nuggies out of it.{w=2.5}{nw}"

    hoppo happy "Yay, Dino nuggies!!!{w=1.5}{nw}"

    pebble "Alright, Hoppo, just swing your pickaxe and we'll get some yummy dino nuggies.{w=2.0}{nw}"

    window hide

    pause 1.0
    #THEY MINE THE GEODE WITH THE SOUND
    play sound stone_mining

    pause 1.8

    show nuggy_geode_half as geode_main

    play sound stone_mining

    pause 1.8

    show nuggy_geode_depleted as geode_main

    pause 1.8

    #NARRATOR: BOTH HOPPO AND PEBBLE ATE DINO NUGGY
    narrator "Hoppo mined {color=#FFFF00}X2 Dino Nuggies{/color}{w=2.2}{nw}"

    hoppo neutral "Here is your nuggy, Pebble.{w=1.5}{nw}"

    pebble happy "Thank you, Hoppo.{w=1.5}{nw}"

    narrator "Hoppo and Pebble ate their Dino nuggies.{w=1.5}{nw}"

    pebble happy "I almost forgot how great freshly mined nuggies taste.{w=2.0}{nw}"

    hoppo neutral "Much warmer than the ones in my pile.{w=1.5}{nw}"

    hoppo neutral "Now let's go.{w=1.5}{nw}"

    hoppo happy "The Lost Froggo won't save themselves!{w=1.5}{nw}"

    pebble happy "You're right.{w=1.5}{nw}"

    pause 5.0
    #END SCENE

    return
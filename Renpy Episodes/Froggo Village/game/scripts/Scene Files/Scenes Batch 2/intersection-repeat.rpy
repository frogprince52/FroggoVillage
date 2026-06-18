label intersection_repeat:

    scene bg level_2_1

    #SETTING THE DIOLOGUE BOX
    $ dialogue_yalign = 0.1

    show hoppo idle left:
        xalign 0.60
        yalign 0.55
        zoom 0.5

    show pebble idle left:
        xalign 0.7
        yalign 0.54
        zoom 0.55

    pause 1.5

    hoppo thinking "Hey Pebble, didn't we already pass this section? {w=2.0}{nw}"

    pebble neutral "Shoot, you're right, Hoppo. I guess my memory of the layout isn't as good as I thought. {w=2.3}{nw}"

    hoppo happy "Well, at least we found some dino nuggies!!! {w=2.0}{nw}"

    pebble happy "We sure did.{w=1.5}{nw}"

    narrator "Suddenly, a loud, distressed croaking echoed in the distance. {w=2.0}{nw}"

    hoppo neutral "Pebble, did you hear that? {w=1.0}{nw}"

    pebble neutral "Yeah, that croak came directly from the pathway in front of us. {w=2.5}{nw}"

    hoppo neutral "Come on, Pebble. We've got to hurry. {w=1.5}{nw}"

    pebble neutral "Whatever you say, Hoppo.{w=1.0}{nw}"

    window hide

    show hoppo walk left:
        xalign 0.60 yalign 0.55
        linear 4.0 xalign 0.20

    show pebble walk left:
        xalign 0.7 yalign 0.54
        linear 5.0  xalign 0.20

    pause 4.0


return
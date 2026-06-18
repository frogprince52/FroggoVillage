label three_paths:

    scene bg level_2_4

    #SETTING THE DIOLOGUE BOX
    $ dialogue_yalign = 0.9

    show hoppo idle left:
        xalign 0.8
        yalign 0.64
        zoom 0.5

    show pebble idle left:
        xalign 0.9
        yalign 0.64
        zoom 0.55

    #Both froggos moving to the three paths
    show hoppo walk left:
        xalign 0.80 yalign 0.64
        linear 3.0 xalign 0.40

    show pebble walk left:
        xalign 0.9 yalign 0.64
        linear 3.0  xalign 0.50

    pause 3.0

    show hoppo idle left

    show pebble idle left

    pause 0.5

    show hoppo idle back

    show pebble idle back 

    pause 0.5

    show hoppo walk back:
        xalign 0.40 yalign 0.64
        linear 1.0 yalign 0.55

    show pebble walk back:
        xalign 0.5 yalign 0.64
        linear 1.0  yalign 0.55

    pause 0.5

    show hoppo idle back

    show pebble idle back 

    pause 0.5 

    #Insert Diologue Here

    hoppo happy "Yay, we found the right room!{w=2.0}{nw}"

    hoppo neutral "Are you happy for our progress Pebble?{w=2.0}{nw}"

    pebble neutral "Listen Hoppo, maybe we aren't cut out for this.{w=2.0}{nw}"

    pebble thinking "We already got lost once, its not too late to turn back.{w=2.0}{nw}"

    pebble neutral "I'm sure one of the expert miners can help them.{w=2.0}{nw}"

    narrator "Suddenly a barrely audible croak was heard from the center tunnel.{w=2.0}{nw}"

    narrator "'Please, can someone help me? I'm scared :('{w=2.0}{nw}"

    hoppo happy "We are comming lost froggo!{w=2.0}{nw}"

    hoppo neutral "Me and Pebble are going to save you!{w=2.0}{nw}"

    narrator "Pebble grumbled but for some reason decided to carry on anyway.{w=2.0}{nw}"

    window hide

    pause 4.0

    return
label bent_path:

    scene bg level_2_2

    #SETTING THE DIOLOGUE BOX
    $ dialogue_yalign = 0.1

    show hoppo idle back:
        xalign 0.33
        yalign 0.9
        zoom 0.5

    show pebble idle back:
        xalign 0.28
        yalign 0.99
        zoom 0.55

    show hoppo walk back:
        xalign 0.33 yalign 0.9
        linear 4.0 xalign 0.60 yalign 0.5

    show pebble walk back:
        xalign 0.28 yalign 0.99
        linear 4.0 xalign 0.5 yalign 0.55

    pause 4.0

    show hoppo idle left

    show pebble idle right

    pause 0.5

    #INSERT DIOLOGUE HERE

    hoppo neutral "Hey Pebble, do you mind if I ask you something? {w=2.0}{nw}"

    pebble neutral "No, go ahead. {w=1.0}{nw}"

    hoppo neutral "How did you appear here in these caves? {w=1.8}{nw}"

    hoppo neutral "I mean, I was just thrown into a small cave all of a sudden not remembering anything, {w=2.5}{nw}"

    hoppo neutral " and then ended up in a village of frogs while myself being a chunky froggo. {w=2.5}{nw}"

    pebble thinking "My earliest memory is hazy. I just recall entering this cave system with the other young froggos to claim our mossy houses. {w=3.0}{nw}"

    pebble thinking "According to Elder Croakus, we originally lived in a beautiful surface village {w=2.5}{nw}"

    pebble neutral "until a terrible event forced him to relocate us to this bottom layer to keep us safe. {w=2.5}{nw}"

    hoppo thinking "Did you ask what exactly happened to make only the Elder and the younger froggos relocate to this underground village? {w=3.0}{nw}"

    pebble neutral "I tried asking the Elder, but it was so long ago that he doesn't remember much. {w=2.5}{nw}"

    pebble neutral "And as far as I know, none of the other froggos remember anything from before our descent. {w=2.5}{nw}"

    hoppo neutral "I guess that makes sense, up to a point... but where did I come from, then? {w=2.5}{nw}"

    pebble neutral "I really wish I could help you, Hoppo, but I honestly don't have an answer for you. {w=2.5}{nw}"

    pebble thinking "The right room should be around the corner. {w=1.5}{nw}"

    hoppo neutral "Alright. {w=1.5}{nw}"

    window hide

    show hoppo walk right:
        xalign 0.60 yalign 0.5
        linear 4.0 xalign 0.85 yalign 0.35

    show pebble walk right:
        xalign 0.5 yalign 0.55
        linear 4.0  xalign 0.75 yalign 0.40

    pause 4.0

return
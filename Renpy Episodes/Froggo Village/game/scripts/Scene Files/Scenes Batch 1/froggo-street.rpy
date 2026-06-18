label froggoStreet:

    scene bg froggoStreet

    show hoppo idle right:
        xalign 0.29
        yalign 0.525
        zoom 0.50

    show pebble idle front:
        xalign 0.48
        yalign 0.85
        zoom 0.55

    #MAKE PEBBLE STATIONARY FIRST
    show pebble idle front

    #HOPPO WALKS UP TO PEBBLE
    #THEN STARTS A COVNVERSATION
    show hoppo idle right

    #SETTING THE DIOLOGUE BOX
    $ dialogue_yalign = 0.1

    # Changed bare 'pause' to 'pause 1.0' so it doesn't wait for a click
    pause 1.0

    # Added {w=3.0}{nw} to wait 3 seconds, then automatically advance
    hoppo thinking "Hmm, I wonder if Pebble heard that croak for help too?{w=3.0}{nw}"

    window hide

    show hoppo walk right:
        xalign 0.29 yalign 0.525
        linear 2.0 xalign 0.47

    pause 2.0

    show hoppo idle right

    pause 1.0

    show hoppo idle front

    show hoppo walk front:
        xalign 0.47 yalign 0.525
        linear 2.0 yalign 0.70

    pause 2.0

    show hoppo idle front

    pause 0.5

    #BOTH FROGGOS TURN AROUND AND LEAVE

    #INSERT DIOLOGUE HERE (Timers adjusted based on text length)
    hoppo neutral "Hey Pebble! Did you hear that as well?{w=2.0}{nw}"

    show pebble idle back

    pebble neutral "Yeah, I heard the croak too. I think that it came from the Dino Nuggy Caves.{w=2.5}{nw}"

    pebble neutral "Maybe a froggo lost their way in the dark caverns again.{w=2.0}{nw}"

    hoppo neutral "Do froggos get lost in the caves often?{w=1.5}{nw}"

    pebble thinking "Well, it happens from time to time, but it isn't a common occurrence.{w=2.0}{nw}"

    pebble thinking "Usually, froggos descend into caves in large groups, or at least three froggos in a group, so they can assist when needed.{w=3.5}{nw}"

    hoppo happy "There is only one way to find out.{w=1.5}{nw}"

    pebble neutral "I guess you're right.{w=1.0}{nw}"

    show pebble idle front

    # Dropped this down from 10.0 to 2.0 so you aren't staring at a quiet screen for too long!
    pause 5.0 

    return
label mine_entrance:

    scene bg mineStreet

    #SETTING THE DIOLOGUE BOX
    $ dialogue_yalign = 0.1

    #FROGGO CROWD
    show froggo_crowd_front:
        xalign 0.45
        yalign 0.65
        zoom 0.65

    show hoppo idle right:
        xalign 0.2
        yalign 0.8
        zoom 0.60

    show pebble idle right:
        xalign 0.1
        yalign 0.8
        zoom 0.65

    #SHOW SECONDARY CHARACTERS
    show mossbit left static:
        xalign 0.6
        yalign 0.8
        zoom 0.60

    show elder left static:
        xalign 0.7
        yalign 0.8
        zoom 0.65

    show froggo_crowd_back:
        xalign 0.45
        yalign 0.95
        zoom 0.65

    #DIOLOGUE OF MOSBIT REASURING THE FROGGOS

    play sound group_croak

    pause 4.0

    narrator "Crowd of froggos gather anxiously by the Dino Nuggy entrance. {w=1.5}{nw}"

    narrator "They waited for Elder Croacus's instructions.{w=1.5}{nw}"

    elder neutral "Everyone! The situation is under control.{w=1.5}{nw}"

    elder neutral "Mossbit and I already have a plan. Mossbit will explain the details.{w=2.0}{nw}"

    mossbit neutral "Everyone listen up! It seems that one froggo got lost in the caverns below.{w=2.0}{nw}"

    mossbit neutral "Judging by the loudness of the SOS croak, they are located on the second level of the mines.{w=2.0}{nw}"

    mossbit thinking "'Hmmm, I don’t see any pro miners in the crowd that makes the situation more tricky.'{w=1.5}{nw}"

    mossbit neutral "We just need a couple of volunteers to go down there and retrieve the lost froggo.{w=1.5}{nw}"

    narrator "A thick, awkward silence hung in the air.{w=2.0}{nw}"

    #PEBBLE GRUMBLES AND SAYS THEY FIGUIRED IT OUT ALREADY
    pebble neutral "You see, Hoppo? The Elder and Mossbit have a plan already, and it will be resolved soon.{w=2.0}{nw}"

    pebble happy "No need for us to hop unnecessarily.{w=1.5}{nw}"

    #THEN FOLLOWS THE HOPPO VOLUNTRR SECTION
    hoppo happy "Me and Pebble can go!{w=1.5}{nw}"

    hoppo neutral "I'm not an expert on dino nuggy mining,{w=1.5}{nw}"

    hoppo neutral "but I'm sure we can figure it out and help our fellow froggo.{w=1.5}{nw}"

    hoppo thinking "How tough can it be?{w=1.5}{nw}"

    #PEBBLE SUPRISED TRIES TO CHANGE HOPPOS MIND BUT TO NO AVAIL
    pebble neutral "...{w=1.0}{nw}"

    pebble neutral "...{w=1.0}{nw}"

    window hide

    #PEBBLE MOVES CLOSER TO HOPPO

    show pebble walk right:
        xalign 0.1 yalign 0.8
        linear 1.0 xalign 0.15

    pause 1.0

    show pebble idle right 

    pause 0.5

    narrator "Pebble quietly wispered to Hoppo...{w=1.5}{nw}"

    pebble neutral "Hoppo, listen, no offense... I appreciate the enthusiasm,{w=1.5}{nw}"

    pebble neutral "but I'm not an expert on the caves.{w=1.5}{nw}"

    pebble thinking "I've been there only a few times.{w=1.5}{nw}"

    pebble thinking "Can’t we just wait until someone else saves the lost froggo?{w=1.5}{nw}"

    pebble neutral "It seems like a lot of work.{w=1.5}{nw}"

    #NARRATOR SAYS A FEW LINES HOW OTHER FROGGOS SEEM TO APREACIATE THE 
    #BRAVERY OF HOPPO
    narrator "The Froggos froze, their nervous energy replaced by a stunned, heavy silence.{w=2.0}{nw}"

    narrator "They looked at Hoppo and Pebble with newfound reverence, measuring the sheer weight of their bravery.{w=2.5}{nw}"

    narrator "Then, the quiet gave way to a deafening chorus of croaks.{w=2.0}{nw}"

    play sound group_croak

    pause 4.0

    #ELDER RESPONCE
    elder thinking "I see we got two brave volunteers!{w=1.5}{nw}"

    elder neutral "Hoppo and Pebble, what a pleasant surprise.{w=1.5}{nw}"

    elder neutral "Such a fresh froggo and already jumps into the unknown!{w=1.5}{nw}"

    elder neutral "I respect such courage!{w=1.5}{nw}"

    #PEBBLE IS ANNOYED THEY WERE DRAGGED INTO IT
    pebble sad "Wait, wait! I didn't give consent to this.{w=1.5}{nw}"

    pebble sad "Hoppo, tell them!{w=1.0}{nw}"

    #MOSSBIT WARNING AND FROGGO CROWD PRAISE

    #HOPPO AND PEBBLE MOVE CLOSER

    show hoppo idle right 

    show pebble idle right 

    pause 0.5

    show hoppo walk right:
        xalign 0.2 yalign 0.8
        linear 3.0 xalign 0.45

    show pebble walk right:
        xalign 0.15 yalign 0.8
        linear 3.0 xalign 0.4

    pause 3.0

    show hoppo idle right 

    show pebble idle right 

    pause 0.5

    mossbit neutral "Hoppo and Pebble, I admire your bravery and courage.{w=1.5}{nw}"

    mossbit neutral "The situation isn't as dramatic as it sounds.{w=1.5}{nw}"

    mossbit neutral "Before you go, since you don't have equipment, check out the storage room right after the entrance.{w=2.5}{nw}"

    mossbit neutral "Good Luck!{w=1.0}{nw}"

    pebble sad "Mossbit wait, I didn't agree to this!{w=1.5}{nw}"

    pebble sad "Why can't we wait until the seasoned froggos return from the mines?{w=2.0}{nw}"

    hoppo happy "Pebble, you're worrying too much.{w=1.5}{nw}"

    hoppo neutral "It's only a cave, how bad can it be?{w=1.5}{nw}"

    hoppo thinking "Besides, Mossbit told us where the gear is so we are set.{w=2.0}{nw}"

    pebble thinking "You owe me a cup of mossy ale when we are done.{w=2.0}{nw}"

    #SCENE CONCLUSION

    narrator "A long, heavy sigh of relief washed over the anxious froggo crowd.{w=2.0}{nw}"

    narrator "Knowing the problem was finally in the hands of true heroes, the lingering fear in the air vanished.{w=2.5}{nw}"

    narrator "One by one, the Froggos turned and hopped away, peacefully returning to their own business.{w=2.5}{nw}"

    window hide

    pause 4.0

    return
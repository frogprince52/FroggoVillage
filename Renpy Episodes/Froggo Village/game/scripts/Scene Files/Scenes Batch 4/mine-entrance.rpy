label mine_entrance:

    scene bg mineStreet

    #SETTING THE DIOLOGUE BOX
    $ dialogue_yalign = 0.1


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

    #FROGGO CROWD
    show froggo_crowd_front:
        xalign 0.45
        yalign 0.65
        zoom 0.65

    show froggo_crowd_back:
        xalign 0.45
        yalign 0.95
        zoom 0.65

    pause

    #DIOLOGUE OF MOSBIT REASURING THE FROGGOS
    narrator "Crowd of froggos gather anxiously by the Dino Nuggy entrance."

    narrator "Waiting for Elder Croacuses Instruction"

    elder neutral "Everyone! The situation is under control."

    elder neutral "Mossbit and I already have a plan. Mossbit will explain the details."

    mossbit neutral "Everyone listen up! It seems that one froggo got lost in the caverns below."

    mossbit neutral "Judging by the loudness of the SOS croak, they are located on the second level of the mines."

    mossbit thinking "'Hmmm, I don’t see any pro miners in the crowd that makes the situation more tricky.'"

    mossbit neutral "We just need a couple of volunteers to go down there and retrieve the lost froggo."

    narrator "A thick, awkward silence hung in the air."

    #PEBBLE GRUMBLES AND SAYS THEY FIGUIRED IT OUT ALREADY
    pebble neutral "You see, Hoppo? The Elder and Mossbit have a plan already, and it will be resolved soon."

    pebble happy "No need for us to hop unnecessarily."

    #THEN FOLLOWS THE HOPPO VOLUNTRR SECTION
    hoppo happy "Me and Pebble can go!"

    hoppo neutral "I'm not an expert on dino nuggy mining,"

    hoppo neutral "but I'm sure we can figure it out and help our fellow froggo."

    hoppo thinking "How tough can it be?"

    #PEBBLE SUPRISED TRIES TO CHANGE HOPPOS MIND BUT TO NO AVAIL
    pebble neutral "..."

    pebble neutral "..."

    narrator "Pebble quietly wispered to Hoppo..."

    pebble neutral "Hoppo, listen, no offense... I appreciate the enthusiasm,"

    pebble neutral "but I'm not an expert on the caves."

    pebble thinking "I've been there only a few times."

    pebble thinking "Can’t we just wait until someone else saves the lost froggo?"

    pebble neutral "It seems like a lot of work."

    #NARRATOR SAYS A FEW LINES HOW OTHER FROGGOS SEEM TO APREACIATE THE 
    #BRAVERY OF HOPPO
    narrator "The Froggos froze, their nervous energy replaced by a stunned, heavy silence."

    narrator "They looked at Hoppo and Pebble with newfound reverence, measuring the sheer weight of their bravery."

    narrator "Then, the quiet gave way to a deafening chorus of croaks."

    #ELDER RESPONCE
    elder thinking "I see we got two brave volunteers! "

    elder neutral "Hoppo and Pebble, what a pleasant surprise."

    elder neutral "Hoppo and Pebble, what a pleasant surprise."

    elder neutral "Such a fresh froggo and already jumps into the unknown!"

    elder neutral "I respect such courage!"

    #PEBBLE IS ANNOYED THEY WERE DRAGGED INTO IT
    pebble sad "Wait, wait! I didn't give consent to this."

    pebble sad "Hoppo, tell them!"

    return
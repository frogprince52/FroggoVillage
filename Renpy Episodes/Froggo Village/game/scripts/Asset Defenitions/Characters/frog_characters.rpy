#DEFINE ALL ASSETS REPRESENTING FROGGO CHARCTERS

#SPEECH SOUND (CALLBACKS FOR ALL CHARACTERS)
init python:
    

    def callbackSoft(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            # Start playing the sound on a loop when text appears
            renpy.sound.play("audio/Chapter-2/Speech sounds/soft-speech.wav", loop=True)
            
        elif event == "slow_done" or event == "end":
            # Stop the sound immediately when typing finishes or user clicks
            renpy.sound.stop()


    def callbackMedium(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            # Start playing the sound on a loop when text appears
            renpy.sound.play("audio/Chapter-2/Speech sounds/default-speech.wav", loop=True)
            
        elif event == "slow_done" or event == "end":
            # Stop the sound immediately when typing finishes or user clicks
            renpy.sound.stop()

    #PEBBLE VOICE
    def callbackLower(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            # Start playing the sound on a loop when text appears
            renpy.sound.play("audio/Chapter-2/Speech sounds/deeper-speech.wav", loop=True)
            
        elif event == "slow_done" or event == "end":
            # Stop the sound immediately when typing finishes or user clicks
            renpy.sound.stop()



#CHARACTER
# 'image' tells Ren'Py which tag to look for
define hoppo = Character("", image="hoppo_side", callback=callbackMedium)
#define hoppo = Character("")
#PORTRAITS

# Define the actual side image
# The naming convention 'side [tag] [attribute]' is vital
image side hoppo_side neutral = "images/Chapter_2/Characters/Hoppo/Portraits/hoppo-portrait-default.png"
image side hoppo_side happy = "images/Chapter_2/Characters/Hoppo/Portraits/hoppo-portrait-happy.png"
image side hoppo_side thinking = "images/Chapter_2/Characters/Hoppo/Portraits/hoppo-portrait-thinking.png"
image side hoppo_side sad = "images/Chapter_2/Characters/Hoppo/Portraits/hoppo-portrait-sad.png"

#Clarifying relationship
image hoppo neutral = "hoppo idle front"
image hoppo happy = "hoppo idle front"
image hoppo thinking = "hoppo idle front"
image hoppo sad = "hoppo idle front"

#IDLE ANIMATIONS
image hoppo idle front:
    "images/Chapter_2/Characters/Hoppo/Idle Animations/hoppo-idle-front.png" # The file path
    
    # Frame 1: (x-start, y-start, width, height)
    crop (0, 0, 192, 192)
    0.25 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.25
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.25
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.25
    # Frame 5
    crop (768, 0, 192,  192)
    0.25

    # Frame 6
    crop (960, 0, 192,  192)
    0.25
    
    repeat # Loops the animation

image hoppo idle back:
    "images/Chapter_2/Characters/Hoppo/Idle Animations/hoppo-idle-back.png"
    
    # Frame 1: (x-start, y-start, width, height)
    crop (0, 0, 192, 192)
    0.25 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.25
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.25
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.25
    # Frame 5
    crop (768, 0, 192,  192)
    0.25

    # Frame 6
    crop (960, 0, 192,  192)
    0.25
    
    repeat # Loops the animation

image hoppo idle right:
    "images/Chapter_2/Characters/Hoppo/Idle Animations/froggo-idle-right.png"
    
    # Frame 1: (x-start, y-start, width, height)
    crop (0, 0, 192, 192)
    0.25 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.25
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.25
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.25
    # Frame 5
    crop (768, 0, 192,  192)
    0.25

    # Frame 6
    crop (960, 0, 192,  192)
    0.25
    
    repeat

image hoppo idle left:
    "images/Chapter_2/Characters/Hoppo/Idle Animations/froggo-idle-left.png"
    
    # Frame 1: (x-start, y-start, width, height)
    crop (0, 0, 192, 192)
    0.25 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.25
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.25
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.25
    # Frame 5
    crop (768, 0, 192,  192)
    0.25

    # Frame 6
    crop (960, 0, 192,  192)
    0.25
    
    repeat

#WALKING ANIMATIONS

image hoppo walk front:
    "images/Chapter_2/Characters/Hoppo/Walk Animations/froggo-sprite-front-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

image hoppo walk back:
    "images/Chapter_2/Characters/Hoppo/Walk Animations/froggo-sprite-back-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

image hoppo walk right:
    "images/Chapter_2/Characters/Hoppo/Walk Animations/froggo-right-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

image hoppo walk left:
    "images/Chapter_2/Characters/Hoppo/Walk Animations/froggo-left-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat



#PEBBLE DEFENITIONS
define pebble = Character("", image="pebble_side", callback=callbackLower)

image side pebble_side neutral = "images/Chapter_2/Characters/Pebble/Portraits/pebble-portrait-default.png"
image side pebble_side happy = "images/Chapter_2/Characters/Pebble/Portraits/pebble-portrait-happy.png"
image side pebble_side thinking = "images/Chapter_2/Characters/Pebble/Portraits/pebble-portrait-thinking.png"
image side pebble_side sad = "images/Chapter_2/Characters/Pebble/Portraits/pebble-portrait-sad.png"

image pebble neutral = "pebble idle front"
image pebble happy = "pebble idle front"
image pebble thinking = "pebble idle front"
image pebble sad = "pebble idle front"

#IDLE ANIMATIONS
image pebble idle front:
    "images/Chapter_2/Characters/Pebble/Idle Animations/pebble-idle-front.png" # The file path
    
    # Frame 1: (x-start, y-start, width, height)
    crop (0, 0, 192, 192)
    0.25 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.25
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.25
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.25
    # Frame 5
    crop (768, 0, 192,  192)
    0.25

    # Frame 6
    crop (960, 0, 192,  192)
    0.25
    
    repeat # Loops the animation

image pebble idle back:
    "images/Chapter_2/Characters/Pebble/Idle Animations/pebble-idle-back.png"
    
    # Frame 1: (x-start, y-start, width, height)
    crop (0, 0, 192, 192)
    0.25 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.25
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.25
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.25
    # Frame 5
    crop (768, 0, 192,  192)
    0.25

    # Frame 6
    crop (960, 0, 192,  192)
    0.25
    
    repeat # Loops the animation

image pebble idle right:
    "images/Chapter_2/Characters/Pebble/Idle Animations/pebble-idle-right.png"
    
    # Frame 1: (x-start, y-start, width, height)
    crop (0, 0, 192, 192)
    0.25 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.25
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.25
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.25
    # Frame 5
    crop (768, 0, 192,  192)
    0.25

    # Frame 6
    crop (960, 0, 192,  192)
    0.25
    
    repeat

image pebble idle left:
    "images/Chapter_2/Characters/Pebble/Idle Animations/pebble-idle-left.png"
    
    # Frame 1: (x-start, y-start, width, height)
    crop (0, 0, 192, 192)
    0.25 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.25
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.25
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.25
    # Frame 5
    crop (768, 0, 192,  192)
    0.25

    # Frame 6
    crop (960, 0, 192,  192)
    0.25
    
    repeat

#WALKING ANIMATIONS

image pebble walk front:
    "images/Chapter_2/Characters/Pebble/Walking Animations/pebble-sprite-front-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

image pebble walk back:
    "images/Chapter_2/Characters/Pebble/Walking Animations/pebble-sprite-back-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

image pebble walk right:
    "images/Chapter_2/Characters/Pebble/Walking Animations/pebble-right-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

image pebble walk left:
    "images/Chapter_2/Characters/Pebble/Walking Animations/pebble-left-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat


#SPOTTY DEFENITIONS
define spotty = Character("", image="spotty_side", callback=callbackSoft)

image side spotty_side neutral = "images/Chapter_2/Characters/Spotty/Portraits/spotty-portrait-default.png"
image side spotty_side happy = "images/Chapter_2/Characters/Spotty/Portraits/spotty-portrait-happy.png"
image side spotty_side thinking = "images/Chapter_2/Characters/Spotty/Portraits/spotty-portrait-thinking.png"
image side spotty_side sad = "images/Chapter_2/Characters/Spotty/Portraits/spotty-portrait-sad.png"

image spotty neutral = "spotty idle front"
image spotty happy = "spotty idle front"
image spotty thinking = "spotty idle front"
image spotty sad = "spotty idle front"

#IDLE ANIMATIONS
image spotty idle front:
    "images/Chapter_2/Characters/Spotty/Idle Animations/spotty-idle-front.png" # The file path
    
    # Frame 1: (x-start, y-start, width, height)
    crop (0, 0, 192, 192)
    0.25 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.25
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.25
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.25
    # Frame 5
    crop (768, 0, 192,  192)
    0.25

    # Frame 6
    crop (960, 0, 192,  192)
    0.25
    
    repeat # Loops the animation

image spotty idle back:
    "images/Chapter_2/Characters/Spotty/Idle Animations/spotty-idle-back.png"
    
    # Frame 1: (x-start, y-start, width, height)
    crop (0, 0, 192, 192)
    0.25 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.25
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.25
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.25
    # Frame 5
    crop (768, 0, 192,  192)
    0.25

    # Frame 6
    crop (960, 0, 192,  192)
    0.25
    
    repeat # Loops the animation

image spotty idle right:
    "images/Chapter_2/Characters/Spotty/Idle Animations/spotty-idle-right.png"
    
    # Frame 1: (x-start, y-start, width, height)
    crop (0, 0, 192, 192)
    0.25 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.25
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.25
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.25
    # Frame 5
    crop (768, 0, 192,  192)
    0.25

    # Frame 6
    crop (960, 0, 192,  192)
    0.25
    
    repeat

image spotty idle left:
    "images/Chapter_2/Characters/Spotty/Idle Animations/spotty-idle-left.png"
    
    # Frame 1: (x-start, y-start, width, height)
    crop (0, 0, 192, 192)
    0.25 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.25
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.25
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.25
    # Frame 5
    crop (768, 0, 192,  192)
    0.25

    # Frame 6
    crop (960, 0, 192,  192)
    0.25
    
    repeat

#WALKING ANIMATIONS

image spotty walk front:
    "images/Chapter_2/Characters/Spotty/Walk Animations/spotty-sprite-front-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

image spotty walk back:
    "images/Chapter_2/Characters/Spotty/Walk Animations/spotty-sprite-back-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

image spotty walk right:
    "images/Chapter_2/Characters/Spotty/Walk Animations/spotty-right-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

image spotty walk left:
    "images/Chapter_2/Characters/Spotty/Walk Animations/spotty-left-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

#ELDER CROAKUS ASSETS
define elder = Character("", image="elder_side", callback=callbackMedium)

image side elder_side neutral = "images/Chapter_2/Characters/Elder Croakus/Portraits/elder-portrait-default.png"
image side elder_side serious = "images/Chapter_2/Characters/Elder Croakus/Portraits/elder-portrait-serious.png"
image side elder_side thinking = "images/Chapter_2/Characters/Elder Croakus/Portraits/elder-portrait-thinking.png"

image elder neutral = "elder front static"
image elder serious = "elder front static"
image elder thinking = "elder front static"

#FRONT IMAGE (STATIC)
image elder front static = "images/Chapter_2/Characters/Elder Croakus/elder-idle-front.png"
image elder right static = "images/Chapter_2/Characters/Elder Croakus/elder-right-static.png"
image elder left static = "images/Chapter_2/Characters/Elder Croakus/elder-left-static.png"

#WALKING ANIMATIONS
image elder walk back:
    "images/Chapter_2/Characters/Elder Croakus/Walking Animations/elder-sprite-back-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

image elder walk right:
    "images/Chapter_2/Characters/Elder Croakus/Walking Animations/elder-right-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

image elder walk left:
    "images/Chapter_2/Characters/Elder Croakus/Walking Animations/elder-left-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat


#MOSSBIT ASSETS
define mossbit = Character("", image="mossbit_side", callback=callbackLower)

image side mossbit_side neutral = "images/Chapter_2/Characters/Mossbit/Portraits/mossbit-portrait-default.png"
image side mossbit_side suprised = "images/Chapter_2/Characters/Mossbit/Portraits/mossbit-portrait-suprised.png"
image side mossbit_side thinking = "images/Chapter_2/Characters/Mossbit/Portraits/mossbit-portrait-thinking.png"

image mossbit neutral = "mossbit right static"
image mossbit serious = "mossbit right static"
image mossbit thinking = "mossbit right static"

#FRONT IMAGE
image mossbit right static = "images/Chapter_2/Characters/Mossbit/mossbit-right-static.png"
image mossbit left static = "images/Chapter_2/Characters/Mossbit/mossbit-left-static.png"

#WALKING ANIMATIONS
image mossbit walk back:
    "images/Chapter_2/Characters/Mossbit/Walking Animations/mossbit-sprite-back-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

image mossbit walk right:
    "images/Chapter_2/Characters/Mossbit/Walking Animations/mossbit-right-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat

image mossbit walk left:
    "images/Chapter_2/Characters/Mossbit/Walking Animations/mossbit-left-walk.png"
    
    # Frame 1
    crop (0, 0, 192, 192)
    0.15 # Time to show this frame
    
    # Frame 2: Move x over by the width of one frame
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3: Move x over again
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15
    # Frame 5
    crop (768, 0, 192,  192)
    0.15
    
    repeat


#FLINT ASSETS
define flint = Character("", image="flint_side", callback=callbackLower)

image side flint_side neutral = "images/Chapter_2/Characters/Flint/Portraits/flint-portrait-default.png"
image side flint_side smug = "images/Chapter_2/Characters/Flint/Portraits/flint-portrait-smug.png"

image flint neutral = "flint left static"
image flint smug = "flint left static"

#FRONT IMAGE
image flint left static = "images/Chapter_2/Characters/Flint/flint-left-static.png"

#BACKGROUND FROGGO CROWD
image froggo_crowd_front = "images/Chapter_2/Characters/Backgrounds Characters/froggo-crowd-front.png"
image froggo_crowd_back = "images/Chapter_2/Characters/Backgrounds Characters/froggo-crowd-back.png"

#FORGGERT
image froggert_front = "images/Chapter_2/Characters/Backgrounds Characters/froggert-front.png"
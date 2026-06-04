#DEFINE ALL ASSETS REPRESENTING FROGGO CHARCTERS

#SPEECH SOUND (CALLBACKS FOR ALL CHARACTERS)
init python:
    

    def callbackSoft(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            # Start playing the sound on a loop when text appears
            renpy.sound.play("audio/Chapter-2/Speech sounds/hoppo-speech.wav", loop=True)
            
        elif event == "slow_done" or event == "end":
            # Stop the sound immediately when typing finishes or user clicks
            renpy.sound.stop()


    def callbackMedium(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            # Start playing the sound on a loop when text appears
            renpy.sound.play("audio/Chapter-2/Speech sounds/hoppo-speech.wav", loop=True)
            
        elif event == "slow_done" or event == "end":
            # Stop the sound immediately when typing finishes or user clicks
            renpy.sound.stop()

    #PEBBLE VOICE
    def callbackPebbleHarsh(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            # Start playing the sound on a loop when text appears
            renpy.sound.play("", loop=True)
            
        elif event == "slow_done" or event == "end":
            # Stop the sound immediately when typing finishes or user clicks
            renpy.sound.stop()



#CHARACTER
# 'image' tells Ren'Py which tag to look for
define hoppo = Character("", image="hoppo_side", callback=callbackMediumHarshness)
#define hoppo = Character("")
#PORTRAITS

# Define the actual side image
# The naming convention 'side [tag] [attribute]' is vital
image side hoppo_side neutral = "raw assets/Chapter 2/Characters/Hoppo/Portraits/hoppo-portrait-default.png"
image side hoppo_side happy = "raw assets/Chapter 2/Characters/Hoppo/Portraits/hoppo-portrait-happy.png"
image side hoppo_side thinking = "raw assets/Chapter 2/Characters/Hoppo/Portraits/hoppo-portrait-thinking.png"
image side hoppo_side sad = "raw assets/Chapter 2/Characters/Hoppo/Portraits/hoppo-portrait-sad.png"

#Clarifying relationship
image hoppo neutral = "hoppo idle front"
image hoppo happy = "hoppo idle front"
image hoppo thinking = "hoppo idle front"
image hoppo sad = "hoppo idle front"

#IDLE ANIMATIONS
image hoppo idle front:
    "raw assets/Chapter 2/Characters/Hoppo/Idle Animations/hoppo-idle-front.png" # The file path
    
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
    "raw assets/Chapter 2/Characters/Hoppo/Idle Animations/hoppo-idle-back.png"
    
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
    "raw assets/Chapter 2/Characters/Hoppo/Idle Animations/froggo-idle-right.png"
    
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
    "raw assets/Chapter 2/Characters/Hoppo/Idle Animations/froggo-idle-left.png"
    
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
    "raw assets/Chapter 2/Characters/Hoppo/Walk Animations/froggo-sprite-front-walk.png"
    
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
    "raw assets/Chapter 2/Characters/Hoppo/Walk Animations/froggo-sprite-back-walk.png"
    
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
    "raw assets/Chapter 2/Characters/Hoppo/Walk Animations/froggo-right-walk.png"
    
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
    "raw assets/Chapter 2/Characters/Hoppo/Walk Animations/froggo-left-walk.png"
    
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
define pebble = Character("", image="pebble_side", callback=callbackPebble)

image side pebble_side neutral = "raw assets/Chapter 2/Characters/Pebble/Portraits/pebble-portrait-default.png"
image side pebble_side happy = "raw assets/Chapter 2/Characters/Pebble/Portraits/pebble-portrait-happy.png"
image side pebble_side thinking = "raw assets/Chapter 2/Characters/Pebble/Portraits/pebble-portrait-thinking.png"
image side pebbel_side sad = "raw assets/Chapter 2/Characters/Pebble/Portraits/pebble-portrait-sad.png"

image pebble neutral = "pebble idle front"
image pebble happy = "pebble idle front"
image pebble thinking = "pebble idle front"
image pebble sad = "pebble idle front"

#IDLE ANIMATIONS
image pebble idle front:
    "raw assets/Chapter 2/Characters/Pebble/Idle Animations/pebble-idle-front.png" # The file path
    
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
    "raw assets/Chapter 2/Characters/Pebble/Idle Animations/pebble-idle-back.png"
    
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
    "raw assets/Chapter 2/Characters/Pebble/Idle Animations/pebble-idle-right.png"
    
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
    "raw assets/Chapter 2/Characters/Pebble/Idle Animations/pebble-idle-left.png"
    
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
    "raw assets/Chapter 2/Characters/Pebble/Walking Animations/pebble-sprite-front-walk.png"
    
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
    "raw assets/Chapter 2/Characters/Pebble/Walking Animations/pebble-sprite-back-walk.png"
    
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
    "raw assets/Chapter 2/Characters/Pebble/Walking Animations/pebble-right-walk.png"
    
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
    "rraw assets/Chapter 2/Characters/Pebble/Walking Animations/pebble-left-walk.png"
    
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

image side spotty_side neutral = "raw assets/Chapter 2/Characters/Spotty/Portraits/spotty-portrait-default.png"
image side spotty_side happy = "raw assets/Chapter 2/Characters/Spotty/Portraits/spotty-portrait-happy.png"
image side spotty_side thinking = "raw assets/Chapter 2/Characters/Spotty/Portraits/spotty-portrait-thinking.png"
image side spotty_side sad = "raw assets/Chapter 2/Characters/Spotty/Portraits/spotty-portrait-sad.png"

image spotty neutral = "spotty idle front"
image spotty happy = "spotty idle front"
image spotty thinking = "spotty idle front"
image spotty sad = "spotty idle front"

#IDLE ANIMATIONS
image spotty idle front:
    "raw assets/Chapter 2/Characters/Spotty/Idle Animations/spotty-idle-front.png" # The file path
    
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
    "raw assets/Chapter 2/Characters/Spotty/Idle Animations/spotty-idle-back.png"
    
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
    "raw assets/Chapter 2/Characters/Spotty/Idle Animations/spotty-idle-right.png"
    
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
    "raw assets/Chapter 2/Characters/Spotty/Idle Animations/spotty-idle-left.png"
    
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
    "raw assets/Chapter 2/Characters/Spotty/Walk Animations/spotty-sprite-front-walk.png"
    
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
    "raw assets/Chapter 2/Characters/Spotty/Walk Animations/spotty-sprite-back-walk.png"
    
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
    "raw assets/Chapter 2/Characters/Spotty/Walk Animations/spotty-right-walk.png"
    
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
    "raw assets/Chapter 2/Characters/Spotty/Walk Animations/spotty-left-walk.png"
    
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
#DEFINE ALL ASSETS REPRESENTING FROGGO CHARCTERS

#SPEECH SOUND (CALLBACKS)
init python:
    def callbackH(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            # Start playing the sound on a loop when text appears
            renpy.sound.play("audio/Chapter-2/Speech sounds/hoppo-speech.wav", loop=True)
            
        elif event == "slow_done" or event == "end":
            # Stop the sound immediately when typing finishes or user clicks
            renpy.sound.stop()

#CHARACTER
# 'image' tells Ren'Py which tag to look for
define hoppo = Character("", image="hoppo_side", callback=callbackH)
#define hoppo = Character("")
#PORTRAITS

# Define the actual side image
# The naming convention 'side [tag] [attribute]' is vital
image side hoppo_side neutral = "images/Chapter-2/Characters/Hoppo/Portraits/hoppo-portrait-default.png"
image side hoppo_side happy = "images/Chapter-2/Characters/Hoppo/Portraits/hoppo-portrait-happy.png"
image side hoppo_side thinking = "images/Chapter-2/Characters/Hoppo/Portraits/hoppo-portrait-thinking.png"
#Clarifying relationship
image hoppo neutral = "hoppo idle front"
image hoppo happy = "hoppo idle front"
image hoppo thinking = "hoppo idle front"

#IDLE ANIMATIONS
image hoppo idle front:
    "images/Chapter-2/Characters/Hoppo/Idle Animations/hoppo-idle-front.png" # The file path
    
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
    "images/Chapter-2/Characters/Hoppo/Idle Animations/hoppo-idle-back.png"
    
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
    "images/Chapter-2/Characters/Hoppo/Idle Animations/froggo-idle-right.png"
    
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
    "images/Chapter-2/Characters/Hoppo/Walk Animations/froggo-sprite-front-walk.png"
    
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
    "images/Chapter-2/Characters/Hoppo/Walk Animations/froggo-sprite-back-walk.png"
    
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
    "images/Chapter-2/Characters/Hoppo/Walk Animations/froggo-right-walk.png"
    
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
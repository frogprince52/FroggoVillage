#DEFINE ALL ASSETS NEEDED FOR FROGGO VILLAGE

#MUSIC




#BACKGROUNDS FOR SCENES

#HOPPO'S HUT
image bg hopposHut = "images/Chapter-2/Backgrounds/hoppos-hut-final.png"
image mossyMatress = "images/Chapter-2/Assets/Hoppo's Hut/mossy-matress.png"
image mysteriousPainting = "images/Chapter-2/Assets/Hoppo's Hut/mysterious-painting.png"
image tallCabinet = "images/Chapter-2/Assets/Hoppo's Hut/tall-cabinet.png"
image dinoNuggyPile = "images/Chapter-2/Assets/Hoppo's Hut/dino-nuggy-pile.png"
image lightFlyJar:
    "images/Chapter-2/Assets/Hoppo's Hut/light-fly-jar.png"

    #FRAME 1
    crop (0, 0, 96, 96)
    0.3

    #FRAME 2
    crop (96, 0, 96, 96) # Changed from 192
    0.3

    #FRAME 3
    crop (192, 0, 96, 96) # Changed from 288
    0.3

    #FRAME 4
    crop (288, 0, 96, 96) # Changed from 384
    0.3
    
    repeat

#HOPPO

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
define hoppo = Character("", image="hoppo", callback=callbackH)
#define hoppo = Character("")
#PORTRAITS

# Define the actual side image
# The naming convention 'side [tag] [attribute]' is vital
image side hoppo = "images/Chapter-2/Characters/Hoppo/Portraits/hoppo-portrait-default.png"

#IDLE ANIMATIONS
image hoppo_idle_front:
    "images/Chapter-2/Characters/Hoppo/Idle Animations/hoppo-idle-front.png" # The file path
    
    # Frame 1: (x-start, y-start, width, height)
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

    # Frame 6
    crop (960, 0, 192,  192)
    0.15
    
    repeat # Loops the animation

#WALKING ANIMATIONS
image hoppo_walk_right:
    "images/Chapter-2/Characters/Hoppo/Walk Animations/froggo-right-walk.png"
    
    # Frame 1
    crop (0, 0, 192,  192)
    0.15
    
    # Frame 2
    crop (192, 0, 192,  192)
    0.15
    
    # Frame 3
    crop (384, 0, 192,  192)
    0.15
    
    # Frame 4
    crop (576, 0, 192,  192)
    0.15

    # Frame 5
    crop (768, 0, 192,  192)
    0.15

    # Frame 6
    crop (960, 0, 192,  192)
    0.15
    
    repeat
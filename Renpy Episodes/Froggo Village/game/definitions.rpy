#DEFINE ALL ASSETS NEEDED FOR FROGGO VILLAGE

#MUSIC

#SPEECH SOUND


#BACKGROUNDS FOR SCENES
image bg hopposHut = "images/Chapter-2/Backgrounds/hoppos-hut-final.png"

#HOPPO

#CHARACTER
# 'image' tells Ren'Py which tag to look for
define hoppo = Character("Hoppo", image="hoppo")

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
image hoppo_walk_right:"images/Chapter-2/Characters/Hoppo/Walk Animations/froggo-right-walk.png"
    
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
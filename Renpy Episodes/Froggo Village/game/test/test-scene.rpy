# FROGGO VILLAGE

# 1. Images
image bg testArea = "images/scene-test.png"
image hoppo = "images/froggo-sprite-default.png"

# 2. Characters - Keep only THIS ONE definition
# The 'image="hoppo"' part is what triggers the side image
define h = Character("", color="#5cff7a", image="hoppo")

# 3. Portraits (Side Images)
# Use 'image side hoppo' so Ren'Py knows it belongs in the textbox
image side hoppo:
    "images/froggo-portrait.png"
    xalign 0.0      # Stick to the left edge
    yalign 1.0      # Stick to the bottom
    xoffset 170      # Nudge it 40 pixels right to get it inside the box
    yoffset -27      # Nudge it up slightly so it doesn't clip the bottom

label start:
    scene bg testArea
    #Moving Hoppo where needed
    show hoppo:
        xalign 0.0
        yalign 0.5
    
    voice "audio/hoppo-linemp3.mp3" 
    h "Hi, my name is Hoppo and this is a test recording."

    #Move Hoppo
    # 'linear' makes the movement smooth over a set number of seconds
    show hoppo:
        linear 5.0 xalign 1.0 yalign 0.5

    #Pauses the audio until hoppo finishes the track
    pause 5.0

    play audio "audio/five-nights-at-freddys-6-am.mp3"

    h "I reached my destination. Thank you!!!"
    return

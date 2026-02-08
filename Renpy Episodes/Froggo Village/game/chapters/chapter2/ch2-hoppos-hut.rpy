# FROGGO VILLAGE SCENE 1


label hopposHut:

scene bg hopposHut

#Show house assets first so i can position them
show mossyMatress:
    xalign 0.29
    yalign 0.5
    zoom 1.2

show mysteriousPainting:
    xalign 0.58
    yalign 0.23
    zoom 0.8

show tallCabinet:
    xalign 0.42
    yalign 0.23
    zoom 0.75

show dinoNuggyPile:
    xalign 0.42
    yalign 0.78
    zoom 1

show lightFlyJar:
    xalign 0.6
    yalign 0.68
    zoom 1.3

show hoppo idle front:
    xalign 0.30
    yalign 0.49
    zoom 0.55

#next session, place hoppo and work on diaologue and positioning
pause

hoppo "Ahhh, I'm still so sleepy... but I'm sure I heard a croak for help. "

hoppo "I have to go check it out just in case a fellow froggo is in trouble."

hoppo "Better have a look around my hut and check my things before I head out, though."

#Hoppo moves to the dino nuggy pile, with an excited face says their line
show hoppo walk right:
    # We start him at his current position
    xalign 0.30 yalign 0.49
    # Then we move him to the new xalign over 2.0 seconds
    linear 2.0 xalign 0.42

#WAIT for 2.0 seconds so the animation can actually play!
pause 2.0

#Then hoppo turns and goes slightly down to the dino nuggy pile
show hoppo walk front:
    xalign 0.42 yalign 0.49
    linear 1.0 yalign 0.61

#WAIT for 2.0 seconds so the animation can actually play!
pause 1.0

#Then make Hoppo stop infront of them
show hoppo idle front
#Change hoppos side image to happy

window hide

pause

#Change hoppos side image to happy
hoppo happy "A pile of dino nuggies I got from the others froggos at Froggert’s Pub. I'll definitely have those for a snack when I come back."

#Then Hoppo turns back and walks to the tall cabinet
show hoppo walk back:
    xalign 0.42 yalign 0.58
    linear 3.0 yalign 0.32

pause 3.0

#Show hoppo idle with their back turned
show hoppo idle back 

pause

hoppo thinking "This cabinet looks quite worn, and it’s... well, it’s huge."
hoppo thinking "It towers so far over my head that I can’t even see what’s at the top."
hoppo thinking "If it didn't belong to a froggo, then who was living here before me?"
 
pause

#Then 

return
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

pause 2.0

hoppo neutral "Ahhh, I'm still so sleepy... but I'm sure I heard a croak for help. {w=2.0}{nw}"

hoppo neutral "I have to go check it out just in case a fellow froggo is in trouble. {w=2.0}{nw}"

hoppo neutral "Better have a look around my hut and check my things before I head out, though. {w=2.0}{nw}"

window hide

#Hoppo moves to the dino nuggy pile, with an excited face says their line
show hoppo walk right:
    # We start him at his current position
    xalign 0.30 yalign 0.49
    # Then we move him to the new xalign over 2.0 seconds
    linear 2.0 xalign 0.42

#WAIT for 2.0 seconds so the animation can actually play!
pause 2.0

show hoppo idle front

pause 0.5

#Then hoppo turns and goes slightly down to the dino nuggy pile
show hoppo walk front:
    xalign 0.42 yalign 0.49
    linear 2.0 yalign 0.61

#WAIT for 2.0 seconds so the animation can actually play!
pause 2.0

#Then make Hoppo stop infront of them
show hoppo idle front

#Change hoppos side image to happy
pause 0.5

#Change diologue box positionig so it moves up
$ dialogue_yalign = 0.1

#Change hoppos side image to happy
hoppo happy "A pile of dino nuggies I got from the others froggos at Froggert’s Pub. {w=2.0}{nw}"
hoppo happy "I'll definitely have those for a snack when I come back. {w=2.0}{nw}"

# Resetting Diologue Box
$ dialogue_yalign = 0.9

show hoppo idle right

pause 0.5

show hoppo idle back

pause 0.5

#Then Hoppo turns back and walks to the tall cabinet
show hoppo walk back:
    xalign 0.42 yalign 0.58
    linear 3.0 yalign 0.32

pause 3.0

#Show hoppo idle with their back turned
show hoppo idle back 

pause 0.5

hoppo thinking "This cabinet looks quite worn, and it’s... well, it’s huge. {w=2.0}{nw}"
hoppo thinking "It towers so far over my head that I can’t even see what’s at the top. {w=2.0}{nw}"
hoppo thinking "If it didn't belong to a froggo, then who was living here before me? {w=2.0}{nw}"
 
show hoppo idle right 

pause 0.5

#Then hopp turns and hopps right again and turns to the mysterious painting
show hoppo walk right:
    xalign 0.42 yalign 0.32
    linear 3.0 xalign 0.59

pause 3.0

show hoppo idle back 

pause 0.5

hoppo thinking "Since I moved in yesterday, I’ve had a strange feeling about this painting. {w=2.5}{nw}"
hoppo thinking "It’s clearly a froggo, but the golden color is something I’ve never seen before.{w=2.5}{nw}"
hoppo thinking "It looks ancient, but I can’t see the face at all it looks like it was ripped off.{w=2.5}{nw}"

#Change diologue box positionig so it moves up
$ dialogue_yalign = 0.1

#Hoppo turns facing the viewer and hops towards the light fly jar
show hoppo idle front

pause 0.5

show hoppo walk front:
    xalign 0.59 yalign 0.32
    linear 3.0 yalign 0.50

pause 3.0

show hoppo idle front 

pause 0.5

hoppo neutral "I caught these lightflies to brighten up the hut. They used to fly away whenever I opened the jar.{w=2.5}{nw}"
hoppo neutral "But I managed to train them to stay inside by feeding them chunks of my dino nuggies.{w=2.5}{nw}"

$ dialogue_yalign = 0.9

show hoppo idle right

pause 0.5

show hoppo walk right:
    xalign 0.59 yalign 0.50
    linear 2.0 xalign 0.65

pause 2.0

show hoppo idle right

pause 0.5

hoppo neutral "Well, everything looks in order. It’s time to leave my mossy abode.{w=2.0}{nw}"
hoppo neutral "I wonder what adventures await for me beyond that door! {w=2.0}{nw}"

pause 4.0

#END OF SCENE

return
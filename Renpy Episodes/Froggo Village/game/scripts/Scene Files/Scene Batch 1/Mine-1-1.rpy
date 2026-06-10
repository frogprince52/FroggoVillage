label Mine_1_1:

scene bg level_1_1

show hoppo idle back:
    xalign 0.425
    yalign 0.85
    zoom 0.60

show pebble idle back:
    xalign 0.515
    yalign 0.95
    zoom 0.65

# PUT TORCHES UP
show torch_active as torch1:
    xalign 0.05
    yalign 0.17
    zoom 0.4

show torch_active as torch2:
    xalign 0.22
    yalign 0.17
    zoom 0.4

show torch_active as torch3:
    xalign 0.7
    yalign 0.17
    zoom 0.4

show torch_active as torch4:
    xalign 0.9
    yalign 0.17
    zoom 0.4

#INSERT DIOLOGUE HERE

show hoppo walk back:
    xalign 0.425
    yalign 0.85
    linear 3.0 yalign 0.30

show pebble walk back:
    xalign 0.515
    yalign 0.95
    linear 3.0 yalign 0.35

pause 3.0


show hoppo idle back

show pebble idle back

pause

#INSERT DIOLOGUE HERE
pebble neutral "Hoppo, I just want to warn you before we descend. Let's just say caves aren't as easy to navigate as Mossbit suggested."

pebble neutral "Since we are doing this, we will need a light source."

pebble thinking "I remember when I was going on group mining trips some time ago,"

pebble thinking "our guides had those firefly helmets that lit up the area."

#HOPPO TURNS AROUND TO THE RIGHT AFTER HOPPING FOR A BIT
show hoppo idle left

hoppo thinking "Hey Pebble, what is the purpose of these tunnels? Any dino nuggies here?"

show pebble idle left

pebble thinking "Oh those? I remember I asked one of the cave guides about them the first time I went on a trip to the mines."

pebble neutral "They said it was from the first froggo cave expeditions trying to find dino nuggies on the first level."

pebble neutral "But unfortunately, none were present here since it's just solid rock and stone."

#THEN TO THE LEFT

show hoppo idle back

pause 0.5

show hoppo idle right

show hoppo walk right:
    xalign 0.425
    yalign 0.85
    linear 3.5 xalign 0.55

pause 3.5

hoppo neutral "Look a sign!"


#HOPPO CHECKS THE SIGN
narrator "A stone sign that reads 'STORAGE' "

#INSERT DIOLOGUE

hoppo happy "Yay we found it"

#THEN PROCEEDS TO BOLT TO THE STORAGE ROOM

#PEBBLE SIGNS AND COMPLAINS WHY IS PEBBLE SO RECKLESS
pebble neutral "Hoppo wait !"

pebble sad "Oh Hoppo why are you so reckless?"

return
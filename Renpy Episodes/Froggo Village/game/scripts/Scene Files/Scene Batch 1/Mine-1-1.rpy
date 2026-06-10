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
    linear 3.0 yalign 0.31

pause 3.0


show hoppo idle back

show pebble idle back

#INSERT DIOLOGUE HERE
pebble neutral "Hoppo, I just want to warn you before we descend. Let's just say caves aren't as easy to navigate as Mossbit suggested.{w=2.5}{nw}"

pebble neutral "Since we are doing this, we will need a light source.{w=1.0}{nw}"

pebble thinking "I remember when I was going on group mining trips some time ago,{w=1.0}{nw}"

pebble thinking "our guides had those firefly helmets that lit up the area.{w=1.5}{nw}"

#HOPPO TURNS AROUND TO THE RIGHT AFTER HOPPING FOR A BIT
show hoppo idle left

hoppo thinking "Hey Pebble, what is the purpose of these tunnels? Any dino nuggies here?{w=1.5}{nw}"

show pebble idle left

pebble thinking "Oh those? I remember I asked one of the cave guides about them the first time I went on a trip to the mines.{w=2.0}{nw}"

pebble neutral "They said it was from the first froggo cave expeditions trying to find dino nuggies on the first level.{w=2.0}{nw}"

pebble neutral "But unfortunately, none were present here since it's just solid rock and stone.{w=1.5}{nw}"

#THEN TO THE LEFT

window hide

show hoppo idle back

pause 0.5

show hoppo idle right

pause 0.5

hoppo neutral "Look a sign!{w=1.0}{nw}"

show pebble idle back

pause 0.5

show pebble idle right

pause 0.5

show hoppo walk right:
    xalign 0.425
    yalign 0.30
    linear 2.0 xalign 0.60

pause 2.0

show hoppo idle back

pause 0.5

#HOPPO CHECKS THE SIGN
narrator "A stone sign that reads 'STORAGE' {w=1.5}{nw}"

#INSERT DIOLOGUE

hoppo happy "Yay we found it! {w=1.8}{nw}"

#THEN PROCEEDS TO BOLT TO THE STORAGE ROOM

show hoppo walk right:
    xalign 0.55
    yalign 0.30
    linear 4.0 xalign 1.25

pause 4.0

hide hoppo

#PEBBLE SIGNS AND COMPLAINS WHY IS PEBBLE SO RECKLESS
pebble neutral "Hoppo wait ! {w=1.5}{nw}"

pebble sad "Oh Hoppo why are you so reckless? {w=2.0}{nw}"

show pebble walk right:
    xalign 0.515
    yalign 0.31
    linear 4.0 xalign 1.20

pause 4.5

return
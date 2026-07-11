init python:
    

    def callbackNarrator(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            # Start playing the sound on a loop when text appears
            renpy.music.set_volume(0.5, channel="sound")
            renpy.sound.play("audio/Chapter-2/Speech sounds/narrator-speech.wav", loop=True)
        elif event == "slow_done" or event == "end":
            # Stop the sound immediately when typing finishes or user clicks
            renpy.sound.stop()


define narrator = Character(None, what_text_align=0.5, what_xalign=0.5, callback=callbackNarrator)
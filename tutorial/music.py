from microbit import *
import music

# built-in melodies
# music.DADADADUM
# music.ENTERTAINER
# music.PRELUDE
# music.ODE
# music.NYAN
# music.RINGTONE
# music.FUNK
# music.BLUES
# music.BIRTHDAY
# music.WEDDING
# music.FUNERAL
# music.PUNCHLINE
# music.PYTHON
# music.BADDY
# music.CHASE
# music.BA_DING
# music.WAWAWAWAA
# music.JUMP_UP
# music.JUMP_DOWN
# music.POWER_UP
# music.POWER_DOWN
names = [music.DADADADUM, music.ENTERTAINER, music.PRELUDE, music.ODE, music.NYAN, music.RINGTONE, music.FUNK, music.BLUES, music.BIRTHDAY, music.WEDDING, music.FUNERAL, music.PUNCHLINE, music.PYTHON, music.BADDY, music.CHASE, music.BA_DING, music.WAWAWAWAA, music.JUMP_UP, music.JUMP_DOWN, music.POWER_UP, music.POWER_DOWN ]
i = 0
music.play(names[12])  # music.PYTHON

while True:
    if button_a.was_pressed():
        music.play(names[i])
        i += 1
        if i >= len(names):
            i = 0
    

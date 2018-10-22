from microbit import *
import music

#NOTE[octave][:duration]
# NOTE : C~B, R for rest
# duration : higher value the longer

tune = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", "C4:4",
"E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]
music.play(tune)

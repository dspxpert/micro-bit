from microbit import *

# built-in Images
# Image.HEART
# Image.HEART_SMALL
# Image.HAPPY
# Image.SMILE
# Image.SAD
# Image.CONFUSED
# Image.ANGRY
# Image.ASLEEP
# Image.SURPRISED
# Image.SILLY
# Image.FABULOUS
# Image.MEH
# Image.YES
# Image.NO
# Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.
# CLOCK7, Image.CLOCK6, Image.CLOCK5, Image.CLOCK4, Image.CLOCK3, Image.CLOCK2,
# Image.CLOCK1
# Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S,
# Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW
# Image.TRIANGLE
# Image.TRIANGLE_LEFT
# Image.CHESSBOARD
# Image.DIAMOND
# Image.DIAMOND_SMALL
# Image.SQUARE
# Image.SQUARE_SMALL
# Image.RABBIT
# Image.COW
# Image.MUSIC_CROTCHET
# Image.MUSIC_QUAVER
# Image.MUSIC_QUAVERS
# Image.PITCHFORK
# Image.XMAS
# Image.PACMAN
# Image.TARGET
# Image.TSHIRT
# Image.ROLLERSKATE
# Image.DUCK
# Image.HOUSE
# Image.TORTOISE
# Image.BUTTERFLY
# Image.STICKFIGURE
# Image.GHOST
# Image.SWORD
# Image.GIRAFFE
# Image.SKULL
# Image.UMBRELLA
# Image.SNAKE

# Image.ALL_CLOCKS and Image.ALL_ARROWS

#display.scroll("Hello, World!")
#display.show(Image.ROLLERSKATE)

boat = Image("05050:"
             "05050:"
             "05050:"
             "99999:"
             "09990")
#display.show(boat)

#display.show(Image.ALL_CLOCKS, loop=True, delay=20)

boat1 = Image("05050:"
            "05050:"
            "05050:"
            "99999:"
            "09990")
boat2 = Image("00000:"
            "05050:"
            "05050:"
            "05050:"
            "99999")
boat3 = Image("00000:"
            "00000:"
            "05050:"
            "05050:"
            "05050")
boat4 = Image("00000:"
            "00000:"
            "00000:"
            "05050:"
            "05050")
boat5 = Image("00000:"
            "00000:"
            "00000:"
            "00000:"
            "05050")
boat6 = Image("00000:"
            "00000:"
            "00000:"
            "00000:"
            "00000")
all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
display.show(all_boats, delay=200)

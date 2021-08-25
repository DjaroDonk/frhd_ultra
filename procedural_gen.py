import frhd_ultra
from frhd_ultra import letter_font
import pyperclip
import random
def between(x,y):
    return(random.randint(x,y))
def not_zero(x):
    if x == 0:
        return(1)
    return(x)

my_track = frhd_ultra.Track.Track()
difficulty = input("What is the difficulty?\n")
track_long = input("Is this track long? ('YES' or 'NO')\n")
letter_font.type_string(my_track,-40,-250,"This track was made by an AI")
letter_font.type_string(my_track,-40,-220,"using FRHD_ULTRA by Djaro")
letter_font.type_string(my_track,-40,-190,"Procedurally Generated map")
letter_font.type_string(my_track,-40,-160,"Difficulty: " + str(difficulty))
if track_long.lower() == "yes":
    letter_font.type_string(my_track,-40,-130,"Warning:")
    letter_font.type_string(my_track,-40,-100,"This Track is long")
pos = [[-40,100],[200,100]]
segments = int(input("How many segments?\n"))
xdev = [int(i) for i in input("What is the range of x length ('min,max')\n").split(",")]
ydev = [int(i) for i in input("What is the range of y length ('min,max')\n").split(",")]
checkdev = int(input("How many segments should there be between checkpoints?\n"))
my_track.insLine(pos[0][0],pos[0][1],pos[1][0],pos[1][1])
letter_font.type_string(my_track,pos[1][0]+50,pos[1][1]-50,"0/"+str(segments//checkdev),'s')
my_track.insCheck(pos[1][0]+20,pos[1][1]-30)
for i in range(1,segments+1):
    pos[0] = pos[1]
    pos[1] = [pos[1][0] + random.randint(xdev[0],xdev[1]),pos[1][1] + random.randint(ydev[0],ydev[1])]
    #pos[1] = [pos[1][0]+xdev(i),pos[1][1]+ydev(i)]
    xlen = pos[1][0] - pos[0][0]
    ylen = pos[1][1] - pos[0][1]
    my_track.insLine(pos[0][0],pos[0][1],pos[1][0],pos[1][1])
    if i%checkdev == 0 and i!=segments:
        my_track.insCheck(pos[1][0]+20,pos[1][1]-30)
        letter_font.type_string(my_track,pos[1][0]+50,pos[1][1]-50,str(int(i/checkdev))+"/"+str(int(segments//checkdev)),'s')
my_track.insStar(pos[1][0]+20,pos[1][1]-30)
letter_font.type_string(my_track,pos[1][0]+50,pos[1][1]-50,str(int(segments//checkdev))+"/"+str(int(segments//checkdev)),'s')
pyperclip.copy(my_track.genCode())
input("Track copied to clipboard")

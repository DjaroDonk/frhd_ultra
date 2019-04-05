import frhdtools
import letter_font
import pyperclip
import random
my_track = frhdtools.Track.Track()
letter_font.type_string(my_track,-40,-190,"Procedurally Generated map")
letter_font.type_string(my_track,-40,-160,"Difficulty: Medium")
letter_font.type_string(my_track,-40,-130,"Warning:")
letter_font.type_string(my_track,-40,-100,"This Track is long")
pos = [[-40,100],[200,100]]
my_track.insLine(pos[0][0],pos[0][1],pos[1][0],pos[1][1])
letter_font.type_string(my_track,pos[1][0]+50,pos[1][1]-50,"0/10",'s')
my_track.insCheck(pos[1][0]+20,pos[1][1]-30)
the_range = 501
for i in range(1,the_range):
    pos[0] = pos[1]
    pos[1] = [pos[1][0] + random.randint(10,200),pos[1][1] + random.randint(10,100)]
    my_track.insLine(pos[0][0],pos[0][1],pos[1][0],pos[1][1])
    if (i%50 == 0) and i+1!=the_range:
        my_track.insCheck(pos[1][0]+20,pos[1][1]-30)
        letter_font.type_string(my_track,pos[1][0]+50,pos[1][1]-50,str(int(i/50))+"/10",'s')
my_track.insStar(pos[1][0]+20,pos[1][1]-30)
letter_font.type_string(my_track,pos[1][0]+50,pos[1][1]-50,"10/10",'s')
pyperclip.copy(my_track.genCode())

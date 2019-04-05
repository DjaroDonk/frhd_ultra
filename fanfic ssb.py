import letter_font
import frhdtools
text_txt = open("text.txt","r",errors='ignore')
new_file = open("new_file.txt",'w')
x = -40

the_segment = frhdtools.Track.Track()
letter_font.type_string(the_segment,-50,-50,"Zoom out to view this","p")
new_file.write(the_segment.genCode().rstrip("#"))

for i in range(5000):
    line = text_txt.readline()
    try:
        the_segment = frhdtools.Track.Track()
        letter_font.type_string(the_segment,-50,100+25*i,line,"p")
        new_file.write(the_segment.genCode().rstrip("#"))
    except Exception as e:
        try:
            print(e)
        except:
            print("Can't print character")
new_file.write("###")
new_file.close()
text_txt.close()

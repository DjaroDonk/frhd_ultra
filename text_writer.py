import frhd_ultra
from frhd_ultra import letter_font
import pyperclip
import random
my_track = frhd_ultra.Track.Track()
the_text="""add your text here"""
letter_font.type_lines(the_text,my_track,-40,100,"p",40)
pyperclip.copy(my_track.genCode())

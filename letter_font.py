import frhdtools
def type_space(x,y,track,line_type="p"):
    return(10)
def type_a(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x+10,y,x+10,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+10,x+10,y+10,line_type)
    return(15)
def type_b(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x,y,x+8,y,line_type)
    track.insLine(x,y+10,x+10,y+10,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    track.insLine(x+8,y,x+8,y+10,line_type)
    track.insLine(x+10,y+10,x+10,y+20,line_type)
    return(15)
def type_c(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    return(15)
def type_d(x,y,track,line_type="p"):
    track.insLine(x,y,x+15,y+2,line_type)
    track.insLine(x,y+20,x+15,y+18,line_type)
    track.insLine(x+15,y+2,x+15,y+18,line_type)
    track.insLine(x+2,y+2,x+2,y+18,line_type)
    return(20)
def type_e(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    track.insLine(x,y+10,x+10,y+10,line_type)
    return(15)
def type_f(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+10,x+10,y+10,line_type)
    return(15)
def type_g(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    track.insLine(x+10,y+20,x+10,y+10,line_type)
    track.insLine(x+10,y+10,x+7,y+10,line_type)
    return(15)
def type_h(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x+10,y,x+10,y+20,line_type)
    track.insLine(x,y+10,x+10,y+10,line_type)
    return(15)
def type_i(x,y,track,line_type="p"):
    track.insLine(x+2,y,x+2,y+20,line_type)
    track.insLine(x,y,x+4,y,line_type)
    track.insLine(x,y+20,x+4,y+20,line_type)
    return(9)
def type_j(x,y,track,line_type="p"):
    track.insLine(x+4,y,x+4,y+20,line_type)
    track.insLine(x,y+20,x+4,y+20,line_type)
    return(9)
def type_k(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x,y+10,x+10,y,line_type)
    track.insLine(x,y+10,x+10,y+20,line_type)
    return(15)
def type_l(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    return(15)
def type_m(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x+20,y,x+20,y+20,line_type)
    track.insLine(x,y,x+10,y+20,line_type)
    track.insLine(x+20,y,x+10,y+20,line_type)
    return(25)
def type_n(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x+10,y,x+10,y+20,line_type)
    track.insLine(x,y,x+10,y+20,line_type)
    return(15)
def type_o(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    track.insLine(x+10,y,x+10,y+20,line_type)
    return(15)
def type_p(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+10,x+10,y+10,line_type)
    track.insLine(x+10,y,x+10,y+10,line_type)
    return(15)
def type_q(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    track.insLine(x+10,y,x+10,y+20,line_type)
    track.insLine(x+8,y+18,x+12,y+22,line_type)
    return(15)
def type_r(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+10,x+10,y+10,line_type)
    track.insLine(x+10,y,x+10,y+10,line_type)
    track.insLine(x+5,y+10,x+10,y+20,line_type)
    return(15)
def type_s(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+10,line_type)
    track.insLine(x+10,y+10,x+10,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    track.insLine(x,y+10,x+10,y+10,line_type)
    return(15)
def type_t(x,y,track,line_type="p"):
    track.insLine(x+5,y,x+5,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    return(15)
def type_u(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x+10,y,x+10,y+20,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    return(15)
def type_v(x,y,track,line_type="p"):
    track.insLine(x,y,x+5,y+20,line_type)
    track.insLine(x+5,y+20,x+10,y,line_type)
    return(15)
def type_w(x,y,track,line_type="p"):
    track.insLine(x,y,x+5,y+20,line_type)
    track.insLine(x+5,y+20,x+10,y,line_type)
    track.insLine(x+10,y,x+15,y+20,line_type)
    track.insLine(x+15,y+20,x+20,y,line_type)
    return(25)
def type_x(x,y,track,line_type="p"):
    track.insLine(x,y,x+10,y+20,line_type)
    track.insLine(x,y+20,x+10,y,line_type)
    return(15)
def type_y(x,y,track,line_type="p"):
    track.insLine(x,y,x+5,y+10,line_type)
    track.insLine(x+5,y+10,x+10,y,line_type)
    track.insLine(x+5,y+10,x+5,y+20,line_type)
    return(15)
def type_z(x,y,track,line_type="p"):
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    track.insLine(x+10,y,x,y+20,line_type)
    return(15)
def type_period(x,y,track,line_type="p"):
    track.insLine(x,y+20,x,y+17,line_type)
    track.insLine(x+3,y+20,x+3,y+17,line_type)
    track.insLine(x,y+20,x+3,y+20,line_type)
    track.insLine(x,y+17,x+3,y+17,line_type)
    return(8)
def type_comma(x,y,track,line_type="p"):
    track.insLine(x,y+22,x+3,y+19,line_type)
    return(8)
def type_dash(x,y,track,line_type="p"):
    track.insLine(x,y+10,x+10,y+10,line_type)
    return(15)
def type_underscore(x,y,track,line_type="p"):
    track.insLine(x,y+20,x+10,y+20,line_type)
    return(15)
def type_fwslash(x,y,track,line_type="p"):
    track.insLine(x,y+20,x+10,y,line_type)
    return(15)
def type_bwslash(x,y,track,line_type="p"):
    track.insLine(x,y,x+10,y+20,line_type)
    return(15)
def type_exclamation(x,y,track,line_type="p"):
    track.insLine(x+1,y,x+1,y+10,line_type)
    track.insLine(x+2,y,x+2,y+10,line_type)
    track.insLine(x,y+20,x,y+17,line_type)
    track.insLine(x+3,y+20,x+3,y+17,line_type)
    track.insLine(x,y+20,x+3,y+20,line_type)
    track.insLine(x,y+17,x+3,y+17,line_type)
    return(8)
def type_question(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+5,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x+10,y,x+10,y+10,line_type)
    track.insLine(x+10,y+10,x+7,y+10,line_type)
    track.insLine(x+7,y+10,x+7,y+18,line_type)
    return(15)
def type_singlequote(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+5,line_type)
    return(6)
def type_doublequote(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+5,line_type)
    track.insLine(x+3,y,x+3,y+5,line_type)
    return(8)
def type_colon(x,y,track,line_type="p"):
    track.insLine(x,y+20,x,y+17,line_type)
    track.insLine(x+3,y+20,x+3,y+17,line_type)
    track.insLine(x,y+20,x+3,y+20,line_type)
    track.insLine(x,y+17,x+3,y+17,line_type)
    track.insLine(x,y+3,x,y,line_type)
    track.insLine(x+3,y+3,x+3,y,line_type)
    track.insLine(x,y+3,x+3,y+3,line_type)
    track.insLine(x,y,x+3,y,line_type)
    return(8)
def type_semicolon(x,y,track,line_type="p"):
    track.insLine(x,y+3,x,y,line_type)
    track.insLine(x+3,y+3,x+3,y,line_type)
    track.insLine(x,y+3,x+3,y+3,line_type)
    track.insLine(x,y,x+3,y,line_type)
    track.insLine(x,y+22,x+3,y+19,line_type)
    return(8)
def type_threedots(x,y,track,line_type="p"):
    type_period(x,y,track,line_type="p")
    type_period(x+7,y,track,line_type="p")
    type_period(x+14,y,track,line_type="p")
    return(25)
def type_asteriks(x,y,track,line_type="p"):
    track.insLine(x,y,x+3,y+3,line_type)
    track.insLine(x,y+3,x+3,y,line_type)
    track.insLine(x,y+1,x+3,y+1,line_type)
    return(8)
def type_hashtag(x,y,track,line_type="p"):
    track.insLine(x,y+7,x+20,y+7,line_type)
    track.insLine(x,y+14,x+20,y+14,line_type)
    track.insLine(x+7,y,x+7,y+20,line_type)
    track.insLine(x+14,y,x+14,y+20,line_type)
    return(25)
def type_at(x,y,track,line_type="p"):
    track.insLine(x,y+20,x+20,y+20,line_type)
    track.insLine(x,y,x+20,y,line_type)
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x+20,y,x+20,y+15,line_type)
    track.insLine(x+5,y+15,x+20,y+15,line_type)
    track.insLine(x+5,y+15,x+5,y+5,line_type)
    track.insLine(x+5,y+5,x+15,y+5,line_type)
    track.insLine(x+15,y+5,x+15,y+15,line_type)
    return(25)
def type_euro(x,y,track,line_type="p"):
    track.insLine(x+2,y,x+2,y+20,line_type)
    track.insLine(x+2,y,x+10,y,line_type)
    track.insLine(x+2,y+20,x+10,y+20,line_type)
    track.insLine(x,y+9,x+10,y+9,line_type)
    track.insLine(x,y+12,x+10,y+12,line_type)
    return(15)
def type_dollar(x,y,track,line_type="p"):
    track.insLine(x,y+3,x,y+10,line_type)
    track.insLine(x+10,y+10,x+10,y+17,line_type)
    track.insLine(x,y+3,x+10,y+3,line_type)
    track.insLine(x,y+17,x+10,y+17,line_type)
    track.insLine(x,y+10,x+10,y+10,line_type)
    track.insLine(x+5,y,x+5,y+20,line_type)
    return(15)
def type_percent(x,y,track,line_type="p"):
    track.insLine(x,y+3,x,y,line_type)
    track.insLine(x+3,y+3,x+3,y,line_type)
    track.insLine(x,y+3,x+3,y+3,line_type)
    track.insLine(x,y,x+3,y,line_type)
    track.insLine(x+17,y+20,x+17,y+17,line_type)
    track.insLine(x+20,y+20,x+20,y+17,line_type)
    track.insLine(x+17,y+20,x+20,y+20,line_type)
    track.insLine(x+17,y+17,x+20,y+17,line_type)
    track.insLine(x,y+20,x+20,y,line_type)
    return(25)
def type_and(x,y,track,line_type="p"):
    track.insLine(x+5,y,x,y+5,line_type)
    track.insLine(x+5,y,x+10,y+5,line_type)
    track.insLine(x,y+5,x+15,y+20,line_type)
    track.insLine(x+10,y+5,x,y+15,line_type)
    track.insLine(x,y+15,x+5,y+20,line_type)
    track.insLine(x+5,y+20,x+15,y+10,line_type)
    return(20)
def type_parenthesesopen(x,y,track,line_type="p"):
    track.insLine(x+10,y,x+5,y+4,line_type)
    track.insLine(x+5,y+4,x+3,y+10,line_type)
    track.insLine(x+3,y+10,x+5,y+16,line_type)
    track.insLine(x+5,y+16,x+10,y+20,line_type)
    return(15)
def type_parenthesesclose(x,y,track,line_type="p"):
    track.insLine(x,y,x+5,y+4,line_type)
    track.insLine(x+5,y+4,x+7,y+10,line_type)
    track.insLine(x+7,y+10,x+5,y+16,line_type)
    track.insLine(x+5,y+16,x,y+20,line_type)
    return(15)
def type_smallerthan(x,y,track,line_type="p"):
    track.insLine(x+10,y,x,y+10,line_type)
    track.insLine(x,y+10,x+10,y+20,line_type)
    return(15)
def type_biggerthan(x,y,track,line_type="p"):
    track.insLine(x,y,x+10,y+10,line_type)
    track.insLine(x+10,y+10,x,y+20,line_type)
    return(15)
def type_bracketsopen(x,y,track,line_type="p"):
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    return(15)
def type_bracketsclose(x,y,track,line_type="p"):
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x+10,y,x+10,y+20,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    return(15)
def type_one(x,y,track,line_type="p"):
    track.insLine(x+5,y,x+5,y+20,line_type)
    track.insLine(x,y+5,x+5,y,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    return(15)
def type_two(x,y,track,line_type="p"):
    track.insLine(x,y+5,x+5,y,line_type)
    track.insLine(x+5,y,x+10,y+5,line_type)
    track.insLine(x+10,y+5,x,y+20,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    return(15)
def type_three(x,y,track,line_type="p"):
    track.insLine(x+10,y,x+10,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    track.insLine(x,y+10,x+10,y+10,line_type)
    return(15)
def type_four(x,y,track,line_type="p"):
    track.insLine(x+8,y,x+8,y+20,line_type)
    track.insLine(x,y+10,x+10,y+10,line_type)
    track.insLine(x+4,y,x,y+10,line_type)
    return(15)
def type_five(x,y,track,line_type="p"):
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y,x,y+10,line_type)
    track.insLine(x,y+10,x+10,y+15,line_type)
    track.insLine(x+10,y+15,x,y+20,line_type)
    return(15)
def type_six(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+10,x+10,y+10,line_type)
    track.insLine(x,y+20,x+10,y+20,line_type)
    track.insLine(x+10,y+10,x+10,y+20,line_type)
    return(15)
def type_seven(x,y,track,line_type="p"):
    track.insLine(x+10,y,x+10,y+20,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x+4,y+10,x+10,y+10,line_type)
    return(15)
def type_eight(x,y,track,line_type="p"):
    track.insLine(x+5,y,x,y+5,line_type)
    track.insLine(x+5,y,x+10,y+5,line_type)
    track.insLine(x,y+5,x+10,y+15,line_type)
    track.insLine(x+10,y+5,x,y+15,line_type)
    track.insLine(x,y+15,x+5,y+20,line_type)
    track.insLine(x+10,y+15,x+5,y+20,line_type)
    return(15)
def type_nine(x,y,track,line_type="p"):
    track.insLine(x,y,x,y+10,line_type)
    track.insLine(x,y,x+10,y,line_type)
    track.insLine(x,y+10,x+10,y+10,line_type)
    track.insLine(x+10,y,x+10,y+20,line_type)
    track.insLine(x+10,y+20,x,y+20,line_type)
    return(15)

# track.insLine(x,y,x,y,line_type)
letter_funcs = {" ":type_space,
                "\n":type_space,
                "a":type_a,
                "b":type_b,
                "c":type_c,
                "d":type_d,
                "e":type_e,
                "f":type_f,
                "g":type_g,
                "h":type_h,
                "i":type_i,
                "j":type_j,
                "k":type_k,
                "l":type_l,
                "m":type_m,
                "n":type_n,
                "o":type_o,
                "p":type_p,
                "q":type_q,
                "r":type_r,
                "s":type_s,
                "t":type_t,
                "u":type_u,
                "v":type_v,
                "w":type_w,
                "x":type_x,
                "y":type_y,
                "z":type_z,
                ".":type_period,
                ",":type_comma,
                "-":type_dash,
                "_":type_underscore,
                "/":type_fwslash,
                "\\":type_bwslash,
                "!":type_exclamation,
                "?":type_question,
                "\'":type_singlequote,
                "‘":type_singlequote,
                "’":type_singlequote,
                "\"":type_doublequote,
                "“":type_doublequote,
                "”":type_doublequote,
                ":":type_colon,
                ";":type_semicolon,
                "\t":type_space,
                "…":type_threedots,
                "*":type_asteriks,
                "#":type_hashtag,
                "@":type_at,
                "$":type_dollar,
                "€":type_euro,
                "%":type_percent,
                "&":type_and,
                "(":type_parenthesesopen,
                ")":type_parenthesesclose,
                "<":type_smallerthan,
                ">":type_biggerthan,
                "[":type_bracketsopen,
                "]":type_bracketsclose,
                "1":type_one,
                "2":type_two,
                "3":type_three,
                "4":type_four,
                "5":type_five,
                "6":type_six,
                "7":type_seven,
                "8":type_eight,
                "9":type_nine,
                "0":type_o}

def type_string(track,x,y,my_text,line_type="p"):
    current_x = x
    current_y = y
    for character in my_text:
        current_x += letter_funcs[character.lower()](current_x,current_y,track,line_type)
    return((current_x,current_y))
        
my_track = frhdtools.Track.Track()

def get_string(my_text,line_type="p",x=-40,y=100):
    temp_track = frhdtools.Track.Track()
    type_string(temp_track,x,y,my_text)
    return(temp_track.genCode())

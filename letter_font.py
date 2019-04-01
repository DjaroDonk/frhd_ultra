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

# track.insLine(x,y,x,y,line_type)
letter_funcs = {" ":type_space,
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
                ",":type_comma}

def type_string(track,x,y,my_text,line_type="p"):
    current_x = x
    current_y = y
    for character in my_text:
        current_x += letter_funcs[character.lower()](current_x,current_y,track,line_type)
    return((current_x,current_y))
        
my_track = frhdtools.Track.Track()

f,x=0,0
def solve():
    global f,x
    if f&1:
        basic.show_number(2) if input.running_time()-x>9000 else basic.show_number((input.running_time()-x-7000)/1000) if input.running_time()-x>=7000 else basic.show_number(-1)
        x,f=0,0
    else:x,f=input.running_time(),1   
input.on_button_pressed(Button.A, solve)

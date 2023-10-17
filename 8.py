x,f=0,0
def solve():global x,f;pause(randint(1000,5000));basic.show_icon(IconNames.HEART);x,f=input.running_time(),1
input.on_button_pressed(Button.A, solve)
def h():
    global x,f
    if f&1:
        basic.show_number(input.running_time()-x)
        f = 0
input.on_button_pressed(Button.B, h)

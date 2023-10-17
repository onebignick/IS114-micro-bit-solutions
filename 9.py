x=5;basic.show_number(x)
def h1():global x;x=max(1,x-1);basic.show_number(x)
input.on_button_pressed(Button.A,h1)
def h2():global x;x=min(9,x+1);basic.show_number(x)
input.on_button_pressed(Button.B,h2)
def solve():
    global x
    while x>=0:basic.show_number(x);pause(1000);x-=1
    x=5;basic.show_number(x)
input.on_button_pressed(Button.AB, solve)

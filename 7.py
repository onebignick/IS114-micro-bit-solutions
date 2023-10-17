basic.show_icon(IconNames.HEART)
a,b,f=250,5,1
def solve():global a,b,f;if a==255: f=0;elif a==0: f=1;a=a+5 if f&1 else a-5;led.set_brightness(a);pause(b)
basic.forever(solve)
def h1():global b;b=max(b,b-5)
input.on_button_pressed(Button.A, h1)
def h2():global b;b+=5
input.on_button_pressed(Button.B, h2)

def solve():
    if input.button_is_pressed(Button.A):
        a,x=True,input.running_time()
        while input.button_is_pressed(Button.A):pass
        r=input.running_time()-x
        basic.show_string("long string") if r>3000 else basic.show_string("short string")
basic.forever(solve)

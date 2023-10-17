def solve():
    a,b=0,input.running_time()
    while input.running_time()-b<2000 and not a:a=1 if input.button_is_pressed(Button.A) else pass
    basic.show_string("single click") if a&1 else basic.show_string("double click")
input.on_button_pressed(Button.A, solve)

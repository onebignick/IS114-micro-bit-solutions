def a(x):
    if x<0:return
    basic.show_number(x)
    pause(1000)
    a(x-1)
a(5)

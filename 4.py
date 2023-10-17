input.on_button_pressed(Button.A, solve=lambda:serial.write_line(str(input.running_time()/1000)))

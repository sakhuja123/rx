#this is the main class that auto runs when r3 raspian OS starts.





def key_input(event):
    init()
    print "Key:", event.char
    key_press = event.char
    sleep_time = 0.060

    if key_press.lower() == "w":
        forward(sleep_time)
    elif key_press.lower() == "s":
        reverse(sleep_time)
    elif key_press.lower() == "a":
        turn_left(sleep_time)
    elif key_press.lower() == "d":
        turn_right(sleep_time)
    elif key_press.lower() == "p":
        stop(sleep_time)
    else:
        pass

    curDis = distance("cm")
    print("Distance:", curDis)

    if curDis <15:
        init()
        reverse(0.5)

command = tk.TK()
command.bind('<keypress>', key_input)
command.mainloop()

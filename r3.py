import time
import r3_constants
import sys

get_input('run_path')
get_input('run_kbd')

# run path: shape, size, speed, duration
# run_path('circle','M',slow,20)



# define key press controls
command = tk.TK()
command.bind('<keypress>', key_input)
command.mainloop()

mode: user.game
-

# position mic under mouth so breathing doesn't get picked up

parrot(ch):
    print("ch")
    mouse_click(0)
    # close the mouse grid if open
    user.grid_close()
    # End any open drags
    # Touch automatically ends left drags so this is for right drags specifically
    user.mouse_drag_end()

parrot(click):
 	print("click")
    mouse_click(1)
    # close the mouse grid if open
    user.grid_close()

parrot(hiss):
 	print("hiss")
    user.mouse_drag(0)
    # close the mouse grid
    user.grid_close()

parrot(kh):
 	print("kh")
    user.mouse_drag(1)
    # close the mouse grid
    user.grid_close()

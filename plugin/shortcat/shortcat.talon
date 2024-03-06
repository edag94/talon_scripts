#shore: user.shortcat()
show: key(ctrl-m)
es: key(esc)

key(ctrl-keypad_0):
    sound.set_microphone("System Default")
    speech.enable()

key(ctrl-keypad_1):
    sound.set_microphone("None")
    speech.disable()

#todo make this a toggle
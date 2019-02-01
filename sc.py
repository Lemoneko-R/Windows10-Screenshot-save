# -*- coding: utf-8 -*-

from PIL import ImageGrab, Image
import datetime

def save():
    im = ImageGrab.grabclipboard()
    if isinstance(im, Image.Image):
        im.save(str("SAVE DIRECTORY HERE")+str(datetime.datetime.today()).replace(" ","-").replace(":","-")+'.jpg')
        print('saved')
    else:
        print('no image')

from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        if key.char == "Key.ctrl_r":
            save()
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:

        it= "{0}".format(
            key)
        if it == "Key.ctrl_r":
            save()


if __name__ == '__main__':

    with Listener(
        on_press = on_press,
    ) as listener:
        listener.join()

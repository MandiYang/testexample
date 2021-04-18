import pyautogui
from pynput.keyboard import *
print('python-autoclicker')
#  ======== settings ========
delay = float(input('delay per seconds:'))  # in seconds
resume_key = Key.shift
pause_key = Key.alt
exit_key = Key.esc
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// AutoClicker by iSayChris")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t shift = Resume")
    print("\t F3 = Pause")
    print("\t esc = Exit")
    print("-----------------------------------------------------")
    print('Press shift to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()

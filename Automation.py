from features import sounds
import pyautogui
import webbrowser as web
from features import talk
import time
try:
    import pygetwindow as gw
except Exception:
    gw = None
def ChromeAuto(command):
    sounds()
    query = command
    # Try to focus Chrome so hotkeys land in the right window
    try:
        if gw is not None:
            wins = gw.getWindowsWithTitle('Chrome')
            if wins:
                try:
                    wins[0].activate()
                    time.sleep(0.3)
                except Exception:
                    pass
    except Exception:
        pass

    if 'new tab' in query:
        pyautogui.hotkey('ctrl', 't')

    elif 'close the tab' in query:
        pyautogui.hotkey('ctrl', 'w')

    elif 'new window' in query:
        pyautogui.hotkey('ctrl', 'n')

    elif 'history' in query:
        pyautogui.hotkey('ctrl', 'h')

    elif 'download' in query:
        pyautogui.hotkey('ctrl', 'j')

    elif 'bookmark' in query:
        pyautogui.hotkey('ctrl', 'd')
        pyautogui.press('enter')

    elif 'incognito' in query:
        pyautogui.hotkey('ctrl', 'shift', 'n')

    elif 'switch tab' in query:
        tab = query.replace("switch tab ", "")
        tab = tab.replace("to", "")
        tab = tab.replace("in chrome", "")
        try:
            num = int(tab)
            pyautogui.hotkey('ctrl', str(num))
        except Exception:
            talk("please say a tab number")

    elif 'open' in query:

        name = query.replace("open ", "")

        NameA = str(name)

        if 'youtube' in NameA:

            web.open("https://www.youtube.com/")

        elif 'instagram' in NameA:

            web.open("https://www.instagram.com/")

        elif 'whatsapp web' in NameA:

            web.open("https://web.whatsapp.com/")

        else:
            talk("i can get you sir")

def YouTubeAuto(command):
    sounds()
    query = str(command)
    if 'pause' in query:
        pyautogui.press('space')
    elif 'resume' in query:
        pyautogui.press('space')
    elif 'full screen' in query:
        pyautogui.press('f')
    elif 'film screen' in query:
        pyautogui.press('t')
    elif 'skip' in query:
        pyautogui.press('l')
    elif 'back' in query:
        pyautogui.press('j')
    elif 'previous' in query:
        pyautogui.hotkey('shift', 'p')
    elif 'next' in query:
        pyautogui.hotkey('shift', 'n')
    elif 'mute' in query:
        pyautogui.press('m')
    elif 'unmute' in query:
        pyautogui.press('m')
    else:
        talk("No Command Found!")
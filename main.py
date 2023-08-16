
import time
import pyautogui
import webbrowser
import enum


class Emojis(enum.Enum):
    SmilingFacewithHearts = "Smiling Face with Hearts"
    SmilingFacewithHeartEyes = "Smiling Face with Heart-Eyes"
    WinkingFace = "Winking Face"
    HeartwithArrow = "Heart with Arrow"
    SparklingHeart = "Sparkling Heart"
    GrowingHeart = "Growing Heart"
    BeatingHeart = "Beating Heart"
    RevolvingHearts = "Revolving Hearts"
    TwoHearts = "Two Hearts"
    HeartDecoration = "Heart Decoration"
    HeartExclamation = "Heart Exclamation"
    BrokenHeart = "Broken Heart"
    MendingHeart = "Mending Heart"
    RedHeart = "Red Heart"






class createline:
    def __init__(self, line, emoji):
        self.line = line
        self.emoji = emoji


# creating list
songarr = []

# appending instances to list
songarr.append(createline("Oru pennin nenaivenna seiyum enai", Emojis.TwoHearts.value))
songarr.append(createline("Kathi illaamal koiyum ithil", Emojis.HeartwithArrow.value))
songarr.append(createline("Meela vazhi ulladhae irupinum", Emojis.SmilingFacewithHeartEyes.value))
songarr.append(createline("Ullam virumbaathu oh yeh", Emojis.RedHeart.value))
songarr.append(createline(" Vizhigalin aruginil vaanam vegu", Emojis.BeatingHeart.value))
songarr.append(createline("Tholaivinil tholaivinil thookam ithu", Emojis.TwoHearts.value))
songarr.append(createline("Ainthu pulangalin yekkam en", Emojis.HeartDecoration.value))
songarr.append(createline("Muthal muthal anubavam oh yeh", Emojis.RedHeart.value))



webbrowser.open("https://web.whatsapp.com/")
time.sleep(10)
pyautogui.moveTo(100, 150)
pyautogui.click()
for i in range(1, 7):
    pyautogui.press('tab')

pyautogui.write("keerthu")
pyautogui.press('enter')

for i in range(0, len(songarr)):
    pyautogui.write(songarr[i].line)
    time.sleep(1)
    pyautogui.hotkey("win", ".")

    pyautogui.write(songarr[i].emoji)
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press("esc")
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)


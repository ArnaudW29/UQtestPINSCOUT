import time

import pyautogui

maps = {
    "geant": [681, 763, 792, 877],
    "mine": [613, 843, 528, 739],
    "mine2": [1117, 758, 1240, 667],
    "morgana": [713, 525, 839, 638],
    "morgana2": [1026, 661, 1172, 552], #si 3ieme piege 1120 , 607
    "crypte": [731, 730, 825, 827],
    "crypte2": [1130, 735, 1202, 812],
}

q = True

print("launching")
print(maps.keys())
inf = input("quel zone?")
time.sleep(2)
if inf in maps.keys():
    print("Bonne map!")
    try:
        while q:
            pyautogui.moveTo(x=maps[inf][0], y=maps[inf][1], duration=0.5)
            time.sleep(0.1)
            pyautogui.press("z")
            time.sleep(4.2)
            pyautogui.moveTo(x=maps[inf][2], y=maps[inf][3], duration=0.5)
            time.sleep(0.1)
            pyautogui.press("z")
            time.sleep(4.2)
    except KeyboardInterrupt:
        print('Script fini')
else:
    print("Mauvaise map")

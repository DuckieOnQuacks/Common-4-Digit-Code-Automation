import keyboard
import time

with open("codes.txt", "r") as f:
    codelist = eval(f.read())

print(codelist)
time.sleep(3)
delay_time = .7
i = 0
index = 0
keyboard.press_and_release("y")

for code in codelist:
    i += 1
    index += 1
    if index == 3:
        print(i)
        print(code)
        keyboard.press_and_release("e")
        time.sleep(delay_time)
        for num in code:
            keyboard.press_and_release(num)
        time.sleep(delay_time)
        index = 0
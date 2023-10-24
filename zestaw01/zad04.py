# Napisać program, który dynamicznie wyświetla „pasek postępu” o zadanej długości

import time

def get_progress_bar(percent):
    filled_length = int(percent)
    bar = "=" * filled_length + "-" * (100 - filled_length)
    result = "|"+bar+"|"+str(percent)+"%"
    return result

for i in range(101):
    print(get_progress_bar(i), end="\r")
    time.sleep(1 / 20)
    
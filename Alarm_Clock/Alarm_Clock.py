import winsound         # for sound  
import time             # for sleep

try:
    while True:       
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        time.sleep(1)
except KeyboardInterrupt:
        pass
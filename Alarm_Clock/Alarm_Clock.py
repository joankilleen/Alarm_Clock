import winsound         # for sound  
import time             # for sleep



winsound.PlaySound(
                    'SystemQuestion',
                    winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
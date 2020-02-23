from threading import Thread

import dogFood
import cameraSonic

obj = dogFood.runDogFood()

Thread(target = obj.startThisThread, args = (), daemon = True).start()
Thread(target = cameraSonic.runCameraSonic, args = (), daemon = True).start()

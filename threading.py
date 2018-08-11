<<<<<<< HEAD
import threading

class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = BuckysMessenger(name = 'Send out messages')
y = BuckysMessenger(name = 'Receive messages')

x.start()
=======
import threading

class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = BuckysMessenger(name = 'Send out messages')
y = BuckysMessenger(name = 'Receive messages')

x.start()
>>>>>>> bf9ec1b50b9a105f9d7e270e398763a0ccb4d098
y.start()
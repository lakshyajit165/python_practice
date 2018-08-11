<<<<<<< HEAD
class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data

try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
=======
class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data

try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
>>>>>>> bf9ec1b50b9a105f9d7e270e398763a0ccb4d098
    print("Received error:", ae.data)
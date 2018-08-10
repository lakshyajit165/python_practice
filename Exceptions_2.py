class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data

try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
    print("Received error:", ae.data)
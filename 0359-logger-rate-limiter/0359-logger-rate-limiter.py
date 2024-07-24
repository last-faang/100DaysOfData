class Logger:
    def __init__(self):
        self.logs = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logs or self.logs[message] <= timestamp:
            self.logs[message] = timestamp + 10 
            return True

        return False

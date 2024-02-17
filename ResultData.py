class ResultData:
    def __init__(self, state, data=None):
        self.state = state
        self.data = data
    
    def to_string(self):
        return {
            "state": self.state,
            "data": self.data
        }
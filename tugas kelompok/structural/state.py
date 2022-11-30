class StateObject:
    def __init__(self):
        self.state = "DEFAULT"
        self.states = {}

    def add_state(self, fn):
        self.states[fn.__name__] = fn
        return fn
    
    def execute(self, condition:callable):
        while condition():
            self.states[self.state](self)

if __name__ == "__main__":
    test = StateObject()
    
    @test.add_state
    def DEFAULT(self):
        print("Default State!")
        self.state = "MIDDLE"
    
    @test.add_state
    def MIDDLE(self):
        print("Middle State!")
        self.state = "FINAL"

    @test.add_state
    def FINAL(self):
        print("Finished!")
        self.state = "FINISHED"

    test.execute(lambda:test.state != "FINISHED")
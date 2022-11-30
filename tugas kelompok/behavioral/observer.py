class Observable:
    def __init__(self):
        self.subscriber = []

    def subscribe(self, subscriber):
        self.subscriber.append(subscriber)

    def print(self, number):
        for it in self.subscriber:
            it(number)


observable = Observable()

observable.subscribe(lambda x: print(f"1: {x}"))
observable.subscribe(lambda x: print(f"2: {x * 2}"))
observable.subscribe(lambda x: print(f"3: {x * x}"))
observable.subscribe(lambda _: print(""))

observable.print(1)
observable.print(2)
observable.print(3)
class Target:
    def request(self) -> str:
        return "Default Behavior"


class Adaptee:
    def specific_request(self) -> str:
        return {
            "status" : "Accepted",
            "Message" : "Success"
        }


class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        msg = ""
        for k, v in self.adaptee.specific_request().items():
            msg += k + ": " + v + "\n"
        return msg


def client_code(target: Target) -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    adapter = Adapter(adaptee)
    print("Translated Dictionary")
    client_code(adapter)
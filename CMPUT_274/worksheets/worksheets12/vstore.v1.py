class VStore:
    def __init__(self):
        self.store = dict()
        return
    # FIXME add __str__() and __repr()__

    def add(self, value):
        # runtime type of parameter, the type of parameter when running
        if type(value) is int:
            self.store[value] = True
        if type(value) is list:
            self.store.update({v: True for v in value})

        return

    def find(self, value):
        if value in self.store:
            return True
        else:
            return False

    def delete(self, value):
        if value in self.store:
            del self.store[value]
            return True
        else:
            return False

    def print_all(self):
        print(self.store.keys())


def main():
    vs = VStore()

    vs.add(95)
    vs.add(90)
    vs.add(85)
    print(vs.find(90))
    print(vs.find(85))
    print(vs.delete(85))
    print(vs.find(85))
    print(vs.delete(70))
    vs.print_all()
    return

if __name__ == "__main__":
    main()

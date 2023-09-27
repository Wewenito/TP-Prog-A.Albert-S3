

class Test:
    def __init__(self) -> None:
        self.__test1 = "test1"
        self.__test2 = "test2"

    def get_nom(self, name):
        if name == "test1":
            return self.__test1
        elif name == "test2":
            return self.__test2





X = Test()

print(X.get_nom("test1"))
print(X.get_nom("test2"))
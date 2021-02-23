from singleton import Singleton

class Config(metaclass=Singleton):
    def __init__(self, file="../config.file"):
        # transform config.file into dictionnary with key: value
        with open(file, 'r') as f:
            tmpList = [value.split("=", 1) for value in f.readlines()]
            self.dic = {elem[0]:elem[1] for elem in tmpList}

    # get value from the config.file. return "" if key not present
    def get(self, key):
        try:
            return self.dic[key]
        except KeyError:
            return ""

if __name__ == "__main__":
    print(Config().get("welcome.message"))
    print(Config().get("unknown"))

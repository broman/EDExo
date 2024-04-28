from os import PathLike


class Journal:
    def __init__(self, path: PathLike):
        self.path = path

    def read(self, path: PathLike):
        pass

    def watch(self, path: PathLike):
        pass

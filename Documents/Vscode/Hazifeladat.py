# Absztrakt osztály: Járat
class Jarat(ABC):
    def __init__(self, jaratszam, honnanhova, jegyar):
        self.jaratszam = jaratszam
        self.honnanhova = honnanhova
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self):
        pass
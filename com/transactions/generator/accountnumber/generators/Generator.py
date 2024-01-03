from abc import ABC, abstractmethod


class GeneratorInterface(ABC):
    NUMBER_OF_ACCOUNTS_PER_LEVEL = 2000
    POOR_BANK_IDS = [i for i in range(1000, 1020)]
    STANDARD_BANK_IDS = [i for i in range(2000, 2020)]
    PRO_BANK_IDS = [i for i in range(3000, 3020)]
    ULTRA_BANK_IDS = [i for i in range(4000, 4020)]

    @abstractmethod
    def level(self):
        pass

    @abstractmethod
    def generate(self, product_level):
        pass

from com.transactions.generator.ProductLevel import ProductLevel
from com.transactions.generator.accountnumber.generators.PoorGenerator import PoorGenerator
from com.transactions.generator.accountnumber.generators.ProGenerator import ProGenerator
from com.transactions.generator.accountnumber.generators.StandardGenerator import StandardGenerator
from com.transactions.generator.accountnumber.generators.UltraGenerator import UltraGenerator


class AccountGeneratorSelector:
    generators = [
        PoorGenerator(),
        StandardGenerator(),
        ProGenerator(),
        UltraGenerator()
    ]

    def select(self, level):
        for generator in self.generators:
            if generator.level() == level:
                return generator

        raise Exception(f"Generator for level: {level} not found! Available: {[g.level() for g in self.generators]}")

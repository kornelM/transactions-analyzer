import random

from com.transactions.generator.ProductLevel import ProductLevel
from com.transactions.generator.accountnumber.generators.Generator import GeneratorInterface


class PoorGenerator(GeneratorInterface):
    POOR_ACCOUNT_NUMBER_STARTER = 1_000

    def level(self):
        return ProductLevel.POOR

    def generate(self, product_level: ProductLevel):
        account_prefix = self.__account_prefix(product_level)
        bank_identity = self.__bank_identity()
        account_number = self.__account_number()

        return account_prefix + bank_identity + account_number

    def __account_prefix(self, product_level: ProductLevel):
        return str(product_level.prefix)

    def __bank_identity(self):
        return str(random.choice(GeneratorInterface.POOR_BANK_IDS))

    def __account_number(self):
        account_number = random.choice(
            range(
                self.POOR_ACCOUNT_NUMBER_STARTER,
                self.POOR_ACCOUNT_NUMBER_STARTER + GeneratorInterface.NUMBER_OF_ACCOUNTS_PER_LEVEL
            )
        )
        return str(account_number)

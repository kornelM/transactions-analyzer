# import data.writer as wt

from com.transactions.generator.ProductLevel import ProductLevel
from com.transactions.generator.accountnumber.generators.AccountNumberGeneratorSelector import AccountGeneratorSelector
from com.transactions.generator.data import writer
from com.transactions.properties import NUMBER_OF_GENERATED_TRANSACTIONS


def generate_account_number3(title):
    return generate_random_account_number2(title)


def generate_account_number(title):
    account_numbers = [generate_random_account_number2(title) for _ in range(NUMBER_OF_GENERATED_TRANSACTIONS)]
    writer.write_to_json("account_numbers", account_numbers)


def generate_random_account_number(product_level):
    selector = AccountGeneratorSelector()

    account_type = str(product_level.prefix)
    account_number = selector.select(product_level).generate(product_level)

    return account_type + account_number


def generate_random_account_number2(title):
    product_level = ProductLevel.get_type_based_on_text(title)
    account_number = generate_random_account_number(product_level)

    return {
        'account_type': product_level.level,
        'account_number': account_number
    }

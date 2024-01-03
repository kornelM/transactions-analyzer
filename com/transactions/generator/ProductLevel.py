from enum import Enum


class ProductLevel(Enum):
    POOR = ("Poor", 10)
    STANDARD = ("Standard", 20)
    PRO = ("Pro", 30)
    ULTRA = ("Ultra", 40)

    def __init__(self, level, prefix):
        self.level = level
        self.prefix = prefix

    def __str__(self):
        return self.level

    def __int__(self):
        return self.prefix

    @staticmethod
    def values():
        return [i for i in ProductLevel]

    @staticmethod
    def levels():
        return [i.level for i in ProductLevel]

    @staticmethod
    def prefixes():
        return [i.prefix for i in ProductLevel]

    @staticmethod
    def get_value_by_level(level) -> 'ProductLevel':
        values = ProductLevel.values()
        for value in values:
            if level is value.level:
                return value
        raise Exception(
            f"Product level for level: {level} not found! Available: {[v.level for v in ProductLevel.values()]}")

    @staticmethod
    def get_type_based_on_text(title):
        # words =
        # for word in words:
        #     if word == target_word:
        #         return True
        # return False

        for pl in ProductLevel.values():
            if pl.level in title.split():
                return pl

        raise Exception(
            f"Product level in title: '{title}' not found! Available: {[v.level for v in ProductLevel.values()]}")

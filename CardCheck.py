import re

class CardCheck:
    @staticmethod
    def check_card_number(card_number):
        pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}-\d{4}$'
        return bool(re.fullmatch(pattern, card_number))

    @classmethod
    def check_name(cls, name):
        pattern = r'^[A-Z]+ [A-Z]+$'
        return bool(re.fullmatch(pattern, name))


# Приклад перевірки:
print(CardCheck.check_card_number("1234-5678-9012-3456-7890"))  # True
print(CardCheck.check_name("YURIY RYBAK"))                      # True
print(CardCheck.check_name("Yuriy Rybak"))                      # False

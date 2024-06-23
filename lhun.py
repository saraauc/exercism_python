class Luhn:
    def __init__(self, card_num):
        self.card_num=str(card_num).strip().replace(" ","")

    def valid(self):
        card_num = self.card_num
        length = len(card_num)
        if length <= 1 or not card_num.isdigit():
            return False

        total = 0
        reverse_digits = card_num[::-1]

        for i in range(length):
            digit = int(reverse_digits[i])
            if i % 2 == 1: 
                digit *= 2
                if digit > 9:
                    digit -= 9
            total += digit

        return total % 10 == 0

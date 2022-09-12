class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(f'Список букв: {self.letters}')

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    def __init__(self, lang, letters):
        super().__init__(lang, letters)

    __letters_num = 26

    @staticmethod
    def is_en_letter(a):
        if a.isascii():
            print(f'Буква: {a} относится к английскому языку')
        else:
            print(f'Буква: {a} не относится к английскому языку')

    @staticmethod
    def example(text):
        return text

    def letters_num(self):
        return __letters_num


if __name__ == '__main__':
    sl = Alphabet('En', 'abcdefghijklmnopqrstuvwxyz')
    sl.print()
    print(sl.letters_num())
    EngAlphabet.is_en_letter('f')
    EngAlphabet.is_en_letter('щ')
    print(EngAlphabet.example('shla sasha po shosse i sosala suhku'))

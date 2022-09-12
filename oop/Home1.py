class character:
    default_name = 'Max'
    default_sername = 'Makarenko'

    def __init__(self,weight,height):
        self.weight = weight
        self.height = height
    def qwerty(self,lang,cantry):
        self.lang = lang
        self.cantry = cantry
        return lang,cantry

a =character('70','173')

print(a.default_name)
print(a.default_sername)
print(a.weight)
print(a.height)
print(a.qwerty('rus','Belarus'))








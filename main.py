class Char():
    """ This is playable Characters in Birth of God """
    class Goku():
        """This is Goku, our favorite saiyan! Goku had all of your transforms."""
        def __init__(self):
            pass 
        
        def normal(self, basic0, strong0, special0, ultimate0):
            self.basic0 = basic0
            self.strong0 = strong0
            self.special0 = special0
            self.ultimate0 = ultimate0
        
        def kaioken(self,basic1,strong1,special1,ultimate1):
            self.basic1 = basic1
            self.strong1 = strong1
            self.special1 = special1
            self.ultimate1 = ultimate1

        def ssj(self, basic2, strong2, special2, ultimate2):
            self.basic2 = basic2
            self.strong2 = strong2
            self.special2 = special2
            self.ultimate2 = ultimate2

        def ssj2(self, basic3, strong3, special3, ultimate3):
            self.basic3 = basic3
            self.strong3 = strong3
            self.special3 = special3
            self.ultimate3 = ultimate3

        def ssj3(self, basic4, strong4, special4, ultimate4):
            self.basic4 = basic4
            self.strong4 = strong4
            self.special4 = special4
            self.ultimate4 = ultimate4

        def ssjGod(self, basic5, strong5, special5, ultimate5):
            self.basic5 = basic5
            self.strong5 = strong5
            self.special5 = special5
            self.ultimate5 = ultimate5

        def ssjgSsj(self, basic6, strong6, special6, ultimate6):
            self.basic6 = basic6
            self.strong6 = strong6
            self.special6 = special6
            self.ultimate6 = ultimate6

        def ui(self, basic7, strong7, special7, ultimate7):
            self.basic7 = basic7
            self.strong7 = strong7
            self.special7 = special7
            self.ultimate7 = ultimate7

        def mUi(self, basic8, strong8, special8, ultimate8,dash8):
            self.basic8 = basic8
            self.strong8 = strong8
            self.special8 = special8
            self.ultimate8 = ultimate8
            self.dash8 = dash8

    class Vegeta():
        """The pridest prince of all saiyans is playable! It's Vegeta Sama!"""

        def __init__(self):
            pass

        def normal(self, basic0, strong0, special0, ultimate0):
            self.basic0 = basic0
            self.strong0 = strong0
            self.special0 = special0
            self.ultimate0 = ultimate0

        def ssj(self,basic1,strong1,special1,ultimate1):
            self.basic1 = basic1
            self.strong1 = strong1
            self.special1 = special1
            self.ultimate1 = ultimate1

        def ssj2(self, basic2, strong2, special2, ultimate2):
            self.basic2 = basic2
            self.strong2 = strong2
            self.special2 = special2
            self.ultimate2 = ultimate2

        def ssjGod(self, basic3, strong3, special3, ultimate3):
            self.basic3 = basic3
            self.strong3 = strong3
            self.special3 = special3
            self.ultimate3 = ultimate3

        def ssjgSsj(self, basic4, strong4, special4, ultimate4):
            self.basic4 = basic4
            self.strong4 = strong4
            self.special4 = special4
            self.ultimate4 = ultimate4

        def ssjgSsjA(self, basic5, strong5, special5, ultimate5):
            self.basic5 = basic5
            self.strong5 = strong5
            self.special5 = special5
            self.ultimate5 = ultimate5

    
char1 = Char().Goku()
char1.normal("punch", "Meteor dash", "kamehameha", "Genki Dama")
char1.kaioken("punch","kaioken attack","kamehameha","kamehamehax20")
char1.ssj("Angry punch", "Now I mad!", "kamehameha", "instant Kamehameha")
char1.ssj2("Velocity of phase 2", "Ultra combo", "kamehameha", "This is the transform that surpass the super saiyan!")
char1.ssj3("Power of ssj3", "Speed punch", "kamehameha", "Super Kamehameha")
char1.ssjGod("super God punch", "God Dragon attack", "Power of SSG", "Kamehameha")
char1.ssjgSsj("Super God punch","hit session","Instant Kamehameha","Kaiokenx20 God Kamehameha")
char1.ui("invisible cuffs", "Mirage", "Unattainable!","speed of gods kamehameha")
char1.mUi("Violent sequence","Destroyer of Worlds","fear of Gods","The Most powerfull Kamehameha","Incredible sequence")

char2 = Char().Vegeta()
char2.normal("punch", "Pride of Prince", "Galick-ho!", "Fireworks")
char2.ssj("Angry investide", "Energy wave", "Galick-ho!", "Big Bang Attack")
char2.ssj2("Velocity of phase 2", "Big Bang Attack", "Energy Balls", "Final Flash")
char2.ssjGod("super God punch", "Velocity of God phase", "Big Bang Attack", "Galick-ho!")
char2.ssjgSsj("Angry Investide","Dash","Galick-ho!","I'm Vegeta sama!!!")
char2.ssjgSsjA("I don't lose!", "God prince dash", "Galick-ho!", "Final Flash")

print("----------------------------------------------------DRAGON BALL SUPER : BIRTH OF GOD ------------------------------------------------------------")
print("---------------------------------------------------------------ALPHA.0.0.1-----------------------------------------------------------------------")
print("\n\n")

player = int(input("Com qual personagem você quer jogar? (1 - Goku) (2 - Vegeta): "))

if player == 1:

    print("Qual Goku vc seleciona?:\n")
    print("Normal -  (digite 1)\n")
    print("Kaioken -  (digite 2)\n")
    print("Super Saiyajin -  (digite 3)\n")
    print("Super Saiyajin 2 -  (digite 4)\n")
    print("Super Saiyajin 3 -  (digite 5)\n")
    print("Super Saiyajin Deus -  (digite 6)\n")
    print("Super Saiyajin Deus Super Saiyajin -  (digite 7)\n")
    print("Instinto Superior incompleto -  (digite 8)\n")
    print("Instinto Superior completo -  (digite 9)\n")
    tr = int(input(":  "))
    if tr == 1:
        print("Eu Gosto de lutar com os mais fortes!\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Goku usou: "+ char1.basic0 +" !")
        elif attk == 2:
            print("Goku usou: " + char1.strong0 + " !")
        elif attk == 3:
            print("Goku usou: " + char1.special0 + " !")
        elif attk == 4:
            print("Goku usou: " + char1.ultimate0 + " !")
        else:
            print("Essa técnica não é canônica!")

    elif tr == 2:
        print("A técnica do senhor kaioh me faz quebrar limites!\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Goku usou: " + char1.basic1 + " !")
        elif attk == 2:
            print("Goku usou: " + char1.strong1 + " !")
        elif attk == 3:
            print("Goku usou: " + char1.special1 + " !")
        elif attk == 4:
            print("Goku usou: " + char1.ultimate1 + " !")
        else:
            print("Essa técnica não é canônica!")

    elif tr == 3:
        print("Eu sou um Saiyajin de coração puro criado na terra!\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Goku usou: " + char1.basic2 + " !")
        elif attk == 2:
            print("Goku usou: " + char1.strong2 + " !")
        elif attk == 3:
            print("Goku usou: " + char1.special2 + " !")
        elif attk == 4:
            print("Goku usou: " + char1.ultimate2 + " !")
        else:
            print("Essa técnica não é canônica!")

    elif tr == 4:
        print("Esse é o Super Saiyajin que supera as forças de um Super Saiyajin comum!\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Goku usou: " + char1.basic3 + " !")
        elif attk == 2:
            print("Goku usou: " + char1.strong3 + " !")
        elif attk == 3:
            print("Goku usou: " + char1.special3 + " !")
        elif attk == 4:
            print("Goku usou: " + char1.ultimate3 + " !")
        else:
            print("Essa técnica não é canônica!")

    elif tr == 5:
        print("Comtemplem o supremo Super Saiyajin 3!\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Goku usou: " + char1.basic4 + " !")
        elif attk == 2:
            print("Goku usou: " + char1.strong4 + " !")
        elif attk == 3:
            print("Goku usou: " + char1.special4 + " !")
        elif attk == 4:
            print("Goku usou: " + char1.ultimate4 + " !")
        else:
            print("Essa técnica não é canônica!")

    elif tr == 6:
        print("Quer dizer que eu me tornei um Deus!?\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            char1.basic5
        elif attk == 2:
            print("Goku usou: " + char1.strong5 + " !")
        elif attk == 3:
            print("Goku usou: " + char1.special5 + " !")
        elif attk == 4:
            print("Goku usou: " + char1.ultimate5 + " !")
        else:
            print("Essa técnica não é canônica!")
    elif tr == 7:
        print("Esse é o Super Saiyajin Deus que consegue se transformar em Super Saiyajin!\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Goku usou: " + char1.basic6 + " !")
        elif attk == 2:
            print("Goku usou: " + char1.strong6 + " !")
        elif attk == 3:
            print("Goku usou: " + char1.special6 + " !")
        elif attk == 4:
            print("Goku usou: " + char1.ultimate6 + " !")
        else:
            print("Essa técnica não é canônica!")

    elif tr == 8:
        print("O poder surge em resposta a uma necessidade, não em resposta a um desejo!\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Goku usou: " + char1.basic7 + " !")
        elif attk == 2:
            print("Goku usou: " + char1.strong7 + " !")
        elif attk == 3:
            print("Goku usou: " + char1.special7 + " !")
        elif attk == 4:
            print("Goku usou: " + char1.ultimate7 + " !")
        else:
            print("Essa técnica não é canônica!")

    elif tr == 9:
        print("Os limites só existem se você os deixar existir!\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Goku usou: " + char1.basic7 + " !")
        elif attk == 2:
            print("Goku usou: " + char1.strong7 + " !")
        elif attk == 3:
            print("Goku usou: " + char1.special7 + " !")
        elif attk == 4:
            print("Goku usou: " + char1.ultimate7 + " !")
        else:
            print("Essa técnica não é canônica!")

elif player == 2:
    
    print("Qual Vegeta vc seleciona?:\n")
    print("Normal -  (digite 1)\n")
    print("Super Saiyajin -  (digite 2)\n")
    print("Super Saiyajin 2 -  (digite 3)\n")
    print("Super Saiyajin Deus -  (digite 4)\n")
    print("Super Saiyajin Deus Super Saiyajin -  (digite 5)\n")
    print("Super Saiyajin Deus Super Saiyajin Ascendido -  (digite 6)\n")
    tr = int(input(":  "))
    if tr == 1:
        print("Você não é derrotado quando perde, mais sim quando você desiste!\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Vegeta usou: " + char1.basic0 + " !")
        elif attk == 2:
            print("Vegeta usou: " + char1.strong0 + " !")
        elif attk == 3:
            print("Vegeta usou: " + char1.special0 + " !")
        elif attk == 4:
            print("Vegeta usou: " + char1.ultimate0 + " !")
        else:
            print("Essa técnica não é canônica!")

    elif tr == 2:
        print("Eu sou calmo e tenho o coração puro... pura maldade!\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Vegeta usou: " + char1.basic1 + " !")
        elif attk == 2:
            print("Vegeta usou: " + char1.strong1 + " !")
        elif attk == 3:
            print("Vegeta usou: " + char1.special1 + " !")
        elif attk == 4:
            print("Vegeta usou: " + char1.ultimate1 + " !")
        else:
            print("Essa técnica não é canônica!")

    elif tr == 3:
        print("Malditos vermes!\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Vegeta usou: " + char1.basic2 + " !")
        elif attk == 2:
            print("Vegeta usou: " + char1.strong2 + " !")
        elif attk == 3:
            print("Vegeta usou: " + char1.special2 + " !")
        elif attk == 4:
            print("Vegeta usou: " + char1.ultimate2 + " !")
        else:
            print("Essa técnica não é canônica!")

    elif tr == 4:
        print("verme insolente! não entre na frente!\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Vegeta usou: " + char1.basic3 + " !")
        elif attk == 2:
            print("Vegeta usou: " + char1.strong3 + " !")
        elif attk == 3:
            print("Vegeta usou: " + char1.special3 + " !")
        elif attk == 4:
            print("Vegeta usou: " + char1.ultimate3 + " !")
        else:
            print("Essa técnica não é canônica!")

    elif tr == 5:
        print("Kakarotto não é o único que vira o lendário Super Saiyajin!!\n\n")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Vegeta usou: " + char1.basic4 + " !")
        elif attk == 2:
            print("Vegeta usou: " + char1.strong4 + " !")
        elif attk == 3:
            print("Vegeta usou: " + char1.special4 + " !")
        elif attk == 4:
            print("Vegeta usou: " + char1.ultimate4 + " !")
        else:
            print("Essa técnica não é canônica!")

    elif tr == 6:
        print("Enquanto o inimigo estiver na minha frente, eu lutarei!!!\n\n")
        print = input("Qual dos ataques devo usar?:\n ")
        print("Ataque basico (1)\n")
        print("Ataque Forte (2)\n")
        print("Ataque especial (3)\n")
        print("Ataque ultimate (4)\n")
        attk = int(input("Qual dos ataques devo usar?:\n "))
        if attk == 1:
            print("Vegeta usou: " + char1.basic4 + " !")
        elif attk == 2:
            print("Vegeta usou: " + char1.strong4 + " !")
        elif attk == 3:
            print("Vegeta usou: " + char1.special4 + " !")
        elif attk == 4:
            print("Vegeta usou: " + char1.ultimate4 + " !")
        else:
            print("Essa técnica não é canônica!")

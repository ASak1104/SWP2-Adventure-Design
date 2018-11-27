class Text:

    def __init__(self):
        # self.listLine1 = ['                                                            \n']
        # self.listLine2 = ['     /_                                                     \n']
        # self.listLine3 = ['   |"""\-=                                                  \n']
        # self.listLine4 = ['   (____)                                                   ']
        self.totalListLine = []
        for _ in range(27):
            self.totalListLine.append(
                ['                                                            l\n']  # 60
            )
        else:
            self.totalListLine.append(
                ['     /_                                                     l\n']
            )
            self.totalListLine.append(
                ['   |"""\-=                                                  l\n']
            )
            self.totalListLine.append(
                ['   (____)                                                   l']
            )


    def initialShape(self):
        mainString = ''
        for myList in self.totalListLine:
            mainString += ''.join(myList)

        return mainString


if __name__ == '__main__':
    text = Text()
    print(text.initialShape())
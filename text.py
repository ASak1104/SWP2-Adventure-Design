class Text:

    def __init__(self):
        # ['                                                            \n']
        # ['     /_                                                     \n']
        # ['   |"""\-=                                                  \n']
        # ['   (____)                                                   ']

        # 게임에서의 초기 좌표계 설정
        self.totalListLine = []
        for _ in range(27):
            self.totalListLine.append(
                ['                                                                                \n']  # 80
            )
        else:
            self.totalListLine.append(
                ['     /_                                                                         \n']
            )
            self.totalListLine.append(
                ['   |"""\-=                                                                      \n']
            )
            self.totalListLine.append(
                ['   (____)                                                                       ']
            )

        # 대포가 날아가는 포물선의 좌표계
        self.currentListLine = self.totalListLine


    def initialMap(self):
        mainString = ''
        for myList in self.totalListLine:
            mainString += ''.join(myList)

        return mainString


    def currentMap(self, listPoint):
        pass


if __name__ == '__main__':
    text = Text()
    print(text.initialShape())
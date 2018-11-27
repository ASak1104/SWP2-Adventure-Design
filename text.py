class Text:

    def __init__(self):
        # ['                                                            \n']
        # ['     /_                                                     \n']
        # ['   |"""\-=                                                  \n']
        # ['   (____)                                                   ']

        # 게임에서의 초기 좌표계 설정(row, column)
        self.totalListLine = []
        for _ in range(27):
            self.totalListLine.append(
                [' '] * 80  # 80
            )
        else:
            self.totalListLine.append([' '] * 5 + ['/', '_'] + [' '] * 73)
            self.totalListLine.append([' '] * 3 + ['|', '\"', '\"', '\"', '\\', '-', '='] + [' '] * 70)
            self.totalListLine.append([' '] * 3 + ['(', '_' * 4, ')'] + [' '] * 70)


        # 시작점의 좌표
        self.startPoint = (28, 10)


    def initialMap(self):
        mainString = ''
        for myList in self.totalListLine:
            mainString += ''.join(myList) + '\n'

        return mainString


    def currentMap(self, target, point):
        myMap = self.totalListLine
        # (row, column)
        myMap[target[0]][target[1]] = '⊙'
        currentPoint = (self.startPoint[0] - point[1], self.startPoint[1] + point[0])
        if currentPoint == target:
            myMap[currentPoint[0]][currentPoint[1]] = '★'
            mainString = ''
            for myList in myMap:
                mainString += ''.join(myList) + '\n'

            return mainString, True
        else:
            myMap[currentPoint[0]][currentPoint[1]] = '●'
            mainString = ''
            for myList in myMap:
                mainString += ''.join(myList) + '\n'

            return mainString, False



if __name__ == '__main__':
    text = Text()
    print(text.initialMap())
    print(text.currentMap((17, 40), (60, 0))[0])
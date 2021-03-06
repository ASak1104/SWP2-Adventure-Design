from copy import deepcopy

class Cannon:

    def __init__(self, target):
        # ['                                                            ']
        # ['     /_                                                     ']
        # ['   |"""\-=                                                  ']
        # ['   (____)                                                   ']

        # 게임에서의 초기 행렬 설정(row, column)
        self.totalListLine = []
        # (30 * 80) matrix, (0, 0) ~ (29, 79)■
        for _ in range(26):
            self.totalListLine.append([' '] * 80)  # column 의 갯수
        else:
            self.totalListLine.append([' '] * 5 + ['/', '_'] + [' '] * 73)
            self.totalListLine.append([' '] * 3 + ['|', '\"', '\"', '\"', '\\', '-', '='] + [' '] * 70)
            self.totalListLine.append([' '] * 3 + ['(', '_' * 4, ')'] + [' '] * 70)
            self.totalListLine.append(['▀'] * 80)

        # 타겟 지정
        self.target = target
        self.totalListLine[target[0]][target[1]] = '◎'

        # 맵 깊은 복사, 새로운 리스트 객체
        self.mutableMap = deepcopy(self.totalListLine)

        # 시작점의 좌표 (row, column)
        self.startPoint = (27, 10)


    # 맵을 문자열로 변환하는 메소드
    def mapToString(self, myMap):
        mainString = ''
        for myList in myMap:
            mainString += ''.join(myList) + '\n'
        return mainString


    # 초기 맵을 반환하는 메소드
    def initialMap(self):
        return self.mapToString(self.totalListLine)


    # 포탄의 위치가 담긴 맵과 명중 여부를 반환하는 메소드
    def currentMap(self, point):
        # 포탄이 움직이는 모습을 구현할 때 사용할 코드
        myMap = self.mutableMap
        # currentPoint(row, column), point(x, y)
        currentPoint = (self.startPoint[0] - point[1], self.startPoint[1] + point[0])
        for row in self.mutableMap:
            if '●' in row:
                row[row.index('●')] = '○'
        if currentPoint == self.target:
            myMap[currentPoint[0]][currentPoint[1]] = '★'
            return self.mapToString(myMap), True
        else:
            myMap[currentPoint[0]][currentPoint[1]] = '●'
            return self.mapToString(myMap), False


if __name__ == '__main__':
    import time
    cannon = Cannon((20, 50))
    tempList = [(0, 0), (1, 1), (2, 2), (3, 3)]
    print(cannon.initialMap())
    for item in tempList:
        print(cannon.currentMap(item)[0])
        time.sleep(1)
    print(cannon.initialMap())
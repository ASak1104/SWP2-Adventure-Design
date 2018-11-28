from copy import deepcopy

class Cannon:

    def __init__(self, target):
        # ['                                                            ']
        # ['     /_                                                     ']
        # ['   |"""\-=                                                  ']
        # ['   (____)                                                   ']

        # 게임에서의 초기 행렬 설정(row, column)
        self.totalListLine = []
        # (30 * 80) matrix, (0, 0) ~ (29, 79)
        for _ in range(27):
            self.totalListLine.append([' '] * 80)  # column 의 갯수
        else:
            self.totalListLine.append([' '] * 5 + ['/', '_'] + [' '] * 73)
            self.totalListLine.append([' '] * 3 + ['|', '\"', '\"', '\"', '\\', '-', '='] + [' '] * 70)
            self.totalListLine.append([' '] * 3 + ['(', '_' * 4, ')'] + [' '] * 70)

        # 리스트 복사 후에 로직을 수정할 필요가 있음
        self.mutableMap = deepcopy(self.totalListLine)

        # 타겟 지정
        self.target = target
        self.totalListLine[target[0]][target[1]] = '◎'

        # 시작점의 좌표
        self.startPoint = (28, 10)


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
        # myMap = deepcopy(self.totalListLine)
        myMap = self.mutableMap
        # (row, column)
        currentPoint = (self.startPoint[0] - point[1], self.startPoint[1] + point[0])
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
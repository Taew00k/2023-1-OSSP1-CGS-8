import pyrestyle

class rectangle:
    count = 0

    # 초기자(initializer)
    def __init__(self, width, height):
        self.width = width
        self.height = height
        rectangle.count += 1

    # 메서드
    '''계산하는 함수'''
    def Calcarea(self):
        ''' 계산하는 함수를 나타낸다
        '''
        area = self.width*self.height + self.width*self.height
        return area
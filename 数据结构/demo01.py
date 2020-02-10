'''
    用一个数组实现两个栈
'''


class DoubleStack:

    def __init__(self):
        self.stack = []
        self.l_len = 0
        self.r_len = 0

    def l_push(self,number):
        if self.r_len == 0:
            self.stack.insert(0,number)
            self.l_len += 1
        else:
            self.stack.insert(self.r_len,number)
            self.l_len += 1

    def l_pop(self):
        if self.l_len == 0:
            raise Exception('The left stack is empty')
        else:
            number = self.stack.pop(-self.l_len)
            self.l_len -= 1
            return number

    def r_push(self,number):
        if self.l_len == 0:
            self.stack.append(number)
            self.r_len += 1
        else:
            self.stack.insert(self.r_len,number)
            self.r_len += 1

    def r_pop(self):
        if self.r_len == 0:
            raise Exception('The right stack is empty')
        else:
            number = self.stack.pop(self.r_len-1)
            self.r_len -= 1
            return number


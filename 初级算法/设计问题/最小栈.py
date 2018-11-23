class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) >= 1:
            self.stack = self.stack[:-1]

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) >= 1:
            return self.stack[-1]
        else:
            return

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)

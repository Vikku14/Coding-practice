class tree:
    # vo kon baita h
    def __init__(self, inval=None):
        self.value = inval
        if self.value:
            self.left = tree()
            self.right = tree()
        else:
            self.left = None
            self.right = None
        return

    def isempty(self):
        return (self.value == None)

    def inorder(self):
        if self.isempty():
            return ([])
        else:
            return (self.left.inorder() +
                    [self.value] +
                    self.right.inorder()
                    )

    def __str__(self):
        return (str(self.inorder()))

    def find(self, v):
        if (self.isempty):
            return False
        else:
            if self.value == v:
                return True
            elif v > self.value:
                return (self.right.find(v))
            else:
                return (self.left.find(v))

    def minval(self):
        if self.left.isempty():
            return self.value
        else:
            return self.left.minval()

    def maxval(self):
        if self.right.isempty():
            return self.value
        else:
            return self.right.maxval()

    def insert(self, v):

        if self.isempty():
            self.value = v
            self.left = tree()
            self.right = tree()
        if self.value == v:
            return
        else:
            if v < self.value:
                self.left.insert(v)
                return
            elif v > self.value:
                self.right.insert(v)
                return

    def delete(self, v):
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return
        if v == self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.copyright()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return

    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
        return

    def copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        return

    def isleaf(self):
        return (self.left.isempty() and self.right.isempty())

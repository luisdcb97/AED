class Fila:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def get_size(self):
        return len(self.data)

    def peek(self):
        if self.is_empty():
            raise IndexError
        else:
            return self.data[0]

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)



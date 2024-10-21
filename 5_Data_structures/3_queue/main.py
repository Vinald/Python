def main():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    # q.enqueue(30)
    q.display()
    # print(q.dequeue())
    # q.display()
 

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

    def display(self):
        print(self.queue)


if __name__ == '__main__':
    main()

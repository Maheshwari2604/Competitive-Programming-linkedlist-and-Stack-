class priority_queue:
    def __init__(self):
        self.queue = []

    def insert(self , data):
        self.queue.append(data)

    def print_list(self):
        if self.queue is None:
            print('queue is empty')
        else:
            print(self.queue)

    def delete(self):
        max = 0
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[max]:
                max = i
        priority = self.queue[max]
        del self.queue[max]
        print(priority)
        return priority

    

if __name__ == "__main__":
    q = priority_queue()
    q.print_list()
    q.insert(3)
    q.insert(13)
    q.insert(36)
    q.insert(23)
    q.insert(30)
    q.print_list()
    q.delete()
    q.print_list()
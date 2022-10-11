import time

class PrioQueue(object):
    def __init__(self, sortOrder = min):
        self.queue = []
        self.sortOrder = sortOrder

    def __str__(self):
        return ' '.join(['\n' + str(i[0]) for i in self.queue])

    def peek(self):

        return self.queue[0]

    def delete(self, data):

        for item in self.queue:
            if item[0] == data:
                self.queue.remove(item)
                return item

            return 'Value not found'

    def changePriority(self, data, newPrio):

        newPrioQ = PrioQueue()

        for item in self.queue:
            if item[0] == data:
                item[1] = newPrio
        
        for item in self.queue:
            newPrioQ.insert(item[0], item[1])

        self.queue = newPrioQ.queue


    def insert(self, data, prio):
        
        if self.queue == []:
            self.queue.append([data, prio])

        else:
            newQ = []
            for item in self.queue:

                if self.sortOrder == 'max':
                    if int(item[1]) > prio:
                        newQ.append(item)
                        continue

                else:
                    if int(item[1]) < prio:
                        newQ.append(item)
                        continue

                if newQ.__contains__([data, prio]):
                    newQ.append(item)
                
                else:
                    newQ.append([data, prio])
                    newQ.append(item)

            if newQ.__contains__([data, prio]) != True:
                newQ.append([data, prio])

            self.queue = newQ

testQ = PrioQueue('min')
testQ.insert(1, 5)
testQ.insert(3, 2)
testQ.insert(5, 9)
testQ.insert(0, 8)
testQ.changePriority(0, 3)
print(testQ)
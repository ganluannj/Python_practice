
class Queue(object):
    
    def __init__(self):
        self.vals=[]
    
    def insert(self, e):
        # insert a element in quene
        self.vals.append(e)
    
    def remove (self):
        # remove a element in quene and return the element
        if(len(self.vals)):
            temp=self.vals[0]
            self.vals.remove(temp)
            return temp
        else:
            raise ValueError('quene is empty!')
    
    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
            
            

#%%
q=Queue()
print(q)
q.insert(3)
q.insert(4)
print (q)

#%%
q.remove()
q.remove()
q.remove()

#%%
queue = Queue()
queue.insert(5)
queue.insert(6)
queue.remove()

queue.insert(7)
queue.remove()

queue.remove()
queue.remove()
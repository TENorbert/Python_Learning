#!/usr/bin python



class stack(object):
    def __init__(self):
        self.mlist = []

    def get(self):
        try:
            return self.mlist.pop()
        except:
            print("Stack in Empty")
    
    def put(self, data):
        self.mlist.append(data)

    def is_empty(self):
        return self.mlist == []

    def peep(self):
        return self.mlist[len(self.mlist)-1]
     
    def show(self):
         print(self.mlist)



ms = stack()
ms.put(1)
ms.put(-1)
ms.put(10)
ms.put(-10)
ms.show()
    
ms.get()
ms.get()
ms.get()

ms.show()

ms.get()
ms.show()
ms.get()

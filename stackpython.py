
class Stack(object):
    
    def __init__(self):
        self.slist = []
    """ Stack created"""
    
    def addItem(self, item):
        self.slist.append(item)
    
    def getItem(self):
        return self.slist.pop()

    def isEmpty(self):
        return self.slist == []

    def sSize(self):
        return len(self.slist)

    def showStack(self):
        for l in self.slist:
            print(l, "\t")

 

#if __name__() == "__main__":

# Method 1
def string_reverse1(istr):
    """ reverse string """
    rev_str = ''
    slen = len(istr)
    while slen > 0:
        rev_str += istr[slen-1]
        slen = slen - 1
    
    return rev_str

# Method2
def string_reverse2(istr):
    return istr[::-1]
    
# Method 3
def string_reverse3(istr):
    lstr = list(istr)
    lstr.reverse()
    return "".join(lstr)


 

ms = Stack()

name = "ABCDEFG"

for l in name:
    ms.addItem(l)


#ms.showStack()
print(ms.sSize())

#print("Size of Stack = {}".format(ms.sSize))
# Now reverese string 
rname =''

ss = ms.sSize()

#while not ms.isEmpty():
while ms.isEmpty() != True:
    rname += ms.getItem()

"""
print("Size of Original String is = {}".format(ss))
print("The Original String is " + name)

print("Size of Reverse String is {}".format(len(rname)))
print("Reverse String is " + rname)

print("Reverse String Method 1: \"{}\" ".format(string_reverse1(name)))
print("Reverse String Method 2: \"{}\" ".format(string_reverse2(name)))
print("Reverse String Method 3: \"{}\" ".format(string_reverse3(name)))

"""


### Time comparison between List and Dict Data Structures!

given_names = ["jack", "bob", "mary", "ann", "pierre", "martha",
               "claus", "clause", "pablo", "susan", "gustav"]

def create_dataset():
    import random
    num_entries = 1000000
    f = open("name_data.txt", "w")
    for i in range(num_entries):
        current = random.choice(given_names)
        f.write(current + "\n")
    f.close()

def read_dataset_list():
    class_counts = []  # using list for counts
    for c in given_names:
        class_counts.append(0)
    with open("name_data.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                class_counts[given_names.index(line)] +=1
    print(class_counts)


def read_dataset_dict():
    class_counts = {} # using dict for counts
    for c in given_names:
        class_counts[c] = 0
    with open("name_data.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                class_counts[line] +=1
    print(class_counts)




import time

t0 = time.time()
create_dataset()
t1 = time.time()
print("creating the dataset took %0.1f seconds\n" %(t1-t0))


t0 = time.time()
read_dataset_list()
t1 = time.time()
print("List Reading Dataset took %0.1f seconds\n" %(t1-t0))


t0 = time.time()
read_dataset_dict()
t1 = time.time()
print("Dict Reading Dataset took %0.1f seconds\n" %(t1-t0))

class Vocabulary:
    def __init__(self, string):
        self.string = string
        self.list1 = []
        self.list2 = []
        for i in string.split():
            self.list1.append(i)
        for i in string:
            self.list2.append(i)

    def statistics(self):
        set1 = set(self.list1)
        set2 = set(self.list2)
        return len(set1), len(set2)

    def update(self, string):
        if len(string) > 1:
            self.list1.append(string)
        else:
            self.list2.append(string)

    def to_string(self):
        temp = None
        for word in self.list1:
            temp = temp + " " + word
        return temp

a = Vocabulary("ana are mere")
print(a.statistics())
b = Vocabulary("Ana nu mai are mere")
print(b.statistics())
print(a.update("eu"))
print(a.statistics())
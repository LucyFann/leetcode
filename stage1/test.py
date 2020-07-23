
class sort():
    def bubble_sort(self,blist):
        count = len(blist)
        for i in range(0, count):
            for j in range(i + 1, count):
                if blist[i] > blist[j]:
                    blist[i], blist[j] = blist[j], blist[i]
        return blist

    def quick_sort(self,qlist):
        if qlist == []:
            return []
        else:
            qfirst = qlist[0]
            qless = self.quick_sort([l for l in qlist[1:] if l < qfirst])
            qmore = self.quick_sort([m for m in qlist[1:] if m >= qfirst])
            return qless + [qfirst] + qmore


    def select_sort(self,slist):
        for i in range(len(slist)):
            x = i
            for j in range(i, len(slist)):
                if slist[j] < slist[x]:
                    x = j
            slist[i], slist[x] = slist[x], slist[i]
        return slist


s = sort()
a = b = c = [2,4,5,2,5]
a = s.quick_sort(a)

print(a)
print(s.bubble_sort(b))
print(s.select_sort(c))
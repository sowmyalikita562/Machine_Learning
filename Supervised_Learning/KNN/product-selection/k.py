
import operator
s={"C3":3,"C2":2,"C4":0,"C5":3,"C1":3}
s=s.items()
print(s)
s = sorted(s, key = operator.itemgetter(1),reverse=True)
print(s)
print(dict(s))

# def f(n):
#     if n<=1:
#         return n
#     else:
#         return (f(n-1) + f(n-2))
#
# a = [f(i) for i in range(20)]
# print(a)
i = str(1)
aid = "520" + i.rjust(5,'0')
print(aid)
print(type(aid))
tokeninfo={}
tokeninfo["aid"] = aid
print(tokeninfo)
print(aid)
print(type(aid))
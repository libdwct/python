'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com

make powerset using bit operator
'''

def powerset(s):
    lt = []
    n = len(s)
    for i in range(1<<n):   #if you don't want Empty Set, use "for i in range(1, 1<<n)"
        lt.append([s[j] for j in range(n) if i & (1<<j)])

    return lt

# example 1
s = [1, 2, 3]
print(powerset(s))
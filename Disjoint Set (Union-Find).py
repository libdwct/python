'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source: https://swexpertacademy.com/
implement disjoint set
'''

p = []
rank = []

def Make_set(x):
    p[x] = x
    rank[x] = 0

def Find_set(x):
    if x != p[x]:
        p[x] = Find_set(p[x])
    return p[x]

def Union(x, y):
    Link(Find_set(x), Find_set(y))

def Link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
    if rank[x] == rank[y]:
        rank[y] += 1

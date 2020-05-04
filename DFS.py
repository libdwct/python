'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source : SW Expert Academy 4871. https://swexpertacademy.com/

problem : if 'start' node and 'end' node are connected, return 1 else 0
graph are given by 2*2 array list
'''



def DFS(graph, start, end):
    visited = []
    stack = [start]
    while(stack):
        node = stack.pop()
        visited.append(node)
        for lt in graph:
            if lt[0] == node:
                if lt[1] not in visited:
                    if lt[1] == end:
                        return 1
                    else:
                        stack.append(lt[1])

    return 0

# example 1
graph = [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
start = 1
end = 6
result = DFS(graph, start, end)
print(result)

# example 2
graph_2 = [[2, 6], [4, 7], [5, 7], [1, 5], [2, 9], [3, 9], [4, 8], [5, 3], [7, 8]]
start_2 = 1
end_2 = 9
result_2 = DFS(graph_2, start_2, end_2)
print(result_2)
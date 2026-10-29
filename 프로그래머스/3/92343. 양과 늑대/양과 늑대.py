import sys
sys.setrecursionlimit(10**8)
def solution(info, edges):
    """
    info = [0,0,1,1,1,0,1,0,1,0,1,1]
    edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
    result = 5
    
    [문제 이해]
    루트 노드에서 시작해서 양을 모은다.
    지나가면서 모은 양의 수는 항상 늑대의 수 보다 더 많아야 한다.
    양의 수를 최대로 많이 모으는 경우의 수를 return.
    
        [제약 조건]
        info의 길이 = 최대 17
        
    [접근 방식]
    
        [직관]
        갈 수 있는 모든 경우의 수를 탐색하는 경우의 수
        -> 이진트리 -> 2의 17승 -> 충분히 가능하지 않을까?
        
    [코드 설계]
        0번을 DFS에 넣고 백트래킹 처리
        
    
    """
    
    n = len(info)
    
    visited = [False] * n
    answer = 0 
    
    def backtrack(node, s, w):
        nonlocal answer
        
        answer = max(answer, s)
        
        for parent, child in edges:
            if visited[parent] and not visited[child]:
                if info[child] == 0:
                    if s+1 > w:
                        visited[child] = True
                        backtrack(child, s+1, w)
                        visited[child] = False

                if info[child] == 1:
                    if s > w+1:
                        visited[child] = True
                        backtrack(child, s, w+1)
                        visited[child] = False
                        
    
    visited[0] = True
    backtrack(0, 1, 0)
    
    return answer
# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#import sys
#sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    """
        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    문제 이해
    입력받은 격자 크기만큼의 달팽이 배열을 출력해라.
    ex) N = 3 ,
    1 2 3
    8 9 4
    7 6 5
    
    제약 조건
    1<= N <= 10
    
    접근 방식
        1. 오른, 밑 , 왼 , 위 순서대로 방향 이동
        	1-1. 방향을 나타내는 숫자를 0, 1, 2, 3 = 오른 , 밑 ,왼, 위로 표시
    		1-2 . 방향이동에 가장 적합 -> DFS or BFS + 가지치기
        	1-3. visited(중복 방문 제거)  + isValid (방문 가능 여부)
    	2. 방문 가능하다면 count 하나씩 증가.
        	2-1.  새로운 배열에 count를 적는다.
    """
    
    
    
    N = int(input()) # 격자 수
    
    dr= [0,1,0, -1]
    dc=[1,0, -1, 0]
    visited = [[False]*N for _ in range(N)]
    snail = [[0]*N for _ in range(N)]
    
    q = deque()
    q.append((0,0,0,1))  # r, c, dir, count
    visited[0][0] = True
    
    def isValid(r, c):
        return 0<= r < N and 0<= c < N
    
    while q:
        r, c, dir, cnt  = q.popleft()
        
        if cnt == N*N:
            snail[r][c] = cnt
            break
        
        snail[r][c] = cnt
        
        while True:
            dir = dir%4
            nr = r+dr[dir]
            nc = c + dc[dir]

            if isValid(nr, nc) and not visited[nr][nc]:
                q.append((nr, nc,dir, cnt+1))
                visited[nr][nc] = True
                break
            
            dir += 1
                
      
    print("#", end = "")
    print(test_case)
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=" ")
        print()
        
        
        

        
        
        
    
	
    
    
    # ///////////////////////////////////////////////////////////////////////////////////

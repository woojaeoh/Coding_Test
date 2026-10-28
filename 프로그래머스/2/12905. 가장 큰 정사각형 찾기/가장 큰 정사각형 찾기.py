def solution(board):
    """
    
    1. 문제 이해
        1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 문제.
        입력: [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]	
        출력 :  9
        제약 조건 : 격자 크기 = 10^3 * 10^3 -> O(n) or O(nlogn)으로 해결 필요
        
    2. 접근 방식
        2-1. 직관
            현재 위치에서 오른쪽이랑 밑만 탐색(BFS)해서 같은 집단을 찾고, 거기서 width , height 검사.
            
        2-2 직관 실패.
            오른쪽이랑 밑만 탐색하는 방식은 정사각형을 전혀 판별할 수 없다.
            딱 정사각형만 판별하는 법. -> DP배열을 이용.
            
            
    3. 코드 설계
        1. 이중 반복문으로 board == 1일 때, (row+1, col) , (row, col+1) 두 방향 BFS탐색
        
    """
    
    answer = 0
    
    
    n = len(board)
    m = len(board[0])

    
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    # def isSquare(r, c):   
    #     # 정사각형이 만들어 지면 -> dp += 1
    #     return board[r+1][c] == 1 and board[r][c+1] == 1 and board[r+1][c+1] == 1
    
    #맨 마지막 행, 열이 dp수행이 안되는 문제
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                dp[i+1][j+1] = min(dp[i+1][j] , dp[i][j+1], dp[i][j]) + 1
    
   # print(dp)
    for i in range(1, n+1):
        for j in range(1, m+1):
            answer = max(answer, dp[i][j]) 
                
    return answer**2
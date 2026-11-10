def solution(n, m, x, y, r, c, k):
    """
    [문제 이해]
    격자 = n * m
    (x, y) -> (r, c)
    
    조건 1. 이동 거리가 총 k여야 한다.
    2. 같은 격자를 두번 이상 방문해도 된다.
    3. 문자열이 사전 순으로 가장 빠른 경로로 탈출해야 한다.
    
    
    [접근 방식]
        [제약 조건]
        격자 크기 <= 50 * 50
        k <= 2500
        
    위 , 아래, 왼, 오  = u, d , l , r
    
    같은 k거리로 도착한 녀석들 중에 사전순으로 가장 빠른놈을 리턴해야 한다.
    그렇다면 사전순으로 빠른 순으로 탐색을 한다. d > l > r > u
    
    -> 가능한 한 방향만 가고 break 
    -> 첫 번째 방향을 선택했을 때 목적지에 도착할 수 없을 수도 있다.
    
    """
    
    
    def isValid(i, j):
        return 0<= i < n and 0<= j < m
    
    # 방향과 문자를 함께 관리
    directions = [
        ("d",1, 0),
         ("l",0, -1),
         ("r",0, 1),
         ("u",-1, 0)]
    
    cur_r, cur_c = x-1, y-1
    
    distance = abs(x-r) + abs(y-c)
    
    if distance > k or (k- distance) %2 !=0:
        return "impossible"
    
    ans = ""
    
    for step in range(k):
        for command, dr, dc in directions:
            
            nr = cur_r + dr
            nc = cur_c + dc

        # 1. 격자 범위를 벗어나면 continue
            if not isValid(nr, nc):
                continue

        # 2. 남은 이동 횟수를 계산
            remaining = k - step -1
        
        # 3. 맨해튼 거리 계산
            distance = abs(nr - (r-1)) + abs(nc - (c-1))
        
        # 4. 남은 횟수로 도착할 수 없다면 continue
            if remaining < distance:
                continue
            
            if (remaining -distance) % 2 != 0:
                continue

        # 5. 가능한 첫 번째 방향을 선택
        #    answer에 추가하고 현재 위치 갱신
            ans += command
            cur_r, cur_c = nr, nc
            break
            
        
    return ans
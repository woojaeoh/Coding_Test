from collections import deque
def solution(queue1, queue2):
    """
    문제 이해
    길이가 같은 두개의 큐가 있음. -> 항상 길이가 같아야 하는건 아니다.
    
    출력: 최소한의 push,pop 횟수
    
    제약 조건 : 
    queue1,2의 길이 = 30만 
    q 내부원소 = 10의 9승
    
    접근 방식
        하나 기준 잡고 sum//2 보다 더 작으면 append, 더 크면 push.
    
    코드 설계

    
    """
    initial_q1 = deque(queue1)
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    s1 = sum(queue1)
    s2 = sum(queue2)
    
    target = (s1 + s2) / 2
    count = 0
    
    if not target.is_integer() and target%2 != 0: # 현재 요소로 절반 절반을 나눌 수 없는 경우.
        return -1
    
    while True:
        if s1 < target:
            x = q2.popleft()
            q1.append(x)
            s1 += x
            s2 -= x
        elif s1 > target:
            x = q1.popleft()
            q2.append(x)
            s1 -= x
            s2 += x
        else:
            break
        
        if count > len(queue1) * 3:
            return -1
        
        count += 1
    
    return count
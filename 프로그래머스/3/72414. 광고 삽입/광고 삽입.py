def solution(play_time, adv_time, logs): # 11: 13 ~ 12:19
    """
    play_time ="02:03:55" -> 전체 재생시간 길이
    adv_time = "00:14:15" -> 공익광고 재생시간 길이
    logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    
    [문제 이해]
    사람들이 가장 많이 보는 누적 구간에, 공익광고를 넣는다.
    
    [제약 조건]
    logs <= 300,000
    전체 시간을 초로 바꾼다 -> 99* 3600 해도 36만 언저리-> ㄱㅊ음.
    

    [접근 방식]
    [직관]
        1. 전체 시간을 초로 바꾼다
        2. 전체 시간의 크기만큼 리스트요소를 만들고
        3. 초로 바꾼 시간에 logs가 지나갈때마다 해당 리스트를 +1 씩 해준다.
        
    [코드 설계]
    
    
    """
    
    
    def time_to_int(time):
        h, m , s = map(int, time.split(":"))
        return h*60*60 + m*60 + s
    
    def int_to_time(time):
        h = time // (60*60)
        m  = (time%3600) // 60
        s = time % 60        
        return f"{h:02d}:{m:02d}:{s:02d}"
    
    total_time = time_to_int(play_time)
    target_time = time_to_int(adv_time)
    
    total_dp = [0] * (total_time + 1)
    
    # print(f"total_time = {total_time}")
    # print(f"sliding_window = {sliding_window}")
    
    for log in logs: # 30만
        s, e = log.split("-")
        
        start_time = time_to_int(s)
        end_time = time_to_int(e)
        
        total_dp[start_time] += 1
        total_dp[end_time] -= 1
        
        # total_dp[start_time] = 1
        # total_dp[end_time] = -1
        
        # for i in range(start_time, end_time+1): #30만 -> 초과
        #     total_dp[i] += 1
            
    for i in range(1, total_time):
        total_dp[i] += total_dp[i-1]
        
    prefix = [0] * (total_time + 1)
    
    for i in range(total_time): # 30만
        prefix[i+1] = prefix[i] + total_dp[i]
        
    longest = -1
    start_time = 0
    
    for t in range(total_time - target_time + 1):
        watch_time = prefix[t + target_time] - prefix[t]
        
        if watch_time > longest:
            longest = watch_time
            start_time = t
    
#    print(longest)
        
        
    # print(time_to_int("01:45:14"))
    # print(total_dp[6314])
    return int_to_time(start_time)
  
from itertools import combinations
def solution(relation): # 15: 48 ~
    """
        [문제 이해]
        후보 키: 유일성과 최소성을 만족 한다.
            유일성 : 겹치는 값이 없다.
            최소성 : 최소 튜플 갯수(조합)로 유일성이 보장되어야한다.
        
        [출력]
        후보 키의 최대 개수
        
        [입력]
        [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
        
        
        [제약 조건]
            최대 컬럼 개수 -> 8개
            모든 컬럼 조합 -> 2의 8승 -1 = 255가지
            모든 로우 갯수 <= 20
            
            이 말인 즉슨 완전탐색이 가능하다.

        [접근 방식]
            [직관] = 완전탐색
                유일성 조건 핵심 : Set안에 튜플들을 전부 넣고, 길이가 전체 튜플 갯수랑 같은지 확인한다.
                최소성 조건 -> 튜플 조합을 저장해놓고 , subset이 된다면 최소성을 만족하지 못하는 튜플로써 제외한다.
    
        [코드 설계]
        
        튜플 조합을 저장할 방법 -> combination
        
        유일성 조건으로 튜플 조합 저장
        전체 튜플 조합 검사 후에
            최소성 조건 검사
        
    """
    
    row = len(relation)
    col = len(relation[0])
    
    num_list = [i for i in range(1, col+1)]
    # print(f"num_list = {num_list}")
    
    candidate_keys = set()
    for col_len in range(1, col+1): # 1 ~ 컬럼 최대 개수
        for comb in combinations(num_list, col_len):
            row_set = set()
            minimality = True
            
            for keys in candidate_keys:
                if set(keys).issubset(comb):
                    minimality = False
                    break
                    
            if not minimality:
                continue
                    
            for r in relation:
                col_comb = tuple(r[c-1] for c in comb)
                row_set.add(col_comb)
            
            
            if len(row_set) == row:
                candidate_keys.add(comb)
            
            
            print(candidate_keys)
    
        
    return len(candidate_keys)
   
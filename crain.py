"""
제목 : 크레인 인형뽑기 게임
작성일 : 2020-11-11
참고 :
1. board is n*n
2. 크레인은 가장 위에 있는 인형 잡기
3. 바구니에서 같은 인형 2개가 겹치면 삭제
4. 인형 없는 곳 크레인 시 아무일도 없음
5. 바구니 크기는 제한없음
6. board에서 값이 0이면 빈칸, 1~100은 서로 다른 인형
7. moves의 value값은 크레인 작동 위치

example)
board 5*5, [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
5   0 0 0 0 0
4   0 0 1 0 3
3   0 2 5 0 1
2   4 2 4 4 2
1   3 5 1 3 1

moves [1,5,3,5,1,2,1,4]

바구니 [4,3,1,1] -> [4,3] -> [4,3,3] -> [4] -> [4,2,4]
answer = (3,3) + (1,1) = 4
"""


def solution(board, moves):
    answer = 0

    bucket = []

    for move in moves:
         # 제일 위에 있는 인형을 찾는다.
        for row in board:
            if row[move-1]!=0:
                bucket.append(row[move-1]) # 바구니에 인형을 넣음
                row[move-1] = 0            # 빈칸으로 만듬
                break
        
        if len(bucket)>=2:
            if bucket[-1]==bucket[-2]:
                answer +=2
                bucket.pop(-1)
                bucket.pop(-1)
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board,moves)
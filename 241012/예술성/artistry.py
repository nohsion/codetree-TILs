from collections import deque

dr = ((-1,0), (1,0), (0,-1), (0,1))   # 상하좌우

def rot():
    arr_n = [[0] * N for _ in range(N)]  # 회전 결과 arr

    # [1] 십자모양 회전
    for i in range(N):
        arr_n[M][i] = arr[i][M]     # 가로 결정
        arr_n[i][M] = arr[M][N-1-i] # 세로 결정

    # [2] 정사각형 4개 회전
    for si, sj in ((0, 0), (0, M + 1), (M + 1, 0), (M + 1, M + 1)):
        for i in range(M):
            for j in range(M):
                arr_n[si + i][sj + j] = arr[si + M - 1 - j][sj + i]
    return arr_n

def dup(g1, g2):    # 그룹 2개의 맞닿은 변의 수 구하기
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == g1:
                for di, dj in dr:
                    ni, nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N and v[ni][nj] == g2: # 범위내, 인접 칸이 그룹2라면
                        cnt += 1
    return cnt

def get_score(g1, g2):  # 그룹 2개의 예술점수 구하기
    g1_cnt, g1_value = gcnts[g1]
    g2_cnt, g2_value = gcnts[g2]
    return (g1_cnt + g2_cnt)*g1_value*g2_value*dup(g1, g2)

def bfs(si, sj, cnt):
    q = deque()

    v[si][sj] = cnt
    q.append((si, sj))
    gcnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in dr:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] == arr[ci][cj]:   # 범위내, 미방문, 나랑 같다면
                v[ni][nj] = cnt
                q.append((ni, nj))
                gcnt += 1
    gcnts[cnt] = (gcnt, arr[si][sj])   # 그룹별 카운트 저장


# [1] 그룹 만들기 & 예술점수 구하기
def solve():
    global v, gcnts
    # (1) 그룹 생성
    v = [[0]*N for _ in range(N)]
    cnt, gcnts = 0, {}  # 그룹 카운트, 그룹별 칸수 카운트
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                cnt += 1
                bfs(i, j, cnt)
    # 그룹 만들기가 끝났다면, 그룹 2개씩 짝지어서 점수계산
    score = 0
    for i in range(1, cnt):
        for j in range(i+1, cnt+1):
            x = get_score(i, j)
            score += x
    return score


N = int(input())
M = N//2
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
ans += solve()      # 초기 예술점수
for _ in range(3):  # 1~3회전
    arr = rot()  # 회전된 arr로 바꿔줘야 함.
    x = solve()  # 각 회전 점수
    ans += x
print(ans)
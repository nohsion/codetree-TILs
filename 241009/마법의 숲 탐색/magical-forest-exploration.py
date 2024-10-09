def paint(ci, cj, d, num):
    # 자기자신 색칠, 상하좌우 색칠. 단, 출구는 -num
    arr[ci][cj] = num
    for i in range(4):
        di, dj = dr[i]
        ni, nj = ci+di, cj+dj
        if i == d:
            arr[ni][nj] = -num
        else:
            arr[ni][nj] = num

def dfs(ci, cj):
    global max_i
    max_i = max(max_i, ci-2)
    if max_i == R:
        return
    num = arr[ci][cj]
    for di, dj in dr:
        ni, nj = ci+di, cj+dj
        # 출구라면 빈칸(0),채우기용(1) 빼고 다 가능
        if num < 0:
            if v[ni][nj] == 0 and arr[ni][nj] not in (0, 1):
                v[ni][nj] = 1
                dfs(ni, nj)
                v[ni][nj] = 0
        # 출구가 아니면 num, -num만 가능
        else:
            if v[ni][nj] == 0 and arr[ni][nj] in (num, -num):
                v[ni][nj] = 1
                dfs(ni, nj)
                v[ni][nj] = 0


R, C, K = map(int, input().split()) # R행, C열, 정령 K명
arr = [[1]+[0]*C+[1] for _ in range(3)] + [[1]+[0]*C+[1] for _ in range(R)] + [[1]*(C+2)]
dr = [(-1,0), (0,1), (1,0), (0,-1)] # 북, 동, 남, 서
ans = 0
for k in range(K):
    c, d = map(int, input().split())
    num, i, j = k+2, 1, c   # 정령 번호, i행, j열
    while True:
        # [1] 남쪽 (3)
        if arr[i+1][j-1] == 0 and arr[i+2][j] == 0 and arr[i+1][j+1] == 0:
            i = i+1
            continue
        # [2] 서쪽(3)->남쪽(2) (반시계)
        elif arr[i-1][j-1] == 0 and arr[i][j-2] == 0 and arr[i+1][j-1] == 0\
                and arr[i+1][j-2] == 0 and arr[i+2][j-1] == 0:
            i, j, d = i+1, j-1, (d-1)%4
        # [3] 동쪽(3)->남쪽(2) (시계)
        elif arr[i-1][j+1] == 0 and arr[i][j+2] == 0 and arr[i+1][j+1] == 0\
                and arr[i+1][j+2] == 0 and arr[i+2][j+1] == 0:
            i, j, d = i+1, j+1, (d+1)%4
        # [4] 이동불가
        elif i == R+1:
            break
        else: break
    # 만약 골렘이 범위 벗어나면, 초기화
    if i < 4:
        arr = [[1]+[0]*C+[1] for _ in range(3)] + [[1]+[0]*C+[1] for _ in range(R)] + [[1]*(C+2)]
    # 정령 맨아래로 이동시키기
    else:
        paint(i, j, d, num)
        max_i = 0
        v = [[0]*(C+2) for _ in range(R+3)]
        dfs(i, j)
        ans += max_i

print(ans)
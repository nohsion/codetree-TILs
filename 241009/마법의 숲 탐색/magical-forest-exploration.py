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

def bfs(si, sj):
    v = [[0]*(C+2) for _ in range(R+3)]
    q = []
    max_i = 0

    v[si][sj] = 1
    q.append((si, sj))

    while q:
        ci, cj = q.pop(0)
        max_i = max(max_i, ci-2)
        if max_i == R:
            return max_i

        num = arr[ci][cj]
        for di, dj in dr:
            ni, nj = ci+di, cj+dj
            if num < 0: # 출구라면 다른 골렘으로 가능
                if v[ni][nj] == 0 and (arr[ni][nj] > 1 or arr[ni][nj] < -1):
                    v[ni][nj] = 1
                    q.append((ni, nj))
            else:       # 출구가 아니면 num, -num만 가능
                if v[ni][nj] == 0 and (arr[ni][nj] == num or arr[ni][nj] == -num):
                    v[ni][nj] = 1
                    q.append((ni, nj))
    return max_i

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
        v = [[0]*(C+2) for _ in range(R+3)]
        ans += bfs(i, j)

print(ans)
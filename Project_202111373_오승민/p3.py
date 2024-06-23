# 프로젝트 문제 3번
input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0
    # 입력 힌트

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]

    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))

    from collections import deque

    # BFS를 사용하여 곰이 갈 수 있는 위치와 벌집 찾기
    def bfs(forest, start_x, start_y, bear_size, N):
        # 상하좌우 방향 정의
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # 방문 여부를 저장하는 리스트
        visited = [[False] * N for _ in range(N)]
        # 거리 정보를 저장하는 리스트
        distance = [[0] * N for _ in range(N)]
        # BFS를 위한 큐 초기화
        queue = deque([(start_x, start_y)])
        visited[start_x][start_y] = True
        # 찾은 벌집의 위치와 거리를 저장할 리스트
        honeycombs = []

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if forest[nx][ny] <= bear_size:
                        visited[nx][ny] = True
                        distance[nx][ny] = distance[x][y] + 1
                        queue.append((nx, ny))
                        if 0 < forest[nx][ny] < bear_size:
                            honeycombs.append((distance[nx][ny], nx, ny))

        honeycombs.sort()
        return honeycombs

    while True:
        # 곰이 먹을 수 있는 벌집 찾기
        honeycombs = bfs(forest, bear_x, bear_y, bear_size, N)
        if not honeycombs:
            break

        # 가장 가까운 벌집으로 이동
        dist, new_x, new_y = honeycombs[0]
        time += dist
        bear_x, bear_y = new_x, new_y
        forest[bear_x][bear_y] = 0
        honeycomb_count += 1

        # 곰의 크기를 증가시킬 조건 확인
        if honeycomb_count == bear_size:
            bear_size += 1
            honeycomb_count = 0


    result = time
    return result

result = problem3(input)

assert result == 14
print("정답입니다.")

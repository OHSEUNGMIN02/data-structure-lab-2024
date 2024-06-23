# 프로젝트 문제 1번
input = [10, 40, 30, 60, 30]

def problem1(input):
    # 평균 계산
    mean = sum(input) / len(input)
    # 입력된 리스트의 합을 구하고, 리스트의 길이로 나누어 평균을 계산합니다.

    # 중앙값 계산을 위해 리스트 정렬
    sorted_numbers = sorted(input)
    # 중앙값을 계산하기 위해 리스트를 오름차순으로 정렬합니다.

    median = sorted_numbers[len(sorted_numbers) // 2]
    # 정렬된 리스트에서 중간 인덱스에 위치한 값을 선택하여 중앙값을 계산합니다.
    # 예를 들어, 리스트의 길이가 5일 때, 중간 인덱스는 2(5 // 2)입니다.
    result = [0,0]

    result[0] = mean
    result[1] = median
    return result

result = problem1(input)

assert result == [34, 30], f"Expected [34, 30], but got {result}"
print("정답입니다.")
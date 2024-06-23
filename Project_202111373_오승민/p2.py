# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    # 스택 초기화
    stack = []
    # 추가로 필요한 닫는 괄호 수 초기화
    close_needed = 0

    # 입력된 문자열의 각 문자에 대해 반복
    for char in input:
        if char == '(':
            # 여는 괄호인 경우 스택에 추가
            stack.append(char)
        elif char == ')':
            if not stack:
                # 스택이 비어있는 경우, 추가로 닫는 괄호가 필요함을 증가
                close_needed += 1
            else:
                # 스택에 여는 괄호가 있는 경우, 쌍을 이루므로 스택에서 제거
                stack.pop()

    # 남아있는 스택의 크기만큼 추가로 필요한 여는 괄호 수
    open_needed = len(stack)
    # 총 추가로 필요한 괄호 수는 여는 괄호 수와 닫는 괄호 수의 합
    result = open_needed + close_needed
    return result
    # 최종 결과 반환

result = problem2(input)

assert result == 3
print("정답입니다.")
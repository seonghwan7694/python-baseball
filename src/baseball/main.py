import random

def is_valid(user_input):
    if len(set(user_input)) != 3:
        raise ValueError()
    if not all(1 <= d <= 9 for d in user_input):
        raise ValueError()

def play_game(ans):
    # 게임 진행
    while True:
        user_input = input("숫자를 입력해주세요 : ")
        user_input = [int(d) for d in user_input]

        # 사용자 입력 유효성 검사
        is_valid(user_input)

        ball, strike = 0, 0

        for i in range(0, 3):
            if user_input[i] == ans[i]:
                strike += 1
            elif user_input[i] in ans:
                ball += 1
            else:
                continue

        if strike == 3:
            print("3스트라이크")
            print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
            return

        if strike == 0 and ball == 0:
            print("낫싱", end="")
        if ball > 0:
            print(f"{ball}볼 ", end="")
        if strike > 0:
            print(f"{strike}스트라이크", end="")
        print()

def restart_game():
    print("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")
    v = input()
    if v == "1":
        return True
    elif v == "2":
        return False
    raise ValueError()

def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    # 프로그램의 메인 로직을 여기에 구현
    while True:
        print("숫자 야구 게임을 시작합니다.")
        ans = random.sample(range(1, 10), 3)# 숫자 생성
        play_game(ans)
        if restart_game():
            continue
        else:
            break

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()

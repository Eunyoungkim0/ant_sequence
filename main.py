from src.ant_sequence import find_middle_two

def main():
    try:
        n = int(input("3부터 100까지의 정수를 입력하세요: "))
        if not 3 <= n <= 100:
            print("3 이상 100 이하의 정수를 입력해주세요.")
            return

        answer = find_middle_two(n)
        print(f"{n}번째 항의 가운데 두 자릿수는 {answer} 입니다.")

    except ValueError:
        print("유효하지 않은 입력입니다. 정수를 입력해주세요.")

if __name__ == "__main__":
    main()
def main() -> None:
    first = int(input())
    second, third = map(int, input().split())
    label = input()
    print(first + second + third, label)


if __name__ == "__main__":
    main()

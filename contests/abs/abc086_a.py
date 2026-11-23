def main() -> None:
    left, right = map(int, input().split())
    print("Even" if left * right % 2 == 0 else "Odd")


if __name__ == "__main__":
    main()

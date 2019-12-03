import math

def main():
    print("Part 1:", sum([(int((int(line) / 3)) - 2) for line in open("input", "r")])) # Part 1
    print("Part 2:", sum([(lambda f, x: x + f(f, (x // 3 )- 2) if x > 0 else 0)
    (lambda f, x: x + f(f, (x // 3) - 2) if x > 0 else 0, (int(i) // 3) - 2) for i in open('input').readlines()])) # Part 2

if __name__ == "__main__":
    main()
#Richard Cheung U30429525
#cs330
def karatsuba(first, second):
    split = min(len(first), len(second))
    split = split >> 1
    a = first[:-split]
    b = first[split:]
    c = second[:-split]
    d = second[split:]
    step1 = karatsuba(a, c)
    step2 = karatsuba(b, d)
    step3 = karatsuba(bin(int(a, 2) + int(b, 2))[2:], bin(int(c, 2) + int(d, 2))[2:])
    step3 = bin(int(step3, 2) - int(step1, 2))[2:]
    step3 = bin(int(step3, 2) - int(step2, 2))[2:]
    step3 += '0' * split
    step1 += ('0' * (split << 1))
    answer = bin(int(step3, 2) + int(step1, 2))[2:]
    answer = bin(int(answer, 2) + int(step2, 2))[2:]
    return answer

def main():
    f = open('07_input', 'r')
    length = int(f.readline())
    first = f.readline().replace('\n', '')
    second = f.readline().replace('\n', '')
    answer = karatsuba(first, second)
    output = open('output', 'w+')
    output.write(answer)
    output.close()


if __name__ == "__main__":
    main()

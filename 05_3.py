import timeit
from bm_search import boyer_moore_search as bm
from kmp_search import kmp_search as kmp
from rk_search import rabin_karp_search as rk


def time_count(text, pattern, loops: int = 10000):   # change loops count here, or use as argument
    bm_time = 0
    kmp_time = 0
    rk_time = 0

    print(f"\nAfter \033[93m{loops} loops\x1b[0m each algorithm tooks in \033[96maverage\x1b[0m:")
    print(f"{"String to be found:":<13} {pattern}")

    for i in range(0, loops):

        t = timeit.timeit("bm(text, pattern)", number=1, globals={"bm": bm, "text": text, "pattern": pattern})
        bm_time += t

        t = timeit.timeit("kmp(text, pattern)", number=1, globals={"kmp": kmp, "text": text, "pattern": pattern})
        kmp_time += t

        t = timeit.timeit("rk(text, pattern)", number=1, globals={"rk": rk, "text": text, "pattern": pattern})
        rk_time += t

    bm_time, kmp_time, rk_time = bm_time/loops * 1000000, kmp_time/loops * 1000000, rk_time/loops * 1000000

    print(f"\033[96m{"Boyer–Moore algorithm:":<30} \033[93m{bm_time:.10f}\x1b[0m μs")
    print(f"\033[96m{"Knuth–Morris–Pratt algorithm:":<30} \033[93m{kmp_time:.10f}\x1b[0m μs")
    print(f"\033[96m{"Rabin–Karp algorithm:":<30} \033[93m{rk_time:.10f}\x1b[0m μs")

    return bm_time, kmp_time, rk_time


def get_from_file(path):
    with open(path, "r", encoding="utf8") as f:
        data = f.read()
    return data


def main():
    bm_total = 0
    kmp_total = 0
    rk_total = 0

    def time_sum(a, b, c):
        nonlocal bm_total, kmp_total, rk_total
        bm_total += a
        kmp_total += b
        rk_total += c

    filename = "article_1.txt"
    text = get_from_file(filename)

    pattern = "поширена дія"                    # at the beginning of the file
    a, b, c = time_count(text, pattern)
    time_sum(a, b, c)

    pattern = "Step] == ele"                    # in the middle of the file
    a, b, c = time_count(text, pattern)
    time_sum(a, b, c)

    pattern = "https://prog"                    # at the end of the file
    a, b, c = time_count(text, pattern)
    time_sum(a, b, c)

    pattern = "Lorem ipsum dolor sit amet"      # not existed string
    a, b, c = time_count(text, pattern)
    time_sum(a, b, c)

    print(f"\nIn total for \033[93m{filename}\x1b[0m file:")
    print(f"\033[96m{"Boyer–Moore algorithm:":<30} \033[93m{bm_total/4:.10f}\x1b[0m μs")
    print(f"\033[96m{"Knuth–Morris–Pratt algorithm:":<30} \033[93m{kmp_total/4:.10f}\x1b[0m μs")
    print(f"\033[96m{"Rabin–Karp algorithm:":<30} \033[93m{rk_total/4:.10f}\x1b[0m μs")


    bm_total = 0
    kmp_total = 0
    rk_total = 0

    filename = "article_2.txt"
    text = get_from_file(filename)

    pattern = "структури даних, програмна імітаційна модель"        # at the beginning of the file
    a, b, c = time_count(text, pattern)
    time_sum(a, b, c)

    pattern = "Параметри 1 серії експериментів: кількість а"        # in the middle of the file
    a, b, c = time_count(text, pattern)
    time_sum(a, b, c)

    pattern = "Conference on Data Engineering Workshops, IE"        # at the end of the file
    a, b, c = time_count(text, pattern)
    time_sum(a, b, c)

    pattern = "Lorem ipsum dolor sit amet"                          # not existed string
    a, b, c = time_count(text, pattern)
    time_sum(a, b, c)

    print(f"\nIn total for \033[93m{filename}\x1b[0m file:")
    print(f"\033[96m{"Boyer–Moore algorithm:":<30} \033[93m{bm_total/4:.10f}\x1b[0m μs")
    print(f"\033[96m{"Knuth–Morris–Pratt algorithm:":<30} \033[93m{kmp_total/4:.10f}\x1b[0m μs")
    print(f"\033[96m{"Rabin–Karp algorithm:":<30} \033[93m{rk_total/4:.10f}\x1b[0m μs")


if __name__ == "__main__":
    main()
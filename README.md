# Аналіз швидкості алгоритмів пошуку
Аналіз алгоритмів пошуку Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа за допомогою заміру часу.\
Для заміру часу використовувався модуль [timeit](https://docs.python.org/uk/3/library/timeit.html).\
Алгоритми були запущені по 10000 разів для пошуку чотирьох рядків (рядок з початку, з середини, з кінця файлу та не існуючий рядок) у двух текстових файлах.\
Було отримано наступні данні:

---

[1-ий файл даних](https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh/view?usp=sharing)

``String to be found:`` **поширена дія** - частина тексту з початку файлу\
``Boyer–Moore algorithm:         81.8163625037 μs``\
``Knuth–Morris–Pratt algorithm:  234.6895474086 μs``\
``Rabin–Karp algorithm:          544.8203914955 μs``

---

``String to be found:`` **Step] == ele** - частина тексту в середині файлу\
``Boyer–Moore algorithm:         137.6008499075 μs``\
``Knuth–Morris–Pratt algorithm:  444.3511222817 μs``\
``Rabin–Karp algorithm:          1202.8385703165 μs``

---

``String to be found:`` **https ://prog** - частина тексту в кінці файлу\
``Boyer–Moore algorithm:         247.6428018104 μs``\
``Knuth–Morris–Pratt algorithm:  909.5224938977 μs``\
``Rabin–Karp algorithm:          2493.0548329154 μs``

---

``String to be found:`` **Lorem ipsum dolor sit amet** - не існуючий рядок\
``Boyer–Moore algorithm:         146.1641303897 μs``\
``Knuth–Morris–Pratt algorithm:  944.8627086047 μs``\
``Rabin–Karp algorithm:          2528.8438297968 μs``

---

Всього:
*   Boyer–Moore algorithm:         **153.3060361528 μs**
*   Knuth–Morris–Pratt algorithm:  **633.3564680482 μs**
*   Rabin–Karp algorithm:          **1692.3894061310 μs**

---

[2-ий файл даних](https://drive.google.com/file/d/13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ/view?usp=sharing)

``String to be found:`` **структури даних, програмна імітаційна модель** - частина тексту з початку файлу\
``Boyer–Moore algorithm:         47.5715274210 μs``\
``Knuth–Morris–Pratt algorithm:  236.5842043029 μs``\
``Rabin–Karp algorithm:          547.7928180939 μs``

---

``String to be found:`` **Параметри 1 серії експериментів: кількість а** - частина тексту в середині файлу\
``Boyer–Moore algorithm:         139.4887857034 μs``\
``Knuth–Morris–Pratt algorithm:  1010.1295053151 μs``\
``Rabin–Karp algorithm:          2421.2037817189 μs``

---

``String to be found:`` **Conference on Data Engineering Workshops, IE** - частина тексту в кінці файлу\
``Boyer–Moore algorithm:         116.6414530911 μs``\
``Knuth–Morris–Pratt algorithm:  1282.8044998067 μs``\
``Rabin–Karp algorithm:          3552.2827744888 μs``

---

``String to be found:`` **Lorem ipsum dolor sit amet** - не існуючий рядок\
``Boyer–Moore algorithm:         197.4147803820 μs``\
``Knuth–Morris–Pratt algorithm:  1397.9577161062 μs``\
``Rabin–Karp algorithm:          3772.5541020027 μs``

---

Всього:
*   Boyer–Moore algorithm:         **125.2791366494 μs**
*   Knuth–Morris–Pratt algorithm:  **981.8689813827 μs**
*   Rabin–Karp algorithm:          **2573.4583690761 μs**

---

На основі отриманих даних видно що у загальному випадку алгоритм Боєра-Мура буде швидшим для обох файлів.

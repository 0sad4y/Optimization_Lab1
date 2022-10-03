import time
from math import *


def main():
    function_index = int(input('Введите номер функции: '))
    method_index = int(input('Введите номер метода: '))
    start_point = float(input('Введите начальную точку: '))

    point = [start_point]
    step = 1
    a = 0
    b = 0
    k = 0
    accuracy = 0.001
    difference = accuracy / 10
    is_finished = False

    def func(x):
        try:
            if function_index == 1:
                res = (x - 1) ** 2
            elif function_index == 2:
                res = 4 * x ** 3 - 8 * x ** 2 - 11 * x + 5
            elif function_index == 3:
                res = x + 3 / x ** 2
            elif function_index == 4:
                res = (x + 2.5) / (4 - x ** 2)
            elif function_index == 5:
                res = -sin(x) - sin(3 * x) / 3
            else:
                res = -2 * sin(x) - sin(2 * x) - 2 * sin(3 * x) / 3
        except ZeroDivisionError:
            res = inf
        return res

    # region dsk
    if func(point[0]) > func(point[0] + step):
        a = point[0]
        point.append(point[0] + step)
        k = 2
    else:
        if func(point[0] - step) >= func(point[0]):
            a = point[0] - step
            b = point[0] + step
            is_finished = True
        else:
            b = point[0]
            point.append(point[0] - step)
            step = -step
            k = 2

    while not is_finished:
        point.append(point[0] + 2 ** (k - 1) * step)

        if func(point[k - 1]) > func(point[k]):
            if step > 0:
                a = point[k - 2]
            else:
                b = point[k]
            k += 1
        else:
            if step > 0:
                b = point[k]
            else:
                a = point[k]
            is_finished = True
    # endregion

    print('[', a, ',', b, ']', sep='')

    result = None
    if method_index == 1:
        while (b - a) / 2 >= accuracy:
            x1 = 0.5 * (a + b) - difference
            x2 = 0.5 * (a + b) + difference
            if func(x1) <= func(x2):
                b = x2
            else:
                a = x1

        result = (a + b) / 2
    elif method_index == 2:
        sequence_fibonacci = [1, 1]
        k = 0

        limit = (b - a) / (2 * accuracy)
        while sequence_fibonacci[len(sequence_fibonacci) - 1] < limit:
            sequence_fibonacci.append(sequence_fibonacci[-1] + sequence_fibonacci[-2])

        number_of_calculations = len(sequence_fibonacci) - 1

        x1 = a + sequence_fibonacci[-3] * (b - a) / sequence_fibonacci[-1]
        x2 = a + sequence_fibonacci[-2] * (b - a) / sequence_fibonacci[-1]

        while k != number_of_calculations - 3:
            if func(x1) <= func(x2):
                b = x2
                x2 = x1
                x1 = a + sequence_fibonacci[-4 - k] * (b - a) / sequence_fibonacci[-2 - k]
            else:
                a = x1
                x1 = x2
                x2 = a + sequence_fibonacci[-3 - k] * (b - a) / sequence_fibonacci[-2 - k]
            k += 1

        if func(x1) <= func(x1 + difference):
            result = (a + x2) / 2
        else:
            result = (x1 + b) / 2
    elif method_index == 3:
        xf_arr = [[a, 0], [0.5 * (a + b), 0], [b, 0], [0, 0]]
        #       [[x1, f(x1)], [x2, f(x2)], [x3, f(x3)], [x4, f(x4)]]
        arg_x = 0

        while True:
            temp = 10000
            for i in range(3):
                xf_arr[i][1] = func(xf_arr[i][0])

                if xf_arr[i][1] == inf:
                    xf_arr[i][1] = 1000000

                if xf_arr[i][1] < temp:
                    temp = xf_arr[i][1]
                    arg_x = xf_arr[i][0]

            xf_arr[3][0] = 0.5 * (((xf_arr[1][0] ** 2 - xf_arr[2][0] ** 2) * xf_arr[0][1] +
                                   (xf_arr[2][0] ** 2 - xf_arr[0][0] ** 2) * xf_arr[1][1] +
                                   (xf_arr[0][0] ** 2 - xf_arr[1][0] ** 2) * xf_arr[2][1]) /
                                  ((xf_arr[1][0] - xf_arr[2][0]) * xf_arr[0][1] +
                                   (xf_arr[2][0] - xf_arr[0][0]) * xf_arr[1][1] +
                                   (xf_arr[0][0] - xf_arr[1][0]) * xf_arr[2][1]))
            xf_arr[3][1] = func(xf_arr[3][0])
            for i in range(4):
                print(xf_arr[i][0], xf_arr[i][1], end=' | ')
            print('')

            if abs(xf_arr[3][0] - arg_x) <= accuracy:
                break

            swapped = True
            k = -1
            while swapped:
                swapped = False
                k += 1
                for i in range(1, 4 - k):
                    if xf_arr[i - 1][0] > xf_arr[i][0]:
                        xf_arr[i - 1], xf_arr[i] = xf_arr[i], xf_arr[i - 1]
                        swapped = True
            for i in range(4):
                print(xf_arr[i][0], xf_arr[i][1], end=' | ')
            print('\n')
            time.sleep(0.2)

            temp = -10000
            unused_index = 0
            for i in range(4):
                if xf_arr[i][1] > temp:
                    temp = xf_arr[i][1]
                    unused_index = i

            temp_x = []
            for i in range(4):
                if i != unused_index:
                    temp_x.append(xf_arr[i][0])
            for i in range(3):
                xf_arr[i][0] = temp_x[i]

        result = xf_arr[3][0]

    print('x =', result)


if __name__ == '__main__':
    main()

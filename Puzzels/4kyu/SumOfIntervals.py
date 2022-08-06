# codewars challenge link
# https://www.codewars.com/kata/52b7ed099cdc285c300001cd


def sum_of_intervals(intervals):
    changed = True
    while changed:
        s_intervals = [list(intervals.pop(0))]
        changed = False
        for interval in intervals:
            append_to_s_interval = True
            for s_int in s_intervals:
                # don't add when both are equal or interval is complete inbetween the interval
                if interval[0] == s_int[0] and interval[1] == s_int[1] \
                        or interval[0] >= s_int[0] and interval[1] <= s_int[1]:
                    changed = True
                    append_to_s_interval = False
                    continue

                # if the FROM and TO of interval is outside an existing interval
                if interval[0] < s_int[0] and interval[1] > s_int[1]:
                    s_int[0] = interval[0]
                    s_int[1] = interval[1]
                    changed = True
                    append_to_s_interval = False
                    continue

                # if The FROM is inbetween an interval and TO is bigger than the interval
                if s_int[0] <= interval[0] <= s_int[1] < interval[1]:
                    s_int[1] = interval[1]
                    changed = True
                    append_to_s_interval = False
                    continue

                # if The TO is inbetween an interval and FROM is smaller than the interval
                if interval[0] < s_int[0] <= interval[1] <= s_int[1]:
                    s_int[0] = interval[0]
                    changed = True
                    append_to_s_interval = False
                    continue
            if append_to_s_interval:
                s_intervals.append(list(interval))
        intervals = s_intervals
    calc_sum = 0
    for interval in intervals:
        calc_sum += interval[1] - interval[0]
    return calc_sum


if __name__ == '__main__':
    print(sum_of_intervals([(-312, 195), (205, 245), (126, 432), (492, 500)]) == 752)
    print(sum_of_intervals([(1, 5)]) == 4)
    print(sum_of_intervals([(1, 5), (6, 10)]) == 8)
    print(sum_of_intervals([(1, 5), (1, 5)]) == 4)
    print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7)
    print(sum_of_intervals([(-211, 420), (-438, -291), (64, 378), (-15, 3), (-52, 333), (-27, 366), (-223, 255)]) == 790)
    print(sum_of_intervals([(266, 491), (477, 483), (-298, -286)]) == 237)


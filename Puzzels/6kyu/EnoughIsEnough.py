# codewars challenge link
# https://www.codewars.com/kata/554ca54ffa7d91b236000023

def delete_nth(order,max_e):
    number_counts = dict()
    new_order = list()
    for number in order:
        if number not in number_counts:
            number_counts[number] = 0
        if number_counts[number] < max_e:
            new_order.append(number)
        number_counts[number] += 1
    return new_order


if __name__ == '__main__':
    print(delete_nth([20, 37, 20, 21], 1) == [20, 37, 21])
    print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) == [1, 1, 3, 3, 7, 2, 2, 2])

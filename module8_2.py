def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result = result + i
        except TypeError:
            incorrect_data = incorrect_data + 1
        print(f"Некорректный тип данных для подсчета суммы {i}")
    return result, incorrect_data


def calculate_average(numbers):
    if isinstance(numbers, (int, float)):
        print(f'В numbers записан некорректный тип данных')
        return None
    elif not isinstance(numbers, (list, tuple)):
        personal_sum(numbers)
        return 0
    else:
        try:
            sum_numbers = personal_sum(numbers)
            if sum_numbers[1] == len(numbers):     # sum_numbers[0] - result, sum_numbers[1] - incorrect_data
                return 0
            else:
                return sum_numbers[0]/(len(numbers) - sum_numbers[1])
        except ZeroDivisionError:
             return 0


print(f'Результат 3: {calculate_average(567)}')



secret_num = ['1', '2', '3', '4']

def check(numbers):
    my_list = []
    for i in numbers:
        if i != ' ':
            my_list.append(i)
    numbers = my_list
    print(numbers)
    if len(numbers) > 4 or len(numbers) < 4:
        return "Enter only four numbers"
    elif len(set(numbers)) < 4:
        return "Values must not be repeated"
    try:
        for i in range(len(numbers)):
            if int(numbers[i]) < 1 or int(numbers[i]) > 9:
                return "Enter values from 1 to 9"
    except ValueError:
        return "Enter only numbers"
    else:
        return numbers

def result_game(numbers):
    count_bulls = 0
    count_cows = 0
    for i in range(len(numbers)):
        if numbers[i] == secret_num[i]:
            count_bulls += 1
        elif numbers[i] in secret_num:
            count_cows += 1
    if count_bulls == 4:
        return 'Your Win!'
    elif count_bulls or count_cows:
        return f'You got {count_bulls} bulls and {count_cows} cows'
    else:
        'No identical values'

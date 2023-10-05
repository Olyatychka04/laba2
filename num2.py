def process_input():
    input_arg = input("Введите данные: ")
    if input_arg.isdigit():
        num = int(input_arg)
        if num < 2:
            return "Число не является простым"
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return "Число не является простым"
        return "Число является простым"

    input_list = eval(input_arg)
    if isinstance(input_list, list):
        product = 1
        for i in range(len(input_list)):
            if i % 2 != 0:
                product *= input_list[i]
        max_element = max(input_list)
        input_list.remove(max_element)
        return "Произведение элементов с нечетными номерами:", product, "Новый список после удаления наибольшего элемента:", input_list

    elif isinstance(input_list, dict):
        sorted_dict = sorted(input_list.items(), key=lambda x: x[0], reverse=True)
        for i in sorted_dict:
            print(i[0], i[1])


    elif isinstance(input_list, str):
            count = 0
            vowel = set("аеиоуюяэ")
            for letter in input_list:
                if letter in vowel:
                    count = count + 1
            count_2 = 0
            consonant = set("бвгджзйклмнпрстфхцчшщ")
            for letter in input_list:
                if letter in consonant:
                    count_2 = count_2 + 1
            return count, count_2
    else:
        return "Неизвестный тип данных"

result = process_input()
print(result)


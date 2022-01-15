with open('task_2.txt', 'r', encoding='utf-8') as f:
    lines_counter = 0
    word_counter = 0

    for line in f:
        lines_counter += 1
        word_counter += len(line.split())

    print(f'''Количество строк - {lines_counter}
Количество слов - {word_counter}''')

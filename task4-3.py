def redaktor(text, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        even_lines = [line.strip() for i, line in enumerate(lines, start=1) if i % 2 == 0]
        print('\n'.join(even_lines))

redaktor("Строка под номером пять", "test.txt")
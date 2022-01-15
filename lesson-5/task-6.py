from itertools import takewhile, dropwhile


def normalize(hours):
    hours = ''.join(takewhile(lambda x: x.isdigit(), dropwhile(lambda y: y.isalpha(), hours)))
    if hours.isdigit():
        return int(hours)
    return 0


def normalizer(a, b, c):
    return normalize(a) + normalize(b) + normalize(c)


with open('text_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # try:
        #     s = line.split()
        #     subject, lect, pract, lab = s
        #     print(subject, lect, pract, lab)
        #         # pass
        # except:
        #     print(line.split())

        try:
            subjects = dict()
            for line in f:
                subject, lect, pract, lab = line.split()
                subjects[subject] = normalizer(lect, pract, lab)
            print(subjects)
        except:
            print('something has gone wrong')

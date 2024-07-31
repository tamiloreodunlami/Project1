def question1(n: dict) -> dict:
    n_new = {}
    for key in n:
        value = n[key]
        n_new[value] = key
    return n_new



def question2(n: dict) -> dict:
    n_new = {}
    for key in n:
        value = n[key]
        if value not in n_new:
            n_new[value] = [key]
        else:
            n_new[value].append(key)

    return n_new



def question3(n: dict, n2: dict) -> dict:
    merged = {}
    for key in set(n.keys()).union(set(n2.keys())):
        if key in n and key in n2:
            merged[key] = n[key] + n2[key]
        elif key in n:
            merged[key] = n[key]
        else:
            merged[key] = n2[key]

    return merged
    


def question4(n: list) -> list:
    covered = []
    n_new = []
    for i in n:
        for j in i:
            covered.append(j)
            if covered.count(j) > 1:
                n_new.append(j)
    return n_new


def main():
    output_1 = question1({'a': 1, 'b': 2, 'c': 3})
    print(output_1)
    output_2 = question2({'a': 1, 'b': 2, 'c': 3, 'd': 2})
    print(output_2)
    output_3 = question3({'a': 1, 'b': 2}, {'a': 3, 'c': 1})
    print(output_3)
    output_4 = question4( [[1, 2], [3, 2], [1, 5, 3], [6, 5]] )
    print(output_4)


if __name__ == "__main__":
    main()


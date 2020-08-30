def LinearSearch(list):
    num = int(input('Number:\t'))
    counter = 0
    null = 0

    for i in list:
        if i == num:
            print('Find number {} in place {}.'.format(num, counter))
        else:
            null += 1
        counter += 1
    if null == counter:
        print('Don\'t find it.')

list = [1, 2, 5, 7, 8, 34, 567, -1, 0, -1, -3, -9, 0]
LinearSearch(list)
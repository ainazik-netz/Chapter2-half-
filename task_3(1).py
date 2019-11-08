while True:
    number = int(input('Write number:'))
    print(f'Previous number is: {number -1}.,next number is {number +1} ')
    question = input('Do you want to continue:yes or no' ).lower()
    if question == 'yes':
        continue
    else:
        brea
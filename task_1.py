while True:
    name = input('Write your name:')
    print(input('Hello' + ' ' + name +'!'))
# print(f'Hello,{name}')
    question = input('Do you want to continue? Yes or No').lower()
    if question == 'Yes':
        continue
    else:
        break

    

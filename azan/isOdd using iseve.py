def isEve(a):
    if(a%2==0):
        return 'is even'
    else:
        return'not even'

def isOdd(a):

    if(isEve(a) == 'not even'):
        return print('is odd')
    else:
        return print('not odd')



if __name__ == '__main__':
    a = int(input())

    isOdd(a)2
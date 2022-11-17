
def isint(num):
    try:
        int(num)
        return True
    except:
        return False

def letterToNumber(letter):
    return ord(letter) - 96

def numberToLetter(number):
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return letters[number-1]
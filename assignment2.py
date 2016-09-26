import crypt


def passwordCheck(cryptedPassword):
    salt = cryptedPassword[0:2]
    dictionary = open(dictonary.txt, 'r')
    for word in dictionary.readlines():
        word = word.split('\n')

cryptedWord = crypt.crypt(word, salt)

if cryptedWord == CryptPass:
    print "password found"
    return
else:
    print "Password not in dictionary"
    return

def main():
    passwordFile = open("insert shadow file", 'r')
    for line in passwordFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptedPassword = line.split(':')[1].strip(' ')
            passwordCheck(cryptedPassword)

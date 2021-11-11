from random import randrange
import sys


def main(argv):
    mail_file = argv[1]
    mails = []
    persons_file = argv[2]
    persons = []
    pair = []

#   Read files
    with open(mail_file, "r") as m:
        for line in m:
            mails.append(line)
    with open(persons_file, "r") as p:
        for line in p:
            persons.append(line)
    i = 0
    while i < len(mails):
        pair.append([mails[i], persons[i]])
        i += 1

#   Randomize the pair array
    i = 0
    while i < len(pair):
        tmp = pair[i]
        random = randrange(len(pair) - 1) - 1
        pair[i] = pair[random]
        pair[random] = tmp
        i += 1

#   Shift person by one position
    shufflelist = []
    for i in pair:
        shufflelist.append("")
    i = 0
    while i < len(pair):
        shufflelist[i] = pair[i][1]
        i += 1
    shufflelist.append(shufflelist.pop(0))
    i = 0
    while i < len(shufflelist):
        pair[i][1] = shufflelist[i]
        i += 1

#   E-mail transfer


if __name__ == "__main__":
    main(sys.argv)

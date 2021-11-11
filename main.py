from random import randrange
import sys


def main(argv):
    mail_file = argv[1]
    mails = []
    persons_file = argv[2]
    persons = []
    pair = []

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

#   Move the person one spot further
    i = 0
    buffer = pair[len(pair) - 1]
    while i < len(pair) - 1:
        buffer = pair[i + 1][1]
        pair[i + 1][1] = pair[i][1]
        i += 1
    pair[0][1] = buffer
    pass


if __name__ == "__main__":
    main(sys.argv)

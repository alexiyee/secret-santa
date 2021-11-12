from random import randrange
import sys
import smtplib
import ssl
import getpass


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

#   E-mail transfer setup
    port = 465
    email = input("Enter gmail adress here: ")
    password = getpass.getpass(prompt="Enter password for the Mailaccount: ")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(email, password)
        sender_email = email

        # send the mails
        i = 0
        while i < len(pair):
            receiver_email = pair[i][0]
            message = pair[i][1]
            server.sendmail(sender_email, receiver_email, message)
            i += 1
    print("You're looking good!")


if __name__ == "__main__":
    main(sys.argv)

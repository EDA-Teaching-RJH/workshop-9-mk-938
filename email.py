#email = input("Please enter an email: ")

def email_checker(mail):
    eMail = mail.split("@")
    domain = eMail[1].split(".")
    organisation = domain[0]
    print (organisation)
    for item in mail:
        if item == "@":
            counter = 
    
    match organisation:
        case "nhs":
            print ("Valid NHS eMail")

        case "ac":
            print ("Valid Academic eMail")

        case "gov":
            print ("Valid Government eMail")


email_checker("qvahxzeueq@nhs.net")
email_checker("njvun@nhs.net")
email_checker("omkueltb@gov.uk")
email_checker("fph@jp@ac.uk")
email_checker("wiq)jadaa@nhs.net")



#2. [rwvqhptft@nhs.net]
#3. [njvun@nhs.net]
#4. [omkueltb@gov.uk]
#5. [qpzyqnlaq@nhs.net]
#6. [dkf*ggnu@gov.uk]
#7. [mtnurpnn@gov.uk]
#8. [wiq)jadaa@nhs.net]
#9. [fph@jp@ac.uk]
#10. [euktfrzm@gov.uk]

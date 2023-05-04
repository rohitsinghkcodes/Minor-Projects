import pywhatkit


def inputFunc():
    ContactTo = input('Enter the whatsapp no to whome you want to send the message: ')
    message = input("Enter Yout message: ")
    timeHour = int(input("Enter time of sending the message(hours): "))
    timeMin = int(input("Enter time of sending the message(mins): "))

    return ContactTo,message,timeHour,timeMin

#This for sending the message to a person
def sendPersonAutomated(ContactTo,message,timeHour,timeMin):
    try:
        pywhatkit.sendwhatmsg(ContactTo,message,timeHour,timeMin)
        print("Successfully Sent!")

    except:
        print("An unexpected error!")


if __name__ == "__main__":
    ContactTo,message,timeHour,timeMin = inputFunc()
    sendPersonAutomated("+919931496730",message,timeHour,timeMin)
    
    #WikiInfo('India')

    #asciiConv('guglani.png','guglani')

    # handWrittenConv()
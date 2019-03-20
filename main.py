''' IoT Greenhouse - GroupMe SMS Service
    Keith E. Kelly
    K2 Creatives, LLC
'''
from time import sleep


from SMSGroupMeService import SMSGroupMeService

def main():
    print("\nGroupMe SMS Texting for IoT Greenhouse.\n")
    #Enter house name and GroupMe token when prompted.
    #name = input("Enter a short name for your greenhouse: ")
    #print("\nOpen your dev.groupme.com page. Access your token and copy here.")
    #token = input("GroupMe token: ")
    groupMe_token = "ZRkZAZGCYBROiAuuDON7nzBYERFYw2bDspakx9QL"

    last_message_id = None

    
    with SMSGroupMeService(groupMe_token, True) as sms_service:
        new_phone = None
        print()
        print("Enter a mobile phone number to assign to the GroupMe service.")
        print("Multiple numbers can be added. Press Enter when done.")
        while new_phone != "":
            new_phone = input("Phone number: ").strip()
            if new_phone != "":
                sms_service.add_member(new_phone)

        member_count = len(sms_service.members)
        if member_count == 0:
            print("No members added. Unable to continue.")
            return       
        else:
            print("%d phone numbers have been added to this service." % member_count)
            print()
            print("Send direct messages to this greenhouse using %s" % sms_service.bot_name)
            print("Include a command using the hash (#) character.")
            print("Example: %s #temp" % sms_service.bot_name)
            print("For a list of commands enter:  %s #help" % sms_service.bot_name)
            print()

            sms_service.start()
            while sms_service.scanning:
                if sms_service.last_message != None:
                    message = sms_service.last_message
                    if message.id != last_message_id:
                        print(message.name + "   " + message.text)
                        print()

                        last_message_id = message.id
                sleep(.5)
            sms_service.close()

if __name__ == "__main__":
    main()
# Efficient Excuses
import yagmail
import traceback

#=========================================================================================
#=========================================================================================
#=========================================================================================

# INPUT DATA:
my_name = ""        # Your name
sender_email = ""   # Your Email
unsecure_pass = ""  # Your "App Password" (Not regular login password)


yag = yagmail.SMTP(sender_email, unsecure_pass)

# Teacher email addresses (can add yours for testing)
adds = ["",
        "",
        "",
        "",
        "",
        "",
        ""]

# Teacher titles/names here, ex: "Mr. Clean", "Tom Brady" ***(SAME ORDER AS THE TEACHER EMAILS)***
names = ["Mr. ",
         "Mr. ",
         "Mr. ",
         "Mrs. ",
         "Mr. ",
         "Mr. ",
         "Ms. "]
#=========================================================================================
#=========================================================================================
#=========================================================================================

intros = ["",
          "Hope you are doing well.",
          "I hope this email finds you well."]

emails = ["I would like to apologize for not submitting my assignment on time.",
          "I just wanted to let you know that I\'m still working on my assignment and will do my best to get it to you as soon as possible.",
          "I wanted to provide an update on my assignment and let you know that it's still in progress. I\'ll make every effort to get it to you as soon as I can.",
          "Just a quick note to let you know that I haven\'t forgotten about my assignment, and I\'m currently working on it. I'll send it to you as soon as it\'s complete.",
          "I\'m still in the process of finishing my assignment, but I wanted to assure you that I\'m making progress and will deliver it to you as soon as I can.",
          "I just wanted to reach out and let you know that my assignment is still a work in progress, but I\'m dedicated to getting it done and will submit it to you as soon as possible.",
          "I wanted to touch base and inform you that I\'m still working on my assignment and haven\'t yet completed it. I will make sure to send it to you as soon as it\'s finished."]

excuses = ["Due to other commitments,",
           "I haven't been feeling well, so",
           "I have been overloaded with other classes, so",
           "I had work, so",
           "Due to college applications,"]

excuses_cons = ["I was unable to hand the assignment in on time.",
                "I was unable to get back to you.",
                "I completely forgot about the assignment.",
                "I completely forgot to get back to you."]

end_parts = ["",
             "Thank you for your understanding.",
             "I apologize for the inconvenience this may have caused.",
             "I will get back to you as soon as possible. Thank you for your understanding."]

sign_off = "\n\nBest,\n\n" + my_name + " & Py3-MS"
greeting = "Dear "
period = "."
space = " "
nl = "\n"
c = ", "
DueTo_space = "Due to "
name_space = ",\n\n"

jo1 = 0
jo2 = 0
jo3 = 0
jo4 = 0
# jo5 = 0
selector1 = 0
selector2 = 0
selector3 = 0
selector4 = 0
selector5 = 0
selector6 = 0
size_adds = len(adds)
size_intros = len(intros)
size_emails = len(emails)
size_excuses = len(excuses)
size_end_part = len(end_parts)
size_excuses_cons = len(excuses_cons)


try:
    # Select Target = = = = = = = =
    print("Select target:", end="\n\n")
    for i in range(1, (size_adds + 1)):
        print(i, end=". ")
        print(adds[i-1], end="\n")
        
    selector1 = input()
    selector1 = int(selector1)
    target_address = adds[(selector1 - 1)]

    
    # Select Email = = = = = = = = =
    print("Select email:", end="\n\n")
    for i in range(1, (size_emails + 1)):
        print(i, end=". ")
        print(emails[i-1], end="\n\n")

    selector2 = input()
    selector2 = int(selector2)
    target_email = emails[(selector2 - 1)]


    # Intro = = = = = = = = = =
    print("Select intro:", end="\n\n")
    for i in range(1, (size_intros + 1)):
        print(i, end=". ")
        print(intros[i-1], end="\n\n")

    selector5 = input()
    selector5 = int(selector5)
    target_intro = intros[(selector5 - 1)]

    
    # Excuse? (Y/N) = = = = = = = = =
    bool_excuse = input("Add an excuse? (y/n)")

    while jo3 != 1:
        if bool_excuse == "y" or bool_excuse == "Y" or bool_excuse == "1":

            # Select Excuse = = = = = = = = = =
            print("Select excuse:", end="\n\n")
        
            for i in range(1, (size_excuses + 1)):
                print(i, end=". ")
                print(excuses[i-1], end="\n\n")
            selector3 = input()
            selector3 = int(selector3)
            target_excuse = excuses[(selector3 - 1)]
            
            ZO_excuse = 1
            jo3 = 1
        
        elif bool_excuse == "n" or bool_excuse == "N" or bool_excuse == "0":

            # No Excuse = = = = = = = = = = = =
            print("\nNo Excuse Added\n")
            ZO_excuse = 0
            jo3 = 1
        else:

            # Not An Option = = = = = = = = = =
            print("-> Not an option, answer again <-")
            jo3 = 0


    # Excuse Consequence = = = = = = = =
    print("Select excuse consequence:", end="\n\n")
        
    for i in range(1, (size_excuses_cons + 1)):
        print(i, end=". ")
        print(excuses_cons[i-1], end="\n\n")
    selector6 = input()
    selector6 = int(selector6)
    target_excuse_cons = excuses_cons[(selector6 - 1)]

    
    # Select Header = = = = = = = = = =
    bool_header = input("Add \"Assignment\" to header? (y/n)")

    while jo1 != 1:
        if bool_header == "y" or bool_header == "Y" or bool_header == "1":

            bool_cust_asn = input("Add custom assignment to header? (y/n)")
            while jo2 != 1:

                if bool_cust_asn == "y" or bool_cust_asn == "Y" or bool_cust_asn == "1":

                    # Get Custom Input = = = = = = = = = =
                    cust_header = input("Type your custom header:")
                    jo2 = 1
                    
                elif bool_cust_asn == "n" or bool_cust_asn == "N" or bool_cust_asn == "0":

                    # Set Input to Assignment = = = = = = =
                    cust_header = "Assignment"
                    jo2 = 1
                    
                else:
                    
                    # Not An Option = = = = = = = = = =
                    print("-> Not an option, answer again <-")
                    jo2 = 0

            ZO_header = 1
            jo1 = 1

        elif bool_header == "n" or bool_header == "N" or bool_header == "0":

            cust_header = my_name
            ZO_header = 0
            jo1 = 1
            
        else:
            
            # Not An Option = = = = = = = = = =
            print("-> Not an option, answer again <-")
            jo1 = 0
        
    

    # Select End Part = = = = = = = = =
    print("Select end part:", end="\n\n")
    for i in range(1, (size_end_part + 1)):
        print(i, end=". ")
        print(end_parts[i-1], end="\n\n")

    selector4 = input()
    selector4 = int(selector4)
    target_end_part = end_parts[(selector4 - 1)]

    
    # Put Together Email = = = = = = =
    if ZO_header == 1:
        header = "Assignment; " + my_name
    elif ZO_header == 0:
        header = my_name

    if ZO_excuse == 1:
        full_target_excuse = target_excuse
    elif ZO_excuse == 0:
        full_target_excuse = ""

    target_name = names[(selector1 - 1)]
    end_note = "\n\n\n\n\n\n\n\n\n\n\n\nYou do not need to respond to this email. This was an automated message sent from S. Caplan's automated Python3 messaging system. The some of the information in this email was sent by " + my_name 


    # Put Together Payload = = = = = =
    payload = greeting + target_name + name_space + target_intro + " " + target_email + " " + full_target_excuse + " " + target_excuse_cons + " " + target_end_part + sign_off + end_note


    print(payload)
    yag.send(target_address, cust_header, payload)
    print("Missile Sent")
    
except Exception as e:
    print("Error sending email:")
    print(traceback.format_exc())

finally:
    # close the Yagmail object
    yag.close()

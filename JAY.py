#0611276442088
#Tlotlso lekhoba
#2br

code = input("Enter the RFID tag: ").strip()

if len(code) == 7 and code[:2].isalpha() and code[:2].isupper() and code[2:5].isdigit():
    print("RFID TAG IS VALID.")
    print("process exited - return codetyg")
    input("Press Enter to exit the terminal...")
    sys.exit(0)
else:
    print("RFID TAG IS INVALID.")
    input("Press Enter to exit the terminal...")
    sys.exit(1)
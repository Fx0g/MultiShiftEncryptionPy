#simple crypto tool with random algorithm
#program by methran
#uploaded to https://github.com/KernelPaniccz/KernelPanic/edit/master/

import time
import os
import math
import random


        
def clear():
    if(os.system == 'nt'):
        _ = 'cls'
    else:
        _ = 'clear'

def encrypt(message):
    global is_encrypted
    is_encrypted = True
    time.sleep(1)
    global enc_msg
    enc_msg = ""
    for i in range (len(message)):
        enc_msg = enc_msg + chr(ord(message[i])- 2)
    print("\nString Has Been Encrypted Successfully!\n\n")
    view_enc = input("\nView The Encrypted? (y/n): ")
    if(view_enc == 'y' or view_enc == "Y"):
        print("\nEncrypted Message :",enc_msg)
    elif(view_enc == 'n' or view_enc == "N"):
        print("\nOK , Encrypted String Has Not Been Viewed")
    else:
        print("\nWrong Choice!")
        time.sleep(1.5)
        main()
    time.sleep(1.5)
    main()
def decrypt(enc):
    time.sleep(1)
    dec = ""
    for i in range(len(enc)):
        dec = dec + chr(ord(enc[i])+ 2)
    print("\nString Has Been Decrypted Successfully!\n\n")
    view_dec = input("\nView The Decrypted? (y/n): ")
    if(view_dec == 'y' or view_dec == "Y"):
        print("\nDecrypted Message :",dec)
    time.sleep(1.8)
    main()
        
def main():
    
    clear()
    encrypt.is_encrypted = False
    print("\n\n--------SELECTION MENU--------\n")
    print("1.Encryption\n")
    print("2.Decryption\n")
    print("3.Exit\n")
    print("------------------------------\n")
    
    ch = input("\nEnter Your Choice: ")
    
    if(ch == "1" or ch == "encryption"):
        msg = input("\n\nEnter Message To be Encrypted: ")
        encrypt(msg)
    elif(ch == "2" or ch == "decryption"):
        print("\n\n\n1.Decrypt Encrypted String \n2.Decrypt New String")
        new_or_old = input("\nEnter Your Choice (1/2): ")
        if(new_or_old == "1"):
            if(is_encrypted == True):
                decrypt(enc_msg)
            else:
                print("\nNo Encrypted Strings Found!")
                time.sleep(1.5)
                need_encrypt = input("\nDo you want to Encrypt? (y/n): ")
                if(need_encrypt == 'y' or need_encrypt == "Y"):
                    msg = input("\n\nEnter Message To be Encrypted: ")
                    encrypt(msg)
                    time.sleep(0.5)
                    decrypt(enc_msg)
                elif(need_encrypt == 'n' or need_encrypt == "N"):
                    print("\nOK , Terminating Program!")
                    time.sleep(0.5)
        elif(new_or_old == "2"):
                new_str=input("\nEnter A String To Decrypt: ")
                decrypt(new_str)
        else:
                print("\nWrong Choice...")
                
    elif(ch == "3" or ch == "exit"):
        print("\nThank You , See You Soon")
    else:
        print("\nWrong Choice!! \nTry Again..")
        time.sleep(1)
        main()
    
main()

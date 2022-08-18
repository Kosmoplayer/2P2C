#!/usr/bin/python
import sys, os
from pathlib import Path, PurePath
abc_low = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
"k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
"u", "v", "w", "x", "y", "z")
abc_up = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
"K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
"U", "V", "W", "X", "Y", "Z")
decrypt_text = ""
def main_menu():
    print("\t\tShift Cipher Program\n")
    while True:
        try:
            choice = int(input("\n\tPlease, choice what to do:\n\n"
            "\t1. Encrypt\n\t2. Decrypt\n\t3. Quit\n\nChoice: "))
        except ValueError:
            print("\nPlease, choice right answer or type 3 to quit.")
            continue
        if choice not in (1, 2, 3):
            print("\nPlease, choice right answer or type 3 to quit.")
            continue
        elif choice == 1:
            encrypt_from_menu()
        elif choice == 2:
            decrypt_from_menu()
        else:
            sys.exit(0)
def encrypt_from_menu():
    while True:
        try:
            choice = int(input("\n\tPlease, choice what to encrypt:\n\n"
            "\t1. Encrypt from input\n\t2. Encrypt from file\n\t3. Return\n\t4. Quit\n\nChoice: "))
        except ValueError:
            print("\nPlease, choice right answer or type 3 to return to main menu or type 4 to quit.")
            continue
        if choice not in (1, 2, 3, 4):
            print("\nPlease, choice right answer or type 3 to return to main menu or type 4 to quit.")
            continue
        elif choice == 1:
            from_input("encrypt")
        elif choice == 2:
            from_file("encrypt")
        elif choice == 3:
            main_menu()
        else:
            sys.exit(0)
def decrypt_from_menu():
    while True:
        try:
            choice = int(input("\n\tPlease, choice what to decrypt:\n\n"
            "\t1. Decrypt from input\n\t2. Decrypt from file\n\t3. Return\n\t4. Quit\n\nChoice: "))
        except ValueError:
            print("\nPlease, choice right answer or type 3 to return to main menu or type 4 to quit.")
            continue
        if choice not in (1, 2, 3, 4):
            print("\nPlease, choice right answer or type 3 to return to main menu or type 4 to quit.")
            continue
        elif choice == 1:
            from_input("decrypt")
        elif choice == 2:
            from_file("decrypt")
        elif choice == 3:
            main_menu()
        else:
            sys.exit(0)
def encrypt_to_menu(processed):
    while True:
        try:
            choice = int(input("\n\tPlease, choice where put encrypted text:\n\n"
            "\t1. In output\n\t2. Save in file\n\t3. Return to last menu\n\t4. Return to main menu\n\t5. Quit\n\nChoice: "))
        except ValueError:
            print("\nPlease, choice right answer or type 3 to return to last menu, 4 return to main menu or type 5 to quit.")
            continue
        if choice not in (1, 2, 3, 4, 5):
            print("\nPlease, choice right answer or type 3 to return to main menu or type 4 to quit.")
            continue
        elif choice == 1:
            to_output("encrypt", processed)
        elif choice == 2:
            to_file()
        elif choice == 3:
            encrypt_from_menu()
        elif choice == 4:
            main_menu()
        else: sys.exit(0)
def decrypt_to_menu(processed):
    while True:
        try:
            choice = int(input("\n\tPlease, choice where put decrypted text:\n\n"
            "\t1. In output\n\t2. Save in file\n\t3. Return to last menu\n\t4. Return to main menu\n\t5. Quit\n\nChoice: "))
        except ValueError:
            print("\nPlease, choice right answer or type 3 to return to last menu, 4 return to main menu or type 5 to quit.")
            continue
        if choice not in (1, 2, 3, 4, 5):
            print("\nPlease, choice right answer or type 3 to return to main menu or type 4 to quit.")
            continue
        elif choice == 1:
            to_output("decrypt", processed)
        elif choice == 2:
            to_file()
        elif choice == 3:
            decrypt_from_menu()
        elif choice == 4:
            main_menu()
        else: sys.exit(0)
def encrypt(text, shift):
    processed_text = ""
    for i in range(len(text)):
        if str.isalpha(text[i]) and (text[i] in abc_low) is True:
            if (int(abc_low.index(text[i])) + int(shift)) <= 25:
                shifted_index = int(abc_low.index(text[i])) + int(shift)
            else:
                shifted_index = int(abc_low.index(text[i])) + int(shift) - (25 * ((int(abc_low.index(text[i])) + int(shift)) // 25))
            processed_text += abc_low[shifted_index]
        elif str.isalpha(text[i]) and (text[i] in abc_up) is True:
            if (int(abc_up.index(text[i])) + int(shift)) <= 25:
                shifted_index = int(abc_up.index(text[i])) + int(shift)
            else:
                shifted_index = int(abc_up.index(text[i])) + int(shift) - (26 * ((int(abc_up.index(text[i])) + int(shift)) // 25))
            processed_text += abc_up[shifted_index]
        else:
            processed_text += text[i]
    return processed_text
def decrypt(text, shift):
    processed_text = ""
    for i in range(len(text)):
        if str.isalpha(text[i]) and (text[i] in abc_low) is True:
            if (int(abc_low.index(text[i])) - int(shift)) > 0:
                shifted_index = int(abc_low.index(text[i])) - int(shift)
            else:
                shifted_index = int(abc_low.index(text[i])) - int(shift) - (25 * ((int(abc_low.index(text[i])) - int(shift)) // 25))
            processed_text += abc_low[shifted_index]
        elif str.isalpha(text[i]) and (text[i] in abc_up) is True:
            if (int(abc_up.index(text[i])) - int(shift)) > 0:
                shifted_index = int(abc_up.index(text[i])) - int(shift)
            else:
                shifted_index = int(abc_up.index(text[i])) - int(shift) - (26 * ((int(abc_up.index(text[i])) - int(shift)) // 25))
            processed_text += abc_up[shifted_index]
        else:
            processed_text += text[i]
    return processed_text
def from_input(mode):
    if mode == "encrypt":
        while True:
            text = str(input("\n\tPlease, input text for encrypt:\n\t"))
            if text.isprintable() is True and text != "":
                while True:
                    try:
                        shift = int(input("\n\tPlease type shift\'s number for encrypt:\n\t"))
                    except ValueError:
                        print("Wrong input, please type number")
                        continue
                    if str(shift).isdigit():
                        break
                processed = (encrypt(text, shift), shift)
                break
            else:
                print("\n\tThis text is unacceptable, please try again or select another program\'s mode")
                encrypt_from_menu()
        encrypt_to_menu(processed)
        # return processed
    else:
        while True:
            text = str(input("\n\tPlease, input text for decrypt:\n\t"))
            if text.isprintable() is True and text != "":
                while True:
                    try:
                        shift = int(input("\n\tPlease type shift\'s number for decrypt:\n\t"))
                    except ValueError:
                        print("Wrong input, please type number")
                        continue
                    if str(shift).isdigit():
                        break
                processed = (decrypt(text, shift), shift)
                break
            else:
                print("\n\tThis text is unacceptable, please try again or select another program\'s mode")
                decrypt_from_menu()
        decrypt_to_menu(processed)
        return processed
def from_file(mode):
    cwd = os.getcwd() + os.sep
    userdir = os.path.expanduser("~") + os.sep
    while True:
        try:
            startpath = int(input("\n\tWhere to start search the file from?\n\t1. From current directory(\"" + cwd + "\")." + ".\n\t2. "
                        "From home directory(\"" + userdir + "\")\n\t3. Type path manual.\n\t4. Return to last menu.\n\t5. Return to main menu.\n\t6. Quit\nChoice: "))
        except ValueError:
            print("Wrong input, please type correct number.")
        if startpath == 1:
            filepath = cwd
            filepath += input("\n\tPlease type path to .txt file to encrypt.\nPath: " + cwd)
            filepath = Path(filepath)
            process_file(filepath, mode)
        elif startpath == 2:
            filepath = userdir
            filepath += input("\n\tPlease type path to .txt file to encrypt.\nPath: " + userdir)
            filepath = Path(filepath)
            process_file(filepath, mode)
        elif startpath == 3:
            filepath = Path(input("\n\tPlease type path to .txt file to encrypt.\nPath: "))
            process_file(filepath, mode)
        elif startpath == 4:
            if mode == "encrypt":
                encrypt_from_menu()
            else:
                decrypt_from_menu()
        elif startpath == 5:
            main_menu()
        else:
            sys.exit(0)
    if mode == "encrypt":
        pass
    else:
        pass
def to_output(mode, processed):
    if mode == "encrypt":
        print("\n\tYour encrypted text:\n\n" + str(processed[0]) + "\nShift: \"" + str(processed[1]) + "\"")
        done()
    else:
        print("\n\tYour decrypted text: \n\n" + str(processed[0]))
        done()
def to_file():
    pass
def done():
    try:
        choice = int(input("\n\tType \"1\" to return to main menu, or anything else for exit.\nChoice: "))
    except ValueError:
        sys.exit(0)
    if choice == 1:
        main_menu()
    else:
        sys.exit(0)
def verify_path(path, type):
    # Need to add Error catching code
    if type == "file":
        if PurePath.match(path, '*.txt') is True and Path.is_file(path):
            return True
        else:
            return False
    else:
        if Path.is_dir(path) is True:
            return True
        else:
            return False
def process_file(filepath, mode):
    if verify_path(filepath, "file") is True:
        while True:
            try:
                shift = int(input("\n\tPlease type shift\'s number for " + mode + ":\n\t"))
            except ValueError:
                print("Wrong input, please type number")
                continue
            if str(shift).isdigit():
                break
        if mode == "encrypt":
            encrypt_to_menu((encrypt(Path.read_text(filepath), shift), shift))
        else:
            decrypt_to_menu((decrypt(Path.read_text(filepath), shift), shift))
    else:
        print("Wrong file or file not found, try again.")
main_menu()
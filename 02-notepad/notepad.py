__author__ = 'Rakshak.R.Hegde'

notesFileName = 'notes.txt'


def looper():
    notes = readNotes()
    print('Welcome to Notepad')
    while True:  # infinite loop
        print('1: Add note   2: Show notes   3: Delete note   4: Save & exit')
        choice = int(input())
        if choice == 1:
            print('Enter note:')
            note = input()
            notes.append(note)
        elif choice == 2:
            showNotes(notes)
        elif choice == 3:
            print('You figure out this part now :D')
        elif choice == 4:
            save(notes)
            exit()
        else:
            print("Invalid choice!")


def readNotes():
    try:
        with open(notesFileName) as f:
            return f.readlines()
    except:
        return []


def showNotes(notes):
    print('Notes are:')
    for note in notes:
        print(note)


def save(notes):
    with open(notesFileName, mode='w') as f:
        f.writelines(notes)
    print('Notes are saved.')


looper()

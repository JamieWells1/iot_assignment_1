import os, os.path

def create_project():
    participants = []
    project = input('Enter a name for your project: ')
    mkdir(project)
    os.chdir(project)
    print('\nProject created!\n')
    def add_project_participants():
        print('(s) : Save and quit')
        participant = input('Add participants by typing their name and their role, separated by a comma: ')
        if participant != 's':
            participants.append(participant)
            add_project_participants()
        else:
            touch('participants.csv')
            with open('participants.csv', 'w') as f:
                for i in range(len(participants)):
                    f.write(f'{participants[i]}\n')
            print('\nParticipants saved!\n')
        user_input = input('Project structure created! (s) : Add a stage | (w) : Add a workstream | (r) : Return to menu ')
        if user_input == 's':
            create_stage(project)
        elif user_input == 'w':
            create_workstream(project)
        else:
            take_input()

    def create_stage(project_directory):
        # stage initialisation
        if os.path.basename(os.getcwd()) != project_directory:
            os.chdir('..')
        stage_attendees = []
        stage = input('Enter a name for your stage: ')
        meeting_date = input('What date is the meeting for this stage? ')
        add_attendees(stage_attendees, stage, meeting_date)
        touch('meeting_notes.txt')
        touch('stage_info.md')
        print('\nStage created!\n')
        user_input = input('Project structure created! (s) : Add another stage | (w) : Add another workstream | (r) : Return to menu ')
        if user_input == 's':
            create_stage(project)
        elif user_input == 'w':
            create_workstream(project)
        else:
            take_input()
    def create_workstream(project_directory):
        # workstream initialisation
        if os.path.basename(os.getcwd()) != project_directory:
            os.chdir('..')
        workstream_attendees = []
        workstream = input('Enter a name for your workstream: ')
        meeting_date = input('What date is the meeting for this workstream? ')
        add_attendees(workstream_attendees, workstream, meeting_date)
        touch('meeting_notes.txt')
        touch('workstream_info.md')
        print('\nWorkstream created!\n')
        user_input = input('Project structure created! (s) : Add another stage | (w) : Add another workstream | (r) : Return to menu ')
        if user_input == 's':
            create_stage(project)
        elif user_input == 'w':
            create_workstream(project)
        else:
            take_input()

    add_project_participants()
    create_stage(project)
    create_workstream(project)
    if user_input == 's':
        create_stage(project)
    elif user_input == 'w':
        create_workstream(project)
    else:
        take_input()

def mkdir(folder_name):
    try:
        os.mkdir(folder_name)
    except Exception as e:
        print(e)

def touch(file_name):
    try:
        open(file_name, 'x')
    except Exception as e:
        print(e)

def edit_file(file_name):
    try:
        with open(file_name, 'r+') as f:
            print('\n')
            for line in f:
                print(line)
            added_text = input("\nType the text you'd like to add: ")
            f.write(added_text + '\n')
            f.close()
            print('\nText added!')
            take_input()
    except Exception as e:
        print(e)
        take_input()

def up_directory():
    os.chdir('..')
    print(f'Directory changed. Current directory: {os.getcwd()}')
    take_input()

def change_directory():
    print(os.listdir())
    user_input = input('\nChoose a folder to change to: ')
    try:
        os.chdir(user_input)
        print(f'Directory changed. Current directory: {os.getcwd()}')
    except Exception as e:
        print('Directory change failed: ',e)
    take_input()

def view_directory():
    print(f'Current directory: {os.getcwd()}')
    take_input()
    
def take_input():
    user_input = input('\n(p) : Create project | (f) : Create file | (d) : Create folder | (e) : Edit file | (u) : Go up directory | (c) Change directory | (v) View current directory | (q) Quit menu\n\nEnter here: ')
    navigation(user_input)

def add_attendees(stage_attendees, stage, meeting_date):
    attendee = input('Add an attendee or (s) to save: ')
    if attendee != 's':
        stage_attendees.append(attendee)
        add_attendees(stage_attendees, stage, meeting_date)
    else:
        mkdir(stage)
        os.chdir(stage)
        touch(f'meeting_{meeting_date}.txt')
        with open(f'meeting_{meeting_date}.txt', 'w') as f:
            f.write('Attendees of this meeting:\n')
            for i in range(len(stage_attendees)):
                f.write(f'{stage_attendees[i]}\n')
        print('\nThe following attendees have been added to the meeting:\n')
        for i in range(len(stage_attendees)):
            print(f'{stage_attendees[i]}')

def navigation(user_input):

    if user_input == 'p':
        create_project()

    if user_input == 'f':
        try:
            touch(input('\nEnter a name for your file: '))
            print('\nFile created!')
            take_input()
        except Exception as e:
            print(e)
            take_input()

    if user_input == 'd':
        try:
            mkdir(input('\nEnter a name for your directory: '))
            print('Directory created!\n')
            take_input()
        except Exception as e:
            print(e)
            take_input()

    if user_input == 'e':
        print(f'\n{os.listdir()}\n')
        edit_file(input('Enter the name of the file you wish to edit: '))

    if user_input == 'u':
        up_directory()

    if user_input == 'c':
        change_directory()

    if user_input == 'v':
        view_directory()

# <------------ Script start ------------>

print('\nWelcome to File Manager: Project Manager Edition!')
print('Choose an option to get started: \n')
user_input = take_input()
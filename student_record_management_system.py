error_message = "\nInvalid input\n Try Again\n"
## Essential user-defined functions for use in this program
def input_alpha(message):
    while True:
        print(message, end="")
        inp = input(" -> ").lower().strip()
        if inp and inp.isalpha():
            return inp
        else:
            print(error_message)

def input_num(message):
    while True:
        print(message, end="")
        inp = input(" -> ").strip()
        if inp and inp.isdigit():
            inp = int(inp)
            return inp
        else:
            print(error_message)

def input_all(message):
    while True:
        print(message, end="")
        inp = input(" -> ").strip()
        if inp:
            return inp
        else:
            print(error_message)

def input_specfic_num(start, end, message):
    while True:
        print(message, end="")
        inp = input(" -> ").strip()
        if inp and inp.isdigit():
            inp = int(inp)
            if start <= inp <= end:
                return inp
            else:
                print(error_message)
                continue
        else:
            print(error_message)

def yes_no(message):
    while True:
        print(message, end="")
        inp = input(" [y/n] -> ").lower().strip()
        if inp and inp.isalpha() and inp in "yn":
            match inp:
                case "y": return True
                case "n": return False
        else:
            print(error_message)

def center(message, num, sign, ends):
    print(f"{f"{message}".center(num,sign)}", end=ends)

# Essential Storage
student_record = {}
subjects = []
additional_information = ["Total Marks Obt.", "Out of", "Average Marks", "Grade", "Remark"]

# Function - Admin Verification
def admin_verification():

    center(" Officials Verification ", 31, "*", "\n")
    password = "Admin@1234"     # Password for the admin
    while True:
        inp = input_all("\nInput Password")
        if inp == password:
            center(" Program Unlocked ", 31, "=", "\n")
            break
        else:
            continue

# Function - Add Students
def add_student(record_dict):

    # loop to add astudents in one go
    while True:
        name = input_alpha("\nEnter 'stop' to stop\nName of Student")
        if name == "stop":
            return record_dict
        elif name not in record_dict:
            record_dict[name] = {}
        else:
            print(f"\n{name.capitalize()} already exists\nTry Again")

# Function - Add Subjects
def add_subjects(subject_list):

    # loop to add subjects in one go
    while True:
        subject = input_all("\nSubject")

        if subject == "stop":
            break
        elif subject not in subject_list:
            subject_list.append(subject)            # Adds subject in subject_list
            center(f"{subject.capitalize()} Added", 30, "-", "\n")
        else:
            print(f"\nSubject : {subject.capitalize()} already exists\nTry Again with another subject\n\n")

# Function - Adding Permanent Headers with default value
def adding_header(record_dict, header_list):
    for name in record_dict:
        for header in header_list:
            record_dict[name][header] = "-"

# Function - Updation of Permanet Header's value
def updating_additional_headers(record_dict, name, marks, subject_list):
    
    # Updating - Total Marks Obtained by student
    total = record_dict[name]["Total Marks Obt."]
    if total and total != "-":
        total += marks
        record_dict[name]["Total Marks Obt."] = total
    else:
        total = marks
        record_dict[name]["Total Marks Obt."] = total

    # Updating - Maximum Marks can be achieved
    record_dict[name]["Out of"] = len(subject_list) * 100

    # Updating - Average marks of student
    average = total / len(subject_list)
    record_dict[name]["Average Marks"] = round(average, 2)

    # Updating Grade and Remakrs simultaneously
    match average:
        case _ if average > 80: grade = "A"; remark = "Pass"
        case _ if average > 60: grade = "B"; remark = "Pass"
        case _ if average > 40: grade = "C"; remark = "Pass"
        case _ if average > 20: grade = "D"; remark = "Pass"
        case _ if average >= 0: grade = "E"; remark = "Fail"
    
    # Assigning Grade and Remark to the students' record
    record_dict[name]["Grade"] = grade
    record_dict[name]["Remark"] = remark

# Function - Updating Student's Details
def update_student_details(record_dict, subject_list, name):

    # Stores student's name whose details have been filled
    filled_student_details = []

    # Checks If the name is there in the record
    if name in record_dict:
        for subject in subject_list:
            marks = input_specfic_num(0, 100, f"\nMarks for {subject}")
            record_dict[name][subject] = marks
            updating_additional_headers(record_dict, name, marks, subject_list) # Function Calling - Assigning Permanent values 
        center("Details Added", 31, "-", "\n\n")
        filled_student_details.append(name)             # Add the student to filled details list

    else:
        print(f"\n{name} is not in our records\nTry again with different name\n")

# Function - Display All Student's Result
def view_all_result(record_dict, header_list):

    # Displays header 
    print("\n\n")
    center("=", 150, "=", "\n")
    center("Name", 11, " " ,"")
    for header in header_list:
        center(f"{header.capitalize()}", 17, " ", "")
    print("\n")
    center("=", 150, "=", "\n")

    for name in record_dict:
    # displays student's data
        center(name.capitalize(), 11, " " ,"")
        for header in record_dict[name]:
            center(f"{record_dict[name][header]}", 17, " ", "")
        print("\n")
        center("", 150, "-", "\n")
    center("=", 150, "=", "\n")

# Function - Display a single student's result
def view_individual_result(record_dict, header_list):

    # loop for searching many student's result in one go
    while True:
        name = input_alpha("\nEnter Name of the Student")
        if name in record_dict:

            # displays header
            print("\n\n")
            center("=", 150, "=", "\n")
            center("Name", 11, " " ,"")
            for header in header_list:
                center(f"{header.capitalize()}", 17, " ", "")
            print("\n")
            center("=", 150, "=", "\n")

            # displays student's data
            center(name.capitalize(), 11, " " ,"")
            for header in record_dict[name]:
                center(f"{record_dict[name][header]}", 17, " ", "")
            print("\n")
            center("-", 150, "-", "\n")
            center("=", 150, "=", "\n")

            # Asks to search more student
            proceed = yes_no("\nWant to search another result?")
            if proceed:
                continue
            else:
                break
        else:
            print(f"{name} is not in our record\nTry with another name\n")

# Function - displays the topper
def topper(record_dict):
    max_marks = 0
    topper_list = []
    
    # Finding the highest marks 
    for name in record_dict:
        marks = record_dict[name]["Total Marks Obt."]
        if marks >= max_marks:
            max_marks = marks

    # Finding names of students got highest marks
    for name in record_dict:

        marks = record_dict[name]["Total Marks Obt."]
        if marks == max_marks:
            if name not in topper_list:
                topper_list.append(name)

    # When no. of topper is 1
    if len(topper_list) == 1:
        center(f" {topper_list[0].capitalize()} is the Topper with Total Marks : {max_marks} ", 61, "=", "\n")
        center(f" Congratulations to {topper_list[0].capitalize()} ", 61, "=", "\n")
        return 
    else:   # When no. of topper is more than 1
        center(f" We have {len(topper_list)} Toppers ", 41 ,"=", "\n\n")
        for topper in topper_list:
            center(f" -> {topper.capitalize()}", 41, " ", "\n")
        center(f" Congratulations to Them ", 41, "=", "\n")
        return 

# Function - displays top 3 students with theit total marks acheived
def top_three(record_dict):

    # To store the marks of first second and third place holders
    first = 0
    second = 0
    third = 0
    topper_dict = {}

    # Checking length is 3 or more
    if len(record_dict) >= 3:

        # Storing names and their marks in one place
        for name in record_dict:
            topper_dict[name] = record_dict[name]["Total Marks Obt."]
        
        # Finding heighest marks and first place holder name
        for name in topper_dict:
            marks = topper_dict[name]
            if marks > first:
                first = marks
                first_name = name
            else:
                continue
        del topper_dict[first_name]     # removing name and marks of first place holder
        
        # Finding heighest marks and second place holder name
        for name in topper_dict:
            marks = topper_dict[name]
            if marks > second:
                second = marks
                second_name = name
            else:
                continue
        del topper_dict[second_name]    # removing name and marks of second place holder

        # Finding heighest marks and third place holder name
        for name in topper_dict:
            marks = topper_dict[name]
            if marks > third:
                third = marks
                third_name = name
            else:
                continue
        del topper_dict[third_name]     # removing name and marks of second place holder

        # displays top 3 students
        center(" Top 3 Students ", 101, "=", "\n\n")
        center(f"First - {first_name.capitalize()} with Marks : {first}", 101, " ", "\n")
        center(f"Second - {second_name.capitalize()} with Marks : {second}", 101, " ", "\n")
        center(f"Third - {third_name.capitalize()} with Marks : {third}", 101, " ", "\n")
        center(f" Congratulations to {first_name.capitalize()}, {second_name.capitalize()} and {third_name.capitalize()} ", 101, "=", "\n")
    else:
        print("\n There are Less than 3 Students\nCan't show Top 3")

# Function - assign all headers with default value
def before_updating_details(record_dict, header_list, name):

    # Assigning defalut value to every header's data
    if name in record_dict:
        for header in header_list:
            record_dict[name][header] = "-"
    else:
        print(f"{name.capitalize()} is not in our records")

# Function - Full Program
def result(record_dict, header_list, subject_list, additional_information_list):

    # Starter Note
    print("\n\n")
    center(" Welcome to The Student Record Program ", 61, "-", "\n\n")

    # Admin Verification with Password
    admin_verification()

    # Checking length of record_dict
    if len(record_dict) == 0:
        
        print("\nWe don't have any data in our record\nTry Adding Students Name And data\n")

        # loop to add students in one go
        while True:
            add_student(record_dict)    # Function Calling - Add Student
            proceed = yes_no("\nWant to add more students?")
            if proceed:
                continue
            else:
                print("\n")
                center("Students List Updated", 41, "=", "\n")
                break

        # Checks if user added students or not
        if len(record_dict) != 0:

            # loop for add subjects in one go
            while True:
                add_subjects(subject_list)  # Function Calling - Add Subject
                
                proceed = yes_no("\nWant to add more subject?")
                if proceed:
                    continue
                else:
                    print("\n")
                    center("Subjects List Updated", 41, "=", "\n\n")
                    header_list = subject_list + additional_information_list    # combining both header lists as one
                    break
            
            adding_header(record_dict, header_list)     # Function Calling - Add header

            # loop to add all student's detail in one go
            while True:

                filled_students_detail = []
                for name in record_dict:
                    print(f"\nEnter Details of {name.capitalize()}\n")
                    update_student_details(record_dict, subject_list, name)
                    filled_students_detail.append(name)

                if len(filled_students_detail) == len(record_dict):
                    print("\nAll Students Detailed have been Filled\n")
                    break
                else:
                    continue

            # loop for perform tasks one after one
            while True:

                task = input_specfic_num(0,5,"\nEnter Task to perform" \
                "\n1 -> Update students details"
                "\n2 -> View All Students Results" \
                "\n3 -> View Top 3 Student's Result" \
                "\n4 -> View Topper" \
                "\n5 -> View a specific student's result" \
                "\n0 -> Stop the program\n\n")
                
                # Matching user input to respective function
                match task:
                    case 1: # updating existing data
                        name = input_alpha("\nEnter Name of the student")
                        before_updating_details(record_dict, header_list, name)
                        update_student_details(record_dict, subject_list, name)

                    case 2: view_all_result(record_dict, header_list)
                    case 3: top_three(record_dict)
                    case 4: topper(record_dict)
                    case 5: view_individual_result(record_dict, header_list)
                    case 0: center("Program Stopped", 31, "=", "\n"); break
        else:
            print("\nStudents list is empty\n\nCant' proceed further")
    else:
        print("\nStudent Record is empty\n")


  
result(student_record, subjects + additional_information , subjects, additional_information)

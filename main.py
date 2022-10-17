from  dbHelper import DBHelper

def menu():
    db = DBHelper()
    while True:
        print("!!-----------------Gurukul Student Management System-------------!!")
        print()
        print("Enter id from following menu:")
        print()
        print("1.Display all student data")
        print("2.Insert new student data")
        print("3.Update student data")
        print("4.Display single student data")
        print("5.Delete student data")
        print("6.Exit from menu")
        print()
        try:
            choice = int(input("ID: "))
            if choice == 1:
                # display all data
                db.fetch_all_data()
            elif choice == 2:
                # insert new student
                student_id = int(input("Enter student id: "))
                student_name = input("Enter student name: ")
                stand = input("Enter student standard: ")
                marks = int(input("Enter student marks: "))
                db.insert_student(student_id,student_name,stand,marks)
            elif choice == 3:
                # update student data
                student_id = int(input("Enter student id which need to update: "))
                student_name = input("Enter new name: ")
                stand = input("Enter new standard: ")
                marks = int(input("Enter updated marks: "))
                db.update_student_details(student_id,student_name,stand,marks)
            elif choice == 4:
                # display sngle student data
                stud_id = int(input("Enter id of student to be display: "))
                db.fetch_one(stud_id)
            elif choice == 5:
                # delete student data
                stud_id = int(input("Enter student id to delete: "))
                db.delete_student(stud_id)
            elif choice == 6:
                break
            else:
                print("Invalid ID....Please try again.")

        except Exception as e:
            print(e)
            print("Invalid details...")





if __name__ == "__main__":
    menu()
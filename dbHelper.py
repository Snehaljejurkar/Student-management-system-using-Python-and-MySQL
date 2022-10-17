import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host = "localhost",
                                    port = 3306,
                                    user = "root",
                                    password = "password",
                                    database = "studentsdb")

        query = 'create table if not exists student(studentid int primary key, student_name varchar(200),standard varchar(100),marks int(5))'

        cur = self.con.cursor()
        cur.execute(query)
        print("created")

    # insert students
    def insert_student(self,studentid,student_name,standard,marks):
        query = "insert into student(studentid,student_name,standard,marks) values({},'{}','{}',{})".format(studentid,student_name,standard,marks)
        # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Student record has been saved into database")

    # fetch all data
    def fetch_all_data(self):
        query = "select * from student"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("student ID : ",row[0])
            print("student Name : ", row[1])
            print("standard : ", row[2])
            print("marks : ", row[3])
            print()
            print()

    def fetch_one(self,id):
        query = "select * from student"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            if id == row[0]:
                print("student ID : ", row[0])
                print("student Name : ", row[1])
                print("standard : ", row[2])
                print("marks : ", row[3])
                print()

    def delete_student(self,studentid):
        query = "delete from student where studentid = {}".format(studentid)
        # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Student has been deleted from database")


    # update student details
    def update_student_details(self,studentid,newname,newStand,newMarks):
        query = "update student set student_name = '{}', standard = '{}', marks = {} where studentid = {}".format(newname,newStand,newMarks,studentid)
        # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Student information has been updated into database")

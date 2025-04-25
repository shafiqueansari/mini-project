import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # Change to your MySQL username
    password="root",  # Change to your MySQL password
    database="practice_db"
)
cursor = conn.cursor()

def add_student(name,age,grade):
    sql="INSERT INTO STUDENTS(name,age,grade)VALUES(%s,%s,%s)"
    value=(name,age,grade)
    cursor.execute(sql,value)
    conn.commit()
    print("Student added successfully!")
    
def view_students():
    cursor.execute("SELECT * FROM STUDENTS")
    results=cursor.fetchall()
    for row in results:
        print (row)
        
def update_students(student_id,name=None,age=None,grade=None):       
    updates=[]
    values=[]
    
    if name:
        updates.append("name=%s")
        values.append(name)
        
    if age:
        updates.append("age=%s")
        values.append(age)
                
    if grade:
        updates.append("grade=%s")
        values.append(grade)    
        
        
    values.append(student_id)
     
    sql=f"Update students set {','.join (updates)}where id =%s"
    cursor.execute(sql,tuple(values))
    conn.commit()
    print("students update successfull!") 
    
    
    def delete_student(student_id):
        sql="delete from students where id =%s"
        val=(student_id)
        cursor.Commit()
        print("student delete successfully!")
        
        
        
    if __name__ == "__main__":
        while True:
         print("\nstudent management system")
        print("1. Add student")
        print("2. View student")
        print("3. Update student")
        print("4. Delete student")
        print("5. Exit")
        
        
        choice=input("enter your choice :")
            
        if choice=='1':
            name=input("enterr name")
            age=int(input(("enter age:"))) 
            grade=input("enter grade:")
            add_student(name,age,grade)
            
            
        elif choice=='2':
            view_students()
            
        elif choice =='3':
            student_id=int(input("enter student id to update:")) 
            name=input("enter new name(leave blank to skip):") 
            age_input=input("enter new age:")
            grade=input("enter new grade(leave blank to skip ):")
            age=int(age_input) if  age_input else None
            update_students(student_id,name,age,grade)
            
        elif choice=='4':
            student_id=int(input("enter student id to delete:"))
            delete_student(student_id)
            
        elif choice=='5':
            print("exiting.....")  
            
        
        
        else:
            print("invalid choice ! try again.")
            
            
           
            
    cursor.close()
    conn.close()                   
                    
                  
        
        
        
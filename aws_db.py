import pymysql
#WmGuGxpcuLRidOtKnus7
#87uy5vOaqpPtyAarHPf3

def connect():
    conn=pymysql.connect(
        host='testdb.cxtgtrdykzq6.ap-south-1.rds.amazonaws.com',
        port=int(3306),
        user="vaibhav",
        passwd="vaibhavnayan",
        db="test_db",
        charset='utf8mb4')

    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore (book_id int, book_name varchar(20))")
    conn.commit()
    conn.close()

def insert(title,author):
    conn=pymysql.connect(
        host='testdb.cxtgtrdykzq6.ap-south-1.rds.amazonaws.com',
        port=int(3306),
        user="vaibhav",
        passwd="vaibhavnayan",
        db="test_db",
        charset='utf8mb4')
    cur=conn.cursor()
    cur.execute("INSERT INTO bookstore VALUES(%s,%s)",(title,author))
    conn.commit()
    conn.close()

def view():
    conn=pymysql.connect(
        host='testdb.cxtgtrdykzq6.ap-south-1.rds.amazonaws.com',
        port=int(3306),
        user="vaibhav",
        passwd="vaibhavnayan",
        db="test_db",
        charset='utf8mb4')

    cur=conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    rows=cur.fetchall()
    conn.close()
    return rows

connect()
insert(1111,"Helllo")
print(view())
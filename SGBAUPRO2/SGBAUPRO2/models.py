import pymysql
from datetime import datetime    

def connect():
    con = pymysql.connect(host='bk67xcsr2ybpdpujukjo-mysql.services.clever-cloud.com',user='uvqzjpyrqoel7l1a',password='GJDntXBJ0IXA151K7vvW',database='bk67xcsr2ybpdpujukjo')
    return con
 

class memberOperations:
    def get_all_faculties(self):  
        con = connect()
        curs = con.cursor()
        curs.execute("SELECT DISTINCT MEETINGNAME FROM DUTYCERT")
        data = [row[0] for row in curs.fetchall()]
        con.close()
        return data


    def get_members_by_faculty(self, faculty):
        con = connect()
        curs = con.cursor()
        query = "SELECT * FROM DUTYCERT WHERE MEETINGNAME = %s"
        curs.execute(query, (faculty,))
        data = curs.fetchall()
        con.close()
        return data

    

    def searchonMemberID(self, id):
        con =connect()    
        curs = con.cursor()
        curs.execute("SELECT * FROM DUTYCERT WHERE MemberID = %s", (id,))
        data = curs.fetchone()
    
        dic = {}
        if data:
         dic['MemberID'] = data[0]
         dic['CERTNAME'] = data[1]
         dic['MEETINGNAME'] = data[2]
         dic['MEETINGDATE'] = datetime.now().strftime('%d-%m-%Y')  # Current date
         dic['MOBILENO'] = data[4]
         dic['EMAILID'] = data[5]
         dic['CATEGORY'] = data[6]
        else:
         dic['MemberID'] = id
         dic['CERTNAME'] = 'name not found'
         dic['MEETINGNAME'] = 'not found'
         dic['MEETINGDATE'] = datetime.now().strftime('%d-%m-%Y')  
         dic['MOBILENO'] = 'not found'
         dic['EMAILID'] = 'not found'
         dic['CATEGORY'] = 'not found'  
        con.close()
        return dic
  



    def addMember(self, mid, certnm, meetname, meetdate, mobno, emailid, catg):
        try:
           con =connect()    
           curs = con.cursor()
           query = "INSERT INTO DUTYCERT (MemberID, CERTNAME, MEETINGNAME, MEETINGDATE, MOBILENO, EMAILID, CATEGORY) VALUES (%s, %s, %s, %s, %s, %s, %s)"
           curs.execute(query, (mid, certnm, meetname, meetdate, mobno, emailid, catg))
           con.commit()
           msg = "Member added successfully"
        except Exception as e:
           msg = "Failed to add Member: " + str(e)
        finally:
           con.close()  
    
           return msg
         

    def deleteMember(self, mid):
        try:
           con =connect()    
           curs = con.cursor()
           curs.execute("DELETE FROM DUTYCERT WHERE MemberID = %s", (mid,))
           con.commit()
           msg = "Member deleted successfully"
        except Exception as e:
           msg = "Failed to delete Member: " + str(e)
        finally:
           con.close()      
           return msg
        
        
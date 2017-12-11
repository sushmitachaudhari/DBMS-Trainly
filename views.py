# -*- coding: utf-8 -*-

import tornado.web
import tornado.gen
import time
import random
import uuid
import hashlib

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        
        if not self.current_user:
            self.render('login.html')
            return
        userid = tornado.escape.xhtml_escape(self.current_user)
        ret = self.db.query(
            'SELECT * FROM user WHERE userid = %s', userid)
        type = ret[0]['usertype']
        if not type:
            self.render('student.html')
        elif (type == 'A'):
            self.render('admin.html')
        elif (type == 'S'):
            self.render('student.html')
        elif (type == 'F'):
            self.render('staff.html')

class LoginHandler(BaseHandler):
    def get(self):
        self.set_secure_cookie("user", '', expires=time.time() + 900)
        self.render('login.html')
    def post(self):
        userid = self.get_argument("ui")
        password = self.get_argument("pw")
        print(userid)
        print(password)
        ret = self.db.query('SELECT * FROM user WHERE userid = %s', userid)
        if ret:
            self.set_secure_cookie("user", self.get_argument("ui"),expires=time.time()+900)
            type = ret[0]['usertype']
            salt = ret[0]['salt']
            pw = ret[0]['Password']

            if pw == hashlib.sha256(salt.encode() + password.encode()).hexdigest():
                if not type:
                    self.render('student.html')
                elif (type == 'A'):
                    self.render('admin.html')
                elif (type == 'S'):
                    self.render('student.html')
                elif (type == 'F'):
                    self.render('staff.html')
            else:
                self.write("Please input the right passworld!")

        else:
            self.render('register.html')

#
# class StartHandler(BaseHandler):
#     def get(self):
#         self.render('student.html')
#
class StudentHandler(BaseHandler):
    def get(self):
        self.render('student.html')

class AdminHandler(BaseHandler):
    def get(self):
        self.render('admin.html')

class StaffHandler(BaseHandler):
    def get(self):
        self.render('staff.html')

class RegisterHandler(BaseHandler):
    def get(self):
        self.render('register.html')


class RigisteresHandler(BaseHandler):
    def post(self):
        ui = self.get_argument('ui')
        fn = self.get_argument('fn')
        ln = self.get_argument('ln')
        pw = self.get_argument('pw')
        # uuid is used to generate a random number
        salt = uuid.uuid4().hex

        # sha256 to encode
        pw = hashlib.sha256(salt.encode() + pw.encode()).hexdigest()

        pp = self.get_argument('pp')
        st = self.get_argument('st')
        ci = self.get_argument('ci')
        pc = self.get_argument('pc')
        co = self.get_argument('co')
        ut = self.get_argument('ut')
        self.db.execute(
            'INSERT INTO `User` (`UserID`,`FirstName`,`LastName`,`Password`,`ProfilePic`,`Street`,`City`,`Postal Code`,`Country`,`usertype`,`salt`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            ui, fn, ln, pw, pp, st, ci, pc, co, ut, salt)
        self.render('registres.html', id=ui)

class AuthHandler(BaseHandler):
    def get(self):
        self.render('auth.html')

class AuthResHandler(BaseHandler):
    def post(self):
        vi = self.get_argument('vi')
        fi = self.get_argument('fi')
        self.db.execute('UPDATE Faculty SET `ValidatorAdmin`=%s,`status`=%s WHERE (`FacultyID` = %s) AND (`Website` IS NOT NULL) AND (`Affiliation` IS NOT NULL)',vi,'Approved',fi)
        self.render('authres.html', fi=fi)

class CatogHandler(BaseHandler):
    def get(self):
        self.render('Catog.html')

class CatogresHandler(BaseHandler):
    def get(self):
        si = tornado.escape.xhtml_escape(self.current_user)
        ret = self.db.query('SELECT u.UserId,c.CourseId,c.Name,st.topic,ec.CourseStatus,ec.Interested FROM (User u INNER JOIN EnrollCourse ec ON u.UserId = ec.UserId) INNER JOIN Course c ON ec.CourseId = c.CourseId INNER JOIN SecTopic st ON c.CourseID = st.CourseId WHERE u.UserId=%s',si)
        for lines in ret:
            print("FirstName:{} ").format(lines)
        self.render('catogres.html', ret=ret)

class EnrollHandler(BaseHandler):
    def get(self):
        self.render('enroll.html')

class EnrollresHandler(BaseHandler):
    def post(self):
        ci = self.get_argument('ci')
        ui = tornado.escape.xhtml_escape(self.current_user)
        dt = self.get_argument('dt')
        pc = random.randint(10000,99999)
        ii = 'Interested'
        cs = 'InProgress'
        self.db.execute(
            'INSERT INTO `EnrollCourse` (`CourseID`,`UserID`,`Date`,`Payment Code`,`Interested`,`CourseStatus`) VALUES (%s,%s,%s,%s,%s,%s)',
            ci, ui,dt,pc,ii,cs)
        self.render('enrollres.html', ci=ci,ui=ui)

class listHandler(BaseHandler):
    def get(self):
        self.render('list.html')

class listresHandler(BaseHandler):
    def post(self):
        ui = tornado.escape.xhtml_escape(self.current_user)
        ci = self.get_argument('ci')

        ret = self.db.query('SELECT q.id,q.cid,co.status,q.mtl,q.type FROM ( SELECT u.UserId AS id,c.CourseId AS cid,m.Name as mtl,m.MaterialType as type,m.order as ord FROM (User u  INNER JOIN EnrollCourse ec ON u.UserId = ec.UserId) INNER JOIN Course c ON ec.CourseId = c.CourseId INNER JOIN Material m ON c.CourseId = m.CourseId WHERE u.UserId = %s AND c.CourseId = %s) q INNER JOIN Completion co ON (q.cid=co.CourseId AND q.id = co.UserId AND q.ord = co.order)',ui,ci)
        # for lines in ret:
        #     print("FirstName:{} ").format(lines)
        self.render('listres.html', ret=ret)

class CCompleteHandler(BaseHandler):
    def get(self):
        self.render('ccomplete.html')

class CCompleteMidHandler(BaseHandler):
    def post(self):
        ci = self.get_argument('ci')
        si = tornado.escape.xhtml_escape(self.current_user)
        # print(ci[0])
        # si = tornado.escape.xhtml_escape(self.current_user)
        # print(ci)
        # print(si)
        ret = self.db.query(
            'SELECT * FROM Completion AS co WHERE(co.CourseId = %s) AND(co.UserId = %s)'
            , ci, si)
        # for lines in ret:
        #     print("FirstName:{} ").format(lines)
        self.render('ccompletemid.html',ret=ret)

class CCompleteResHandler(BaseHandler):
    def post(self):
        si = tornado.escape.xhtml_escape(self.current_user)
        # ci = self.get_argument('ci')
        ci = self.get_argument('ci')
        od = self.get_argument('od')
        self.db.execute(
            'UPDATE Completion co SET status = %s WHERE ( ( co.CourseId = %s) AND (co.UserId = %s)AND (co.order=%s))',
            'Completed',ci,si,od)
        ret = self.db.query('SELECT * FROM Completion AS co WHERE(co.CourseId = %s) AND(co.UserId = %s) AND(co.status = %s)'
                            ,ci,si,'Notcompleted')
        if not ret:
            self.db.execute(
            'UPDATE EnrollCourse SET `coursestatus` = %s WHERE (courseId = %s) AND (UserId = %s)',
                'Complete', ci,si)
            flag = 1
        else:
            flag = 0
        self.render('ccompleteres.html',flag=flag,si = si,ci = ci)

class CertificateHandler(BaseHandler):
    def get(self):
        self.render('certificate.html')

class CertificateResHandler(BaseHandler):
    def post(self):
        ci = self.get_argument('ci')
        ui = self.get_argument('ui')
        cn = self.get_argument('cn')
        self.db.execute(
            'INSERT INTO `Certification` (`UserID`,`CourseId`,`certificationNo`) VALUES (%s,%s,%s);',
            ui,ci,cn)
        self.render('certificateres.html', ci=ci,ui=ui,cn=cn)

class HistoryResHandler(BaseHandler):
    def get(self):
        ui = tornado.escape.xhtml_escape(self.current_user)
        ret = self.db.query('SELECT u.UserId, u.FirstName, u.LastName,c.CourseId,c.Name,ec.CourseStatus,ec.date,ec.`Payment Code`,SUM(c.cost) AS Total  FROM (User u INNER JOIN EnrollCourse ec ON u.UserId = ec.UserId) INNER JOIN Course c ON ec.CourseId = c.CourseId WHERE u.UserId=%s GROUP BY u.UserId,c.CourseId',ui)
        self.render('historyres.html', ret=ret)

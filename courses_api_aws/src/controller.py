import pymysql 
import hashlib
import random 
import string
from datetime import datetime, timedelta
from model import User, Course, Section, Instructor
import model

# FIXME: set environment variables for those
DB_SERVER = ''
DB_USER   = 'admin'
DB_PASSWD = ''
DB_NAME   = 'courses'

# other parameters
TOKEN_SIZE     = 32
TOKEN_LIFETIME = 5 # minutes

class Controller: 
    """Models a controller for the courses API."""

    # FIXME: consider using a connection pool
    conn = None

    @staticmethod
    def get_connection():
        """Creates a db connection (if one does not already exist) and returns it."""
        if not Controller.conn: 
            Controller.conn = pymysql.connect(host=DB_SERVER, user=DB_USER, passwd=DB_PASSWD, db=DB_NAME, connect_timeout=5, autocommit=True)
        return Controller.conn

    @staticmethod 
    def authenticate(email, password):
        """Authenticates a given user based on the informed credentials, returning a token when successful, None otherwise."""
        conn = Controller.get_connection()
        cur = conn.cursor()
        sql = 'SELECT * FROM users WHERE email = %s'
        cur.execute(sql, [email])
        row = cur.fetchone()
        if row:
            u = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            sh = hashlib.sha512()
            sh.update(u.salt.encode('utf-8'))
            sh.update(password.encode('utf-8'))
            # if authentication is successful
            if sh.hexdigest() == u.password: 
                # generates an unique token
                while True: 
                    u.token = ''
                    for i in range(TOKEN_SIZE):
                        u.token += random.choice(string.ascii_letters + string.digits)
                    sql = 'SELECT expiration FROM users WHERE token = %s'
                    cur.execute(sql, [u.token])
                    if not cur.fetchone():
                        break
                # sets the token expiration
                u.expiration = datetime.now() + timedelta(minutes=TOKEN_LIFETIME)
                # updates the database
                sql = 'UPDATE users SET token = %s, expiration = %s WHERE email = %s'
                cur.execute(sql, [u.token, u.expiration, u.email])
                return u.token
        return None
    
    @staticmethod 
    def authorize(token): 
        """Returns a boolean depending whether or not the given token is expired."""
        conn = Controller.get_connection()
        cur = conn.cursor()
        sql = 'SELECT expiration FROM users WHERE token = %s'
        cur.execute(sql, [token])
        row = cur.fetchone()
        if row: 
            expiration = row[0]
            if datetime.now() <= expiration:
                return True
        return False

    @staticmethod
    def get_courses(token, prefix=None, number=None):
        """Returns a course (or a list of courses) based on given search parameters."""
        if Controller.authorize(token):
            conn = Controller.get_connection()
            cur = conn.cursor()
            sql = 'SELECT * FROM courses WHERE true'
            fields = []
            if prefix:
                sql += ' AND prefix = %s'
                fields.append(prefix)
            if number: 
                sql += ' AND number = %s'
                fields.append(number)
            sql += ' ORDER BY prefix, number'
            cur.execute(sql, fields)
            if prefix and number:
                row = cur.fetchone()
                if row: 
                    c = Course(row[0], row[1], row[2], row[3], row[4], row[5])
                    return model.get_json(c)
            else:
                courses = []
                for row in cur.fetchall():
                    c = Course(row[0], row[1], row[2], row[3], row[4], row[5])
                    courses.append(model.get_json(c))
                return courses
        return None

    @staticmethod 
    def get_course_sections(token, prefix=None, number=None, semester=None, year=None):
        """Returns a course (or a list of courses) with corresponding sections based on given search parameters."""
        if Controller.authorize(token):
            conn = Controller.get_connection()
            cur = conn.cursor()
            sql = '''
                SELECT  C.prefix, C.number, C.title, C.description, C.credits, C.prereqs, 
                        S.crn, S.section, S.semester, S.year, I.email, I.name, I.title, I.office, I.hours, S.times, S.start, S.end, S.location, S.campus 
                FROM courses C, sections S, instructors I 
                WHERE C.prefix = S.prefix AND C.number = S.number AND S.instructor = I.email 
            '''
            fields = []
            if prefix: 
                sql += ' AND C.prefix = %s '
                fields.append(prefix)
            if number:
                sql += ' AND C.number = %s '
                fields.append(number)
            if semester:
                sql += ' AND semester = %s '
                fields.append(semester)
            if year: 
                sql += ' AND year = %s '
                fields.append(year)
            sql += 'ORDER BY C.prefix, C.number, S.section'
            row = cur.execute(sql, fields)
            courses = []
            current = None
            for row in cur.fetchall():
                c = Course(row[0], row[1], row[2], row[3], row[4], row[5])
                i = Instructor(row[10], row[11], row[12], row[13], row[14])
                s = Section(row[6], row[7], row[8], row[9], i, row[15], row[16], row[17], row[18])
                if not current: 
                    current = c 
                if current == c: 
                    current.add_section(s)
                else:
                    courses.append(model.get_json(current))
                    current = c
                    current.add_section(s)
            if current: 
                courses.append(model.get_json(current))
            return courses
        return None

    @staticmethod 
    def get_instructors(token, email=None):
        """Returns an instructor (or a list of instructors) based on given search parameter"""
        if Controller.authorize(token):
            conn = Controller.get_connection()
            cur = conn.cursor()
            sql = 'SELECT * FROM instructors'
            fields = []
            if email:
                sql += ' WHERE email = %s'
                fields.append(email)
            sql += ' ORDER BY name'
            cur.execute(sql, fields)
            if email:
                row = cur.fetchone()
                if row: 
                    i = Instructor(row[0], row[1], row[2], row[3], row[4])
                    return model.get_json(i)
            else:
                instructors = []
                for row in cur.fetchall():
                    i = Instructor(row[0], row[1], row[2], row[3], row[4])
                    instructors.append(model.get_json(i))
                return instructors
        return None
from flask import Flask, request, jsonify, abort
import sqlite3

app = Flask('courses_api')

@app.route('/courses', methods=['GET'])
def courses():
    sql = 'SELECT * FROM courses'
    conn = sqlite3.connect('database.db')
    courses = []
    rows = conn.execute(sql).fetchall()
    if rows:
        for row in rows:
            course = {}
            course['prefix']      = row[0]
            course['number']      = row[1]
            course['title']       = row[2]
            course['description'] = row[3]
            course['credits']     = row[4]
            if row[5]:
                course['prereqs'] = row[5] 
            courses.append(course)
        conn.close()
        return jsonify(courses)
    else:
        conn.close()
        abort(404)

@app.route('/courses/<prefix>', methods=['GET'])
def courses_with_prefix(prefix):
    sql = 'SELECT * FROM courses WHERE prefix = \'' + prefix.upper() + '\''
    conn = sqlite3.connect('database.db')
    courses = []
    rows = conn.execute(sql).fetchall()
    if rows:
        for row in rows:
            course = {}
            course['prefix']      = row[0]
            course['number']      = row[1]
            course['title']       = row[2]
            course['description'] = row[3]
            course['credits']     = row[4]
            if row[5]:
                course['prereqs'] = row[5] 
            courses.append(course)
        conn.close()
        return jsonify(courses)
    else:
        conn.close()
        abort(404)

@app.route('/courses/<prefix>/<number>', methods=['GET'])
def courses_with_prefix_and_number(prefix, number):
    sql = 'SELECT * FROM courses WHERE prefix = \'' + prefix.upper() + '\' AND number = \'' + number.upper() + '\'' 
    conn = sqlite3.connect('database.db')
    courses = []
    rows = conn.execute(sql).fetchall()
    if rows:
        for row in rows:
            course = {}
            course['prefix']      = row[0]
            course['number']      = row[1]
            course['title']       = row[2]
            course['description'] = row[3]
            course['credits']     = row[4]
            if row[5]:
                course['prereqs'] = row[5] 
            courses.append(course)
        conn.close()
        return jsonify(courses)
    else:
        conn.close()
        abort(404)

@app.route('/courses/sections', methods=['GET'])
def sections():
    semester = year = None
    args = request.args
    if 'semester' in args:
        semester = args['semester'].lower()
        if semester not in ['winter', 'spring', 'summer', 'fall']:
            semester = None
    if 'year' in args:
        year = args['year']
        if not year.isnumeric():
            year = None    
    sql = 'SELECT crn, section, prefix, number, semester, year, times, start, end, location, campus, email, name, title, office, hours FROM sections, instructors WHERE sections.instructor_email = instructors.email'
    if semester:
        sql += ' AND semester = \'' + semester + '\''
    if year:
        sql += ' AND year = ' + year
    conn = sqlite3.connect('database.db')
    sections = []
    rows = conn.execute(sql).fetchall()
    if rows:
        for row in rows:
            section = {}
            section['crn']             = row[0]
            section['number']          = row[1]
            section['times']           = row[2]
            section['start']           = row[3]
            section['end']             = row[4]
            section['location']        = row[5]
            section['campus']          = row[6]
            section['instructor']      = {}
            section['instructor']['email']  = row[7]
            section['instructor']['name']   = row[8]
            section['instructor']['title']  = row[9]
            section['instructor']['office'] = row[10]
            section['instructor']['hours']  = row[11]
            sections.append(section)
        conn.close()
        return jsonify(sections)
    else:
        conn.close()
        abort(404)

@app.route('/courses/<prefix>/sections', methods=['GET'])
def sections_with_course_prefix(prefix):
    semester = year = None
    args = request.args
    if 'semester' in args:
        semester = args['semester'].lower()
        if semester not in ['winter', 'spring', 'summer', 'fall']:
            semester = None
    if 'year' in args:
        year = args['year']
        if not year.isnumeric():
            year = None    
    sql = 'SELECT crn, section, prefix, number, semester, year, times, start, end, location, campus, email, name, title, office, hours FROM sections, instructors WHERE prefix = \'' + prefix.upper() + '\' AND sections.instructor_email = instructors.email'
    if semester:
        sql += ' AND semester = \'' + semester + '\''
    if year:
        sql += ' AND year = ' + year
    conn = sqlite3.connect('database.db')
    sections = []
    rows = conn.execute(sql).fetchall()
    if rows:
        for row in rows:
            section = {}
            section['crn']             = row[0]
            section['number']          = row[1]
            section['times']           = row[2]
            section['start']           = row[3]
            section['end']             = row[4]
            section['location']        = row[5]
            section['campus']          = row[6]
            section['instructor']      = {}
            section['instructor']['email']  = row[7]
            section['instructor']['name']   = row[8]
            section['instructor']['title']  = row[9]
            section['instructor']['office'] = row[10]
            section['instructor']['hours']  = row[11]
            sections.append(section)
        conn.close()
        return jsonify(sections)
    else:
        conn.close()
        abort(404)

@app.route('/courses/<prefix>/<number>/sections', methods=['GET'])
def sections_with_course_prefix_and_number(prefix, number):
    semester = year = None
    args = request.args
    if 'semester' in args:
        semester = args['semester'].lower()
        if semester not in ['winter', 'spring', 'summer', 'fall']:
            semester = None
    if 'year' in args:
        year = args['year']
        if not year.isnumeric():
            year = None    
    sql = 'SELECT crn, section, prefix, number, semester, year, times, start, end, location, campus, email, name, title, office, hours FROM sections, instructors WHERE prefix = \'' + prefix.upper() + '\' AND number = ' + number.upper() + ' AND sections.instructor_email = instructors.email'
    if semester:
        sql += ' AND semester = \'' + semester + '\''
    if year:
        sql += ' AND year = ' + year
    conn = sqlite3.connect('database.db')
    sections = []
    rows = conn.execute(sql).fetchall()
    if rows:
        for row in rows:
            section = {}
            section['crn']             = row[0]
            section['number']          = row[1]
            section['times']           = row[2]
            section['start']           = row[3]
            section['end']             = row[4]
            section['location']        = row[5]
            section['campus']          = row[6]
            section['instructor']      = {}
            section['instructor']['email']  = row[7]
            section['instructor']['name']   = row[8]
            section['instructor']['title']  = row[9]
            section['instructor']['office'] = row[10]
            section['instructor']['hours']  = row[11]
            sections.append(section)
        conn.close()
        return jsonify(sections)
    else:
        conn.close()
        abort(404)

@app.route('/instructors', methods=['GET'])
def instructors():
    sql = 'SELECT * from instructors'
    conn = sqlite3.connect('database.db')
    rows = conn.execute(sql).fetchall()
    if rows:
        instructors = []
        for row in rows:
            instructor = {}
            instructor['email']  = row[0]
            instructor['name']   = row[1]
            instructor['title']  = row[2]
            instructor['office'] = row[3]
            instructor['hours']  = row[4]
            instructors.append(instructor)
        conn.close()
        return jsonify(instructors)
    else:
        conn.close()
        abort(404)

@app.route('/instructors/<email>', methods=['GET'])
def instructors_with_email(email):
    sql = 'SELECT * from instructors WHERE email = \'' + email + '\''
    conn = sqlite3.connect('database.db')
    row = conn.execute(sql).fetchone()
    if row:
        instructor = {}
        instructor['email']  = row[0]
        instructor['name']   = row[1]
        instructor['title']  = row[2]
        instructor['office'] = row[3]
        instructor['hours']  = row[4]
        conn.close()
        return jsonify(instructor)
    else:
        conn.close()
        abort(404)
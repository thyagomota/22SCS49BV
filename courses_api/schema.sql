DROP TABLE IF EXISTS sections;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS instructors;

CREATE TABLE courses (
    prefix TEXT NOT NULL, 
    number TEXT NOT NULL, 
    title TEXT NOT NULL, 
    description TEXT NOT NULL, 
    credits INTEGER NOT NULL, 
    prereqs TEXT, 
    PRIMARY KEY (prefix, number)
);

CREATE TABLE instructors (
    email TEXT PRIMARY KEY, 
    name TEXT NOT NULL, 
    title TEXT, 
    office TEXT, 
    hours TEXT
);

CREATE TABLE sections (
    crn INTEGER PRIMARY KEY, 
    section TEXT NOT NULL, 
    prefix TEXT NOT NULL, 
    number TEXT NOT NULL, 
    semester TEXT NOT NULL, 
    year INTEGER NOT NULL, 
    instructor_email TEXT NOT NULL, 
    times TEXT, 
    start TEXT, 
    end TEXT, 
    location TEXT, 
    campus TEXT
);

INSERT INTO instructors VALUES ('tmota@msudenver.edu', 'Thyago Mota', 'Assistant Professor', 'AES-200R', 'M 01:00pm-03:00pm, W 08:00am-11:00am');
INSERT INTO instructors VALUES ('cohenb@msudenver.edu', 'Blanche Cohen', 'Adjunct Instructor', null, null);
INSERT INTO instructors VALUES ('fzeng@msudenver.edu', 'Fanyu Zeng', 'Adjunct Instructor', null, null);
INSERT INTO instructors VALUES ('aibrahi8@msudenver.edu', 'Adil Ibrahim', 'Adjunct Instructor', null, null);
INSERT INTO instructors VALUES ('rranjidh@msudenver.edu', 'Ranjidha Rajan', 'Adjunct Instructor', null, null);
INSERT INTO instructors VALUES ('fjiang@msudenver.edu', 'Feng Jiang', 'Assistant Professor', null, null);

INSERT INTO courses VALUES ('CS', '3810', 'Principles of Database Systems', 'This course covers the principles and methodologies of database design, and techniques for database application development. The topics covered include relational algebra, SQL queries, normalization, entity-relationship model, SQL/Host-language interface, stored procedure, object-oriented databases, and semi-structured databases.', 4, 'CS 2050 and MTH 1410 with grades of C- or better, or permission of instructor');
INSERT INTO courses VALUES ('CS', '1030', 'Computer Science Principles', 'Computer Science Principles introduces students to the central ideas of computer science vital for success in today’s world. Students are invited to develop the computational thinking skills that apply across disciplines, as we explore computing from multiple perspectives, including: cognitive, economic, ethical, legal, mathematical, philosophical, social, and technical. The course integrates computational thinking practices with big ideas in computing to address: collaborative teamwork, communication, creativity, critical thinking, innovation, problem solving, and programming. Students are afforded the opportunity to participate in active-learning experiences and to create computational artifacts that bring ideas to life.', 4, null);

INSERT INTO sections VALUES (31998, '001', 'CS', '1030', 'spring', 2022, 'cohenb@msudenver.edu', 'TR 12:00pm-01:50pm', '2022-01-18', '2022-05-14', 'AES-285', 'main');
INSERT INTO sections VALUES (31999, '002', 'CS', '1030', 'spring', 2022, 'cohenb@msudenver.edu', 'MW 12:00pm-01:50pm', '2022-01-18', '2022-05-14', 'AES-285', 'main');
INSERT INTO sections VALUES (32000, '003', 'CS', '1030', 'spring', 2022, 'cohenb@msudenver.edu', 'MW 04:00pm-05:50pm', '2022-01-18', '2022-05-14', 'AES-285', 'main');
INSERT INTO sections VALUES (32380, '004', 'CS', '1030', 'spring', 2022, 'fzeng@msudenver.edu', 'TR 06:00pm-07:50pm', '2022-01-18', '2022-05-14', null, 'online');

INSERT INTO sections VALUES (33781, '001', 'CS', '3810', 'spring', 2022, 'tmota@msudenver.edu', 'TR 12:00pm-01:50pm', '2022-01-18', '2022-05-14', 'AES-220', 'main');


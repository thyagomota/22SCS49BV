# Courses API

## Description

The Courses API allows users to get information about the courses being offered in a semester, including their class schedule and instructor information.

## Goals

1. Get information about courses
2. Get information about instructors

## Data Model

### Courses

* <ins>prefix</ins>: string (a 2-3 letter subject prefix)
* <ins>number</ins>: string (a 4 digit/letter code)
* title: string (the course's title)
* description: string (the course's description)
* credits: number (the number of credits of the course)
* prereqs: string (the list of prerequisites for the course)

### Course Sections 

* <ins>crn</ins>: number (the Course Reference Number - a 5-digit number that uniquely identifies a course section)
* prefix: string (a 2-3 letter subject prefix)
* number: string (a 4 digit/letter code)
* section: string (the section number as a 3-digit/letter code)
* semester: string (as in <em>winter</em>, <em>spring</em>, <em>summer</em>, or <em>fall</em>)
* year: number (in YYYY format)
* instructor: string (email of the instrutor that is teaching the course section)
* times: string (class meeting days and times using the format [MTWRFS] 99:99xm-99:99xm)
* start: date (when the course section begins in the format YYYY-MM-DD)
* end: date (when the course section ends in the format YYYY-MM-DD)
* location: string (where the course section meets in the format building abbreviation and room number)
* campus: string (as in <em>main</em> or <em>online</em>)

### Instructors 

* <ins>email</ins>: string (instructor's email)
* name: string (instructor's name using last, first name format)
* title: string (instructor's title)
* office: string (location of the instructor's office in the format building abbreviation and room number)
* hours: string (instructor's office hours using the format [MTWRFS] 99:99xm-99:99xm)

## Database Schema 

Available here. 

## API Endpoints

### Get information about courses

* GET /courses
    * inputs: 
        * none
    * output: 
        * the list of all courses
* GET /courses/sections
    * inputs:
        * semester: as in <em>winter</em>, <em>spring</em>, <em>summer</em>, or <em>fall</em>
        * year: in YYYY format  
    * output:
        * the list of all course sections being offered, filtered by semester and/or year 
* GET /courses/sections/{crn}
    * inputs:
        * crn: a course section unique identifier 
    * output:
        * information about a specific course section  
* GET /courses/{prefix}
    * inputs: 
        * a course prefix
    * output: 
        * the list of all courses with given prefix
* GET /courses/{prefix}/sections
    * inputs: 
        * a course prefix
        * semester: as in <em>winter</em>, <em>spring</em>, <em>summer</em>, or <em>fall</em>
        * year: in YYYY format  
    * output: 
        * the list of all course sections being offered for courses with given prefix, filtered by semester and/or year 
* GET /courses/{prefix}/{number}
    * inputs: 
        * a course prefix
        * a course number
    * output: 
        * the full course description
* GET /courses/{prefix}/{number}/sections
    * inputs: 
        * a course prefix
        * a course number
        * semester: as in <em>winter</em>, <em>spring</em>, <em>summer</em>, or <em>fall</em>
        * year: in YYYY format  
    * output: 
        * the list of all sections being offered for a specific course, filtered by semester and/or year
  
### Get information about instructors

* GET /instructors
    * inputs:
        * none
    * output:
        * the list of all instructors
* GET /instructors/{email}
    * inputs:
        * email: the email of an instructor
    * output:
        * Information about the instructor

## API Specification 

Available here.

#ifndef COURSE_H
#define COURSE_H
#include <iostream>
#include <vector>
#include <string>
#include "professor.h"

using namespace std;

class Course{
public:
	string course_name;
	string syllabus;
	string description;
    vector<string> prerequisites;
	Professor creator;
	Course(string name, string syll,string des, vector<string>prereq, Professor creator);
	void loadCourseInfo();
	void uploadMovieUnderCourse();
	void deleteMovieUnderCourse();

};

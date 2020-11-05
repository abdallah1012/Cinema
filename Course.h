#ifndef COURSE_H
#define COURSE_H
#pragma once
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Course{
public:
    Course(string name, string syll,string des, vector<string>prereq);
	string course_name;
	string syllabus;
	string description;
    vector<string> prerequisites;
    //Professor creator;
	void loadCourseInfo();
	void uploadMovieUnderCourse();
	void deleteMovieUnderCourse();

};
#endif // COURSE_H

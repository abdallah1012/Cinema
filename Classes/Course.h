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
private: 
	int course_ID;


};

#include "Course.h"
Course::Course(string name, string syll,string des, vector<string>prereq, Professor creator){
	this.course_name = name;
	this.syllabus =syll;
	this.description = des;
	this.prerequisites = prereq;
	this.creator = creator;
}


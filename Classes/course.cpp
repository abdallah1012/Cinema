#include "Course.h"
Course::Course(string name, string syll,string des, vector<string>prereq, Professor creator){
	this.course_name = name;
	this.syllabus =syll;
	this.description = des;
	this.prerequisites = prereq;
	this.creator = creator;
}


void Course::loadCourseInfo(){
//function to load course information e.g. syllabus and professor, to be viewed by a user
}

void Course:uploadMovieUnderCourse(){
//function to be called when professor wants to upload a movie, because a movie will naturally belong to a course
//commit movie info to MovieManagementSystem
}

void Course:uploadMovieUnderCourse(){
//function to be called when professor wants to delete a movie, because a movie will naturally belong to a course
//delete movie info from MovieManagementSystem
}

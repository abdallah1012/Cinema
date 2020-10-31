#ifndef STUDENT_H
#define STUDENT_H
#include "user.h"
#include <string>
#include <vector>
class Student: protected User
{
public:
	vector<course> student_courses;
    	Student(string f,string l,date dv,vector<string>courses);
	void sign_in(user_id, string password);
	void register_course(course_id);
	void add_interjection(movie_id,time);
	void recommended();
	void feedback(Professor p);
};

#endif // STUDENT_H

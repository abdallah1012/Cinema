#include "student.h"

Student::Student(string f, string l, date dv, vector<string>courses)
{
	first_name = f;
	last_name = l;
	date_of_birth = dv;

	for (int i = 0; i<courses.size(); i++) {
		student_courses[i] = courses[i];
	}

}

void Student::sign_in(user_id, string password){
    /*
     student enters username and password to be checked if correct in database
     then we go to sign in menu.
     */
   
}

void Student::register_course(course_id){
    /* takes as a parameter the course and adds it to the table of
      courses for this student
      */
}
void Student::add_interjection(movie_id,time){
    /* takes as a parameter a movie and timestamp
      adds an interjection on that timestamp (to be accepted by professor)
     */
}
void Student::feedback(Professor p,course c){
	/* the student rates the course and the professor based on a rating system TBD
	*/
}
void Student::recommended(){
    /* display recommended movies for student based on recommendation engine
     */
}

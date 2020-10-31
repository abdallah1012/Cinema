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

bool Student::sign_up(){
    /*
     student supplies information to sign up in database
     */
    return true;
}
bool Student::sign_in(user_id, string password){
    /*
     student enters username and password to be checked if correct in database
     then we go to sign in menu.
     */
    return true;
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
void User::AddComment(String comment_header, String comment_content, movie M){
    /* takes a movie and adds a comment or feedback from student on it
        notify professor
    */
}
void User::WatchMovie(Movie M){
    /* takes a movie as a parameter
     * play the mp3 file
     */
}
void Student::recommended(){
    /* display recommended movies for student based on recommendation engine
     */
}

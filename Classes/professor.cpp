#include<professor.h>

Professor::Professor(String fn,String ln,date db, vector<String> pc)
{ //never called outside of sign_in
    first_name=fn;
    last_name=ln;
    date_of_birth=db;
    
    for(int i=0;i<pc.size();i++){
        professor_courses[i]=pc[i];
    }
}


void Professor::CreateCourse(args[])
{
    //send call to Movie Management System to save course info passed in args[]
}

void Professor::DeleteCourse(course_id)
{
    //if(course.creator==this)
    // send call to Movie management system to delete course
}

void Professor::AdmitStudentToCourse(student_id,course_id);
{
	//send call to Movie management system to save student data in course
}

void Professor::RemoveStudent(student_id,course_id);
{
    // send call to Movie Management System to remove student from course
}

void Professor::UploadMovie(args[])
{
    //Movie m(args[]);
    //send call to Movie management system to commit movie to database
}

void Professor::DeleteMovie(movie_id)
{
   // send call to Movie management system to delete movie
}


void Professor::AcceptInterjection()
{
	//listening on message passing interface for interjections
   	// send call to retrieve movie
	//edit movie instance
	//send call to commit edit movie
}
void Professor::RejectInterjection()
{
	//listening on message passing buffer for interjections
   	// delete interjection from message passing buffer
}
void Professor::AccessMovieStatistics(string movie_id)
{
    StaticticsEngine ss();
    return ss.GetMovieStats(movie_id); //suffiecient to identify a movie
}

void Professor::AccessCourseStatistics(string movie_id)
{
    StaticticsEngine ss();
    return ss.GetCourseStats(movie_id); //suffiecient to identify a movie

}


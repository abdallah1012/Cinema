#include <string>
#include <vector>
#include "user.h"

class Professor:protected User
{
private:
    vector<course> professor_courses;
    
    Professor(String fn,String ln,date db, vector<String> pc);
    
    String SignIn(String fn,String ln,date db, vector<String> pc, String password);
    
    void CreateCourse(all course constructor parameters);
    
    void DeleteCourse(course C);
    
    void AdmitStudent(student_id,course_id);
    
    void RemoveStudent(student_id,course_id);

    void UploadMovie(args[]);
        
    void DeleteMovie(movie_id);
    
    void AcceptInterjection();
    void RejectInterjection();

    void AccessMovieStatistics(movie_id);
    
    void AccessCourseStatistics(course_id);

};

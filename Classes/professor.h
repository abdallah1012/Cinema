#include <String>
#include <Vector>
#include <user.h>

class Professor:protected User
{
private:
    vector<course> professor_courses;
    
    Professor(String fn,String ln,date db, vector<String> pc);
    
    String SignIn(String fn,String ln,date db, vector<String> pc, String password);
    
    void CreateCourse(all course constructor parameters);
    
    void DeleteCourse(course C);
    
    void AdmitStudent(student user unique ID, course C);
    
    void RemoveStudent(student user unique ID, course C);

    void UploadMovie(all movie constructor parameters);
        
    void DeleteMovie(movie unique ID);
    
    void AddInterjection(String uploader,String interjection_name,String interjection_content, Movie M, time t);
    
    void AcceptInterjection();
    
    Dependsonreturn AccessMovieStatistics(Movie M);
    
    Dependsonreturn AccessCourseStatistics(Course C);

};

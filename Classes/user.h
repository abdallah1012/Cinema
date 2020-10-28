#include <String>
//#include <Date> any date library
//#include <time> any time library


class User
{
protected:
    String * first_name;
    String * last_name;
    date * birth_date;
    String * id;
    

    void WatchMovie(movie m);

    
    void AddComment(String comment_header, String comment_content, movie M);
    
    void RemoveComment(String comment_header, movie M);
    
    bool ViewCourseMaterial(Course C);
};

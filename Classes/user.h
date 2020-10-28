#include <string>
#include "movie.h"


class User
{
protected:
    string first_name;
    string last_name;
    //date * birth_date;
    int user_id;
    void WatchMovie(Movie m);
    void AddComment(string comment_header, string comment_content, Movie M);
    void RemoveComment(string comment_header, Movie M);
    
};

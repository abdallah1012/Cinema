#include <user.h>

//No constructor for user.

void User::WatchMovie(movie m)
{
    m.Watch();
}

void User::AddComment(String comment_header, String comment_content, movie M)
{
    //function Call to AddComment function in Movie Management.
    MovieManagment * mm= new MovieManagment();
    return mm.AddComment(this->id,comment_header,comment_content,M);
    delete mm;
}

void User::RemoveComment(String comment_header, movie M)//Movie management verifies that a single user can not have more than 1 comment with the same name.
{
    //function Call to RemoveComment function in Movie Management.
    MovieManagment * mm= new MovieManagment();
    return mm.RemoveComment(this->id,comment_header,M);
    delete mm;
}

bool User::ViewCourseMaterial(Course C)
{
    CourseManagment * cm= new CourseManagment();
    return cm.BelongsToCourse();
    delete cm;
}

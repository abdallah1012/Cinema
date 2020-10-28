#include "user.h"

void User::WatchMovie(Movie M) {
//send call to Movie Management System to retrieve movie URL and stream movie
}

void User::AddComment(String comment_header, String comment_content, movie M)
{

    //send call to Movie Management System to add comment to a movie
    //comment is typically a pair (String, user_id)
}

void User::RemoveComment(String comment_header, movie M)//Movie management verifies that a single user can not have more than 1 comment with the same name.
{
    //send call to ovie Management System to check owner of comment
    //if this==comment.owner
    //	send call to Movie Management System to delete comment 
}

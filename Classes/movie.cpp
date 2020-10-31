#include "movie.h"

movie::movie(course *c)
{
  parentCourse = c;
}

void movie::play()
{
    //plays the movie
}

void movie::pause()
{
    //pauses the movie
}

void movie::addStudent(student s)
{
    //adds student to the array students
}

void movie::changeTitle(string t)
{
    //adds a title to a movie
}

void movie::changeDescription(string d)
{
    //adds a description to the movie
}

void movie::deleteMovie(string profPassword)
{
    //check if profPassword == parentCourse.Professor.password
    //the prof deletes the movie
}

void movie::addTranscript(string t)
{
    //transcript = t
}

void movie::deleteComment(int i, string profPassword)
{
    //check if profPassword == parentCourse.Professor.password
    //deletes the ith comment
}

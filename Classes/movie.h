#ifndef MOVIE_H
#define MOVIE_H

#include "course.h"
#include "student.h"

class movie
{
public:
    movie(coure *c, string t , string d);

    //OBJECT mediafile;

    course *parentCourse;
    // note that the owner is parentCourse.Professor
    student students[50];   //might not keep
    int timer[50];          //tracks each student's time watched might not keep
    bool watched[50];       //might not keep
    string URL;
    string title;
    string description;
    string transcript;
    string comments[100];

    void play();
    void pause();
    void addStudent(student *s);
    void changeTitle(string t);
    void changeDescription(string d);
    void addTranscript(string t);
    void deleteMovie(string profPassword);
    void deleteComment(int i, string profPassword);
};

#endif // MOVIE_H

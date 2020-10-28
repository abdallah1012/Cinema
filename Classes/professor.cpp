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


String Professor::SignIn(String fn,String ln,date db, vector<String> pc, String password)
{
    //function call to a function in Usermanagement that performs an SQL Query with targets password==password for user entry corresponding to this->id
    UserManagement * um= new UserManagement();
    if(um.ProfSignIn())
    {
        Professor * prof= new Professor(String fn,String ln,date db, vector<String> pc);
        return "Succesfully Logged In";
    }
    else{
        return "ID or Password is incorrect";
    }
    delete um;
}

void Professor::CreateCourse(S:all course constructor parameters)
{
    CourseManagement * cm= new CourseManagement();//or we can use usermanagement doesnt matter
    Course * C= new Course(S);
    if(cm.AddCourse(C)) //AddCourse returns a boolean if the addition succeeded
    {
        professor_courses.push_back(C);
    }
    
    delete cm;
}

void Professor::DeleteCourse(S:all course constructor parameters)
{
    CourseManagement * cm= new CourseManagement();//or we can use usermanagement doesnt matter
    Course * C= new Course(S);
    if(cm.DeleteCourse(C)) //DeleteCourse returns a boolean if the course was found and deleted
    {
        int i;
        for(i=0;i<professor_courses.size();i++)
        {
            if(professor_courses[i]==C)
                break;
        }
        professor_courses.remove(i);
    }
    
    delete cm;
}

void Professor::AdmitStudent(student user unique ID, course C);
{
    CourseManagement * cm = new CourseManagement();
    
    cm.AddStudent(student-id, C);
    
    delete dm;
}

void Professor::RemoveStudent(student user unique ID, course C);
{
    CourseManagement * cm = new CourseManagement();
    
    cm.RemoveStudent(student-id, C);
    
    delete cm;
    
}

void Professor::UploadMovie(S:all movie constructor parameters)
{
    Movie * m= new Movie(S); //movie needs its course as an attribute
    MovieManagment * mm= new MovieManagment();
    return mm.AddMovie(M);
    delete mm;
    delete m;
}

void Professor::DeleteMovie(movie-id)
{
    MovieManagment * mm= new MovieManagment();
    return mm.RemoveMovie(movie-id); //suffiecient to identify a movie
    delete mm;
}

void Professor::AddInterjection(String uploader,String interjection_name,String interjection_content, Movie M, time t)
{
    //might be changed to creating interjection as a standalone stake holder and class
    MovieManagment * mm= new MovieManagment();
    mm.AddInterjection(String uploader,String interjection_name,String interjection_content, Movie M, time t); //or mm.AddInterjection(interjection n=new interjection(...)); delete n;
    delete mm;
}

void Professor::AcceptInterjection(?)
{
    CourseManagement * cm = new CourseManagement();
    
    cm.FetchUnacceptedInterjections();;//to be added after deciding if interjections will be a class or not
    delete cm;
}

DependsonReturn Professor::AccessMovieStatistics(Movie M)
{
    StaticticsEngine * ss= new StaticticsEngine();
    return ss.GetMovieStats(movie-id); //suffiecient to identify a movie
    delete mm;
}

DependsonReturn Professor::AccessCourseStatistics(Movie M)
{
    StaticticsEngine * ss= new StaticticsEngine();
    return ss.GetCourseStats(movie-id); //suffiecient to identify a movie
    delete mm;
}


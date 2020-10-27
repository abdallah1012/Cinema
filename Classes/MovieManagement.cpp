#include "MovieManagement.h"
#include <string>
struct movieManagement{

string toRecommendation(String studentName)
{
	/*
	
	1. stdHist = Send SQL query and get list of last 10 videos that student watched from his history table
	2. Movies = Send SQL query for all movies 
	
	return (stdHist, Movies)
	
	*/
}

String toStatistics (String studentName)
{
	/*
	1. retrieve necessary data from the history table
	*/
}

void addToHistory(string StudentName, string ID, string Date, String Duration)
{
	/*
	
	1. send SQL UPDATE to history table with attributes (studentName, MovieID, Date, Duration) where we update the
		MovieID column to add the ID of the movie they watched. (ie. if they already watched movies with 
		IDs 10 and 21 then it would be (10, 21) then adding movie 34 it becomes (10, 21, 34))
	2. Similarly for the date and duration, since each movie was watched at a date
	
	WARNING: add SQL query to history first to check if student watched this before. If true
			 then update duration if the older one was shorter and update Date.
	
	Note: We use regex to split by ",\s" to get the movie IDs separately
	This has been done so that the table doesn't have several entries for the same student
	*/	
}

string loadMovie(string studentName, string ID)
{
	/*
	
	To load the movie we need to uniquely identify it, therefore when a student requests a movie, we should query
	based on the course, professor and the movie name.
	
	1. Send SQL query with ID as where clause
	
	2. Select clause has only URL column
	
	Note: If this returns more than 1 URL then we have a database conflict or logic error in registerMovie
	
	*/
	
	//addToHistory(studentName, MovieName, ProfessorName, CourseName, Date(time(0))
	
	return URL;
}

bool registerMovie(string MovieName, string CourseName, string ProfessorName)
{
	
	/*
	
	1. Send SQL query to see if the movie name is taken by that professor (if yes then return false)
	2. Use Youtube API to add movie to youtube
	3. Get the URL of the movie
	4. Send SQL insert statement to database tables Movies and MoviesURL
		with: (MovieName, CourseName, ProfessorName) & (URL) 
	[Note: ID is created by default when adding to database if we assign it as increasing unique key]
	
	Note: to avoid piling all movies in one table, we can make a seperate table that contains (ID, URL)
	whose UNIQUE KEY (ID) is that of table with (MovieName, CourseName, ProfessorName)
	
	Explanation:
	URL is needed to stream later on
	MovieName Is needed to show the name later on
	CourseName is needed when a student/professor enters a course and needs to retrieve all movies of that course
	ProfessorName is needed when the professor needs to retrieve all his videos or a student searches by professor name
	*/
	
	return true; //True if successful
}


};
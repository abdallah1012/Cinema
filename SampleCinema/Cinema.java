import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Cinema {
	private ArrayList<Movie> cine = new ArrayList<Movie>();
	Scanner scan = new Scanner(System.in);

	public Cinema() {

	}

	public void add(Movie movie) {
		cine.add(movie);
	}

	public void delete(String name) {
		try {
			for (int i = 0; i < cine.size(); i++) {
				if (cine.get(i).getName().equalsIgnoreCase(name))
					cine.remove(i);
			}
		} catch (NullPointerException e) {
			System.out.println("Name of movie doesn't exist");
		}
	}

	public void Reserve(String name, int nbseats) {
		Movie movie = null;
		try {
			for (int i = 0; i < cine.size(); i++) {
				if (cine.get(i).getName().equalsIgnoreCase(name))
					movie = cine.get(i);
			}
		} catch (NullPointerException e) {
			System.out.println("Name of movie doesn't exist");
		}

		for (int j = 0; j < nbseats; j++) {
			
			
			System.out.println("Enter the seat number you want to reserve");
			int y = scan.nextInt();
//			try {
//				y = scan.nextInt();
//			} catch (ArrayIndexOutOfBoundsException e) {
//				System.out.println("Seat number doesn't exist");
//			}
			if (movie.getSeats()[y] ==0){
				movie.getSeats()[y] = 1;
				System.out.println("Your seat has been reserved !");
				}
			else{
				System.out.println("Seat is taken.");
				j--;
				}
			
			
			
		}
	
	}

	public void SortbyRating() {
		for (int i = 0; i < cine.size(); i++) {
			for (int j = 1; j < cine.size() - i; j++) {
				if (cine.get(j).getRating() > cine.get(j - 1).getRating()) {
					Movie temp = cine.get(j);
					cine.set(j, cine.get(j - 1));
					cine.set(j - 1, temp);
				}
			}
		}
	}

	public void CancelReservation(String name, int nbseats) {
		Movie movie = null;
		try {
			for (int i = 0; i < cine.size(); i++) {
				if (cine.get(i).getName().equalsIgnoreCase(name))
					movie = cine.get(i);
			}
		} catch (NullPointerException e) {
			System.out.println("Name of movie doesn't exist");
		}

		for (int j = 0; j < nbseats; j++) {
			int y = 0;
			System.out.println("Enter the seat number you want to cancel");
			try {
				y = scan.nextInt();
			} catch (ArrayIndexOutOfBoundsException e) {
				System.out.println("Seat number doesn't exist");
			}
			if (movie.getSeats()[y] == 1) {
				movie.getSeats()[y] = 0;
				continue;
			} else {
				System.out.println("Seat is already empty.");
				continue;
			}

		}
	}

	public String show() {
		String s="";
		for (int i = 0; i < cine.size(); i++) {
			s+= cine.get(i).getName()+"\n";
		}

		return s;

	}

	public Movie ShowMovie(String m) {
		for (int i = 0; i < cine.size(); i++) {
			if (cine.get(i).getName().equalsIgnoreCase(m))
				return (cine.get(i));

		}
		return null;
	}
	public void SortByTime(){
		for(int i=0;i<cine.size();i++){
			for(int j=1;j<cine.size()-i;j++){
				if(cine.get(j-1).getTime().compareTo(cine.get(j).getTime())>0){
					Movie temp=cine.get(j);
					cine.set(j, cine.get(j-1));
					cine.set(j-1, temp);
				}
			}
		}
	}
}
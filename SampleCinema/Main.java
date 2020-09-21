import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		File input = new File("movies");
		final Cinema cinema=new Cinema();
		Scanner scan = new Scanner(input);
		while (scan.hasNextLine()) {
			String movieinfo = scan.nextLine();
			String[] s = movieinfo.split("-");
			String[] t = s[5].split(":");
			int seats[] = new int[Integer.parseInt(s[6])];
			Movie movie = new Movie(s[0], s[1], Double.parseDouble(s[2]), s[3], Integer.parseInt((s[4])),
					new Time(Integer.parseInt(t[0]), Integer.parseInt(t[1])), seats, Double.parseDouble(s[7]),
					Boolean.getBoolean(s[8]));
			cinema.add(movie);
		
		}
		Bmigui3 f=new Bmigui3(cinema);
		cinema.Reserve("The Maze Runner",5 );
		//cinema.SortbyRating();
		//cinema.show();
	}

}
import java.util.Arrays;

public class Movie {
	private String name;
	private double rating;
	private String type;
	private int duration;
	private String description;
	private Time time;
	private boolean is3d;
	private int[] seats;
	private double price;

	
	public Movie(String name, String description, double rating, String type, int duration, Time time,
			int[] seats, double price, boolean is3d) {
	
		this.name = name;
		this.rating = rating;
		this.type = type;
		this.duration = duration;
		this.description = description;
		this.time = time;
		this.is3d = is3d;
		this.seats = seats;
		this.price = price;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getRating() {
		return rating;
	}

	public void setRating(double rating) {
		if (rating >= 1 && rating <= 10)
			this.rating = rating;
	}

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public double getDuration() {
		return duration;
	}

	public void setDuration(int duration) {
		this.duration = duration;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public Time getTime() {
		return time;
	}

	public void setTime(Time time) {
		this.time = time;
	}

	public boolean isIs3d() {
		return is3d;
	}

	public void setIs3d(boolean is3d) {
		this.is3d = is3d;
	}

	public int[] getSeats() {
		return seats;
	}

	public void setSeats(int[] seats) {
		this.seats = seats;
	}

	public double getPrice() {
		return price;
	}

	public void setPrice(double price) {
		if(is3d==true)
		this.price = price+5000;
		else 
			this.price=price;
	}

	@Override
	public String toString() {
		return "\nMovie name: " + name + "\nRating: " + rating + "\nType: " + type + "\nDuration: " + duration
				+"\nMinutes "+ "\nDescription: " + description + "\nTime: " + time + "\nPrice: " + price ;
	}

}

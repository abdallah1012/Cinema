
public class Time implements Comparable {
	private int hours;
	private int minutes;

	
	public Time(int hours, int minutes) {
		this.hours = hours;
		this.minutes = minutes;
	}

	public int getHours() {
		return hours;
	}

	public void setHours(int hours) {
		if (hours >= 0 && hours <= 23)
			this.hours = hours;
	}

	public int getMinutes() {
		return minutes;
	}

	public void setMinutes(int minutes) {
		if (minutes >= 0 && minutes <= 59)
			this.minutes = minutes;
	}

	@Override
	public String toString() {
		return hours + " : " + minutes;
	}

	public int compareTo(Time t) {
		int hours = t.hours;
		int mins = t.minutes;
		if (this.getHours() > hours)
			return 1;
		else if (this.getHours() < hours)
			return -1;
		else if (this.getHours() == hours) {
			if (this.getMinutes() > minutes)
				return 1;
			else if (this.getMinutes() < mins)
				return -1;
			else
				return 0;
		}
		return 0;
	}

	@Override
	public int compareTo(Object o) {
		// TODO Auto-generated method stub
		return 0;
	}

}

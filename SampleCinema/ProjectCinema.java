import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JButton;
import java.awt.Color;
import java.awt.Font;
import java.awt.Button;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.awt.SystemColor;
import javax.swing.ImageIcon;
import java.awt.Toolkit;
import java.awt.Window.Type;
import javax.swing.JTextArea;

public class ProjectCinema  {

	private JFrame frmCinemaCity;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					ProjectCinema window = new ProjectCinema();
					window.frmCinemaCity.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public ProjectCinema() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmCinemaCity = new JFrame();
		frmCinemaCity.getContentPane().setBackground(new Color(230, 230, 250));
		frmCinemaCity.setType(Type.POPUP);
		frmCinemaCity.setBackground(new Color(255, 255, 255));
		frmCinemaCity.setIconImage(Toolkit.getDefaultToolkit().getImage("C:\\Users\\PC\\Downloads\\movies.png"));
		frmCinemaCity.setTitle("Cinema City");
		frmCinemaCity.setBounds(100, 100, 1563, 905);
		frmCinemaCity.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmCinemaCity.getContentPane().setLayout(null);
		
		JButton btnShowMovies = new JButton("Show movies");
		btnShowMovies.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
			}
		});
		btnShowMovies.setSelectedIcon(new ImageIcon("C:\\Users\\PC\\Downloads\\movies.ico"));
		btnShowMovies.setIcon(new ImageIcon("C:\\Users\\PC\\Downloads\\movies.ico"));
		btnShowMovies.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent arg0) {
				File input = new File("movies");
				final Cinema cinema=new Cinema();
				Scanner scan = null;
				try {
					scan = new Scanner(input);
				} catch (FileNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
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
				JOptionPane.showMessageDialog(btnShowMovies, cinema.show());
				
			}
		});
		btnShowMovies.setFont(new Font("Calibri", Font.PLAIN, 40));
		btnShowMovies.setBackground(new Color(221, 160, 221));
		btnShowMovies.setBounds(521, 32, 812, 96);
		frmCinemaCity.getContentPane().add(btnShowMovies);
		
		JButton btnReserveA = new JButton("Reserve a movie");
		btnReserveA.setBackground(new Color(135, 206, 235));
		btnReserveA.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent arg0) {
				File input = new File("movies");
				final Cinema cinema=new Cinema();
				Scanner scan = null;
				try {
					scan = new Scanner(input);
				} catch (FileNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
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
				cinema.Reserve(JOptionPane.showInputDialog("Enter the name of the movie"), Integer.parseInt(JOptionPane.showInputDialog("Enter the number of seats")));
			}
		});
		btnReserveA.setFont(new Font("Calibri", Font.PLAIN, 40));
		btnReserveA.setBounds(521, 191, 812, 96);
		frmCinemaCity.getContentPane().add(btnReserveA);
		
		JButton btnCancelReservation = new JButton("Cancel reservation");
		btnCancelReservation.setBackground(new Color(240, 128, 128));
		btnCancelReservation.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent arg0) {
				File input = new File("movies");
				final Cinema cinema=new Cinema();
				Scanner scan = null;
				try {
					scan = new Scanner(input);
				} catch (FileNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
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
				cinema.CancelReservation(JOptionPane.showInputDialog("Enter the name of the movie"), Integer.parseInt(JOptionPane.showInputDialog("Enter the number of seats")));
				
			}
		});
		btnCancelReservation.setFont(new Font("Calibri", Font.PLAIN, 40));
		btnCancelReservation.setBounds(521, 344, 812, 96);
		frmCinemaCity.getContentPane().add(btnCancelReservation);
		
		JButton btnSortMovies = new JButton("Sort movies by rating");
		btnSortMovies.setBackground(new Color(255, 218, 185));
		btnSortMovies.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				File input = new File("movies");
				final Cinema cinema=new Cinema();
				Scanner scan = null;
				try {
					scan = new Scanner(input);
				} catch (FileNotFoundException k) {
					// TODO Auto-generated catch block
					k.printStackTrace();
				}
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
				cinema.SortbyRating();
				JOptionPane.showMessageDialog(null, "Sorted successfully");
				JOptionPane.showMessageDialog(btnShowMovies, cinema.show());
				
				
			}
		});
		btnSortMovies.setFont(new Font("Calibri", Font.PLAIN, 40));
		btnSortMovies.setBounds(521, 506, 812, 96);
		frmCinemaCity.getContentPane().add(btnSortMovies);
		
		JButton btnShowMovie = new JButton("Show movie");
		btnShowMovie.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				File input = new File("movies");
				final Cinema cinema=new Cinema();
				Scanner scan = null;
				try {
					scan = new Scanner(input);
				} catch (FileNotFoundException k) {
					// TODO Auto-generated catch block
					k.printStackTrace();
				}
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
				JOptionPane.showMessageDialog(null,cinema.ShowMovie(JOptionPane.showInputDialog("Enter the name of the movie")) );
				
			}
		});
		btnShowMovie.setBackground(new Color(255, 192, 203));
		btnShowMovie.setFont(new Font("Calibri", Font.PLAIN, 40));
		btnShowMovie.setBounds(521, 663, 812, 96);
		frmCinemaCity.getContentPane().add(btnShowMovie);
		
		JButton btnSortMovies_1 = new JButton("Sort movies by time");
		btnSortMovies_1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent arg0) {
				File input = new File("movies");
				final Cinema cinema=new Cinema();
				Scanner scan = null;
				try {
					scan = new Scanner(input);
				} catch (FileNotFoundException k) {
					// TODO Auto-generated catch block
					k.printStackTrace();
				}
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
				cinema.SortByTime();
				JOptionPane.showMessageDialog(null, "Sorted successfully");
				JOptionPane.showMessageDialog(null, cinema.show());
				
			}
		});
		btnSortMovies_1.setToolTipText("");
		btnSortMovies_1.setBackground(new Color(152, 251, 152));
		btnSortMovies_1.setFont(new Font("Calibri", Font.PLAIN, 40));
		btnSortMovies_1.setBounds(521, 826, 812, 96);
		frmCinemaCity.getContentPane().add(btnSortMovies_1);
	}
}

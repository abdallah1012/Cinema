import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

public class Bmigui3 implements ActionListener{
	private JFrame frame;
	private JTextField heightField;
	private JTextField weightField;
	private JLabel bmiLabel;
	private JButton computeButton;

	public Bmigui3(Cinema c) {
		
		
		heightField = new JTextField(5);
		weightField = new JTextField(5);
		bmiLabel = new JLabel("Type your height and weight");
		computeButton = new JButton("Compute");

		JPanel north = new JPanel(new GridLayout(2, 2));
		north.add(new JLabel("Height: "));
		north.add(heightField);
		north.add(new JLabel("Weight: "));
		north.add(weightField);

		frame = new JFrame("BMI");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(new Dimension(700,700));
		frame.setLayout(new BorderLayout());
		frame.add(north, BorderLayout.NORTH);
		frame.add(bmiLabel, BorderLayout.CENTER);
		frame.add(computeButton, BorderLayout.SOUTH);
		computeButton.addActionListener(this);
		frame.pack();
		frame.setVisible(true);
	}

	public void actionPerformed(ActionEvent event) {
		
		String s=heightField.getText();
		int i=Integer.parseInt(s);
		if (i==1){
			
		}

		
	}
}

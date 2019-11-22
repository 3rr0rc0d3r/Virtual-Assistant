import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.swing.*;
import javax.swing.colorchooser.ColorChooserComponentFactory;
import javax.swing.plaf.ColorChooserUI;

public class VirtualAssistant {
    public static void main(String[] args) {
        JFrame f = new JFrame("Virtual Assistant by 3rr0rc0d3r");
        //final TextField tf=new TextField();
        //tf.setBounds(50,50, 150,20);
        JButton b=new JButton("Start");
        b.setBounds(95,120,200,200);
        b.setIcon(new ImageIcon("src/microphone_icon.png"));


        JButton b2 = new JButton("Stop and Close");
        b2.setBounds(95, 330,200 , 35);
        b2.setBackground(Color.LIGHT_GRAY);

        JLabel l = new JLabel("VIRTUAL ASSISTANT");
        l.setBounds(95, 35, 200, 30);
        l.setForeground(Color.RED);
        l.setBorder(BorderFactory.createLineBorder(Color.black,1));
        l.setHorizontalAlignment(JLabel.CENTER);



        b.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                //tf.setText("Devang's listener");
                //String command = null;

                //if (System.getProperty("os.name").equals("Linux"))
                //{

                //command = "gnome-terminal";

                //  }

                JOptionPane.showMessageDialog(f, "Software is running!");


                try {
                    Process pro = Runtime.getRuntime().exec("gnome-terminal" );
                } catch (IOException ex) {
                    ex.printStackTrace();
                }



            }


        });

        b2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {

                try {
                    Process pro2 = Runtime.getRuntime().exec("pkill gnome-terminal");
                }
                catch (IOException ex)
                {
                    ex.printStackTrace();
                }
            }
        });

        f.add(b);
        f.add(b2);
        f.add(l);
        //f.add(tf);
        f.setSize(400,450);
        f.setLayout(null);
        f.setVisible(true);

    }
}

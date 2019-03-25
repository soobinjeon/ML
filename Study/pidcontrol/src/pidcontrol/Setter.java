package pidcontrol;

import java.util.Scanner;

public class Setter  extends Thread {
    private int id;
    private SharedData sdata;
    private Scanner sc;

    public Setter(int id, SharedData sd) {
        this.id = id;
        sdata = sd;
        sc = new Scanner(System.in);
    }

    public void run() {
        while (true) {
            double value = sc.nextDouble();
            sdata.setSpeed(value);
        }
    }
}

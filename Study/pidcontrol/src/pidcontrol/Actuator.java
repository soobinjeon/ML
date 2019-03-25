package pidcontrol;

public class Actuator extends Thread {
    private int id;
    private SharedData sdata;
    private double ms = 50;
    public Actuator(int id, SharedData sd) {
        this.id = id;
        sdata = sd;
    }

    public void run() {
        while (true) {
            try {
                Thread.sleep((long)ms);
                //v = v0 + at
                double v0 = sdata.getActVal();
                double a = sdata.getControlVal();
                double akph = a * (ms / 1000);
                akph = (1.0f/1000.0f) / (1.0f/3600.0f) * akph;
                double nspeed = v0 + akph;
                sdata.setActVal(nspeed);
                //System.out.println("Execute Actuator(" + id + ") setSpd("+sdata.getSetSpeed()+") "
                //        +"ctrA("+sdata.getControlVal()+") Speed : "+sdata.getActVal());
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

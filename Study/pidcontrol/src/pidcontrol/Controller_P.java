package pidcontrol;

public class Controller_P extends Thread{
    private int id;
    private SharedData sdata;
    public Controller_P(int id, SharedData sd){
        this.id = id;
        sdata = sd;
    }

    public void run(){
        double errorsum = 0;
        double error_prev = 0;
        while(true){
            try {
                Thread.sleep(500);
                double setSpeed = sdata.getSetSpeed();
                double adata = sdata.getActVal();
                //a = (v - v0) / t
                double v = 1000.0d/3600.0d * setSpeed;
                double v0 = 1000.0d/3600.0d * adata;
                double p = (v - v0);
                errorsum += p;
                double d = p - error_prev;
                double pid = p * 0.95f + errorsum * 0.42f + d * 0.1f;
                double a= (pid - v0) / (1000.0d/500.0d);
                if(adata != setSpeed){
                    sdata.setControlValue(a);
                }else
                    sdata.setControlValue(0.0f);
                //System.out.println("Execute Controller("+id+")..");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

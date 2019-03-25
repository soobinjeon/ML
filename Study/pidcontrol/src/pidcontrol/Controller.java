package pidcontrol;

public class Controller extends Thread{
    private int id;
    private SharedData sdata;
    public Controller(int id, SharedData sd){
        this.id = id;
        sdata = sd;
    }

    public void run(){
        while(true){
            try {
                Thread.sleep(1000);
                double setSpeed = sdata.getSetSpeed();
                double adata = sdata.getActVal();
                if(adata > setSpeed){
                    sdata.setControlValue(-1.f);
                }else if (adata < setSpeed){
                    sdata.setControlValue(1.f);
                }else
                    sdata.setControlValue(0.0f);
                //System.out.println("Execute Controller("+id+")..");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

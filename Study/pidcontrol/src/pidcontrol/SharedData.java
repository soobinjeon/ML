package pidcontrol;

public class SharedData {
    private double control_val;
    private double act_val;
    private double setSpeed;

    public SharedData(){
        control_val = 0;
        act_val = 0;
    }

    public void setControlValue(double cv){
        control_val = cv;
    }

    public void setActVal(double ac){
        act_val = ac;
    }

    public double getControlVal(){
        return control_val;
    }

    public double getActVal(){
        return act_val;
    }

    public void setSpeed(double sp){
        setSpeed = sp;
    }

    public double getSetSpeed(){
        return setSpeed;
    }
}

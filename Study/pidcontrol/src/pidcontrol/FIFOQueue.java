package pidcontrol;

import java.util.ArrayList;
import java.util.LinkedList;

public class FIFOQueue {
    private int maxSize = 0;
    private double setspd = 0;
    private boolean isSetMaxValue = false;
    ArrayList<Double> list = new ArrayList<Double>();
    public FIFOQueue(int size, double setspd, boolean smv){
        maxSize = size;
        this.setspd = setspd;
        isSetMaxValue = smv;
    }

    public void Add(Double value){
        if(list.size() == maxSize){
            list.remove(0);
        }
        list.add(value);
    }

    public double[] getValues(){
        double[] rdata = new double[list.size()];
        for(int i=0;i<list.size();i++){
            if(i == 0 && isSetMaxValue)
                rdata[i] = 0;
            else if(i==1 && isSetMaxValue)
                rdata[i] = setspd;
            else
                rdata[i] = list.get(i);
        }
        return rdata;
    }
}

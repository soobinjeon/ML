package pidcontrol;

import org.knowm.xchart.QuickChart;
import org.knowm.xchart.SwingWrapper;
import org.knowm.xchart.XYChart;
import org.knowm.xchart.internal.chartpart.Axis;
import org.knowm.xchart.internal.chartpart.Chart;
import org.knowm.xchart.internal.series.AxesChartSeries;
import org.knowm.xchart.style.AxesChartStyler;

import java.util.ArrayList;
import java.util.Queue;

public class pidcontrol {
    Thread control;
    Actuator actor;
    Setter setter;
    SharedData sdata;
    double setSpeed = 50.0f;

    private Axis xAxis;
    private Axis yAxis;

    public pidcontrol(){
        sdata = new SharedData();
        sdata.setSpeed(setSpeed);
        //control = new Controller(1, sdata);
        control = new Controller_P(1, sdata);
        actor= new Actuator(1, sdata);
        setter = new Setter(1, sdata);

        // add axes
    }

    public void startpid() throws InterruptedException {

        FIFOQueue xData = new FIFOQueue(100, sdata.getSetSpeed(), false);
        FIFOQueue yData = new FIFOQueue(100, sdata.getSetSpeed(), true);
        xData.Add(1.0d);
        yData.Add(0.0d);
        // Create Chart
        XYChart chart = QuickChart.getChart("Sample Chart", "X", "Y", "y(x)", xData.getValues(), yData.getValues());

        final SwingWrapper<XYChart> sw = new SwingWrapper<XYChart>(chart);
        sw.displayChart();

        Thread.sleep(2000);
        control.start();
        actor.start();
        setter.start();

        double cnt=2;
        while(true){
            xData.Add(cnt++);
            yData.Add(sdata.getActVal());
            //System.out.println();
            chart.updateXYSeries("y(x)", xData.getValues(), yData.getValues(), null);
            sw.repaintChart();
            Thread.sleep(100);
        }

    }
}

import sys
sys.path.append(r'X:\CODE\Reusable')
import time
import picoscope
import tsiFlowMeter
import alicatFlowMeter

scope = picoscope.picoWrapper()
# port 24, N2O, 56747
flowMeter56747 = alicatFlowMeter.alicat(1)
# port 25, O2, 54083 
flowMeter54083 = alicatFlowMeter.alicat(24)

atmPressure = 0.9948 #bara # 16/10/2013
startTime=time.perf_counter()
#while True:
while(startTime+40>time.perf_counter()):
    print('%f\t%f\t%f\t%f\t%f\t%f'%(
          time.perf_counter(),
          scope.voltage(0),                    
          flowMeter56747.massFlow(),   
          flowMeter54083.massFlow(),                  
          flowMeter56747.pressure(),  
          flowMeter54083.pressure())
          )
    time.sleep(0.001)
scope.close()




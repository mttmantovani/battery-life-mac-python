CYCLES=$(system_profiler SPPowerDataType | grep "Cycle Count" | awk '{print $3}')
CAPACITY=$(system_profiler SPPowerDataType | grep "Full Charge Capacity" | awk '{print $5}')
DESIGN_CAPACITY=$(ioreg -l -w0 | grep "\"DesignCapacity\" =" | awk '{print $5}')
PYTHON=/usr/local/bin/python3
WD=$DEV/battery-life
OUTPUT=$WD/data.csv


$PYTHON $WD/battery_life.py --cycles $CYCLES \
                            --output $OUTPUT \
                            --capacity $CAPACITY \
                            --design-capacity $DESIGN_CAPACITY
                    


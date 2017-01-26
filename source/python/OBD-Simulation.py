import obd
import time

connection = obd.OBD('/dev/pts/4') # auto-connects to USB or RF port
cmd1 = obd.commands.SPEED # select an OBD command (sensor)
cmd2 = obd.commands.MAF

while 1:
    vss = connection.query(cmd1) # send the command, and parse the response
    maf = connection.query(cmd2)

    if (vss is None) or (maf is None):
        continue

  #  print(vss)
   # print(maf)

    print(vss.time)
#   print(vss.value.magnitude)
#   print(maf.value.magnitude)
    kpl = 302.15 * ((vss.value.magnitude) / (maf.value.magnitude))
    print(kpl)
    print('')

#    print(1/kpl)
#    valStr = str(kpl)
#    print(valStr + " kpl")
    time.sleep(1)

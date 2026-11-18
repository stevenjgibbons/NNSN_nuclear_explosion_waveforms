
Folder *remove_response_example* containing a bash script that generates a
displacement trace with the instrument response removed.  

```
sh ./resp_remove_one_file.sh  USS19902971457/USS19902971457_NS.MOR7.00.SHZ.mseed  RESPONSES/MOR7.xml
```

You will probably have to adjust the paths in the script to make it find the location you have saved the waveforms and responses.

(1) Raw seismogram:  

![Raw seismogram.](./MOR7_raw.png)

(2) Panel of response removal:  

![Panel for intermediate stages of removing the instrument response.](./MOR7_response_removal_panel.png)

(3) Displacement seismogram with instrument response removed:  

![The resulting displacement seismogram.](./MOR7_1990_disp_seismogram.png)




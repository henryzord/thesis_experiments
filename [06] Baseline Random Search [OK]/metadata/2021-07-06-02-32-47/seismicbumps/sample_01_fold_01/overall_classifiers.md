# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |
| seismic = b and genergy > 78910 and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps3 > 0.5 and energy > 650 | 1 | 0.001736 |
| seismic = a and genergy <= 17640 and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps3 <= 0.5 and energy <= 650 | 1 | 0.000461 |
| seismic = a and genergy > 78910 and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps3 <= 0.5 and energy > 650 | 1 | 0.000230 |
| nbumps <= 1 and gpuls > 1209 and nbumps3 > 0 and seismic = b | 1 | 0.002485 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.0 and gpuls <= 1333.0 and gpuls > 32.0 and gdenergy <= 180.0 and gdpuls <= 96.0 and gdpuls <= 79.0 and gdenergy <= 104.0 and gdenergy <= 89.0 and gdpuls > -75.0 and gdpuls > -70.0 and gdpuls > -56.0 and gdpuls > -53.0 and genergy <= 55350.0 and gdpuls > -43.0 and gdpuls > -39.0 and genergy <= 40030.0 and gpuls <= 665.0 and gpuls <= 522.0 and gpuls <= 462.0 and gpuls <= 440.0 and gdpuls > -32.0 and gdpuls > -27.0 | 0 | 0.737559 |
| nbumps <= 1.0 and gpuls <= 1333.0 and gpuls <= 32.0 | 0 | 0.475524 |
| nbumps <= 1.0 and gpuls <= 1333.0 and gdenergy <= 180.0 and gdpuls <= 96.0 and gdpuls <= 79.0 and gdpuls > -75.0 and gdpuls > -70.0 and gdpuls <= -56.0 | 0 | 0.390244 |
| nbumps <= 1.0 and gpuls <= 1333.0 and genergy <= 127770.0 and gdenergy <= 180.0 and gdpuls <= 96.0 and gdpuls <= 79.0 and gdpuls > -75.0 and gdenergy > -73.0 and seismoacoustic != c and shift != W and gdenergy > -56.0 | 0 | 0.513300 |
| nbumps <= 1.0 and gpuls <= 1333.0 and genergy <= 127770.0 and gdenergy <= 180.0 and gdpuls > -75.0 and gdpuls > -53.0 and gdpuls > -43.0 and energy <= 4500.0 and genergy <= 66030.0 and gdenergy <= 104.0 and seismoacoustic != c and energy <= 600.0 and gpuls <= 731.0 and gdenergy > -57.0 and gpuls > 243.0 | 0 | 0.648955 |
| gdenergy <= 180.0 and nbumps <= 1.0 and gpuls <= 1333.0 and gdpuls <= 96.0 and genergy <= 127770.0 and genergy > 3330.0 and gpuls > 87.0 and seismoacoustic != c and gpuls <= 812.0 and gdpuls <= 79.0 and gdenergy <= 104.0 and genergy <= 65150.0 | 0 | 0.542822 |
| gdenergy <= 180.0 and energy <= 600.0 and gdenergy <= 104.0 | 0 | 0.580197 |
| gdenergy > 180.0 | 0 | 0.361702 |
| gpuls <= 1252.0 and genergy > 127360.0 | 0 | 0.265044 |
| genergy <= 78580.0 and genergy <= 69660.0 and gpuls > 847.0 | 0 | 0.268623 |
| genergy <= 78580.0 and genergy <= 69660.0 and gpuls <= 786.0 and nbumps3 <= 2.0 and energy <= 40400.0 and energy <= 23500.0 and maxenergy <= 8000.0 and gpuls > 110.0 and genergy > 20860.0 and gpuls > 306.0 and maxenergy <= 5000.0 and maxenergy > 800.0 and seismoacoustic != b | 0 | 0.198980 |
| gdenergy > 128.0 and gdpuls <= 78.0 | 0 | 0.142857 |
| gdpuls <= -70.0 | 0 | 0.126033 |
| energy > 40600.0 and energy > 67700.0 and genergy <= 348780.0 | 0 | 0.128801 |
| gdpuls > -51.0 and genergy <= 1132810.0 and gpuls <= 645.0 and nbumps3 <= 3.0 and gpuls <= 624.0 and gdpuls <= 132.0 and genergy > 21240.0 and genergy > 27980.0 and shift = W and maxenergy > 500.0 and genergy > 39410.0 | 0 | 0.212281 |
| genergy <= 1132810.0 and shift != W and genergy > 19390.0 | 0 | 0.115933 |
| genergy <= 1132810.0 and gdpuls > -52.0 and gdpuls <= -29.0 | 0 | 0.204647 |
| genergy > 1132810.0 | 0 | 0.102937 |
| energy > 40600.0 and energy <= 54800.0 | 0 | 0.068323 |
| gdenergy > -30.0 and gpuls > 280.0 and gpuls <= 2873.0 and nbumps3 <= 3.0 and gdenergy > -20.0 and nbumps2 <= 2.0 and gpuls > 387.0 and seismic = a and gdpuls <= 119.0 and nbumps > 0.0 | 0 | 0.191649 |
| gdenergy > -53.0 and gpuls <= 357.0 and genergy > 20760.0 and seismic = a | 0 | 0.086423 |
| gdenergy > -54.0 and gdpuls > 66.0 and nbumps <= 4.0 and gdenergy > 89.0 and genergy > 16690.0 and gdpuls <= 96.0 | 0 | 0.058539 |
| gdenergy > -54.0 and nbumps4 > 0.0 and genergy <= 664090.0 and gdenergy <= 95.0 and gpuls <= 1742.0 | 0 | 0.075717 |
| gdenergy > 129.0 and seismic = a | 0 | 0.032258 |
| gdenergy <= -54.0 | 1 | 0.185494 |
| energy <= 34000.0 and gpuls > 1894.0 and gpuls <= 2096.0 | 0 | 0.057447 |
| energy <= 34000.0 and nbumps4 > 0.0 | 0 | 0.022556 |
| nbumps4 <= 0.0 and genergy > 32270.0 and genergy > 36230.0 and gdpuls > -25.0 and gdenergy <= -29.0 and genergy > 88360.0 | 1 | 0.118644 |
| nbumps4 <= 0.0 and energy > 5800.0 and gdpuls > -17.0 and gdpuls > -7.0 and energy <= 9600.0 | 1 | 0.188616 |
| energy > 19000.0 | 1 | 0.236111 |
| genergy <= 649840.0 and energy > 13700.0 | 1 | 0.072727 |
| genergy <= 649840.0 and nbumps <= 5.0 and gpuls > 1375.0 and genergy > 390180.0 and gdpuls > -23.0 | 0 | 0.030525 |
| gpuls <= 2326.0 and gpuls <= 1375.0 and genergy <= 136810.0 and maxenergy <= 5000.0 and energy <= 6100.0 and energy <= 4300.0 and genergy <= 88360.0 and nbumps <= 2.0 and gpuls <= 822.0 and energy <= 3400.0 and energy <= 1900.0 and gdpuls > -14.0 and gdenergy > 88.0 and gdpuls > 35.0 and shift = W | 1 | 0.111888 |
| nbumps > 0.0 and genergy <= 763520.0 and nbumps <= 7.0 and gpuls <= 1397.0 and genergy <= 136810.0 and nbumps2 > 0.0 and gdpuls > 3.0 | 1 | 0.216949 |
| ghazard = a and nbumps <= 7.0 and gpuls <= 1369.0 and gdpuls <= 0.0 and genergy <= 108750.0 and genergy <= 32270.0 and genergy > 18040.0 | 0 | 0.053467 |
| gdpuls > -20.0 and nbumps <= 3.0 and gpuls <= 1369.0 and gpuls > 398.0 | 0 | 0.119347 |
| genergy <= 763520.0 and gdpuls > -27.0 and nbumps <= 3.0 and gpuls > 321.0 | 1 | 0.586124 |
| gdpuls > -23.0 | 0 | 0.311207 |
|  | 1 | 0.885714 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

seismic|genergy|nbumps|nbumps2|nbumps3|energy|class
---|---|---|---|---|---|---
b|(78910-inf)|(1.5-inf)|(0.5-inf)|(0.5-inf)|(650-inf)|0
a|(78910-inf)|(1.5-inf)|(0.5-inf)|(0.5-inf)|(650-inf)|0
b|(17640-78910]|(1.5-inf)|(0.5-inf)|(0.5-inf)|(650-inf)|0
a|(17640-78910]|(1.5-inf)|(0.5-inf)|(0.5-inf)|(650-inf)|0
b|(-inf-17640]|(1.5-inf)|(0.5-inf)|(0.5-inf)|(650-inf)|0
a|(-inf-17640]|(1.5-inf)|(0.5-inf)|(0.5-inf)|(650-inf)|0
b|(78910-inf)|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(650-inf)|0
a|(78910-inf)|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(650-inf)|0
a|(17640-78910]|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(650-inf)|0
b|(78910-inf)|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(650-inf)|0
a|(78910-inf)|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(650-inf)|0
b|(17640-78910]|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(650-inf)|0
b|(-inf-17640]|(1.5-inf)|(-inf-0.5]|(0.5-inf)|(650-inf)|1
b|(78910-inf)|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(650-inf)|1
a|(17640-78910]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(650-inf)|0
a|(78910-inf)|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(650-inf)|0
b|(17640-78910]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(650-inf)|0
b|(-inf-17640]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(650-inf)|1
a|(78910-inf)|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(650-inf)|0
b|(17640-78910]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(650-inf)|0
a|(17640-78910]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(650-inf)|0
b|(-inf-17640]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(650-inf)|0
b|(17640-78910]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(650-inf)|0
b|(78910-inf)|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|(650-inf)|0
a|(17640-78910]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(650-inf)|0
a|(-inf-17640]|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|(650-inf)|0
b|(-inf-17640]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(650-inf)|0
a|(-inf-17640]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(650-inf)|0
a|(78910-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(650-inf)|1
a|(78910-inf)|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-650]|0
b|(78910-inf)|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(650-inf)|0
b|(17640-78910]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-650]|0
a|(17640-78910]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-650]|0
a|(17640-78910]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(650-inf)|0
b|(17640-78910]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(650-inf)|0
b|(-inf-17640]|(1.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-650]|1
a|(-inf-17640]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(650-inf)|0
a|(78910-inf)|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-650]|0
b|(78910-inf)|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-650]|0
b|(-inf-17640]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(650-inf)|0
a|(17640-78910]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-650]|0
b|(17640-78910]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-650]|0
b|(-inf-17640]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-650]|0
a|(-inf-17640]|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|(-inf-650]|0
a|(-inf-17640]|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|(-inf-650]|1
b|(78910-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-650]|0
a|(78910-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-650]|0
b|(17640-78910]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-650]|0
a|(17640-78910]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-650]|0
b|(-inf-17640]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-650]|0
a|(-inf-17640]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-650]|0

## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.0 AND gpuls <= 1333.0 AND gpuls > 32.0 AND gdenergy <= 180.0 AND gdpuls <= 96.0 AND gdpuls <= 79.0 AND gdenergy <= 104.0 AND gdenergy <= 89.0 AND gdpuls > -75.0 AND gdpuls > -70.0 AND gdpuls > -56.0 AND gdpuls > -53.0 AND genergy <= 55350.0 AND gdpuls > -43.0 AND gdpuls > -39.0 AND genergy <= 40030.0 AND gpuls <= 665.0 AND gpuls <= 522.0 AND gpuls <= 462.0 AND gpuls <= 440.0 AND gdpuls > -32.0 AND gdpuls > -27.0|0 (437.0/8.0)
nbumps <= 1.0 AND gpuls <= 1333.0 AND gpuls <= 32.0|0 (136.0)
nbumps <= 1.0 AND gpuls <= 1333.0 AND gdenergy <= 180.0 AND gdpuls <= 96.0 AND gdpuls <= 79.0 AND gdpuls > -75.0 AND gdpuls > -70.0 AND gdpuls <= -56.0|0 (96.0)
nbumps <= 1.0 AND gpuls <= 1333.0 AND genergy <= 127770.0 AND gdenergy <= 180.0 AND gdpuls <= 96.0 AND gdpuls <= 79.0 AND gdpuls > -75.0 AND gdenergy > -73.0 AND seismoacoustic != c AND shift != W AND gdenergy > -56.0|0 (162.0)
nbumps <= 1.0 AND gpuls <= 1333.0 AND genergy <= 127770.0 AND gdenergy <= 180.0 AND gdpuls > -75.0 AND gdpuls > -53.0 AND gdpuls > -43.0 AND energy <= 4500.0 AND genergy <= 66030.0 AND gdenergy <= 104.0 AND seismoacoustic != c AND energy <= 600.0 AND gpuls <= 731.0 AND gdenergy > -57.0 AND gpuls > 243.0|0 (309.0/16.0)
gdenergy <= 180.0 AND nbumps <= 1.0 AND gpuls <= 1333.0 AND gdpuls <= 96.0 AND genergy <= 127770.0 AND genergy > 3330.0 AND gpuls > 87.0 AND seismoacoustic != c AND gpuls <= 812.0 AND gdpuls <= 79.0 AND gdenergy <= 104.0 AND genergy <= 65150.0|0 (209.0/9.0)
gdenergy <= 180.0 AND energy <= 600.0 AND gdenergy <= 104.0|0 (237.0/7.0)
gdenergy > 180.0|0 (85.0)
gpuls <= 1252.0 AND genergy > 127360.0|0 (58.0/2.0)
genergy <= 78580.0 AND genergy <= 69660.0 AND gpuls > 847.0|0 (59.0/2.0)
genergy <= 78580.0 AND genergy <= 69660.0 AND gpuls <= 786.0 AND nbumps3 <= 2.0 AND energy <= 40400.0 AND energy <= 23500.0 AND maxenergy <= 8000.0 AND gpuls > 110.0 AND genergy > 20860.0 AND gpuls > 306.0 AND maxenergy <= 5000.0 AND maxenergy > 800.0 AND seismoacoustic != b|0 (40.0)
gdenergy > 128.0 AND gdpuls <= 78.0|0 (25.0)
gdpuls <= -70.0|0 (27.0/2.0)
energy > 40600.0 AND energy > 67700.0 AND genergy <= 348780.0|0 (26.0/2.0)
gdpuls > -51.0 AND genergy <= 1132810.0 AND gpuls <= 645.0 AND nbumps3 <= 3.0 AND gpuls <= 624.0 AND gdpuls <= 132.0 AND genergy > 21240.0 AND genergy > 27980.0 AND shift = W AND maxenergy > 500.0 AND genergy > 39410.0|0 (47.0/3.0)
genergy <= 1132810.0 AND shift != W AND genergy > 19390.0|0 (23.0)
genergy <= 1132810.0 AND gdpuls > -52.0 AND gdpuls <= -29.0|0 (63.0/11.0)
genergy > 1132810.0|0 (20.0/1.0)
energy > 40600.0 AND energy <= 54800.0|0 (11.0)
gdenergy > -30.0 AND gpuls > 280.0 AND gpuls <= 2873.0 AND nbumps3 <= 3.0 AND gdenergy > -20.0 AND nbumps2 <= 2.0 AND gpuls > 387.0 AND seismic = a AND gdpuls <= 119.0 AND nbumps > 0.0|0 (55.0/9.0)
gdenergy > -53.0 AND gpuls <= 357.0 AND genergy > 20760.0 AND seismic = a|0 (18.0)
gdenergy > -54.0 AND gdpuls > 66.0 AND nbumps <= 4.0 AND gdenergy > 89.0 AND genergy > 16690.0 AND gdpuls <= 96.0|0 (12.0/1.0)
gdenergy > -54.0 AND nbumps4 > 0.0 AND genergy <= 664090.0 AND gdenergy <= 95.0 AND gpuls <= 1742.0|0 (17.0/1.0)
gdenergy > 129.0 AND seismic = a|0 (5.0)
gdenergy <= -54.0|1 (9.0/2.0)
energy <= 34000.0 AND gpuls > 1894.0 AND gpuls <= 2096.0|0 (9.0)
energy <= 34000.0 AND nbumps4 > 0.0|0 (9.0/3.0)
nbumps4 <= 0.0 AND genergy > 32270.0 AND genergy > 36230.0 AND gdpuls > -25.0 AND gdenergy <= -29.0 AND genergy > 88360.0|1 (7.0)
nbumps4 <= 0.0 AND energy > 5800.0 AND gdpuls > -17.0 AND gdpuls > -7.0 AND energy <= 9600.0|1 (13.0/1.0)
energy > 19000.0|1 (8.0/1.0)
genergy <= 649840.0 AND energy > 13700.0|1 (7.0/2.0)
genergy <= 649840.0 AND nbumps <= 5.0 AND gpuls > 1375.0 AND genergy > 390180.0 AND gdpuls > -23.0|0 (6.0/2.0)
gpuls <= 2326.0 AND gpuls <= 1375.0 AND genergy <= 136810.0 AND maxenergy <= 5000.0 AND energy <= 6100.0 AND energy <= 4300.0 AND genergy <= 88360.0 AND nbumps <= 2.0 AND gpuls <= 822.0 AND energy <= 3400.0 AND energy <= 1900.0 AND gdpuls > -14.0 AND gdenergy > 88.0 AND gdpuls > 35.0 AND shift = W|1 (10.0/3.0)
nbumps > 0.0 AND genergy <= 763520.0 AND nbumps <= 7.0 AND gpuls <= 1397.0 AND genergy <= 136810.0 AND nbumps2 > 0.0 AND gdpuls > 3.0|1 (12.0/3.0)
ghazard = a AND nbumps <= 7.0 AND gpuls <= 1369.0 AND gdpuls <= 0.0 AND genergy <= 108750.0 AND genergy <= 32270.0 AND genergy > 18040.0|0 (8.0)
gdpuls > -20.0 AND nbumps <= 3.0 AND gpuls <= 1369.0 AND gpuls > 398.0|0 (12.0)
genergy <= 763520.0 AND gdpuls > -27.0 AND nbumps <= 3.0 AND gpuls > 321.0|1 (13.0/1.0)
gdpuls > -23.0|0 (14.0)
|1 (6.0/1.0)


## J48 Decision Tree

* nbumps <= 1
	* gpuls <= 1209: 0 (1553.0/43.0)
	* gpuls > 1209
		* nbumps3 <= 0: 0 (72.0/5.0)
		* nbumps3 > 0
			* seismic = a: 0 (12.0/2.0)
			* seismic = b: 1 (12.0/6.0)
			* seismic = c: 0 (0.0)
			* seismic = d: 0 (0.0)
* nbumps > 1: 0 (414.0/78.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)



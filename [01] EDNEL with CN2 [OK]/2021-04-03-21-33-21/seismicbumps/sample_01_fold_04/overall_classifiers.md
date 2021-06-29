# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.934137 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic != a and genergy > 189465.0 and seismoacoustic != a and maxenergy <= 3500.0 | 1 | 0.001228 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic != a and genergy > 189465.0 and seismoacoustic = a and nbumps2 > 1.5 and nbumps <= 3.5 | 1 | 0.001917 |
| nbumps >= 1.5 and gpuls >= 740.5 and nbumps2 >= 0.5 and gdenergy < -29.5 and maxenergy >= 1500.0 | 1 | 0.004132 |
| nbumps <= 1.5 and gpuls <= 1357.0 and seismoacoustic != c and shift = W and nbumps4 <= 0.5 and seismic != a and nbumps2 <= 0.5 and ghazard = b and genergy <= 21325.0 and genergy > 19400.0 | 1 | 0.000829 |
| nbumps < 1.5 and gpuls >= 1357.0 and nbumps3 >= 0.5 and genergy < 422215.0 | 1 | 0.002365 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic != a and genergy > 189465.0 and seismoacoustic = a and nbumps2 > 1.5 and nbumps > 3.5 | 1 | 0.000922 |
| nbumps > 1.5 and nbumps2 > 0.5 and seismic != a and genergy > 189465.0 and seismoacoustic = a and nbumps2 <= 1.5 and genergy <= 412485.0 | 1 | 0.001917 |
| genergy <= 17640 and gpuls <= 1139.5 and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps5 = all and nbumps6 = all and energy <= 550 | 1 | 0.000461 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.934137 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 744 and gdenergy <= -30 and gdenergy >= -32 | 1 | 0.002299 |
| nbumps >= 2 and nbumps2 >= 1 and energy >= 5800 and energy <= 9200 and maxenergy >= 5000 and gpuls >= 768 | 1 | 0.004130 |
|  | 0 | 0.939801 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

genergy|gpuls|nbumps|nbumps2|nbumps5|nbumps6|energy|class
---|---|---|---|---|---|---|---
(17640-48545]|(1139.5-inf)|(1.5-inf)|(0.5-inf)|all|all|(550-inf)|1
(48545-inf)|(1139.5-inf)|(1.5-inf)|(0.5-inf)|all|all|(550-inf)|0
(17640-48545]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|all|all|(550-inf)|0
(-inf-17640]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|all|all|(550-inf)|0
(48545-inf)|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|all|all|(550-inf)|0
(17640-48545]|(1139.5-inf)|(0.5-1.5]|(0.5-inf)|all|all|(550-inf)|1
(48545-inf)|(1139.5-inf)|(0.5-1.5]|(0.5-inf)|all|all|(550-inf)|0
(48545-inf)|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|all|all|(550-inf)|0
(17640-48545]|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|all|all|(550-inf)|0
(48545-inf)|(1139.5-inf)|(1.5-inf)|(-inf-0.5]|all|all|(550-inf)|0
(-inf-17640]|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|all|all|(550-inf)|0
(-inf-17640]|(-inf-1139.5]|(1.5-inf)|(-inf-0.5]|all|all|(550-inf)|1
(48545-inf)|(-inf-1139.5]|(1.5-inf)|(-inf-0.5]|all|all|(550-inf)|0
(17640-48545]|(-inf-1139.5]|(1.5-inf)|(-inf-0.5]|all|all|(550-inf)|0
(17640-48545]|(1139.5-inf)|(0.5-1.5]|(-inf-0.5]|all|all|(550-inf)|1
(48545-inf)|(1139.5-inf)|(0.5-1.5]|(-inf-0.5]|all|all|(550-inf)|0
(17640-48545]|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|all|all|(550-inf)|0
(48545-inf)|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|all|all|(550-inf)|0
(-inf-17640]|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|all|all|(550-inf)|0
(48545-inf)|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|all|all|(-inf-550]|0
(-inf-17640]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|all|all|(-inf-550]|1
(17640-48545]|(-inf-1139.5]|(1.5-inf)|(0.5-inf)|all|all|(-inf-550]|0
(48545-inf)|(1139.5-inf)|(0.5-1.5]|(0.5-inf)|all|all|(-inf-550]|0
(17640-48545]|(1139.5-inf)|(0.5-1.5]|(0.5-inf)|all|all|(-inf-550]|0
(48545-inf)|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|all|all|(-inf-550]|0
(-inf-17640]|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|all|all|(-inf-550]|0
(17640-48545]|(-inf-1139.5]|(0.5-1.5]|(0.5-inf)|all|all|(-inf-550]|0
(-inf-17640]|(-inf-1139.5]|(0.5-1.5]|(-inf-0.5]|all|all|(-inf-550]|1
(17640-48545]|(1139.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-550]|0
(48545-inf)|(1139.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-550]|0
(17640-48545]|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-550]|0
(-inf-17640]|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-550]|0
(48545-inf)|(-inf-1139.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-550]|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 744) and (gdenergy <= -30) and (gdenergy >= -32)|1 (5.0/0.0)
(nbumps >= 2) and (nbumps2 >= 1) and (energy >= 5800) and (energy <= 9200) and (maxenergy >= 5000) and (gpuls >= 768)|1 (9.0/0.0)
|0 (2309.0/139.0)


## PART

Decision list:

rules | predicted class
---|---
|0 (1549.0/102.0)


## J48 Decision Tree

* nbumps <= 1.5
	* gpuls <= 1357.0
		* seismoacoustic = c: 0 (35.0)
		* seismoacoustic != c
			* shift = W
				* nbumps4 <= 0.5
					* seismic = a
						* ghazard = a
							* nbumps3 <= 0.5
								* seismoacoustic = a
									* nbumps <= 0.5: 0 (203.0/5.0)
									* nbumps > 0.5: 0 (56.0/3.0)
								* seismoacoustic != a
									* nbumps <= 0.5: 0 (129.0/6.0)
									* nbumps > 0.5: 0 (23.0)
							* nbumps3 > 0.5
								* energy <= 1500.0
									* seismoacoustic = a: 0 (5.0/2.0)
									* seismoacoustic != a: 0 (6.0/1.0)
								* energy > 1500.0: 0 (56.0)
						* ghazard != a
							* nbumps <= 0.5: 0 (34.0/1.0)
							* nbumps > 0.5: 0 (8.0)
					* seismic != a
						* nbumps2 <= 0.5
							* ghazard = b
								* genergy <= 21325.0
									* genergy <= 19400.0: 0 (6.0)
									* genergy > 19400.0: 1 (5.0/2.0)
								* genergy > 21325.0: 0 (28.0)
							* ghazard != b
								* seismoacoustic = a
									* nbumps <= 0.5
										* gdpuls <= 100.0: 0 (158.0/4.0)
										* gdpuls > 100.0: 0 (9.0/3.0)
									* nbumps > 0.5
										* energy <= 6500.0: 0 (20.0)
										* energy > 6500.0: 0 (5.0/1.0)
								* seismoacoustic != a
									* nbumps <= 0.5: 0 (84.0/5.0)
									* nbumps > 0.5: 0 (20.0/1.0)
						* nbumps2 > 0.5
							* energy <= 850.0: 0 (64.0)
							* energy > 850.0: 0 (5.0/2.0)
				* nbumps4 > 0.5: 0 (25.0)
			* shift != W
				* nbumps <= 0.5
					* seismic = a
						* ghazard = a
							* seismoacoustic = a: 0 (366.0/5.0)
							* seismoacoustic != a: 0 (140.0/1.0)
						* ghazard != a: 0 (9.0)
					* seismic != a: 0 (105.0)
				* nbumps > 0.5
					* nbumps4 <= 0.5
						* seismic = a
							* nbumps3 <= 0.5
								* seismoacoustic = a
									* gdenergy <= -54.5: 0 (6.0/2.0)
									* gdenergy > -54.5: 0 (22.0)
								* seismoacoustic != a: 0 (13.0)
							* nbumps3 > 0.5
								* seismoacoustic = a: 0 (67.0/1.0)
								* seismoacoustic != a: 0 (28.0/1.0)
						* seismic != a: 0 (27.0)
					* nbumps4 > 0.5: 0 (9.0/2.0)
	* gpuls > 1357.0
		* nbumps3 <= 0.5
			* ghazard = a
				* nbumps4 <= 0.5
					* seismic = a
						* seismoacoustic = a
							* nbumps <= 0.5
								* gdenergy <= 28.5: 0 (9.0)
								* gdenergy > 28.5: 0 (5.0/2.0)
							* nbumps > 0.5
								* energy <= 700.0: 0 (5.0)
								* energy > 700.0: 0 (8.0/1.0)
						* seismoacoustic != a: 0 (6.0/1.0)
					* seismic != a
						* genergy <= 226260.0: 0 (5.0/2.0)
						* genergy > 226260.0: 0 (5.0)
				* nbumps4 > 0.5: 0 (6.0)
			* ghazard != a: 0 (7.0)
		* nbumps3 > 0.5
			* seismic = a: 0 (8.0/2.0)
			* seismic != a
				* genergy <= 422215.0: 1 (6.0)
				* genergy > 422215.0: 0 (6.0/2.0)
* nbumps > 1.5
	* nbumps2 <= 0.5
		* nbumps3 <= 2.5
			* ghazard = a
				* seismoacoustic = a
					* nbumps3 <= 1.5: 0 (13.0)
					* nbumps3 > 1.5
						* nbumps4 <= 0.5
							* seismic = a
								* maxenergy <= 5500.0: 0 (15.0)
								* maxenergy > 5500.0: 0 (5.0/1.0)
							* seismic != a
								* genergy <= 48280.0: 0 (5.0)
								* genergy > 48280.0: 0 (5.0/1.0)
						* nbumps4 > 0.5: 0 (5.0/1.0)
				* seismoacoustic != a: 0 (21.0)
			* ghazard != a: 0 (5.0/1.0)
		* nbumps3 > 2.5
			* genergy <= 46180.0: 0 (5.0/2.0)
			* genergy > 46180.0: 0 (5.0/1.0)
	* nbumps2 > 0.5
		* seismic = a
			* seismoacoustic = c: 0 (5.0/2.0)
			* seismoacoustic != c
				* seismoacoustic = a
					* shift = W: 0 (113.0/16.0)
					* shift != W
						* gpuls <= 42.5: 0 (5.0)
						* gpuls > 42.5: 0 (5.0/2.0)
				* seismoacoustic != a
					* shift = W
						* ghazard = a: 0 (67.0/13.0)
						* ghazard != a
							* maxenergy <= 2500.0: 0 (5.0/1.0)
							* maxenergy > 2500.0: 0 (6.0)
					* shift != W: 0 (7.0/1.0)
		* seismic != a
			* genergy <= 189465.0
				* seismoacoustic = a
					* nbumps4 <= 0.5: 0 (50.0/8.0)
					* nbumps4 > 0.5
						* nbumps2 <= 1.5
							* maxenergy <= 25000.0: 0 (5.0/2.0)
							* maxenergy > 25000.0: 0 (6.0)
						* nbumps2 > 1.5: 0 (12.0)
				* seismoacoustic != a
					* maxenergy <= 2500.0
						* ghazard = b: 0 (5.0/1.0)
						* ghazard != b: 0 (12.0)
					* maxenergy > 2500.0
						* nbumps4 <= 0.5: 0 (21.0/9.0)
						* nbumps4 > 0.5
							* nbumps3 <= 1.5: 0 (6.0/1.0)
							* nbumps3 > 1.5
								* nbumps2 <= 2.5: 0 (8.0/3.0)
								* nbumps2 > 2.5: 0 (5.0/1.0)
			* genergy > 189465.0
				* seismoacoustic = a
					* nbumps2 <= 1.5
						* genergy <= 412485.0: 1 (6.0/1.0)
						* genergy > 412485.0: 0 (9.0/2.0)
					* nbumps2 > 1.5
						* nbumps <= 3.5: 1 (6.0/1.0)
						* nbumps > 3.5: 1 (8.0/4.0)
				* seismoacoustic != a
					* maxenergy <= 3500.0: 1 (6.0/2.0)
					* maxenergy > 3500.0: 0 (9.0/1.0)


## SimpleCart Decision Tree

* nbumps < 1.5
	* gpuls < 1357.0
		* genergy < 17665.0
			* energy < 650.0
				* gpuls < 219.5: 0(426.0/6.0)
				* gpuls >= 219.5: 0(303.0/0.0)
			* energy >= 650.0
				* genergy < 3450.0: 0(3.0/2.0)
				* genergy >= 3450.0: 0(78.0/3.0)
		* genergy >= 17665.0: 0(917.0/38.0)
	* gpuls >= 1357.0
		* nbumps3 < 0.5: 0(50.0/6.0)
		* nbumps3 >= 0.5
			* genergy < 422215.0: 1(6.0/1.0)
			* genergy >= 422215.0
				* genergy < 1186935.0: 0(5.0/4.0)
				* genergy >= 1186935.0: 0(4.0/0.0)
* nbumps >= 1.5
	* gpuls < 740.5: 0(231.0/35.0)
	* gpuls >= 740.5
		* nbumps2 < 0.5: 0(46.0/5.0)
		* nbumps2 >= 0.5
			* gdenergy < -29.5
				* maxenergy < 1500.0: 0(4.0/1.0)
				* maxenergy >= 1500.0: 1(12.0/4.0)
			* gdenergy >= -29.5: 0(98.0/35.0)



# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |
| nbumps > 1.5 and genergy > 304420.0 and genergy <= 1522825.0 and gdenergy > 46.5 and gpuls > 2134.0 | 1 | 0.002757 |
| gpuls <= 1139.5 and gdenergy = all and gdpuls = all and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps3 <= 0.5 and nbumps5 = all and nbumps89 = all and energy <= 650 and maxenergy <= 450 | 1 | 0.000461 |
| nbumps <= 1.5 and gpuls > 1357.0 and nbumps3 > 0.5 and genergy <= 422215.0 | 1 | 0.002365 |
| nbumps > 1.5 and genergy > 304420.0 and genergy <= 1522825.0 and gdenergy <= 46.5 and gpuls <= 2364.5 and genergy > 359935.0 and nbumps4 <= 1.5 and gpuls <= 2211.5 and gpuls <= 2078.5 and genergy <= 614380.0 and gdenergy > -29.5 and nbumps2 > 0.5 and genergy > 508290.0 | 1 | 0.001228 |
| gpuls <= 1139.5 and gdenergy = all and gdpuls = all and nbumps > 1.5 and nbumps2 > 0.5 and nbumps3 <= 0.5 and nbumps5 = all and nbumps89 = all and energy <= 650 and maxenergy > 450 | 1 | 0.000461 |
| gpuls > 1139.5 and gdenergy = all and gdpuls = all and nbumps > 1.5 and nbumps2 > 0.5 and nbumps3 <= 0.5 and nbumps5 = all and nbumps89 = all and energy > 650 and maxenergy <= 450 | 1 | 0.000461 |
| nbumps > 1.5 and genergy > 304420.0 and genergy <= 1522825.0 and gdenergy <= 46.5 and gpuls <= 2364.5 and genergy > 359935.0 and nbumps4 <= 1.5 and gpuls <= 2211.5 and gpuls <= 2078.5 and genergy <= 614380.0 and gdenergy <= -29.5 | 1 | 0.002941 |
| nbumps > 1.5 and genergy > 304420.0 and genergy <= 1522825.0 and gdenergy <= 46.5 and gpuls <= 2364.5 and genergy > 359935.0 and nbumps4 <= 1.5 and gpuls > 2211.5 | 1 | 0.001473 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1357.0 and seismoacoustic != c and ghazard != c and shift != W and nbumps <= 0.5 | 0 | 0.801926 |
| nbumps <= 1.5 and gpuls <= 1357.0 and seismoacoustic != c and ghazard != c and nbumps4 <= 0.5 and nbumps2 > 0.5 and seismoacoustic = a and energy <= 650.0 | 0 | 0.372431 |
| nbumps <= 1.5 and gpuls <= 1357.0 and seismoacoustic != c and ghazard != c and nbumps4 <= 0.5 and seismic = a and ghazard = a and seismoacoustic = a and nbumps2 <= 0.5 | 0 | 0.661257 |
| nbumps <= 1.5 and gpuls <= 1210.0 and seismoacoustic != c and ghazard != c and nbumps3 <= 0.5 and shift = W and nbumps <= 0.5 and ghazard = a and seismoacoustic = a and gdpuls <= 100.0 | 0 | 0.491156 |
| nbumps <= 1.5 and seismoacoustic != c and seismoacoustic != a and ghazard != c and nbumps2 <= 0.5 and seismic = a | 0 | 0.580410 |
| ghazard != c and nbumps <= 1.5 and seismoacoustic != c and gpuls <= 1207.0 and seismoacoustic != a and nbumps > 0.5 | 0 | 0.409771 |
| ghazard != c and nbumps2 <= 0.5 and shift = W and nbumps4 <= 0.5 and seismoacoustic != c and seismoacoustic != a and maxenergy <= 3500.0 and nbumps <= 0.5 and ghazard = a | 0 | 0.331081 |
| ghazard != c and nbumps2 <= 0.5 and nbumps4 > 0.5 | 0 | 0.265971 |
| ghazard = c | 0 | 0.157303 |
| shift != W and nbumps2 <= 0.5 | 0 | 0.086133 |
| seismic = a and seismoacoustic != c and shift = W | 0 | 0.581473 |
| genergy <= 117615.0 and nbumps3 <= 1.5 and seismic != a and seismoacoustic != c and shift = W and nbumps4 <= 0.5 and nbumps3 > 0.5 and seismoacoustic = a | 0 | 0.220417 |
| genergy <= 114745.0 and nbumps3 <= 1.5 and nbumps4 <= 0.5 and nbumps3 <= 0.5 and seismoacoustic != c and seismoacoustic != a and ghazard != a and maxenergy <= 550.0 and genergy > 21325.0 | 0 | 0.143069 |
| seismoacoustic = c and seismic != a | 0 | 0.056604 |
| genergy <= 113610.0 and seismoacoustic != c and nbumps3 <= 2.5 and ghazard = a and seismic = a and seismoacoustic = a and gdenergy > -43.0 | 0 | 0.019565 |
| genergy <= 113610.0 and seismoacoustic != c and nbumps3 <= 2.5 and ghazard = a and seismic != a and seismoacoustic = a | 0 | 0.234834 |
| seismoacoustic != a and ghazard = a and maxenergy <= 2500.0 | 0 | 0.075815 |
| ghazard != a and nbumps3 <= 1.5 and seismoacoustic != a and seismoacoustic = b and shift = W and nbumps3 <= 0.5 and maxenergy <= 25000.0 and energy <= 1000.0 and genergy <= 20610.0 | 0 | 0.039263 |
| seismoacoustic = c and nbumps3 <= 0.5 | 0 | 0.032258 |
| seismoacoustic != c and seismic != a and nbumps4 > 0.5 and seismoacoustic != a and ghazard = a | 0 | 0.084429 |
| seismoacoustic != c and seismic = a and gdpuls > -39.5 | 1 | 0.500000 |
| seismoacoustic != c and seismic != a and ghazard != a and seismoacoustic != a and nbumps3 <= 1.5 and nbumps > 1.0 and nbumps3 > 0.5 | 0 | 0.042517 |
| seismoacoustic != c and seismic != a and nbumps4 <= 1.5 and seismoacoustic != a and nbumps2 > 0.5 and genergy <= 39915.0 | 1 | 0.105263 |
| seismoacoustic != c and seismic != a and nbumps3 > 1.5 and ghazard = a and seismoacoustic != a | 0 | 0.062888 |
| shift = W and seismic != a and seismoacoustic != a and nbumps2 > 0.5 and nbumps <= 4.0 and gdenergy <= 116.0 | 1 | 0.115839 |
| seismoacoustic != c and seismic != a and seismoacoustic != a and nbumps3 > 0.5 | 1 | 0.150278 |
| seismoacoustic != c and seismic != a and gdenergy <= 73.0 and seismoacoustic = a and nbumps > 3.5 | 0 | 0.133333 |
| shift = W and gdenergy <= 74.5 and seismoacoustic = a and nbumps2 <= 1.5 and genergy <= 422215.0 and gdpuls > -27.5 | 1 | 0.435771 |
| seismoacoustic != c and nbumps2 <= 1.5 and seismic != a and seismoacoustic = a and nbumps <= 2.5 | 0 | 0.168666 |
| shift = W and gdenergy <= 88.5 and seismoacoustic = a and nbumps > 2.5 and genergy > 356465.0 | 1 | 0.421053 |
| shift = W and nbumps4 <= 0.5 and gdenergy <= 88.5 | 1 | 0.685598 |
|  | 0 | 0.392857 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

gpuls|gdenergy|gdpuls|nbumps|nbumps2|nbumps3|nbumps5|nbumps89|energy|maxenergy|class
---|---|---|---|---|---|---|---|---|---|---
(-inf-1139.5]|all|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|(650-inf)|(450-inf)|0
(1139.5-inf)|all|all|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|(650-inf)|(450-inf)|0
(1139.5-inf)|all|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|(650-inf)|(450-inf)|0
(-inf-1139.5]|all|all|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|(650-inf)|(450-inf)|0
(1139.5-inf)|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|(650-inf)|(450-inf)|0
(-inf-1139.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|(650-inf)|(450-inf)|0
(1139.5-inf)|all|all|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|(650-inf)|(450-inf)|0
(-inf-1139.5]|all|all|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|(650-inf)|(450-inf)|0
(1139.5-inf)|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|(650-inf)|(450-inf)|0
(-inf-1139.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|(650-inf)|(450-inf)|0
(1139.5-inf)|all|all|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|(650-inf)|(450-inf)|0
(1139.5-inf)|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|(650-inf)|(450-inf)|0
(-inf-1139.5]|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|(650-inf)|(450-inf)|0
(-inf-1139.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|(-inf-650]|(450-inf)|1
(1139.5-inf)|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|(650-inf)|(-inf-450]|1
(-inf-1139.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|(650-inf)|(-inf-450]|0
(1139.5-inf)|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|(-inf-650]|(450-inf)|0
(-inf-1139.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|(-inf-650]|(450-inf)|0
(1139.5-inf)|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|(-inf-650]|(-inf-450]|1
(-inf-1139.5]|all|all|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|(-inf-650]|(-inf-450]|0
(1139.5-inf)|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|(-inf-650]|(-inf-450]|0
(-inf-1139.5]|all|all|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|(-inf-650]|(-inf-450]|0
(-inf-1139.5]|all|all|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-650]|(-inf-450]|1
(1139.5-inf)|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-650]|(-inf-450]|0
(-inf-1139.5]|all|all|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|(-inf-650]|(-inf-450]|0

## JRip

Decision list:

rules | predicted class
---|---
=> class=0 (2320.0/150.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5 AND gpuls <= 1357.0 AND seismoacoustic != c AND ghazard != c AND shift != W AND nbumps <= 0.5|0 (619.0/6.0)
nbumps <= 1.5 AND gpuls <= 1357.0 AND seismoacoustic != c AND ghazard != c AND nbumps4 <= 0.5 AND nbumps2 > 0.5 AND seismoacoustic = a AND energy <= 650.0|0 (91.0/1.0)
nbumps <= 1.5 AND gpuls <= 1357.0 AND seismoacoustic != c AND ghazard != c AND nbumps4 <= 0.5 AND seismic = a AND ghazard = a AND seismoacoustic = a AND nbumps2 <= 0.5|0 (314.0/9.0)
nbumps <= 1.5 AND gpuls <= 1210.0 AND seismoacoustic != c AND ghazard != c AND nbumps3 <= 0.5 AND shift = W AND nbumps <= 0.5 AND ghazard = a AND seismoacoustic = a AND gdpuls <= 100.0|0 (155.0/3.0)
nbumps <= 1.5 AND seismoacoustic != c AND seismoacoustic != a AND ghazard != c AND nbumps2 <= 0.5 AND seismic = a|0 (229.0/11.0)
ghazard != c AND nbumps <= 1.5 AND seismoacoustic != c AND gpuls <= 1207.0 AND seismoacoustic != a AND nbumps > 0.5|0 (107.0)
ghazard != c AND nbumps2 <= 0.5 AND shift = W AND nbumps4 <= 0.5 AND seismoacoustic != c AND seismoacoustic != a AND maxenergy <= 3500.0 AND nbumps <= 0.5 AND ghazard = a|0 (90.0/6.0)
ghazard != c AND nbumps2 <= 0.5 AND nbumps4 > 0.5|0 (61.0/3.0)
ghazard = c|0 (28.0)
shift != W AND nbumps2 <= 0.5|0 (21.0)
seismic = a AND seismoacoustic != c AND shift = W|0 (278.0/39.0)
genergy <= 117615.0 AND nbumps3 <= 1.5 AND seismic != a AND seismoacoustic != c AND shift = W AND nbumps4 <= 0.5 AND nbumps3 > 0.5 AND seismoacoustic = a|0 (50.0/4.0)
genergy <= 114745.0 AND nbumps3 <= 1.5 AND nbumps4 <= 0.5 AND nbumps3 <= 0.5 AND seismoacoustic != c AND seismoacoustic != a AND ghazard != a AND maxenergy <= 550.0 AND genergy > 21325.0|0 (26.0)
seismoacoustic = c AND seismic != a|0 (9.0)
genergy <= 113610.0 AND seismoacoustic != c AND nbumps3 <= 2.5 AND ghazard = a AND seismic = a AND seismoacoustic = a AND gdenergy > -43.0|0 (9.0)
genergy <= 113610.0 AND seismoacoustic != c AND nbumps3 <= 2.5 AND ghazard = a AND seismic != a AND seismoacoustic = a|0 (67.0/9.0)
seismoacoustic != a AND ghazard = a AND maxenergy <= 2500.0|0 (22.0)
ghazard != a AND nbumps3 <= 1.5 AND seismoacoustic != a AND seismoacoustic = b AND shift = W AND nbumps3 <= 0.5 AND maxenergy <= 25000.0 AND energy <= 1000.0 AND genergy <= 20610.0|0 (8.0/1.0)
seismoacoustic = c AND nbumps3 <= 0.5|0 (5.0)
seismoacoustic != c AND seismic != a AND nbumps4 > 0.5 AND seismoacoustic != a AND ghazard = a|0 (21.0/4.0)
seismoacoustic != c AND seismic = a AND gdpuls > -39.5|1 (4.0)
seismoacoustic != c AND seismic != a AND ghazard != a AND seismoacoustic != a AND nbumps3 <= 1.5 AND nbumps > 1.0 AND nbumps3 > 0.5|0 (6.0/1.0)
seismoacoustic != c AND seismic != a AND nbumps4 <= 1.5 AND seismoacoustic != a AND nbumps2 > 0.5 AND genergy <= 39915.0|1 (5.0)
seismoacoustic != c AND seismic != a AND nbumps3 > 1.5 AND ghazard = a AND seismoacoustic != a|0 (11.0/2.0)
shift = W AND seismic != a AND seismoacoustic != a AND nbumps2 > 0.5 AND nbumps <= 4.0 AND gdenergy <= 116.0|1 (8.0/2.0)
seismoacoustic != c AND seismic != a AND seismoacoustic != a AND nbumps3 > 0.5|1 (4.0)
seismoacoustic != c AND seismic != a AND gdenergy <= 73.0 AND seismoacoustic = a AND nbumps > 3.5|0 (23.0/7.0)
shift = W AND gdenergy <= 74.5 AND seismoacoustic = a AND nbumps2 <= 1.5 AND genergy <= 422215.0 AND gdpuls > -27.5|1 (13.0/1.0)
seismoacoustic != c AND nbumps2 <= 1.5 AND seismic != a AND seismoacoustic = a AND nbumps <= 2.5|0 (16.0/1.0)
shift = W AND gdenergy <= 88.5 AND seismoacoustic = a AND nbumps > 2.5 AND genergy > 356465.0|1 (5.0)
shift = W AND nbumps4 <= 0.5 AND gdenergy <= 88.5|1 (8.0/1.0)
|0 (7.0)


## J48 Decision Tree

* nbumps <= 1.5
	* gpuls <= 1357.0: 0 (1774.0/47.0)
	* gpuls > 1357.0
		* nbumps3 <= 0.5: 0 (56.0/6.0)
		* nbumps3 > 0.5
			* genergy <= 422215.0: 1 (7.0/1.0)
			* genergy > 422215.0: 0 (13.0/4.0)
* nbumps > 1.5
	* genergy <= 304420.0: 0 (374.0/58.0)
	* genergy > 304420.0
		* genergy <= 1522825.0
			* gdenergy <= 46.5
				* gpuls <= 2364.5
					* genergy <= 359935.0: 0 (5.0)
					* genergy > 359935.0
						* nbumps4 <= 1.5
							* gpuls <= 2211.5
								* gpuls <= 2078.5
									* genergy <= 614380.0
										* gdenergy <= -29.5: 1 (10.0/2.0)
										* gdenergy > -29.5
											* nbumps2 <= 0.5: 0 (5.0)
											* nbumps2 > 0.5
												* genergy <= 508290.0: 0 (8.0/3.0)
												* genergy > 508290.0: 1 (6.0/2.0)
									* genergy > 614380.0: 0 (21.0/3.0)
								* gpuls > 2078.5: 0 (7.0)
							* gpuls > 2211.5: 1 (5.0/1.0)
						* nbumps4 > 1.5: 0 (5.0)
				* gpuls > 2364.5: 0 (7.0)
			* gdenergy > 46.5
				* gpuls <= 2134.0: 0 (5.0/1.0)
				* gpuls > 2134.0: 1 (6.0)
		* genergy > 1522825.0: 0 (6.0)



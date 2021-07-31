# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.522648 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = f and bkxcr = f and skrxp = f and mulch = t | nowin | 0.011206 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = t and wkovl = f and bkxcr = f and bkona = f and mulch = f and simpl = t | nowin | 0.001199 |
| bxqsq = f and hdchk = f and rimmx = f and wkna8 = f and wknck = t | nowin | 0.222659 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = f and bkblk = f and katri = n | nowin | 0.045269 |
| bxqsq = t and hdchk = f and rimmx = f and wkna8 = f and wknck = f | nowin | 0.186110 |
| bxqsq = f and hdchk = f and rimmx = f and wkna8 = t and wknck = f | nowin | 0.060206 |
| bxqsq = t and hdchk = f and rimmx = f and wkna8 = t and wknck = f | nowin | 0.009247 |
| rimmx = f and bxqsq = t | nowin | 0.307479 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri = b and bkblk = f | nowin | 0.010554 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = t | nowin | 0.064306 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = t | nowin | 0.004645 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri = n and rxmsq = t and qxmsq = f | nowin | 0.009901 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = f and bkblk = f and katri = b | nowin | 0.009247 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx = f and bxqsq = t | nowin | 0.307479 |
| stlmt = f and rimmx = t | won | 0.427177 |
| wknck = t and r2ar8 = t and wkovl = t | nowin | 0.211165 |
| wkna8 = t and bknwy = f | nowin | 0.086223 |
| wknck = f and hdchk = f and wkna8 = f and bkxbq = t | won | 0.604730 |
| wknck = t and bkxcr = t | nowin | 0.193370 |
| mulch = t and katri = n | nowin | 0.096907 |
| bkon8 = f and bkona = t and bkxbq = t | nowin | 0.051948 |
| bkon8 = f and wkpos = t and skrxp = f and katri = n and rxmsq = f and thrsk = f | won | 0.574300 |
| katri = w | won | 0.329502 |
| qxmsq = f and bkblk = f and thrsk = f and bknwy = f and skrxp = f and wkcti = f | nowin | 0.466981 |
| bkon8 = f and wknck = t and qxmsq = f and wkcti = f | nowin | 0.143939 |
| bkon8 = f and wkpos = t and katri = n | won | 0.452677 |
| bkon8 = f and bkblk = t and hdchk = f and cntxt = t | won | 0.452677 |
| r2ar8 = t | nowin | 0.680851 |
| reskr = f and simpl = f | won | 0.288095 |
| reskr = t | nowin | 0.750000 |
| bknwy = f and bkblk = f and reskd = f and skach = f | won | 0.200000 |
|  | nowin | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| bxqsq = t and rimmx = f | nowin | 0.307479 |
| wknck = t and rimmx = f and r2ar8 = t and wkovl = t | nowin | 0.148211 |
| wkpos = f and cntxt = f and rimmx = f and bknwy = f | nowin | 0.057789 |
| wknck = t and rimmx = f and bkxcr = t | nowin | 0.065421 |
| wkpos = f and katri = n and bkxbq = f and wkcti = f and bkblk = f and bxqsq = f | nowin | 0.034749 |
| mulch = t and rimmx = f and katri = n | nowin | 0.030381 |
| katri = b and bkblk = f and bkxbq = f | nowin | 0.020248 |
| skrxp = t and rimmx = f and wknck = t | nowin | 0.020888 |
| wkpos = f and bkxbq = f and katri = n and rimmx = f and bkblk = f and reskr = t | nowin | 0.010554 |
| rxmsq = t and qxmsq = f and bkxbq = f and bxqsq = f and r2ar8 = t | nowin | 0.011206 |
| wkovl = f and wknck = t and rimmx = f and bkona = t | nowin | 0.006623 |
| wkpos = f and hdchk = t | nowin | 0.003984 |
| wkpos = f and cntxt = f and rimmx = f and simpl = t | nowin | 0.002660 |
| thrsk = t and rimmx = f and wknck = t | nowin | 0.004645 |
|  | won | 0.985545 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

bxqsq|hdchk|rimmx|wkna8|wknck|class
---|---|---|---|---|---
t|f|t|t|t|won
t|f|f|t|t|nowin
f|f|t|f|t|won
t|f|t|f|t|won
f|f|t|t|f|won
f|t|f|t|f|nowin
t|f|f|f|t|nowin
f|f|f|f|t|nowin
t|f|f|t|f|nowin
f|f|f|t|f|nowin
t|f|t|f|f|won
f|f|t|f|f|won
f|t|f|f|f|nowin
f|f|f|f|f|won
t|f|f|f|f|nowin

## JRip

Decision list:

rules | predicted class
---|---
(bxqsq = t) and (rimmx = f)|nowin (666.0/0.0)
(wknck = t) and (rimmx = f) and (r2ar8 = t) and (wkovl = t)|nowin (261.0/0.0)
(wkpos = f) and (cntxt = f) and (rimmx = f) and (bknwy = f)|nowin (92.0/0.0)
(wknck = t) and (rimmx = f) and (bkxcr = t)|nowin (105.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (wkcti = f) and (bkblk = f) and (bxqsq = f)|nowin (54.0/0.0)
(mulch = t) and (rimmx = f) and (katri = n)|nowin (47.0/0.0)
(katri = b) and (bkblk = f) and (bkxbq = f)|nowin (31.0/0.0)
(skrxp = t) and (rimmx = f) and (wknck = t)|nowin (32.0/0.0)
(wkpos = f) and (bkxbq = f) and (katri = n) and (rimmx = f) and (bkblk = f) and (reskr = t)|nowin (16.0/0.0)
(rxmsq = t) and (qxmsq = f) and (bkxbq = f) and (bxqsq = f) and (r2ar8 = t)|nowin (17.0/0.0)
(wkovl = f) and (wknck = t) and (rimmx = f) and (bkona = t)|nowin (10.0/0.0)
(wkpos = f) and (hdchk = t)|nowin (6.0/0.0)
(wkpos = f) and (cntxt = f) and (rimmx = f) and (simpl = t)|nowin (4.0/0.0)
(thrsk = t) and (rimmx = f) and (wknck = t)|nowin (7.0/0.0)
|won (1522.0/22.0)


## PART

Decision list:

rules | predicted class
---|---
rimmx = f AND bxqsq = t|nowin (666.0)
stlmt = f AND rimmx = t|won (525.0)
wknck = t AND r2ar8 = t AND wkovl = t|nowin (261.0)
wkna8 = t AND bknwy = f|nowin (92.0)
wknck = f AND hdchk = f AND wkna8 = f AND bkxbq = t|won (537.0)
wknck = t AND bkxcr = t|nowin (105.0)
mulch = t AND katri = n|nowin (47.0)
bkon8 = f AND bkona = t AND bkxbq = t|nowin (24.0)
bkon8 = f AND wkpos = t AND skrxp = f AND katri = n AND rxmsq = f AND thrsk = f|won (242.0/3.0)
katri = w|won (86.0)
qxmsq = f AND bkblk = f AND thrsk = f AND bknwy = f AND skrxp = f AND wkcti = f|nowin (96.0)
bkon8 = f AND wknck = t AND qxmsq = f AND wkcti = f|nowin (19.0)
bkon8 = f AND wkpos = t AND katri = n|won (51.0/2.0)
bkon8 = f AND bkblk = t AND hdchk = f AND cntxt = t|won (51.0/2.0)
r2ar8 = t|nowin (28.0)
reskr = f AND simpl = f|won (12.0/1.0)
reskr = t|nowin (12.0)
bknwy = f AND bkblk = f AND reskd = f AND skach = f|won (5.0/1.0)
|nowin (11.0)


## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* hdchk = f
					* bkxbq = f
						* wkpos = t
							* katri = n
								* rxmsq = f: won (231.0/2.0)
								* rxmsq = t
									* qxmsq = f: nowin (15.0)
									* qxmsq = t: won (25.0)
							* katri = w: won (43.0)
							* katri = b
								* bkblk = f: nowin (16.0)
								* bkblk = t: won (10.0/1.0)
						* wkpos = f
							* bkblk = f
								* katri = n: nowin (77.0/3.0)
								* katri = w: won (38.0)
								* katri = b: nowin (14.0)
							* bkblk = t: won (46.0/1.0)
					* bkxbq = t: won (537.0)
				* hdchk = t: nowin (7.0)
			* wkna8 = t: nowin (109.0/3.0)
		* wknck = t
			* r2ar8 = t
				* wkovl = t: nowin (261.0)
				* wkovl = f
					* bkxcr = f
						* bkona = f
							* mulch = f
								* simpl = f: won (6.0)
								* simpl = t: nowin (5.0/2.0)
							* mulch = t: nowin (10.0)
						* bkona = t: nowin (19.0)
					* bkxcr = t: nowin (35.0)
			* r2ar8 = f
				* bkxcr = f
					* skrxp = f
						* mulch = f
							* thrsk = f
								* reskr = f
									* bknwy = f
										* skewr = t
											* bkxbq = f: won (11.0/2.0)
											* bkxbq = t
												* simpl = f: won (6.0/1.0)
												* simpl = t: nowin (8.0/3.0)
										* skewr = f: won (14.0/2.0)
									* bknwy = t: won (6.0)
								* reskr = t: nowin (5.0)
							* thrsk = t: nowin (7.0)
						* mulch = t: nowin (17.0)
					* skrxp = t: nowin (31.0)
				* bkxcr = t: nowin (70.0)
	* bxqsq = t: nowin (666.0)
* rimmx = t: won (525.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* r2ar8=(t): nowin(572.0/8.0)
		* r2ar8!=(t)
			* bkxcr=(t): nowin(107.0/0.0)
			* bkxcr!=(t)
				* skrxp=(t): nowin(32.0/0.0)
				* skrxp!=(t)
					* bxqsq=(t): nowin(27.0/0.0)
					* bxqsq!=(t)
						* mulch=(t): nowin(17.0/0.0)
						* mulch!=(t)
							* thrsk=(t): nowin(7.0/0.0)
							* thrsk!=(t)
								* reskr=(t): nowin(5.0/0.0)
								* reskr!=(t): won(35.0/10.0)
	* wknck!=(t)
		* bxqsq=(t): nowin(357.0/0.0)
		* bxqsq!=(t)
			* wkna8=(t): nowin(106.0/3.0)
			* wkna8!=(t)
				* wkpos=(f)
					* bkxbq=(f)
							* katri=(n)|(b)
							* bkblk=(f): nowin(88.0/3.0)
							* bkblk!=(f)
								* hdchk=(t): nowin(7.0/0.0)
								* hdchk!=(t): won(40.0/1.0)
							* katri!=(n)|(b): won(43.0/0.0)
					* bkxbq!=(f): won(107.0/0.0)
				* wkpos!=(f)
					* rxmsq=(t)
						* qxmsq=(f)
							* bkxbq=(f): nowin(16.0/0.0)
							* bkxbq!=(f): won(9.0/0.0)
						* qxmsq!=(f): won(30.0/1.0)
					* rxmsq!=(t)
						* katri=(b)
							* bkblk=(f)
								* bkxbq=(f): nowin(15.0/0.0)
								* bkxbq!=(f): won(6.0/0.0)
							* bkblk!=(f): won(42.0/0.0)
						* katri!=(b): won(649.0/2.0)
* rimmx!=(f): won(525.0/0.0)



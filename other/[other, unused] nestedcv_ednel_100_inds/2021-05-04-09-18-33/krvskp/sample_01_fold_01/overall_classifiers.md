# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.522648 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = t and katri = n and rxmsq = t and qxmsq = f | nowin | 0.008592 |
| rimmx = f and bxqsq = f and wknck = t | nowin | 0.225146 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = t and katri = b | nowin | 0.010162 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = f and katri = b and bkblk = f | nowin | 0.009247 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = f and katri = n and bkblk = f | nowin | 0.041063 |
| rimmx = f and bxqsq = t | nowin | 0.308118 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = t | nowin | 0.064306 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx = f and bxqsq = t | nowin | 0.308118 |
| stlmt = f and rimmx = t | won | 0.428339 |
| wknck = t and r2ar8 = t and wkovl = t | nowin | 0.213247 |
| wkna8 = f and wknck = f and hdchk = f and bkxbq = t | won | 0.552147 |
| wkna8 = f and wknck = t and bkxcr = t | nowin | 0.200737 |
| wkna8 = t | nowin | 0.191960 |
| mulch = t | nowin | 0.082649 |
| bkon8 = f and bkona = t and bkxbq = t | nowin | 0.054466 |
| bkon8 = f and wkpos = t and skrxp = f and katri = n and rxmsq = f and thrsk = f | won | 0.591323 |
| katri = w | won | 0.369478 |
| bkblk = t and bkspr = f and wkovl = t | won | 0.147440 |
| qxmsq = f and bkblk = f and reskr = t | nowin | 0.310924 |
| qxmsq = t | won | 0.166934 |
| bkblk = t and bkspr = t | won | 0.104478 |
| bknwy = f and katri = n and simpl = f | nowin | 0.527096 |
| bknwy = f and katri = b | nowin | 0.426667 |
| simpl = t and bkon8 = f and wkpos = f and r2ar8 = f and reskd = f | won | 0.126233 |
| simpl = t and wkpos = t and wknck = f | won | 0.315559 |
| simpl = t | nowin | 0.686804 |
|  | won | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| bxqsq = t and rimmx = f | nowin | 0.308118 |
| wknck = t and rimmx = f and r2ar8 = t and wkovl = t | nowin | 0.149660 |
| wkpos = f and cntxt = f and rimmx = f and bknwy = f | nowin | 0.060150 |
| wknck = t and rimmx = f and bkxcr = t | nowin | 0.067744 |
| wkpos = f and katri = n and bkxbq = f and rimmx = f and bkblk = f and wkcti = f | nowin | 0.031008 |
| mulch = t and rimmx = f and katri = n | nowin | 0.027237 |
| katri = b and bkblk = f and bkxbq = f | nowin | 0.022164 |
| skrxp = t and rimmx = f and wknck = t | nowin | 0.020248 |
| wkpos = f and katri = n and bkxbq = f and rimmx = f and bkblk = f and reskr = t | nowin | 0.010554 |
| rxmsq = t and qxmsq = f and bkxbq = f and r2ar8 = t and bxqsq = f | nowin | 0.010554 |
| wkovl = f and wknck = t and rimmx = f and bkona = t | nowin | 0.007280 |
| wkpos = f and hdchk = t | nowin | 0.003984 |
| thrsk = t and rimmx = f and wknck = t | nowin | 0.004645 |
| wkpos = f and katri = n and bkxbq = f and wknck = f and bkblk = f and r2ar8 = t | nowin | 0.002660 |
| wkna8 = t and rimmx = f and r2ar8 = t | nowin | 0.001332 |
| bkon8 = t and wknck = t and rimmx = f | nowin | 0.002660 |
| thrsk = t and wkna8 = t | nowin | 0.001332 |
|  | won | 0.993377 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(bxqsq = t) and (rimmx = f)|nowin (668.0/0.0)
(wknck = t) and (rimmx = f) and (r2ar8 = t) and (wkovl = t)|nowin (264.0/0.0)
(wkpos = f) and (cntxt = f) and (rimmx = f) and (bknwy = f)|nowin (96.0/0.0)
(wknck = t) and (rimmx = f) and (bkxcr = t)|nowin (109.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (rimmx = f) and (bkblk = f) and (wkcti = f)|nowin (48.0/0.0)
(mulch = t) and (rimmx = f) and (katri = n)|nowin (42.0/0.0)
(katri = b) and (bkblk = f) and (bkxbq = f)|nowin (34.0/0.0)
(skrxp = t) and (rimmx = f) and (wknck = t)|nowin (31.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (rimmx = f) and (bkblk = f) and (reskr = t)|nowin (16.0/0.0)
(rxmsq = t) and (qxmsq = f) and (bkxbq = f) and (r2ar8 = t) and (bxqsq = f)|nowin (16.0/0.0)
(wkovl = f) and (wknck = t) and (rimmx = f) and (bkona = t)|nowin (11.0/0.0)
(wkpos = f) and (hdchk = t)|nowin (6.0/0.0)
(thrsk = t) and (rimmx = f) and (wknck = t)|nowin (7.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (wknck = f) and (bkblk = f) and (r2ar8 = t)|nowin (4.0/0.0)
(wkna8 = t) and (rimmx = f) and (r2ar8 = t)|nowin (2.0/0.0)
(bkon8 = t) and (wknck = t) and (rimmx = f)|nowin (4.0/0.0)
(thrsk = t) and (wkna8 = t)|nowin (2.0/0.0)
|won (1510.0/10.0)


## PART

Decision list:

rules | predicted class
---|---
rimmx = f AND bxqsq = t|nowin (668.0)
stlmt = f AND rimmx = t|won (526.0)
wknck = t AND r2ar8 = t AND wkovl = t|nowin (264.0)
wkna8 = f AND wknck = f AND hdchk = f AND bkxbq = t|won (540.0)
wkna8 = f AND wknck = t AND bkxcr = t|nowin (109.0)
wkna8 = t|nowin (109.0/3.0)
mulch = t|nowin (43.0/2.0)
bkon8 = f AND bkona = t AND bkxbq = t|nowin (25.0)
bkon8 = f AND wkpos = t AND skrxp = f AND katri = n AND rxmsq = f AND thrsk = f|won (235.0/4.0)
katri = w|won (90.0)
bkblk = t AND bkspr = f AND wkovl = t|won (31.0/2.0)
qxmsq = f AND bkblk = f AND reskr = t|nowin (37.0)
qxmsq = t|won (26.0/1.0)
bkblk = t AND bkspr = t|won (14.0)
bknwy = f AND katri = n AND simpl = f|nowin (53.0/5.0)
bknwy = f AND katri = b|nowin (29.0)
simpl = t AND bkon8 = f AND wkpos = f AND r2ar8 = f AND reskd = f|won (13.0/5.0)
simpl = t AND wkpos = t AND wknck = f|won (22.0/3.0)
simpl = t|nowin (29.0/1.0)
|won (7.0)


## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* bkxbq = f
					* wkpos = t
						* katri = n
							* rxmsq = f: won (200.0/1.0)
							* rxmsq = t
								* qxmsq = f: nowin (12.0)
								* qxmsq = t: won (21.0)
						* katri = w: won (39.0)
						* katri = b: nowin (21.0/4.0)
					* wkpos = f
						* katri = n
							* bkblk = f: nowin (64.0/3.0)
							* bkblk = t: won (22.0/4.0)
						* katri = w: won (43.0)
						* katri = b
							* bkblk = f: nowin (9.0)
							* bkblk = t: won (20.0/4.0)
				* bkxbq = t: won (459.0)
			* wkna8 = t: nowin (94.0/2.0)
		* wknck = t: nowin (436.0/31.0)
	* bxqsq = t: nowin (569.0)
* rimmx = t: won (451.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* r2ar8=(t): nowin(568.0/6.0)
		* r2ar8!=(t)
			* bkxcr=(t): nowin(106.0/0.0)
			* bkxcr!=(t)
				* skrxp=(t): nowin(30.0/0.0)
				* skrxp!=(t)
					* bxqsq=(t): nowin(26.0/0.0)
					* bxqsq!=(t)
						* mulch=(t): nowin(16.0/0.0)
						* mulch!=(t)
							* thrsk=(t): nowin(7.0/0.0)
							* thrsk!=(t)
								* bkona=(t): nowin(6.0/0.0)
								* bkona!=(t)
									* reskr=(t): nowin(6.0/0.0)
									* reskr!=(t)
										* blxwp=(t): nowin(3.0/0.0)
										* blxwp!=(t)
											* bkon8=(t): nowin(2.0/0.0)
											* bkon8!=(t): won(33.0/0.0)
	* wknck!=(t)
		* bxqsq=(t): nowin(369.0/0.0)
		* bxqsq!=(t)
			* wkna8=(t): nowin(106.0/3.0)
			* wkna8!=(t)
				* bkxbq=(f)
					* wkpos=(f)
							* katri=(n)|(b)
							* bkblk=(f): nowin(82.0/4.0)
							* bkblk!=(f)
								* hdchk=(t): nowin(7.0/0.0)
								* hdchk!=(t): won(41.0/1.0)
							* katri!=(n)|(b): won(48.0/0.0)
					* wkpos!=(f)
						* katri=(b)
							* bkblk=(f): nowin(19.0/0.0)
							* bkblk!=(f): won(6.0/1.0)
						* katri!=(b)
							* rxmsq=(t)
								* qxmsq=(f): nowin(13.0/0.0)
								* qxmsq!=(f): won(24.0/0.0)
							* rxmsq!=(t): won(269.0/2.0)
				* bkxbq!=(f): won(540.0/0.0)
* rimmx!=(f): won(526.0/0.0)



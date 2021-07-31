# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.522648 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = f and katri = b and bkblk = f | nowin | 0.009247 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = t and katri = n and rxmsq = t and qxmsq = f | nowin | 0.009247 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = f and bkxcr = f and skrxp = f and mulch = t | nowin | 0.011206 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = t | nowin | 0.066053 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = t and katri = b and bkblk = f | nowin | 0.011858 |
| rimmx = f and bxqsq = t | nowin | 0.308118 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = f and bkxcr = t | nowin | 0.044586 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = f and bkxcr = f and skrxp = t | nowin | 0.018325 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = f and katri = n and bkblk = f | nowin | 0.044109 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = t | nowin | 0.175431 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx = f and bxqsq = t | nowin | 0.308118 |
| stlmt = f and rimmx = t | won | 0.427406 |
| wknck = t and r2ar8 = t and wkovl = t | nowin | 0.210356 |
| wkna8 = f and wknck = f and hdchk = f and bkxbq = t | won | 0.548519 |
| wkna8 = t | nowin | 0.194643 |
| wknck = t and bkxcr = t | nowin | 0.193015 |
| mulch = f and bkon8 = f and bkona = f and wkpos = t and skrxp = f and katri = n and rxmsq = f | won | 0.515556 |
| katri = n and qxmsq = f and bkblk = f and mulch = f and reskr = f and wkcti = f | nowin | 0.305594 |
| mulch = f and bkon8 = f and katri = w | won | 0.382222 |
| qxmsq = f and bkblk = f | nowin | 0.503663 |
| bkxbq = f | won | 0.823388 |
|  | nowin | 0.833333 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| bxqsq = t and rimmx = f | nowin | 0.308118 |
| wknck = t and rimmx = f and r2ar8 = t and wkovl = t | nowin | 0.147727 |
| wkpos = f and cntxt = f and rimmx = f and bknwy = f | nowin | 0.061327 |
| wknck = t and rimmx = f and bkxcr = t | nowin | 0.065421 |
| wkpos = f and katri = n and bkxbq = f and wkcti = f and bkblk = f and bxqsq = f | nowin | 0.033505 |
| mulch = t and rimmx = f and katri = n | nowin | 0.030381 |
| katri = b and bkblk = f and bkxbq = f | nowin | 0.020888 |
| skrxp = t and rimmx = f and wknck = t | nowin | 0.018967 |
| wkpos = f and katri = n and bkxbq = f and rimmx = f and bkblk = f and reskr = t | nowin | 0.011206 |
| rxmsq = t and qxmsq = f and bkxbq = f and r2ar8 = t and bxqsq = f | nowin | 0.011206 |
| wkovl = f and wknck = t and rimmx = f and bkona = t | nowin | 0.006623 |
|  | won | 0.977199 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(bxqsq = t) and (rimmx = f)|nowin (668.0/0.0)
(wknck = t) and (rimmx = f) and (r2ar8 = t) and (wkovl = t)|nowin (260.0/0.0)
(wkpos = f) and (cntxt = f) and (rimmx = f) and (bknwy = f)|nowin (98.0/0.0)
(wknck = t) and (rimmx = f) and (bkxcr = t)|nowin (105.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (wkcti = f) and (bkblk = f) and (bxqsq = f)|nowin (52.0/0.0)
(mulch = t) and (rimmx = f) and (katri = n)|nowin (47.0/0.0)
(katri = b) and (bkblk = f) and (bkxbq = f)|nowin (32.0/0.0)
(skrxp = t) and (rimmx = f) and (wknck = t)|nowin (29.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (rimmx = f) and (bkblk = f) and (reskr = t)|nowin (17.0/0.0)
(rxmsq = t) and (qxmsq = f) and (bkxbq = f) and (r2ar8 = t) and (bxqsq = f)|nowin (17.0/0.0)
(wkovl = f) and (wknck = t) and (rimmx = f) and (bkona = t)|nowin (10.0/0.0)
|won (1535.0/35.0)


## PART

Decision list:

rules | predicted class
---|---
rimmx = f AND bxqsq = t|nowin (554.0)
stlmt = f AND rimmx = t|won (447.0)
wknck = t AND r2ar8 = t AND wkovl = t|nowin (224.0)
wkna8 = f AND wknck = f AND hdchk = f AND bkxbq = t|won (438.0)
wkna8 = t|nowin (90.0/3.0)
wknck = t AND bkxcr = t|nowin (88.0)
mulch = f AND bkon8 = f AND bkona = f AND wkpos = t AND skrxp = f AND katri = n AND rxmsq = f|won (214.0/7.0)
katri = n AND qxmsq = f AND bkblk = f AND mulch = f AND reskr = f AND wkcti = f|nowin (76.0/7.0)
mulch = f AND bkon8 = f AND katri = w|won (69.0)
qxmsq = f AND bkblk = f|nowin (108.0/12.0)
bkxbq = f|won (76.0/9.0)
|nowin (8.0)


## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* bkxbq = f
					* wkpos = t
						* katri = n
							* rxmsq = f: won (231.0/2.0)
							* rxmsq = t
								* qxmsq = f: nowin (14.0)
								* qxmsq = t: won (25.0)
						* katri = w: won (43.0)
						* katri = b
							* bkblk = f: nowin (18.0)
							* bkblk = t: won (10.0/1.0)
					* wkpos = f
						* katri = n
							* bkblk = f: nowin (77.0/4.0)
							* bkblk = t: won (25.0/4.0)
						* katri = w: won (45.0)
						* katri = b
							* bkblk = f: nowin (14.0)
							* bkblk = t: won (25.0/4.0)
				* bkxbq = t: won (537.0)
			* wkna8 = t: nowin (112.0/3.0)
		* wknck = t
			* r2ar8 = t: nowin (331.0/6.0)
			* r2ar8 = f
				* bkxcr = f
					* skrxp = f
						* mulch = f: won (56.0/23.0)
						* mulch = t: nowin (17.0)
					* skrxp = t: nowin (28.0)
				* bkxcr = t: nowin (70.0)
	* bxqsq = t: nowin (668.0)
* rimmx = t: won (524.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* r2ar8=(t): nowin(571.0/6.0)
		* r2ar8!=(t)
			* bkxcr=(t): nowin(105.0/0.0)
			* bkxcr!=(t)
				* skrxp=(t): nowin(30.0/0.0)
				* skrxp!=(t)
					* bxqsq=(t): nowin(25.0/0.0)
					* bxqsq!=(t)
						* mulch=(t): nowin(17.0/0.0)
						* mulch!=(t)
							* thrsk=(t): nowin(7.0/0.0)
							* thrsk!=(t)
								* bkona=(t): nowin(6.0/0.0)
								* bkona!=(t)
									* reskr=(t): nowin(5.0/0.0)
									* reskr!=(t): won(33.0/5.0)
	* wknck!=(t)
		* bxqsq=(t): nowin(360.0/0.0)
		* bxqsq!=(t)
			* wkna8=(t)
				* bknwy=(f): nowin(98.0/0.0)
				* bknwy!=(f)
					* r2ar8=(t): nowin(7.0/0.0)
					* r2ar8!=(t)
						* simpl=(t): nowin(4.0/0.0)
						* simpl!=(t): won(3.0/0.0)
			* wkna8!=(t)
				* wkpos=(f)
					* bkxbq=(f)
							* katri=(n)|(b)
							* bkblk=(f): nowin(87.0/4.0)
							* bkblk!=(f)
								* hdchk=(t): nowin(7.0/0.0)
								* hdchk!=(t): won(42.0/1.0)
							* katri!=(n)|(b): won(45.0/0.0)
					* bkxbq!=(f): won(106.0/0.0)
				* wkpos!=(f)
					* rxmsq=(t)
						* qxmsq=(f)
							* bkxbq=(f): nowin(16.0/0.0)
							* bkxbq!=(f): won(10.0/0.0)
						* qxmsq!=(f): won(31.0/1.0)
					* rxmsq!=(t)
						* katri=(b)
							* bkblk=(f)
								* bkxbq=(f): nowin(16.0/0.0)
								* bkxbq!=(f): won(6.0/0.0)
							* bkblk!=(f): won(42.0/0.0)
						* katri!=(b): won(648.0/2.0)
* rimmx!=(f): won(524.0/0.0)



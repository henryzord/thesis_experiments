# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.521921 |
| rimmx = f and bxqsq = t | nowin | 0.308437 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = t | nowin | 0.004645 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = f and bkblk = f and katri = n | nowin | 0.041063 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = t | nowin | 0.178591 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = f and bkxcr = f and skrxp = t | nowin | 0.018325 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = f and bkxcr = f and skrxp = f and mulch = f and thrsk = f and reskr = t | nowin | 0.003984 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = f and bkxcr = f and skrxp = f and mulch = t | nowin | 0.010554 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = f and bkxcr = t | nowin | 0.046408 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri = n and rxmsq = t and qxmsq = f | nowin | 0.008592 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = f and bkxcr = f and skrxp = f and mulch = f and thrsk = f and reskr = f and bkona = t | nowin | 0.003984 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = t | nowin | 0.064889 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = f and bkblk = f and katri = b | nowin | 0.009247 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = f and bkxcr = f and skrxp = f and mulch = f and thrsk = t | nowin | 0.004645 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri = b and bkblk = f | nowin | 0.012508 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx = f and bxqsq != f | nowin | 0.308437 |
| stlmt = f and rimmx != f | won | 0.426829 |
| wknck != f and r2ar8 = t and wkovl = t | nowin | 0.214343 |
| wkna8 != f and bknwy = f | nowin | 0.090485 |
| wknck = f and hdchk = f and bkxbq != f | won | 0.612245 |
| wknck != f and bkxcr != f | nowin | 0.200368 |
| mulch != f and katri != w | nowin | 0.097510 |
| bkon8 = f and bkona != f and bkxbq != f | nowin | 0.054348 |
| bkon8 = f and katri != w and wkpos = t and katri = n and skrxp = f and rxmsq = f and thrsk = f and wknck = f and dsopp = f | won | 0.519403 |
| katri = w | won | 0.363636 |
| qxmsq != f and dwipd = l | won | 0.090395 |
| bkon8 = f and bkblk != f and hdchk = f and cntxt != f and katri = n | won | 0.125000 |
| reskr != f | nowin | 0.221557 |
| bkon8 = f and bkxbq != f and blxwp = f | won | 0.162162 |
| bkxbq = f and dsopp != f and bkxcr = f and wkpos = t and thrsk = f and dwipd = l | won | 0.138889 |
| qxmsq != f and cntxt = f | won | 0.031250 |
| bkxbq = f and bkblk != f and hdchk = f and cntxt != f and dwipd != l | won | 0.094891 |
| qxmsq != f and blxwp = f and simpl = f | won | 0.004032 |
| qxmsq = f and bkxbq = f and rxmsq != f and r2ar8 = t | nowin | 0.235955 |
| qxmsq = f and bkxbq = f and dsopp != f and skewr != t | won | 0.072072 |
| qxmsq = f and bkxbq = f and bkblk = f and katri = n and wkpos != t and wkcti = f | nowin | 0.333333 |
| rxmsq = f and bkxbq = f and hdchk = f and bkblk != f and cntxt != f and thrsk = f | won | 0.120482 |
| rxmsq = f and bkxbq = f and katri != n and bkblk = f | nowin | 0.350649 |
| bkxbq = f and hdchk = f and rxmsq = f and dwipd != l and dsopp = f | won | 0.163636 |
| rxmsq = f and bkxbq = f and skrxp != f and wkovl != t | nowin | 0.226415 |
| bkxbq != f | nowin | 0.145833 |
| hdchk = f and rxmsq != f | won | 0.160714 |
| hdchk = f and reskd != f and bknwy = f | nowin | 0.037037 |
| hdchk = f and reskd = f and blxwp = f and bkspr = f and r2ar8 != t and thrsk = f and wknck != f | won | 0.342105 |
| wknck != f | nowin | 0.266667 |
| hdchk = f and skewr = t and wkpos = t and wtoeg = n | won | 0.266304 |
| skewr = t and r2ar8 = t and thrsk = f | nowin | 0.423077 |
| simpl = f | won | 0.454545 |
| wkna8 = f and skewr = t and thrsk != f and r2ar8 = t | won | 0.166667 |
| wkna8 = f and thrsk != f | won | 0.494949 |
| bknwy = f | nowin | 0.800000 |
|  | nowin | 0.666667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| bxqsq = t and rimmx = f | nowin | 0.308437 |
| wknck = t and rimmx = f and r2ar8 = t and wkovl = t | nowin | 0.150623 |
| wkpos = f and cntxt = f and rimmx = f and bknwy = f | nowin | 0.060739 |
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
| wkna8 = t and rimmx = f | nowin | 0.001523 |
| bkon8 = t and wknck = t and rimmx = f | nowin | 0.002660 |
|  | won | 0.993377 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(bxqsq = t) and (rimmx = f)|nowin (669.0/0.0)
(wknck = t) and (rimmx = f) and (r2ar8 = t) and (wkovl = t)|nowin (266.0/0.0)
(wkpos = f) and (cntxt = f) and (rimmx = f) and (bknwy = f)|nowin (97.0/0.0)
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
(wkna8 = t) and (rimmx = f)|nowin (7.0/3.0)
(bkon8 = t) and (wknck = t) and (rimmx = f)|nowin (4.0/0.0)
|won (1507.0/10.0)


## PART

Decision list:

rules | predicted class
---|---
rimmx = f AND bxqsq != f|nowin (669.0)
stlmt = f AND rimmx != f|won (525.0)
wknck != f AND r2ar8 = t AND wkovl = t|nowin (266.0)
wkna8 != f AND bknwy = f|nowin (97.0)
wknck = f AND hdchk = f AND bkxbq != f|won (540.0)
wknck != f AND bkxcr != f|nowin (109.0)
mulch != f AND katri != w|nowin (47.0)
bkon8 = f AND bkona != f AND bkxbq != f|nowin (25.0)
bkon8 = f AND katri != w AND wkpos = t AND katri = n AND skrxp = f AND rxmsq = f AND thrsk = f AND wknck = f AND dsopp = f|won (174.0)
katri = w|won (92.0)
qxmsq != f AND dwipd = l|won (16.0)
bkon8 = f AND bkblk != f AND hdchk = f AND cntxt != f AND katri = n|won (23.0)
reskr != f|nowin (37.0)
bkon8 = f AND bkxbq != f AND blxwp = f|won (24.0)
bkxbq = f AND dsopp != f AND bkxcr = f AND wkpos = t AND thrsk = f AND dwipd = l|won (20.0)
qxmsq != f AND cntxt = f|won (4.0)
bkxbq = f AND bkblk != f AND hdchk = f AND cntxt != f AND dwipd != l|won (13.0)
qxmsq != f AND blxwp = f AND simpl = f|won (2.0/1.0)
qxmsq = f AND bkxbq = f AND rxmsq != f AND r2ar8 = t|nowin (21.0)
qxmsq = f AND bkxbq = f AND dsopp != f AND skewr != t|won (8.0)
qxmsq = f AND bkxbq = f AND bkblk = f AND katri = n AND wkpos != t AND wkcti = f|nowin (30.0)
rxmsq = f AND bkxbq = f AND hdchk = f AND bkblk != f AND cntxt != f AND thrsk = f|won (10.0)
rxmsq = f AND bkxbq = f AND katri != n AND bkblk = f|nowin (27.0)
bkxbq = f AND hdchk = f AND rxmsq = f AND dwipd != l AND dsopp = f|won (9.0)
rxmsq = f AND bkxbq = f AND skrxp != f AND wkovl != t|nowin (12.0)
bkxbq != f|nowin (7.0)
hdchk = f AND rxmsq != f|won (6.0)
hdchk = f AND reskd != f AND bknwy = f|nowin (3.0/1.0)
hdchk = f AND reskd = f AND blxwp = f AND bkspr = f AND r2ar8 != t AND thrsk = f AND wknck != f|won (13.0)
wknck != f|nowin (8.0)
hdchk = f AND skewr = t AND wkpos = t AND wtoeg = n|won (6.0)
skewr = t AND r2ar8 = t AND thrsk = f|nowin (10.0)
simpl = f|won (5.0)
wkna8 = f AND skewr = t AND thrsk != f AND r2ar8 = t|won (4.0/2.0)
wkna8 = f AND thrsk != f|won (7.0)
bknwy = f|nowin (3.0/1.0)
|nowin (2.0)


## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* hdchk = f
					* bkxbq = f
						* wkpos = t
							* katri = n
								* rxmsq = f: won (201.0/1.0)
								* rxmsq = t
									* qxmsq = f: nowin (12.0)
									* qxmsq = t: won (23.0)
							* katri = w: won (37.0)
							* katri = b
								* bkblk = f: nowin (19.0)
								* bkblk = t: won (6.0/1.0)
						* wkpos = f
							* bkblk = f
								* katri = n: nowin (69.0/4.0)
								* katri = w: won (36.0)
								* katri = b: nowin (13.0)
							* bkblk = t: won (37.0/1.0)
					* bkxbq = t: won (470.0)
				* hdchk = t: nowin (7.0)
			* wkna8 = t: nowin (96.0/3.0)
		* wknck = t
			* r2ar8 = t: nowin (296.0/6.0)
			* r2ar8 = f
				* bkxcr = f
					* skrxp = f
						* mulch = f
							* thrsk = f
								* reskr = f
									* bkona = f: won (37.0/5.0)
									* bkona = t: nowin (3.0)
								* reskr = t: nowin (5.0)
							* thrsk = t: nowin (6.0)
						* mulch = t: nowin (16.0)
					* skrxp = t: nowin (26.0)
				* bkxcr = t: nowin (62.0)
	* bxqsq = t: nowin (577.0)
* rimmx = t: won (461.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* r2ar8=(t)
			* wkovl=(t): nowin(459.0/0.0)
			* wkovl!=(t)
				* bkxcr=(t): nowin(78.0/0.0)
				* bkxcr!=(t)
					* bkona=(t): nowin(17.0/0.0)
					* bkona!=(t)
						* bkspr=(f)
							* mulch=(t): nowin(11.0/0.0)
							* mulch!=(t)
								* bxqsq=(t): nowin(3.0/0.0)
								* bxqsq!=(t)
									* bkon8=(t): nowin(2.0/0.0)
									* bkon8!=(t): won(3.0/0.0)
						* bkspr!=(f): won(3.0/0.0)
		* r2ar8!=(t)
			* bkxcr=(t): nowin(107.0/0.0)
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
											* bkon8!=(t): won(34.0/0.0)
	* wknck!=(t)
		* bxqsq=(t): nowin(369.0/0.0)
		* bxqsq!=(t)
			* wkna8=(t)
				* bknwy=(f): nowin(97.0/0.0)
				* bknwy!=(f)
					* r2ar8=(t): nowin(7.0/0.0)
					* r2ar8!=(t)
						* simpl=(t): nowin(3.0/0.0)
						* simpl!=(t): won(3.0/0.0)
			* wkna8!=(t)
				* bkxbq=(f)
					* wkpos=(f)
							* katri=(n)|(b)
							* bkblk=(f)
								* r2ar8=(t): nowin(60.0/0.0)
								* r2ar8!=(t)
									* reskr=(t): nowin(13.0/0.0)
									* reskr!=(t)
										* wkcti=(f): nowin(6.0/0.0)
										* wkcti!=(f)
											* dsopp=(f): nowin(3.0/2.0)
											* dsopp!=(f): won(2.0/0.0)
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
							* rxmsq!=(t)
								* dsopp=(t)
									* thrsk=(t): won(2.0/1.0)
									* thrsk!=(t)
										* dwipd=(g)
											* skewr=(t): won(3.0/1.0)
											* skewr!=(t): won(7.0/0.0)
										* dwipd!=(g): won(22.0/0.0)
								* dsopp!=(t): won(235.0/0.0)
				* bkxbq!=(f): won(540.0/0.0)
* rimmx!=(f): won(525.0/0.0)



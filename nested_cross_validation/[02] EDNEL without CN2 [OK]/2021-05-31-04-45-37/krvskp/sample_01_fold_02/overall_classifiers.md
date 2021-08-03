# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.522648 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = t | nowin | 0.004645 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri = n and rxmsq = t and qxmsq = f | nowin | 0.008592 |
| rimmx = f and bxqsq = f and wknck = t and bknwy = f and wkovl = f and bkxcr = f and skrxp = f and mulch = f and bkona = t | nowin | 0.007937 |
| rimmx = f and bxqsq = f and wknck = t and bknwy = t | nowin | 0.006836 |
| rimmx = f and bxqsq = f and wknck = t and bknwy = f and wkovl = t | nowin | 0.152063 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = f and bkblk = f and katri = n | nowin | 0.042836 |
| rimmx = f and bxqsq = f and wknck = t and bknwy = f and wkovl = f and bkxcr = f and skrxp = f and mulch = t | nowin | 0.011858 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = f and bkblk = f and katri = b | nowin | 0.009247 |
| rimmx = f and bxqsq = t | nowin | 0.307799 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri = b and bkblk = f | nowin | 0.011858 |
| rimmx = f and bxqsq = f and wknck = t and bknwy = f and wkovl = f and bkxcr = f and skrxp = t | nowin | 0.024073 |
| rimmx = f and bxqsq = f and wknck = t and bknwy = f and wkovl = f and bkxcr = t | nowin | 0.067164 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = t | nowin | 0.066633 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx = f and bxqsq = t | nowin | 0.307799 |
| stlmt = f and rimmx = t | won | 0.427524 |
| wknck = t and wkovl = t and r2ar8 = t | nowin | 0.212439 |
| wkna8 = t and bknwy = f | nowin | 0.092179 |
| wknck = f and hdchk = f and bkxbq = t | won | 0.612940 |
| wknck = t and bkxcr = t | nowin | 0.198895 |
| mulch = t and wknck = t | nowin | 0.080338 |
| hdchk = f and bkona = t and bkxbq = t | nowin | 0.050218 |
| hdchk = f and wkpos = t and skrxp = f and katri = n and rxmsq = f and wknck = f and dsopp = f | won | 0.526171 |
| hdchk = f and katri = w | won | 0.353383 |
| qxmsq = t and dwipd = l | won | 0.085106 |
| hdchk = f and bkblk = t and wkovl = t | won | 0.160976 |
| reskr = t | nowin | 0.262774 |
| bkxcr = t and wkpos = f | nowin | 0.129310 |
| bkon8 = f and bkxbq = t and wtoeg = n | won | 0.123188 |
| dsopp = t and wkpos = t and wtoeg = n | won | 0.135714 |
| bkon8 = f and bkxbq = f and bkblk = f and katri = b | nowin | 0.315789 |
| bkon8 = f and thrsk = t and skrxp = f | nowin | 0.106838 |
| thrsk = f and bkon8 = f and wtoeg = t and bkspr = f and dsopp = t | won | 0.116071 |
| thrsk = f and bkon8 = f and r2ar8 = t and wtoeg = n and dwipd = g and wkpos = f | nowin | 0.193500 |
| thrsk = f and bkon8 = f and r2ar8 = f and bkblk = f and simpl = f | won | 0.129630 |
| thrsk = f and bkon8 = f and katri = n and wtoeg = n and dwipd = l and r2ar8 = t | nowin | 0.296296 |
| thrsk = f and bkon8 = f and bkspr = f and cntxt = t | won | 0.126834 |
| thrsk = f and bkon8 = f and bkspr = t | won | 0.213472 |
| skrxp = f and wkpos = t | nowin | 0.538947 |
| simpl = t | nowin | 0.595238 |
|  | nowin | 0.520000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| bxqsq = t and rimmx = f | nowin | 0.307799 |
| wknck = t and rimmx = f and wkovl = t and bknwy = f | nowin | 0.152063 |
| wkpos = f and cntxt = f and rimmx = f and bknwy = f | nowin | 0.061914 |
| wknck = t and rimmx = f and bkxcr = t | nowin | 0.067164 |
| wkpos = f and katri = n and bkxbq = f and wkcti = f and bkblk = f and bkon8 = f | nowin | 0.030381 |
| mulch = t and rimmx = f and katri = n | nowin | 0.029754 |
| katri = b and bkblk = f and bkxbq = f | nowin | 0.021526 |
| skrxp = t and rimmx = f and wknck = t | nowin | 0.017682 |
| wkpos = f and katri = n and bkxbq = f and rimmx = f and bkblk = f and r2ar8 = t | nowin | 0.009247 |
|  | won | 0.961538 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(bxqsq = t) and (rimmx = f)|nowin (667.0/0.0)
(wknck = t) and (rimmx = f) and (wkovl = t) and (bknwy = f)|nowin (269.0/0.0)
(wkpos = f) and (cntxt = f) and (rimmx = f) and (bknwy = f)|nowin (99.0/0.0)
(wknck = t) and (rimmx = f) and (bkxcr = t)|nowin (108.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (wkcti = f) and (bkblk = f) and (bkon8 = f)|nowin (47.0/0.0)
(mulch = t) and (rimmx = f) and (katri = n)|nowin (46.0/0.0)
(katri = b) and (bkblk = f) and (bkxbq = f)|nowin (33.0/0.0)
(skrxp = t) and (rimmx = f) and (wknck = t)|nowin (27.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (rimmx = f) and (bkblk = f) and (r2ar8 = t)|nowin (14.0/0.0)
|won (1560.0/60.0)


## PART

Decision list:

rules | predicted class
---|---
rimmx = f AND bxqsq = t|nowin (667.0)
stlmt = f AND rimmx = t|won (525.0)
wknck = t AND wkovl = t AND r2ar8 = t|nowin (263.0)
wkna8 = t AND bknwy = f|nowin (99.0)
wknck = f AND hdchk = f AND bkxbq = t|won (540.0)
wknck = t AND bkxcr = t|nowin (108.0)
mulch = t AND wknck = t|nowin (38.0)
hdchk = f AND bkona = t AND bkxbq = t|nowin (23.0)
hdchk = f AND wkpos = t AND skrxp = f AND katri = n AND rxmsq = f AND wknck = f AND dsopp = f|won (191.0)
hdchk = f AND katri = w|won (94.0)
qxmsq = t AND dwipd = l|won (16.0)
hdchk = f AND bkblk = t AND wkovl = t|won (33.0)
reskr = t|nowin (36.0)
bkxcr = t AND wkpos = f|nowin (15.0)
bkon8 = f AND bkxbq = t AND wtoeg = n|won (17.0)
dsopp = t AND wkpos = t AND wtoeg = n|won (19.0)
bkon8 = f AND bkxbq = f AND bkblk = f AND katri = b|nowin (30.0)
bkon8 = f AND thrsk = t AND skrxp = f|nowin (13.0/3.0)
thrsk = f AND bkon8 = f AND wtoeg = t AND bkspr = f AND dsopp = t|won (16.0/3.0)
thrsk = f AND bkon8 = f AND r2ar8 = t AND wtoeg = n AND dwipd = g AND wkpos = f|nowin (21.0/5.0)
thrsk = f AND bkon8 = f AND r2ar8 = f AND bkblk = f AND simpl = f|won (19.0/5.0)
thrsk = f AND bkon8 = f AND katri = n AND wtoeg = n AND dwipd = l AND r2ar8 = t|nowin (16.0)
thrsk = f AND bkon8 = f AND bkspr = f AND cntxt = t|won (15.0/5.0)
thrsk = f AND bkon8 = f AND bkspr = t|won (13.0/2.0)
skrxp = f AND wkpos = t|nowin (19.0/8.0)
simpl = t|nowin (14.0)
|nowin (10.0/1.0)


## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* hdchk = f
					* bkxbq = f
						* wkpos = t
							* katri = n
								* rxmsq = f: won (180.0/2.0)
								* rxmsq = t
									* qxmsq = f: nowin (10.0)
									* qxmsq = t: won (16.0)
							* katri = w: won (34.0)
							* katri = b
								* bkblk = f: nowin (13.0)
								* bkblk = t: won (6.0)
						* wkpos = f
							* bkblk = f
								* katri = n: nowin (62.0/2.0)
								* katri = w: won (34.0)
								* katri = b: nowin (11.0)
							* bkblk = t: won (42.0)
					* bkxbq = t: won (430.0)
				* hdchk = t: nowin (6.0)
			* wkna8 = t: nowin (86.0/2.0)
		* wknck = t
			* bknwy = f
				* wkovl = t: nowin (214.0)
				* wkovl = f
					* bkxcr = f
						* skrxp = f
							* mulch = f
								* bkona = f: won (35.0/9.0)
								* bkona = t: nowin (9.0)
							* mulch = t: nowin (15.0)
						* skrxp = t: nowin (33.0)
					* bkxcr = t: nowin (94.0)
			* bknwy = t: nowin (15.0/5.0)
	* bxqsq = t: nowin (526.0)
* rimmx = t: won (425.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* wkovl=(t): nowin(480.0/2.0)
		* wkovl!=(t)
			* bkxcr=(t): nowin(179.0/0.0)
			* bkxcr!=(t)
				* skrxp=(t): nowin(39.0/0.0)
				* skrxp!=(t)
					* mulch=(t): nowin(25.0/0.0)
					* mulch!=(t)
						* bxqsq=(t): nowin(21.0/0.0)
						* bxqsq!=(t)
							* bkona=(t): nowin(12.0/0.0)
							* bkona!=(t): won(36.0/13.0)
	* wknck!=(t)
		* bxqsq=(t): nowin(367.0/0.0)
		* bxqsq!=(t)
			* wkna8=(t): nowin(110.0/3.0)
			* wkna8!=(t)
				* wkpos=(f)
					* bkxbq=(f)
							* katri=(n)|(b)
							* bkblk=(f): nowin(84.0/3.0)
							* bkblk!=(f): won(41.0/7.0)
							* katri!=(n)|(b): won(49.0/0.0)
					* bkxbq!=(f): won(107.0/0.0)
				* wkpos!=(f)
					* katri=(b)
						* bkblk=(f): nowin(18.0/7.0)
						* bkblk!=(f): won(44.0/0.0)
					* katri!=(b)
						* rxmsq=(t)
							* qxmsq=(f): nowin(13.0/8.0)
							* qxmsq!=(f): won(25.0/0.0)
						* rxmsq!=(t): won(650.0/2.0)
* rimmx!=(f): won(525.0/0.0)



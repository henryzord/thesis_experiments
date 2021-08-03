# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.521921 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = f and katri = n and bkblk = f | nowin | 0.044109 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = f and skrxp = t | nowin | 0.025974 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = t | nowin | 0.064838 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = t and katri = b | nowin | 0.007952 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = t | nowin | 0.064889 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = f and skrxp = f and mulch = t | nowin | 0.015102 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = f and skrxp = f and mulch = f and bkona = f and bkon8 = t | nowin | 0.002660 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = t | nowin | 0.155889 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = f and skrxp = f and mulch = f and bkona = t | nowin | 0.007280 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = t and katri = n and rxmsq = t and qxmsq = f | nowin | 0.008592 |
| rimmx = f and bxqsq = t | nowin | 0.308118 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = f and skrxp = f and mulch = f and bkona = f and bkon8 = f and thrsk = t | nowin | 0.003322 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = f and katri = b | nowin | 0.006344 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| bxqsq = t and rimmx = f | nowin | 0.308118 |
| wknck = t and rimmx = f and wkovl = t and bknwy = f | nowin | 0.154453 |
| wkpos = f and cntxt = f and rimmx = f and bknwy = f | nowin | 0.058380 |
| wknck = t and rimmx = f and bkxcr = t | nowin | 0.064838 |
| wkpos = f and katri = n and bkxbq = f and wknck = f and bkblk = f and r2ar8 = t | nowin | 0.034127 |
| mulch = t and rimmx = f and katri = n | nowin | 0.027868 |
| katri = b and bkblk = f and bkxbq = f | nowin | 0.020248 |
| wkovl = f and skrxp = t and rimmx = f | nowin | 0.019608 |
| wkpos = f and wkovl = f and katri = n and bkxbq = f and wknck = f and reskr = t | nowin | 0.007937 |
| wkovl = f and wkpos = f and hdchk = t | nowin | 0.004645 |
| rxmsq = t and qxmsq = f and bkxbq = f and dsopp = f and bxqsq = f | nowin | 0.009247 |
| wkovl = f and wknck = t and rimmx = f and bkona = t | nowin | 0.007280 |
| wkpos = f and wkovl = f and katri = n and bkxbq = f and rimmx = f and bkxcr = t | nowin | 0.003322 |
| wkovl = f and wkpos = f and katri = n and simpl = t and bkxbq = f and wknck = f and dsopp = f and bknwy = t | nowin | 0.001332 |
| wkovl = f and wkpos = f and skach = t | nowin | 0.001996 |
| thrsk = t and rimmx = f and wknck = t | nowin | 0.003322 |
| wkpos = f and wkovl = f and rimmx = f and cntxt = f and r2ar8 = t | nowin | 0.001332 |
| wkpos = f and simpl = t and wkovl = f and katri = n and bkxbq = f and wknck = f and wkcti = f | nowin | 0.001332 |
| bkon8 = t and wknck = t and rimmx = f | nowin | 0.002660 |
| wkpos = f and katri = b and cntxt = f and simpl = t | nowin | 0.001332 |
|  | won | 0.994036 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(bxqsq = t) and (rimmx = f)|nowin (668.0/0.0)
(wknck = t) and (rimmx = f) and (wkovl = t) and (bknwy = f)|nowin (274.0/0.0)
(wkpos = f) and (cntxt = f) and (rimmx = f) and (bknwy = f)|nowin (93.0/0.0)
(wknck = t) and (rimmx = f) and (bkxcr = t)|nowin (104.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (wknck = f) and (bkblk = f) and (r2ar8 = t)|nowin (53.0/0.0)
(mulch = t) and (rimmx = f) and (katri = n)|nowin (43.0/0.0)
(katri = b) and (bkblk = f) and (bkxbq = f)|nowin (31.0/0.0)
(wkovl = f) and (skrxp = t) and (rimmx = f)|nowin (30.0/0.0)
(wkpos = f) and (wkovl = f) and (katri = n) and (bkxbq = f) and (wknck = f) and (reskr = t)|nowin (12.0/0.0)
(wkovl = f) and (wkpos = f) and (hdchk = t)|nowin (7.0/0.0)
(rxmsq = t) and (qxmsq = f) and (bkxbq = f) and (dsopp = f) and (bxqsq = f)|nowin (14.0/0.0)
(wkovl = f) and (wknck = t) and (rimmx = f) and (bkona = t)|nowin (11.0/0.0)
(wkpos = f) and (wkovl = f) and (katri = n) and (bkxbq = f) and (rimmx = f) and (bkxcr = t)|nowin (5.0/0.0)
(wkovl = f) and (wkpos = f) and (katri = n) and (simpl = t) and (bkxbq = f) and (wknck = f) and (dsopp = f) and (bknwy = t)|nowin (2.0/0.0)
(wkovl = f) and (wkpos = f) and (skach = t)|nowin (3.0/0.0)
(thrsk = t) and (rimmx = f) and (wknck = t)|nowin (5.0/0.0)
(wkpos = f) and (wkovl = f) and (rimmx = f) and (cntxt = f) and (r2ar8 = t)|nowin (2.0/0.0)
(wkpos = f) and (simpl = t) and (wkovl = f) and (katri = n) and (bkxbq = f) and (wknck = f) and (wkcti = f)|nowin (2.0/0.0)
(bkon8 = t) and (wknck = t) and (rimmx = f)|nowin (4.0/0.0)
(wkpos = f) and (katri = b) and (cntxt = f) and (simpl = t)|nowin (2.0/0.0)
|won (1509.0/9.0)


## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* bkxbq = f
					* wkpos = t
						* katri = n
							* rxmsq = f: won (206.0/2.0)
							* rxmsq = t
								* qxmsq = f: nowin (10.0)
								* qxmsq = t: won (23.0)
						* katri = w: won (37.0)
						* katri = b: nowin (22.0/9.0)
					* wkpos = f
						* katri = n
							* bkblk = f: nowin (65.0/4.0)
							* bkblk = t: won (19.0/2.0)
						* katri = w: won (35.0)
						* katri = b: nowin (29.0/14.0)
				* bkxbq = t: won (479.0)
			* wkna8 = t: nowin (100.0/3.0)
		* wknck = t
			* wkovl = t: nowin (254.0/2.0)
			* wkovl = f
				* bkxcr = f
					* skrxp = f
						* mulch = f
							* bkona = f
								* bkon8 = f
									* thrsk = f: won (44.0/6.0)
									* thrsk = t: nowin (4.0)
								* bkon8 = t: nowin (4.0)
							* bkona = t: nowin (9.0)
						* mulch = t: nowin (20.0)
					* skrxp = t: nowin (35.0)
				* bkxcr = t: nowin (90.0)
	* bxqsq = t: nowin (601.0)
* rimmx = t: won (469.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* r2ar8=(t)
			* wkovl=(t): nowin(460.0/0.0)
			* wkovl!=(t)
				* bkxcr=(t): nowin(84.0/0.0)
				* bkxcr!=(t)
					* bkona=(t): nowin(17.0/0.0)
					* bkona!=(t)
						* bkspr=(f)
							* mulch=(t): nowin(10.0/0.0)
							* mulch!=(t)
								* cntxt=(t): nowin(5.0/0.0)
								* cntxt!=(t)
									* bkon8=(t): nowin(2.0/0.0)
									* bkon8!=(t): won(4.0/0.0)
						* bkspr!=(f): won(4.0/0.0)
		* r2ar8!=(t)
			* bkxcr=(t): nowin(100.0/0.0)
			* bkxcr!=(t)
				* skrxp=(t): nowin(35.0/0.0)
				* skrxp!=(t)
					* bxqsq=(t): nowin(27.0/0.0)
					* bxqsq!=(t)
						* mulch=(t): nowin(14.0/0.0)
						* mulch!=(t)
							* bkona=(t): nowin(6.0/0.0)
							* bkona!=(t)
								* reskr=(t): nowin(6.0/0.0)
								* reskr!=(t)
									* thrsk=(t): nowin(5.0/0.0)
									* thrsk!=(t)
										* blxwp=(t): nowin(3.0/0.0)
										* blxwp!=(t)
											* bkon8=(t): nowin(2.0/0.0)
											* bkon8!=(t)
												* skach=(t): nowin(2.0/0.0)
												* skach!=(t): won(34.0/0.0)
	* wknck!=(t)
		* bxqsq=(t): nowin(362.0/0.0)
		* bxqsq!=(t)
			* wkna8=(t)
				* bknwy=(f): nowin(93.0/0.0)
				* bknwy!=(f)
					* r2ar8=(t): nowin(9.0/0.0)
					* r2ar8!=(t)
						* simpl=(t): nowin(5.0/0.0)
						* simpl!=(t): won(3.0/0.0)
			* wkna8!=(t)
				* wkpos=(f)
					* bkxbq=(f)
							* katri=(n)|(b)
							* bkblk=(f): nowin(86.0/4.0)
							* bkblk!=(f)
								* hdchk=(t): nowin(7.0/0.0)
								* hdchk!=(t): won(36.0/1.0)
							* katri!=(n)|(b): won(43.0/0.0)
					* bkxbq!=(f): won(104.0/0.0)
				* wkpos!=(f)
					* katri=(b)
						* bkxbq=(f)
							* bkblk=(f): nowin(17.0/0.0)
							* bkblk!=(f): won(9.0/1.0)
						* bkxbq!=(f): won(44.0/0.0)
					* katri!=(b)
						* rxmsq=(t)
							* qxmsq=(f)
								* bkxbq=(f): nowin(13.0/0.0)
								* bkxbq!=(f): won(9.0/0.0)
							* qxmsq!=(f): won(28.0/0.0)
						* rxmsq!=(t): won(654.0/2.0)
* rimmx!=(f): won(524.0/0.0)



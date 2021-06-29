# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.522419 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl = t | nowin | 0.152284 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos != t and katri != w and bkblk = f | nowin | 0.049404 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 != f | nowin | 0.065885 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri != b and rxmsq != f and qxmsq = f | nowin | 0.008575 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl != t and bkxcr = f and bkona = f and mulch != f | nowin | 0.011184 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl != t and bkxcr = f and bkona = f and mulch = f and skrxp != f | nowin | 0.011184 |
| rimmx = f and bxqsq != f | nowin | 0.308011 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl != t and bkxcr != f | nowin | 0.067039 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri = b and bkblk = f | nowin | 0.012484 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl != t and bkxcr = f and bkona != f | nowin | 0.022757 |
| rimmx = f and bxqsq = f and wknck != f and bknwy != f | nowin | 0.004720 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk != f | nowin | 0.005295 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| bxqsq = t and rimmx = f | nowin | 0.308011 |
| wknck = t and rimmx = f and wkovl = t and bknwy = f | nowin | 0.152284 |
| wkpos = f and cntxt = f and rimmx = f and bknwy = f | nowin | 0.058860 |
| wknck = t and rimmx = f and bkxcr = t | nowin | 0.067039 |
| wkpos = f and katri = n and bkxbq = f and wknck = f and bkblk = f and r2ar8 = t | nowin | 0.031572 |
| mulch = t and rimmx = f and reskr = f | nowin | 0.028442 |
| katri = b and bkblk = f and bkxbq = f | nowin | 0.020847 |
| wkovl = f and skrxp = t and rimmx = f | nowin | 0.018289 |
| wkovl = f and wkpos = f and katri = n and bkxbq = f and wknck = f and reskr = t | nowin | 0.007921 |
| wkovl = f and wkpos = f and katri = n and rimmx = f and bkxbq = f and bkxcr = t | nowin | 0.003316 |
| wkovl = f and wknck = t and rimmx = f and bkona = t | nowin | 0.007921 |
| rxmsq = t and qxmsq = f and bkxbq = f and wkcti = f and bxqsq = f | nowin | 0.009881 |
| wkpos = f and wkovl = f and rimmx = f and bkxbq = f and katri = n and simpl = t and reskd = t | nowin | 0.002654 |
| wkovl = f and wkpos = f and rimmx = f and cntxt = f | nowin | 0.003316 |
| wkovl = f and wknck = t and rimmx = f and thrsk = t | nowin | 0.003316 |
| wkpos = f and hdchk = t | nowin | 0.002654 |
| wknck = t and rimmx = f and bkon8 = t | nowin | 0.002654 |
| skach = t and bkblk = f | nowin | 0.001992 |
| wkpos = f and katri = n and wkovl = f and rimmx = f and reskr = t and wknck = t | nowin | 0.002654 |
|  | won | 0.995364 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(bxqsq = t) and (rimmx = f)|nowin (669.0/0.0)
(wknck = t) and (rimmx = f) and (wkovl = t) and (bknwy = f)|nowin (270.0/0.0)
(wkpos = f) and (cntxt = f) and (rimmx = f) and (bknwy = f)|nowin (94.0/0.0)
(wknck = t) and (rimmx = f) and (bkxcr = t)|nowin (108.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (wknck = f) and (bkblk = f) and (r2ar8 = t)|nowin (49.0/0.0)
(mulch = t) and (rimmx = f) and (reskr = f)|nowin (44.0/0.0)
(katri = b) and (bkblk = f) and (bkxbq = f)|nowin (32.0/0.0)
(wkovl = f) and (skrxp = t) and (rimmx = f)|nowin (28.0/0.0)
(wkovl = f) and (wkpos = f) and (katri = n) and (bkxbq = f) and (wknck = f) and (reskr = t)|nowin (12.0/0.0)
(wkovl = f) and (wkpos = f) and (katri = n) and (rimmx = f) and (bkxbq = f) and (bkxcr = t)|nowin (5.0/0.0)
(wkovl = f) and (wknck = t) and (rimmx = f) and (bkona = t)|nowin (12.0/0.0)
(rxmsq = t) and (qxmsq = f) and (bkxbq = f) and (wkcti = f) and (bxqsq = f)|nowin (15.0/0.0)
(wkpos = f) and (wkovl = f) and (rimmx = f) and (bkxbq = f) and (katri = n) and (simpl = t) and (reskd = t)|nowin (4.0/0.0)
(wkovl = f) and (wkpos = f) and (rimmx = f) and (cntxt = f)|nowin (5.0/0.0)
(wkovl = f) and (wknck = t) and (rimmx = f) and (thrsk = t)|nowin (5.0/0.0)
(wkpos = f) and (hdchk = t)|nowin (4.0/0.0)
(wknck = t) and (rimmx = f) and (bkon8 = t)|nowin (4.0/0.0)
(skach = t) and (bkblk = f)|nowin (3.0/0.0)
(wkpos = f) and (katri = n) and (wkovl = f) and (rimmx = f) and (reskr = t) and (wknck = t)|nowin (4.0/0.0)
|won (1510.0/7.0)


## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* hdchk = f
					* bkxbq = f
						* wkpos = t
							* katri = b
								* bkblk = f: nowin (11.0)
								* bkblk != f: won (7.0/1.0)
							* katri != b
								* rxmsq = f: won (189.0/2.0)
								* rxmsq != f
									* qxmsq = f: nowin (7.0)
									* qxmsq != f: won (9.0)
						* wkpos != t
							* katri = w: won (30.0)
							* katri != w
								* bkblk = f: nowin (55.0/3.0)
								* bkblk != f: won (25.0)
					* bkxbq != f: won (364.0)
				* hdchk != f: nowin (6.0)
			* wkna8 != f: nowin (73.0/1.0)
		* wknck != f
			* bknwy = f
				* wkovl = t: nowin (175.0)
				* wkovl != t
					* bkxcr = f
						* bkona = f
							* mulch = f
								* skrxp = f: won (26.0/7.0)
								* skrxp != f: nowin (9.0)
							* mulch != f: nowin (10.0)
						* bkona != f: nowin (26.0)
					* bkxcr != f: nowin (65.0)
			* bknwy != f: nowin (13.0/6.0)
	* bxqsq != f: nowin (466.0)
* rimmx != f: won (352.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* r2ar8=(t)
			* wkovl=(t): nowin(457.0/0.0)
			* wkovl!=(t)
				* bkxcr=(t): nowin(79.0/0.0)
				* bkxcr!=(t)
					* bkona=(t): nowin(16.0/0.0)
					* bkona!=(t)
						* bkspr=(f)
							* mulch=(t): nowin(11.0/0.0)
							* mulch!=(t)
								* cntxt=(t): nowin(5.0/0.0)
								* cntxt!=(t)
									* bkon8=(t): nowin(2.0/0.0)
									* bkon8!=(t): won(4.0/0.0)
						* bkspr!=(f): won(4.0/0.0)
		* r2ar8!=(t)
			* bkxcr=(t): nowin(105.0/0.0)
			* bkxcr!=(t)
				* skrxp=(t): nowin(33.0/0.0)
				* skrxp!=(t)
					* bxqsq=(t): nowin(27.0/0.0)
					* bxqsq!=(t)
						* mulch=(t): nowin(14.0/0.0)
						* mulch!=(t)
							* thrsk=(t): nowin(7.0/0.0)
							* thrsk!=(t)
								* bkona=(t): nowin(6.0/0.0)
								* bkona!=(t)
									* reskr=(t): nowin(5.0/0.0)
									* reskr!=(t)
										* blxwp=(t): nowin(3.0/0.0)
										* blxwp!=(t)
											* bkon8=(t): nowin(2.0/0.0)
											* bkon8!=(t)
												* skach=(t): nowin(2.0/0.0)
												* skach!=(t): won(32.0/0.0)
	* wknck!=(t)
		* bxqsq=(t): nowin(368.0/0.0)
		* bxqsq!=(t)
			* wkna8=(t)
				* bknwy=(f): nowin(94.0/0.0)
				* bknwy!=(f)
					* wkovl=(f): nowin(10.0/0.0)
					* wkovl!=(f): nowin(3.0/1.0)
			* wkna8!=(t)
				* wkpos=(f)
					* bkxbq=(f)
							* katri=(n)|(b)
							* bkblk=(f)
								* wkcti=(f): nowin(61.0/0.0)
								* wkcti!=(f)
									* r2ar8=(t): nowin(13.0/0.0)
									* r2ar8!=(t)
										* reskr=(t): nowin(5.0/0.0)
										* reskr!=(t)
											* dsopp=(f): nowin(2.0/1.0)
											* dsopp!=(f): won(2.0/0.0)
							* bkblk!=(f)
								* hdchk=(t): nowin(8.0/0.0)
								* hdchk!=(t): won(40.0/1.0)
							* katri!=(n)|(b): won(46.0/0.0)
					* bkxbq!=(f): won(104.0/0.0)
				* wkpos!=(f)
					* katri=(b)
						* bkxbq=(f)
							* bkblk=(f): nowin(19.0/0.0)
							* bkblk!=(f)
								* rxmsq=(t): won(1.0/1.0)
								* rxmsq!=(t): won(7.0/0.0)
						* bkxbq!=(f): won(42.0/0.0)
					* katri!=(b)
						* rxmsq=(t)
							* qxmsq=(f)
								* bkxbq=(f): nowin(13.0/0.0)
								* bkxbq!=(f): won(7.0/0.0)
							* qxmsq!=(f): won(26.0/0.0)
						* rxmsq!=(t)
							* dsopp=(t)
								* thrsk=(t): won(2.0/1.0)
								* thrsk!=(t)
									* dwipd=(g)
										* wtoeg=(t)
											* skewr=(t): won(1.0/1.0)
											* skewr!=(t): won(3.0/0.0)
										* wtoeg!=(t): won(12.0/0.0)
									* dwipd!=(g): won(43.0/0.0)
							* dsopp!=(t): won(599.0/0.0)
* rimmx!=(f): won(526.0/0.0)



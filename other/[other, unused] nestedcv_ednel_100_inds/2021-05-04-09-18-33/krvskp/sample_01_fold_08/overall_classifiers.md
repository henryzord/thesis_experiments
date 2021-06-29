# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.521739 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = t and katri = n and rxmsq = t and qxmsq = f | nowin | 0.007937 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = t and bknwy = t and simpl = t | nowin | 0.004645 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = f and skrxp = t | nowin | 0.024073 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = f and katri = n and bkblk = f | nowin | 0.041615 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = t and bknwy = t and simpl = f and r2ar8 = t | nowin | 0.003322 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = f and skrxp = f and mulch = f and bkona = f and thrsk = t | nowin | 0.004645 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = t | nowin | 0.068323 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = t and katri = b and bkblk = f | nowin | 0.011858 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = t and bknwy = f | nowin | 0.152542 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = f and skrxp = f and mulch = f and bkona = t | nowin | 0.007280 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = t and bknwy = t and bkxbq = f | nowin | 0.002129 |
| rimmx = f and bxqsq = t | nowin | 0.308437 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = f and skrxp = f and mulch = t | nowin | 0.016393 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = t and bknwy = f | nowin | 0.061327 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = f and katri = b and r2ar8 = t and bkblk = f | nowin | 0.008592 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| bxqsq = t and rimmx = f | nowin | 0.308437 |
| wknck = t and rimmx = f and r2ar8 = t and wkovl = t | nowin | 0.149660 |
| wkpos = f and cntxt = f and rimmx = f and bknwy = f | nowin | 0.061327 |
| wknck = t and rimmx = f and bkxcr = t | nowin | 0.068323 |
| wkpos = f and katri = n and bkxbq = f and rimmx = f and bkblk = f and r2ar8 = t | nowin | 0.033505 |
| wknck = t and rimmx = f and skrxp = t | nowin | 0.027237 |
| mulch = t and rimmx = f and katri = n | nowin | 0.020888 |
| katri = b and bkblk = f and bkxbq = f | nowin | 0.020888 |
| wkpos = f and wkovl = f and rimmx = f and bkxbq = f and katri = n and reskr = t | nowin | 0.007937 |
| rimmx = f and wknck = t and bkona = t | nowin | 0.007280 |
| bkxbq = f and rimmx = f and wkpos = f and wkovl = f and katri = n and simpl = t and reskd = t | nowin | 0.002660 |
| bkxbq = f and rimmx = f and rxmsq = t and qxmsq = f and dsopp = f | nowin | 0.008592 |
| wkpos = f and hdchk = t | nowin | 0.003984 |
| wkpos = f and r2ar8 = f and katri = n and rimmx = f and bkxbq = f and wkcti = f | nowin | 0.003984 |
| wknck = t and rimmx = f and thrsk = t | nowin | 0.003322 |
| wkpos = f and skach = t and bkblk = f | nowin | 0.001996 |
| wkna8 = t and rimmx = f and simpl = t | nowin | 0.001996 |
| wknck = t and rimmx = f and blxwp = t | nowin | 0.002660 |
| bkon8 = t and wknck = t and rimmx = f | nowin | 0.001996 |
|  | won | 0.996016 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(bxqsq = t) and (rimmx = f)|nowin (669.0/0.0)
(wknck = t) and (rimmx = f) and (r2ar8 = t) and (wkovl = t)|nowin (264.0/0.0)
(wkpos = f) and (cntxt = f) and (rimmx = f) and (bknwy = f)|nowin (98.0/0.0)
(wknck = t) and (rimmx = f) and (bkxcr = t)|nowin (110.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (rimmx = f) and (bkblk = f) and (r2ar8 = t)|nowin (52.0/0.0)
(wknck = t) and (rimmx = f) and (skrxp = t)|nowin (42.0/0.0)
(mulch = t) and (rimmx = f) and (katri = n)|nowin (32.0/0.0)
(katri = b) and (bkblk = f) and (bkxbq = f)|nowin (32.0/0.0)
(wkpos = f) and (wkovl = f) and (rimmx = f) and (bkxbq = f) and (katri = n) and (reskr = t)|nowin (12.0/0.0)
(rimmx = f) and (wknck = t) and (bkona = t)|nowin (11.0/0.0)
(bkxbq = f) and (rimmx = f) and (wkpos = f) and (wkovl = f) and (katri = n) and (simpl = t) and (reskd = t)|nowin (4.0/0.0)
(bkxbq = f) and (rimmx = f) and (rxmsq = t) and (qxmsq = f) and (dsopp = f)|nowin (13.0/0.0)
(wkpos = f) and (hdchk = t)|nowin (6.0/0.0)
(wkpos = f) and (r2ar8 = f) and (katri = n) and (rimmx = f) and (bkxbq = f) and (wkcti = f)|nowin (6.0/0.0)
(wknck = t) and (rimmx = f) and (thrsk = t)|nowin (5.0/0.0)
(wkpos = f) and (skach = t) and (bkblk = f)|nowin (3.0/0.0)
(wkna8 = t) and (rimmx = f) and (simpl = t)|nowin (3.0/0.0)
(wknck = t) and (rimmx = f) and (blxwp = t)|nowin (4.0/0.0)
(bkon8 = t) and (wknck = t) and (rimmx = f)|nowin (3.0/0.0)
|won (1506.0/6.0)


## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* bkxbq = f
					* wkpos = t
						* katri = n
							* rxmsq = f: won (155.0/2.0)
							* rxmsq = t
								* qxmsq = f: nowin (8.0)
								* qxmsq = t: won (19.0)
						* katri = w: won (29.0)
						* katri = b
							* bkblk = f: nowin (15.0)
							* bkblk = t: won (5.0/1.0)
					* wkpos = f
						* katri = n
							* bkblk = f: nowin (51.0/3.0)
							* bkblk = t: won (12.0/1.0)
						* katri = w: won (34.0)
						* katri = b
							* r2ar8 = t
								* bkblk = f: nowin (7.0)
								* bkblk = t: won (6.0/3.0)
							* r2ar8 = f: won (6.0)
				* bkxbq = t: won (364.0)
			* wkna8 = t
				* bknwy = f: nowin (71.0)
				* bknwy = t
					* simpl = f
						* r2ar8 = t: nowin (2.0)
						* r2ar8 = f: won (2.0)
					* simpl = t: nowin (5.0)
		* wknck = t
			* wkovl = t
				* bknwy = f: nowin (172.0)
				* bknwy = t
					* bkxbq = f: nowin (3.0)
					* bkxbq = t: won (2.0/1.0)
			* wkovl = f
				* bkxcr = f
					* skrxp = f
						* mulch = f
							* bkona = f
								* thrsk = f: won (39.0/7.0)
								* thrsk = t: nowin (5.0)
							* bkona = t: nowin (7.0)
						* mulch = t: nowin (20.0)
					* skrxp = t: nowin (28.0)
				* bkxcr = t: nowin (69.0)
	* bxqsq = t: nowin (442.0)
* rimmx = t: won (339.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* r2ar8=(t): nowin(575.0/7.0)
		* r2ar8!=(t)
			* bkxcr=(t): nowin(105.0/0.0)
			* bkxcr!=(t)
				* skrxp=(t): nowin(32.0/0.0)
				* skrxp!=(t)
					* bxqsq=(t): nowin(24.0/0.0)
					* bxqsq!=(t)
						* mulch=(t): nowin(18.0/0.0)
						* mulch!=(t)
							* thrsk=(t): nowin(7.0/0.0)
							* thrsk!=(t)
								* bkona=(t): nowin(6.0/0.0)
								* bkona!=(t)
									* reskr=(t): nowin(5.0/0.0)
									* reskr!=(t)
										* blxwp=(t): nowin(3.0/0.0)
										* blxwp!=(t): won(36.0/3.0)
	* wknck!=(t)
		* bxqsq=(t): nowin(365.0/0.0)
		* bxqsq!=(t)
			* wkna8=(t): nowin(110.0/3.0)
			* wkna8!=(t)
				* wkpos=(f)
					* bkxbq=(f)
							* katri=(n)|(b)
							* bkblk=(f): nowin(81.0/3.0)
							* bkblk!=(f)
								* hdchk=(t): nowin(7.0/0.0)
								* hdchk!=(t): won(37.0/1.0)
							* katri!=(n)|(b): won(44.0/0.0)
					* bkxbq!=(f): won(102.0/0.0)
				* wkpos!=(f)
					* katri=(b)
						* bkxbq=(f)
							* bkblk=(f): nowin(18.0/0.0)
							* bkblk!=(f): won(7.0/1.0)
						* bkxbq!=(f): won(43.0/0.0)
					* katri!=(b)
						* rxmsq=(t)
							* qxmsq=(f)
								* bkxbq=(f): nowin(12.0/0.0)
								* bkxbq!=(f): won(8.0/0.0)
							* qxmsq!=(f): won(25.0/0.0)
						* rxmsq!=(t): won(661.0/2.0)
* rimmx!=(f): won(524.0/0.0)



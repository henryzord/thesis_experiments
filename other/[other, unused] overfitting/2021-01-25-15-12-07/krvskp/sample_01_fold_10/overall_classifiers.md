# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.522419 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri != b and rxmsq != f and qxmsq = f | nowin | 0.008575 |
| rimmx = f and bxqsq = f and wknck != f and wkovl = t | nowin | 0.152780 |
| rimmx = f and bxqsq != f | nowin | 0.308011 |
| rimmx = f and bxqsq = f and wknck != f and wkovl != t and bkxcr = f and bkona = f and mulch = f and thrsk != f | nowin | 0.011184 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri = b | nowin | 0.009430 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos != t and katri != w and bkblk = f | nowin | 0.049404 |
| rimmx = f and bxqsq = f and wknck != f and wkovl != t and bkxcr != f | nowin | 0.067039 |
| rimmx = f and bxqsq = f and wknck != f and wkovl != t and bkxcr = f and bkona = f and mulch = f and thrsk = f and skrxp != f | nowin | 0.004636 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk != f | nowin | 0.005295 |
| rimmx = f and bxqsq = f and wknck != f and wkovl != t and bkxcr = f and bkona != f | nowin | 0.022757 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 != f | nowin | 0.065885 |
| rimmx = f and bxqsq = f and wknck != f and wkovl != t and bkxcr = f and bkona = f and mulch != f | nowin | 0.014426 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx = f and bxqsq = t | nowin | 0.308011 |
| stlmt = f and rimmx = t | won | 0.427295 |
| wknck = t and bknwy = f and wkovl = t | nowin | 0.216520 |
| wkna8 = f and wknck = f and hdchk = f and bkxbq = t | won | 0.553846 |
| wkna8 = f and wknck = t and bkxcr = t | nowin | 0.198165 |
| wkna8 = t | nowin | 0.195229 |
| mulch = t | nowin | 0.089630 |
| bkon8 = f and bkona = t and bkxbq = t | nowin | 0.047930 |
| bkon8 = f and wkpos = t and skrxp = f and katri = n and rxmsq = f and thrsk = f | won | 0.605224 |
| katri = w | won | 0.368852 |
| qxmsq = f and bkblk = t and bkon8 = f | won | 0.231481 |
| qxmsq = f and thrsk = f and bknwy = f and skrxp = f and wkcti = f | nowin | 0.635220 |
| qxmsq = t | won | 0.320988 |
| reskr = f and wknck = t and wkpos = t | nowin | 0.407407 |
| reskr = f and skach = f and cntxt = f | won | 0.380952 |
| reskr = t | nowin | 0.520000 |
| blxwp = f and skach = f and r2ar8 = f and thrsk = f | won | 0.336700 |
| wkpos = f | nowin | 0.882353 |
|  | won | 0.400000 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
rimmx = f AND bxqsq = t|nowin (669.0)
stlmt = f AND rimmx = t|won (526.0)
wknck = t AND bknwy = f AND wkovl = t|nowin (270.0)
wkna8 = f AND wknck = f AND hdchk = f AND bkxbq = t|won (540.0)
wkna8 = f AND wknck = t AND bkxcr = t|nowin (108.0)
wkna8 = t|nowin (108.0/1.0)
mulch = t|nowin (45.0/1.0)
bkon8 = f AND bkona = t AND bkxbq = t|nowin (22.0)
bkon8 = f AND wkpos = t AND skrxp = f AND katri = n AND rxmsq = f AND thrsk = f|won (242.0/3.0)
katri = w|won (89.0)
qxmsq = f AND bkblk = t AND bkon8 = f|won (54.0/4.0)
qxmsq = f AND thrsk = f AND bknwy = f AND skrxp = f AND wkcti = f|nowin (95.0)
qxmsq = t|won (27.0/1.0)
reskr = f AND wknck = t AND wkpos = t|nowin (22.0)
reskr = f AND skach = f AND cntxt = f|won (20.0/1.0)
reskr = t|nowin (13.0)
blxwp = f AND skach = f AND r2ar8 = f AND thrsk = f|won (11.0/1.0)
wkpos = f|nowin (13.0)
|won (3.0/1.0)


## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* hdchk = f
					* bkxbq = f
						* wkpos = t
							* katri = b: nowin (24.0/8.0)
							* katri != b
								* rxmsq = f: won (224.0/2.0)
								* rxmsq != f
									* qxmsq = f: nowin (9.0)
									* qxmsq != f: won (20.0)
						* wkpos != t
							* katri = w: won (36.0)
							* katri != w
								* bkblk = f: nowin (66.0/3.0)
								* bkblk != f: won (32.0/1.0)
					* bkxbq != f: won (424.0)
				* hdchk != f: nowin (5.0)
			* wkna8 != f: nowin (84.0)
		* wknck != f
			* wkovl = t: nowin (225.0/2.0)
			* wkovl != t
				* bkxcr = f
					* bkona = f
						* mulch = f
							* thrsk = f
								* skrxp = f: won (34.0/5.0)
								* skrxp != f: nowin (6.0)
							* thrsk != f: nowin (15.0)
						* mulch != f: nowin (17.0)
					* bkona != f: nowin (29.0)
				* bkxcr != f: nowin (85.0)
	* bxqsq != f: nowin (539.0)
* rimmx != f: won (428.0)


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



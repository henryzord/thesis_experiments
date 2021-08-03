# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.522648 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr = f and skrxp = f and mulch = f and thrsk = f and bkona = f and reskr = f and blxwp != f | nowin | 0.001332 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 = t | nowin | 0.176788 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr = f and skrxp = f and mulch = f and thrsk = f and bkona != f | nowin | 0.003984 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 != f | nowin | 0.066053 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr != f | nowin | 0.044586 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr = f and skrxp = f and mulch = f and thrsk != f | nowin | 0.004645 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos != t and katri != w and bkblk = f | nowin | 0.052543 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri != b and rxmsq != f and qxmsq = f | nowin | 0.009247 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk != f | nowin | 0.004645 |
| rimmx = f and bxqsq != f | nowin | 0.307159 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri = b and bkblk = f | nowin | 0.011858 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr = f and skrxp = f and mulch = f and thrsk = f and bkona = f and reskr != f | nowin | 0.003322 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr = f and skrxp = f and mulch != f | nowin | 0.011206 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr = f and skrxp != f | nowin | 0.018325 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr = f and skrxp = f and mulch = f and thrsk = f and bkona = f and reskr = f and blxwp = f and skach != f | nowin | 0.001332 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx = f and bxqsq = t | nowin | 0.307159 |
| stlmt = f and rimmx = t | won | 0.426363 |
| wknck = t and r2ar8 = t | nowin | 0.248157 |
| wkna8 = f and wknck = f and bkxbq = t | won | 0.587527 |
| wkna8 = t | nowin | 0.194643 |
| wknck = t and bkxcr = t | nowin | 0.137525 |
| mulch = f and bkona = f and wkpos = t and skrxp = f and katri = n and rxmsq = f | won | 0.549848 |
| katri = n and qxmsq = f and bkblk = f | nowin | 0.422181 |
| katri = w | won | 0.666667 |
| qxmsq = f and bkblk = t | won | 0.497418 |
| katri = b | nowin | 0.423839 |
|  | won | 0.875000 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
rimmx = f AND bxqsq = t|nowin (590.0)
stlmt = f AND rimmx = t|won (466.0)
wknck = t AND r2ar8 = t|nowin (296.0/4.0)
wkna8 = f AND wknck = f AND bkxbq = t|won (478.0)
wkna8 = t|nowin (96.0/3.0)
wknck = t AND bkxcr = t|nowin (65.0)
mulch = f AND bkona = f AND wkpos = t AND skrxp = f AND katri = n AND rxmsq = f|won (230.0/9.0)
katri = n AND qxmsq = f AND bkblk = f|nowin (147.0/18.0)
katri = w|won (76.0)
qxmsq = f AND bkblk = t|won (53.0/11.0)
katri = b|nowin (30.0/1.0)
|won (25.0)


## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* hdchk = f
					* bkxbq = f
						* wkpos = t
							* katri = b
								* bkblk = f: nowin (18.0)
								* bkblk != f: won (10.0/1.0)
							* katri != b
								* rxmsq = f: won (274.0/2.0)
								* rxmsq != f
									* qxmsq = f: nowin (14.0)
									* qxmsq != f: won (25.0)
						* wkpos != t
							* katri = w: won (45.0)
							* katri != w
								* bkblk = f: nowin (91.0/4.0)
								* bkblk != f: won (43.0/1.0)
					* bkxbq != f: won (537.0)
				* hdchk != f: nowin (7.0)
			* wkna8 != f: nowin (112.0/3.0)
		* wknck != f
			* r2ar8 = t: nowin (334.0/6.0)
			* r2ar8 != t
				* bkxcr = f
					* skrxp = f
						* mulch = f
							* thrsk = f
								* bkona = f
									* reskr = f
										* blxwp = f
											* skach = f: won (34.0/1.0)
											* skach != f: nowin (2.0)
										* blxwp != f: nowin (2.0)
									* reskr != f: nowin (5.0)
								* bkona != f: nowin (6.0)
							* thrsk != f: nowin (7.0)
						* mulch != f: nowin (17.0)
					* skrxp != f: nowin (28.0)
				* bkxcr != f: nowin (70.0)
	* bxqsq != f: nowin (665.0)
* rimmx != f: won (524.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* r2ar8=(t)
			* wkovl=(t): nowin(463.0/0.0)
			* wkovl!=(t)
				* bkxcr=(t): nowin(76.0/0.0)
				* bkxcr!=(t)
					* bkona=(t): nowin(17.0/0.0)
					* bkona!=(t)
						* bkspr=(f)
							* mulch=(t): nowin(10.0/0.0)
							* mulch!=(t)
								* cntxt=(t): nowin(4.0/0.0)
								* cntxt!=(t): won(3.0/2.0)
						* bkspr!=(f): won(3.0/0.0)
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
		* bxqsq=(t): nowin(359.0/0.0)
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
							* bkblk=(f)
								* wkcti=(f): nowin(65.0/0.0)
								* wkcti!=(f)
									* reskr=(t): nowin(14.0/0.0)
									* reskr!=(t)
										* r2ar8=(t): nowin(5.0/0.0)
										* r2ar8!=(t): won(4.0/3.0)
							* bkblk!=(f)
								* hdchk=(t): nowin(7.0/0.0)
								* hdchk!=(t): won(42.0/1.0)
							* katri!=(n)|(b): won(45.0/0.0)
					* bkxbq!=(f): won(107.0/0.0)
				* wkpos!=(f)
					* rxmsq=(t)
						* qxmsq=(f)
							* bkxbq=(f): nowin(16.0/0.0)
							* bkxbq!=(f): won(10.0/0.0)
						* qxmsq!=(f)
							* katri=(b): won(3.0/1.0)
							* katri!=(b): won(28.0/0.0)
					* rxmsq!=(t)
						* katri=(b)
							* bkblk=(f)
								* bkxbq=(f): nowin(16.0/0.0)
								* bkxbq!=(f): won(6.0/0.0)
							* bkblk!=(f): won(42.0/0.0)
						* katri!=(b)
							* dsopp=(t)
								* thrsk=(t): won(3.0/1.0)
								* thrsk!=(t)
									* dwipd=(g)
										* wtoeg=(t)
											* skewr=(t): won(2.0/1.0)
											* skewr!=(t): won(4.0/0.0)
										* wtoeg!=(t): won(12.0/0.0)
									* dwipd!=(g): won(39.0/0.0)
							* dsopp!=(t): won(587.0/0.0)
* rimmx!=(f): won(524.0/0.0)



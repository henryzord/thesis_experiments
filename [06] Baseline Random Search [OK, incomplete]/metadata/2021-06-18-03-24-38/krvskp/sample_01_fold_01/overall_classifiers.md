# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.522648 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 = t and wkovl = t | nowin | 0.150623 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 = t and wkovl != t and bkxcr = f and bkona = f and mulch != f | nowin | 0.007280 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr = f and skrxp = f and mulch = f and wkovl != t and simpl != f and wtoeg != n | nowin | 0.003258 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 = t and wkovl != t and bkxcr = f and bkona != f | nowin | 0.011206 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr != f | nowin | 0.046408 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr = f and skrxp = f and mulch = f and wkovl = t | nowin | 0.002081 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = t and katri = b | nowin | 0.009544 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 != f | nowin | 0.064889 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 = t and wkovl != t and bkxcr != f | nowin | 0.023438 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr = f and skrxp = f and mulch = f and wkovl != t and simpl != f and wtoeg = n and cntxt != f | nowin | 0.001851 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = t and katri != b and rxmsq != f and qxmsq = f | nowin | 0.008592 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr = f and skrxp = f and mulch != f | nowin | 0.010554 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos != t and katri != w and bkblk = f | nowin | 0.048946 |
| rimmx = f and bxqsq != f | nowin | 0.307799 |
| rimmx = f and bxqsq = f and wknck != f and r2ar8 != t and bkxcr = f and skrxp != f | nowin | 0.018325 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx = f and bxqsq = t | nowin | 0.307799 |
| stlmt = f and rimmx = t | won | 0.427990 |
| wknck = t and r2ar8 = t and wkovl = t | nowin | 0.214516 |
| wkna8 = t and bknwy = f | nowin | 0.090570 |
| wknck = f and hdchk = f and bkxbq = t | won | 0.614075 |
| wknck = t and bkxcr = t | nowin | 0.201107 |
| mulch = t | nowin | 0.094313 |
| bkon8 = f and bkona = t and bkxbq = t | nowin | 0.054585 |
| bkon8 = f and wkpos = t and skrxp = f and katri = n and rxmsq = f and thrsk = f and wknck = f | won | 0.555880 |
| bkon8 = f and katri = w | won | 0.364000 |
| qxmsq = f and bkblk = t and bkon8 = f and hdchk = f and cntxt = t | won | 0.232256 |
| qxmsq = f and cntxt = t and bknwy = f and bkxbq = f and thrsk = f and wkovl = t | nowin | 0.477273 |
| bkon8 = f and bkona = f and qxmsq = t | won | 0.242813 |
| reskr = f and bkon8 = f and bkona = f and bkxbq = t and blxwp = f | won | 0.242424 |
| reskr = t | nowin | 0.271186 |
| bkxbq = f and hdchk = f and rxmsq = t and wkcti = f | nowin | 0.218182 |
| bkxbq = f and hdchk = f and wkovl = t | won | 0.228814 |
| rxmsq = f and skrxp = f and r2ar8 = f and bkxbq = f and bkspr = f and bkxcr = f and thrsk = f | won | 0.241431 |
| rxmsq = f and wknck = t | nowin | 0.800000 |
| wkpos = f and dsopp = f | nowin | 0.708333 |
|  | won | 0.777778 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
rimmx = f AND bxqsq = t|nowin (667.0)
stlmt = f AND rimmx = t|won (526.0)
wknck = t AND r2ar8 = t AND wkovl = t|nowin (266.0)
wkna8 = t AND bknwy = f|nowin (97.0)
wknck = f AND hdchk = f AND bkxbq = t|won (541.0)
wknck = t AND bkxcr = t|nowin (109.0)
mulch = t|nowin (49.0/2.0)
bkon8 = f AND bkona = t AND bkxbq = t|nowin (25.0)
bkon8 = f AND wkpos = t AND skrxp = f AND katri = n AND rxmsq = f AND thrsk = f AND wknck = f|won (201.0/1.0)
bkon8 = f AND katri = w|won (89.0)
qxmsq = f AND bkblk = t AND bkon8 = f AND hdchk = f AND cntxt = t|won (52.0/2.0)
qxmsq = f AND cntxt = t AND bknwy = f AND bkxbq = f AND thrsk = f AND wkovl = t|nowin (83.0)
bkon8 = f AND bkona = f AND qxmsq = t|won (26.0/1.0)
reskr = f AND bkon8 = f AND bkona = f AND bkxbq = t AND blxwp = f|won (24.0)
reskr = t|nowin (16.0)
bkxbq = f AND hdchk = f AND rxmsq = t AND wkcti = f|nowin (11.0)
bkxbq = f AND hdchk = f AND wkovl = t|won (22.0/4.0)
rxmsq = f AND skrxp = f AND r2ar8 = f AND bkxbq = f AND bkspr = f AND bkxcr = f AND thrsk = f|won (21.0/3.0)
rxmsq = f AND wknck = t|nowin (26.0)
wkpos = f AND dsopp = f|nowin (12.0)
|won (7.0)


## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* bkxbq = f
					* wkpos = t
						* katri = b: nowin (25.0/6.0)
						* katri != b
							* rxmsq = f: won (269.0/2.0)
							* rxmsq != f
								* qxmsq = f: nowin (13.0)
								* qxmsq != f: won (24.0)
					* wkpos != t
						* katri = w: won (48.0)
						* katri != w
							* bkblk = f: nowin (85.0/4.0)
							* bkblk != f: won (49.0/8.0)
				* bkxbq != f: won (541.0)
			* wkna8 != f: nowin (110.0/3.0)
		* wknck != f
			* r2ar8 = t
				* wkovl = t: nowin (266.0)
				* wkovl != t
					* bkxcr = f
						* bkona = f
							* mulch = f: won (8.0/2.0)
							* mulch != f: nowin (11.0)
						* bkona != f: nowin (17.0)
					* bkxcr != f: nowin (36.0)
			* r2ar8 != t
				* bkxcr = f
					* skrxp = f
						* mulch = f
							* wkovl = t: nowin (8.0/3.0)
							* wkovl != t
								* simpl = f: won (22.0/5.0)
								* simpl != f
									* wtoeg = n
										* cntxt = f: won (9.0/2.0)
										* cntxt != f: nowin (9.0/4.0)
									* wtoeg != n: nowin (10.0/3.0)
						* mulch != f: nowin (16.0)
					* skrxp != f: nowin (28.0)
				* bkxcr != f: nowin (73.0)
	* bxqsq != f: nowin (667.0)
* rimmx != f: won (526.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* r2ar8=(t)
			* wkovl=(t): nowin(458.0/0.0)
			* wkovl!=(t)
				* bkxcr=(t): nowin(78.0/0.0)
				* bkxcr!=(t)
					* bkona=(t): nowin(17.0/0.0)
					* bkona!=(t): nowin(16.0/6.0)
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
									* reskr!=(t): won(34.0/5.0)
	* wknck!=(t)
		* bxqsq=(t): nowin(368.0/0.0)
		* bxqsq!=(t)
			* wkna8=(t)
				* bknwy=(f): nowin(97.0/0.0)
				* bknwy!=(f)
					* r2ar8=(t): nowin(7.0/0.0)
					* r2ar8!=(t): won(3.0/3.0)
			* wkna8!=(t)
				* bkxbq=(f)
					* wkpos=(f)
							* katri=(n)|(b)
							* bkblk=(f)
								* r2ar8=(t): nowin(59.0/0.0)
								* r2ar8!=(t)
									* reskr=(t): nowin(13.0/0.0)
									* reskr!=(t)
										* wkcti=(f): nowin(6.0/0.0)
										* wkcti!=(f): won(4.0/3.0)
							* bkblk!=(f)
								* hdchk=(t): nowin(7.0/0.0)
								* hdchk!=(t): won(41.0/1.0)
							* katri!=(n)|(b): won(48.0/0.0)
					* wkpos!=(f)
						* katri=(b)
							* bkblk=(f): nowin(18.0/0.0)
							* bkblk!=(f): won(6.0/1.0)
						* katri!=(b)
							* rxmsq=(t)
								* qxmsq=(f): nowin(13.0/0.0)
								* qxmsq!=(f): won(24.0/0.0)
							* rxmsq!=(t)
								* dsopp=(t): won(34.0/2.0)
								* dsopp!=(t): won(233.0/0.0)
				* bkxbq!=(f): won(541.0/0.0)
* rimmx!=(f): won(526.0/0.0)



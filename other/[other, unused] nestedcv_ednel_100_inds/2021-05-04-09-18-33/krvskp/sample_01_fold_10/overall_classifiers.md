# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.522648 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl != t and bkxcr = f and skrxp = f and mulch = f and bkona = f and thrsk != f | nowin | 0.003322 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk != f | nowin | 0.005305 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl != t and bkxcr = f and skrxp != f | nowin | 0.024707 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 != f and bknwy != f and wkovl = t and r2ar8 = t | nowin | 0.001332 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl != t and bkxcr = f and skrxp = f and mulch = f and bkona = f and thrsk = f and bkon8 = f and blxwp != f | nowin | 0.001332 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl != t and bkxcr = f and skrxp = f and mulch = f and bkona != f | nowin | 0.007937 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl != t and bkxcr = f and skrxp = f and mulch != f | nowin | 0.012508 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri != b and rxmsq != f and qxmsq = f | nowin | 0.008592 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 != f and bknwy = f | nowin | 0.058971 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl != t and bkxcr = f and skrxp = f and mulch = f and bkona = f and thrsk = f and bkon8 = f and blxwp = f and reskr != f | nowin | 0.001332 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl != t and bkxcr = f and skrxp = f and mulch = f and bkona = f and thrsk = f and bkon8 = f and blxwp = f and reskr = f and skach != f | nowin | 0.001332 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos != t and katri != w and bkblk = f and wkcti != f and r2ar8 = t | nowin | 0.008592 |
| rimmx = f and bxqsq != f | nowin | 0.307799 |
| rimmx = f and bxqsq = f and wknck != f and bknwy != f and mulch != f | nowin | 0.005964 |
| rimmx = f and bxqsq = f and wknck != f and bknwy != f and mulch = f and simpl != f | nowin | 0.001332 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl != t and bkxcr = f and skrxp = f and mulch = f and bkona = f and thrsk = f and bkon8 != f | nowin | 0.002660 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl = t | nowin | 0.152063 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos != t and katri != w and bkblk = f and wkcti = f | nowin | 0.039078 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri = b and bkblk = f | nowin | 0.012508 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 != f and bknwy != f and wkovl != t | nowin | 0.006623 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos != t and katri != w and bkblk = f and wkcti != f and r2ar8 != t and reskr = f and dsopp = f | nowin | 0.000888 |
| rimmx = f and bxqsq = f and wknck != f and bknwy = f and wkovl != t and bkxcr != f | nowin | 0.066584 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos != t and katri != w and bkblk = f and wkcti != f and r2ar8 != t and reskr != f | nowin | 0.003322 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx = f and bxqsq != f | nowin | 0.307799 |
| stlmt = f and rimmx != f | won | 0.427990 |
| wknck != f and bknwy = f and wkovl = t | nowin | 0.216412 |
| wkna8 = f and wknck = f and hdchk = f and bkxbq != f | won | 0.553498 |
| wkna8 = f and wknck != f and bkxcr != f | nowin | 0.197053 |
| wkna8 != f | nowin | 0.195589 |
| mulch != f | nowin | 0.089817 |
| bkon8 = f and bkona != f and bkxbq != f | nowin | 0.048035 |
| bkon8 = f and katri != w and wkpos = t and skrxp = f and katri = n | won | 0.630986 |
| katri != w and bkblk = f and wkcti = f | nowin | 0.424541 |
| katri = w | won | 0.717742 |
| bkblk != f | won | 0.546230 |
| r2ar8 != t and wknck != f | won | 0.132353 |
|  | nowin | 0.795455 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
rimmx = f AND bxqsq != f|nowin (593.0)
stlmt = f AND rimmx != f|won (466.0)
wknck != f AND bknwy = f AND wkovl = t|nowin (235.0)
wkna8 = f AND wknck = f AND hdchk = f AND bkxbq != f|won (469.0)
wkna8 = f AND wknck != f AND bkxcr != f|nowin (100.0)
wkna8 != f|nowin (92.0/1.0)
mulch != f|nowin (33.0)
bkon8 = f AND bkona != f AND bkxbq != f|nowin (21.0)
bkon8 = f AND katri != w AND wkpos = t AND skrxp = f AND katri = n|won (267.0/18.0)
katri != w AND bkblk = f AND wkcti = f|nowin (86.0/5.0)
katri = w|won (70.0)
bkblk != f|won (51.0/9.0)
r2ar8 != t AND wknck != f|won (13.0/4.0)
|nowin (16.0/2.0)


## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* hdchk = f
					* bkxbq = f
						* wkpos = t
							* katri = b
								* bkblk = f: nowin (19.0)
								* bkblk != f
									* rxmsq = f: won (7.0)
									* rxmsq != f: won (2.0/1.0)
							* katri != b
								* rxmsq = f
									* dsopp = f: won (242.0)
									* dsopp != f
										* thrsk = f
											* dwipd = l: won (23.0)
											* dwipd != l
												* skewr = t: won (3.0/1.0)
												* skewr != t: won (7.0)
										* thrsk != f: won (3.0/1.0)
								* rxmsq != f
									* qxmsq = f: nowin (13.0)
									* qxmsq != f: won (23.0)
						* wkpos != t
							* katri = w: won (45.0)
							* katri != w
								* bkblk = f
									* wkcti = f: nowin (61.0)
									* wkcti != f
										* r2ar8 = t: nowin (13.0)
										* r2ar8 != t
											* reskr = f
												* dsopp = f: nowin (3.0/1.0)
												* dsopp != f: won (2.0)
											* reskr != f: nowin (5.0)
								* bkblk != f
									* thrsk = f: won (33.0)
									* thrsk != f
										* katri = n: won (4.0)
										* katri != n
											* r2ar8 = t: won (2.0/1.0)
											* r2ar8 != t: won (2.0)
					* bkxbq != f: won (538.0)
				* hdchk != f: nowin (8.0)
			* wkna8 != f
				* bknwy = f: nowin (94.0)
				* bknwy != f
					* wkovl = t
						* r2ar8 = t: nowin (2.0)
						* r2ar8 != t: won (2.0/1.0)
					* wkovl != t: nowin (10.0)
		* wknck != f
			* bknwy = f
				* wkovl = t: nowin (269.0)
				* wkovl != t
					* bkxcr = f
						* skrxp = f
							* mulch = f
								* bkona = f
									* thrsk = f
										* bkon8 = f
											* blxwp = f
												* reskr = f
													* skach = f: won (34.0)
													* skach != f: nowin (2.0)
												* reskr != f: nowin (2.0)
											* blxwp != f: nowin (2.0)
										* bkon8 != f: nowin (4.0)
									* thrsk != f: nowin (5.0)
								* bkona != f: nowin (12.0)
							* mulch != f: nowin (19.0)
						* skrxp != f: nowin (38.0)
					* bkxcr != f: nowin (107.0)
			* bknwy != f
				* mulch = f
					* simpl = f: won (6.0)
					* simpl != f: nowin (2.0)
				* mulch != f: nowin (9.0)
	* bxqsq != f: nowin (667.0)
* rimmx != f: won (526.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* r2ar8=(t)
			* wkovl=(t): nowin(455.0/0.0)
			* wkovl!=(t)
				* bkxcr=(t): nowin(78.0/0.0)
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
									* reskr=(t): nowin(4.0/0.0)
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
							* katri!=(n)|(b): won(45.0/0.0)
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
							* dsopp!=(t): won(597.0/0.0)
* rimmx!=(f): won(526.0/0.0)



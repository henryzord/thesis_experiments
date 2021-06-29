# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.522648 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = f and bkblk = f and katri = n and r2ar8 = t | nowin | 0.032882 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = f and skrxp = f and mulch = t | nowin | 0.015102 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = f and skrxp = f and mulch = f and bkona = t | nowin | 0.007280 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = t | nowin | 0.155889 |
| rimmx = f and bxqsq = t | nowin | 0.307159 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = t | nowin | 0.064889 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = f and bkblk = f and katri = n and r2ar8 = f and wkcti = f | nowin | 0.008592 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = t | nowin | 0.064255 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = f and skrxp = f and mulch = f and bkona = f and thrsk = t | nowin | 0.003322 |
| rimmx = f and bxqsq = f and wknck = t and wkovl = f and bkxcr = f and skrxp = t | nowin | 0.025974 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = f and bkblk = f and katri = n and r2ar8 = f and wkcti = t and reskr = t | nowin | 0.003984 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = f and bkblk = f and katri = b | nowin | 0.008592 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri = n and rxmsq = t and qxmsq = f | nowin | 0.008592 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = f and bkxbq = f and wkpos = t and katri = b and bkblk = f | nowin | 0.011206 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and hdchk = t | nowin | 0.004645 |

## Ordered rules

# Text representation of classifiers as-is

## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* hdchk = f
					* bkxbq = f
						* wkpos = t
							* katri = n
								* rxmsq = f: won (231.0/2.0)
								* rxmsq = t
									* qxmsq = f: nowin (13.0)
									* qxmsq = t: won (26.0)
							* katri = w: won (45.0)
							* katri = b
								* bkblk = f: nowin (17.0)
								* bkblk = t: won (10.0/1.0)
						* wkpos = f
							* bkblk = f
								* katri = n
									* r2ar8 = t: nowin (51.0)
									* r2ar8 = f
										* wkcti = f: nowin (13.0)
										* wkcti = t
											* reskr = f: won (7.0/3.0)
											* reskr = t: nowin (6.0)
								* katri = w: won (39.0)
								* katri = b: nowin (13.0)
							* bkblk = t: won (41.0/1.0)
					* bkxbq = t: won (538.0)
				* hdchk = t: nowin (7.0)
			* wkna8 = t: nowin (110.0/3.0)
		* wknck = t
			* wkovl = t: nowin (281.0/2.0)
			* wkovl = f
				* bkxcr = f
					* skrxp = f
						* mulch = f
							* bkona = f
								* thrsk = f: won (50.0/10.0)
								* thrsk = t: nowin (5.0)
							* bkona = t: nowin (11.0)
						* mulch = t: nowin (23.0)
					* skrxp = t: nowin (40.0)
				* bkxcr = t: nowin (103.0)
	* bxqsq = t: nowin (665.0)
* rimmx = t: won (525.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* r2ar8=(t)
			* wkovl=(t): nowin(457.0/0.0)
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
			* bkxcr=(t): nowin(99.0/0.0)
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
							* bkblk=(f)
								* r2ar8=(t): nowin(64.0/0.0)
								* r2ar8!=(t)
									* wkcti=(f): nowin(13.0/0.0)
									* wkcti!=(f)
										* reskr=(t): nowin(6.0/0.0)
										* reskr!=(t)
											* dsopp=(f): nowin(3.0/2.0)
											* dsopp!=(f): won(2.0/0.0)
							* bkblk!=(f)
								* hdchk=(t): nowin(7.0/0.0)
								* hdchk!=(t): won(36.0/1.0)
							* katri!=(n)|(b): won(43.0/0.0)
					* bkxbq!=(f): won(104.0/0.0)
				* wkpos!=(f)
					* katri=(b)
						* bkxbq=(f)
							* bkblk=(f): nowin(17.0/0.0)
							* bkblk!=(f)
								* rxmsq=(t): won(1.0/1.0)
								* rxmsq!=(t): won(8.0/0.0)
						* bkxbq!=(f): won(44.0/0.0)
					* katri!=(b)
						* rxmsq=(t)
							* qxmsq=(f)
								* bkxbq=(f): nowin(13.0/0.0)
								* bkxbq!=(f): won(9.0/0.0)
							* qxmsq!=(f): won(28.0/0.0)
						* rxmsq!=(t)
							* dsopp=(t)
								* thrsk=(t): won(3.0/1.0)
								* thrsk!=(t)
									* dwipd=(g)
										* wtoeg=(t)
											* skewr=(t): won(2.0/1.0)
											* skewr!=(t): won(4.0/0.0)
										* wtoeg!=(t): won(11.0/0.0)
									* dwipd!=(g): won(38.0/0.0)
							* dsopp!=(t): won(595.0/0.0)
* rimmx!=(f): won(525.0/0.0)



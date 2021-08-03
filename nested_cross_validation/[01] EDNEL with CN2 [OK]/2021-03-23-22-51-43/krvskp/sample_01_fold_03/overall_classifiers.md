# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | won | 0.521921 |
| bkblk = t and bxqsq = f and cntxt = t and hdchk = t and qxmsq = f and rimmx = f and rxmsq = f and spcop = f and wknck = f and wkpos = f | nowin | 0.004645 |
| bkblk = t and bxqsq = t and cntxt = t and hdchk = f and qxmsq = f and rimmx = f and rxmsq = f and spcop = f and wknck = f and wkpos = f | nowin | 0.011206 |
| bkblk = f and bxqsq = t and cntxt = f and hdchk = f and qxmsq = f and rimmx = f and rxmsq = f and spcop = f and wknck = f and wkpos = t | nowin | 0.117128 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = t | nowin | 0.177239 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = t and katri = n and rxmsq = t and qxmsq = f | nowin | 0.009247 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = t and katri = b and bkblk = f | nowin | 0.011858 |
| bkblk = f and bxqsq = f and cntxt = t and hdchk = f and qxmsq = f and rimmx = f and rxmsq = f and spcop = f and wknck = t and wkpos = f | nowin | 0.052751 |
| bkblk = t and bxqsq = t and cntxt = t and hdchk = f and qxmsq = f and rimmx = f and rxmsq = f and spcop = f and wknck = t and wkpos = f | nowin | 0.015102 |
| bkblk = t and bxqsq = t and cntxt = t and hdchk = f and qxmsq = f and rimmx = f and rxmsq = f and spcop = f and wknck = f and wkpos = t | nowin | 0.018325 |
| bkblk = f and bxqsq = t and cntxt = t and hdchk = f and qxmsq = t and rimmx = f and rxmsq = t and spcop = f and wknck = t and wkpos = t | nowin | 0.001996 |
| rimmx = f and bxqsq = t | nowin | 0.308118 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = f and katri = n and bkblk = f | nowin | 0.044109 |
| rimmx = f and bxqsq = f and wknck = t and r2ar8 = f and bkxcr = f and skrxp = f and mulch = t | nowin | 0.011206 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = t | nowin | 0.066053 |
| bkblk = f and bxqsq = f and cntxt = f and hdchk = f and qxmsq = f and rimmx = f and rxmsq = f and spcop = f and wknck = t and wkpos = t | nowin | 0.168514 |
| bkblk = t and bxqsq = f and cntxt = t and hdchk = f and qxmsq = f and rimmx = f and rxmsq = f and spcop = f and wknck = t and wkpos = f | nowin | 0.007937 |
| bkblk = t and bxqsq = f and cntxt = t and hdchk = f and qxmsq = f and rimmx = f and rxmsq = f and spcop = f and wknck = t and wkpos = t | nowin | 0.013158 |
| rimmx = f and bxqsq = f and wknck = f and wkna8 = f and bkxbq = f and wkpos = f and katri = b and bkblk = f | nowin | 0.009247 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx = f and bxqsq = t | nowin | 0.308118 |
| stlmt = f and rimmx = t | won | 0.426483 |
| wknck = t and r2ar8 = t and wkovl = t | nowin | 0.212439 |
| wkna8 = t and bknwy = f | nowin | 0.091333 |
| wknck = f and hdchk = f and bkxbq = t | won | 0.608400 |
| wknck = t and bkxcr = t | nowin | 0.194495 |
| mulch = t | nowin | 0.100564 |
| bkon8 = f and bkona = t and bkxbq = t | nowin | 0.047722 |
| bkon8 = f and wkpos = t and skrxp = f and katri = n and rxmsq = f and thrsk = f and wknck = f | won | 0.556162 |
| bkon8 = f and katri = w | won | 0.346457 |
| qxmsq = f and bkblk = t and bkon8 = f and cntxt = t | won | 0.225078 |
| qxmsq = f and bkxbq = f and cntxt = t and wkcti = f | nowin | 0.488827 |
| qxmsq = t | won | 0.257471 |
| reskr = f and bkon8 = f and bkxbq = t | won | 0.235671 |
| reskr = t | nowin | 0.333333 |
| bkon8 = f and skach = f and rxmsq = t and r2ar8 = t | nowin | 0.296296 |
| bkon8 = f and skach = f and rxmsq = f and dwipd = l and skrxp = t | nowin | 0.241429 |
| bkon8 = f and skach = f and skrxp = f and bkspr = f and blxwp = f and bkblk = f and reskd = f and rxmsq = f and r2ar8 = f and thrsk = f | won | 0.334641 |
| wknck = f and wkpos = t | won | 0.356719 |
| rxmsq = f | nowin | 0.907258 |
|  | won | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| bxqsq = t and rimmx = f | nowin | 0.308118 |
| wknck = t and rimmx = f and r2ar8 = t and wkovl = t | nowin | 0.149178 |
| wkpos = f and cntxt = f and rimmx = f and bknwy = f | nowin | 0.061327 |
| wknck = t and rimmx = f and bkxcr = t | nowin | 0.066002 |
| wkpos = f and katri = n and bkxbq = f and wkcti = f and bkblk = f and bxqsq = f | nowin | 0.033505 |
| mulch = t and rimmx = f and katri = n | nowin | 0.030381 |
| katri = b and bkblk = f and bkxbq = f | nowin | 0.020888 |
| skrxp = t and rimmx = f and wknck = t | nowin | 0.018967 |
| wkpos = f and katri = n and bkxbq = f and rimmx = f and bkblk = f and reskr = t | nowin | 0.011206 |
| rxmsq = t and qxmsq = f and bkxbq = f and r2ar8 = t and bxqsq = f | nowin | 0.011206 |
| wkovl = f and wknck = t and rimmx = f and bkona = t | nowin | 0.006623 |
| wkpos = f and hdchk = t | nowin | 0.003984 |
| thrsk = t and rimmx = f and wknck = t | nowin | 0.004645 |
| wkpos = f and cntxt = f and rimmx = f and simpl = t | nowin | 0.001996 |
| wkpos = f and skach = t and bkblk = f | nowin | 0.001996 |
| wkpos = f and katri = n and bkxbq = f and wknck = f and bkblk = f and r2ar8 = t | nowin | 0.002660 |
| bkon8 = t and wknck = t and rimmx = f | nowin | 0.001996 |
|  | won | 0.994036 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

bkblk|bxqsq|cntxt|hdchk|qxmsq|rimmx|rxmsq|spcop|wknck|wkpos|class
---|---|---|---|---|---|---|---|---|---|---
f|f|t|f|t|f|t|f|t|f|won
t|f|t|f|t|f|t|f|t|f|won
f|t|t|f|t|t|t|f|t|t|won
f|t|t|f|f|f|t|f|t|f|nowin
f|f|t|f|f|f|t|f|t|f|won
f|t|t|f|f|t|f|f|t|f|won
t|f|t|f|f|t|f|f|t|f|won
f|t|f|f|f|f|t|f|t|f|nowin
f|f|t|f|f|t|f|f|t|f|won
f|t|f|f|f|t|f|f|t|f|won
f|f|t|f|t|f|f|f|t|f|won
f|t|t|f|t|f|t|f|t|t|nowin
f|t|t|f|t|t|f|f|t|t|won
t|t|t|f|f|f|f|f|t|f|nowin
f|t|t|f|f|f|f|f|t|f|nowin
f|t|f|f|t|f|t|f|t|t|nowin
t|f|t|f|f|f|f|f|t|f|nowin
f|f|t|f|f|f|f|f|t|f|nowin
f|f|f|f|t|f|t|f|t|t|nowin
t|f|t|f|f|f|f|t|f|f|won
f|t|f|f|f|f|f|f|t|f|nowin
f|t|t|f|t|t|t|f|f|t|won
f|f|t|f|f|f|t|f|f|f|nowin
t|t|t|f|f|t|f|f|t|t|won
f|t|f|f|f|f|t|f|f|f|nowin
t|f|t|f|f|t|f|f|f|f|won
f|t|f|f|t|t|t|f|f|t|won
f|f|t|f|f|t|f|f|f|f|won
f|t|t|f|f|t|f|f|t|t|won
t|f|f|f|f|f|t|f|f|f|nowin
f|t|t|f|t|f|f|f|t|t|nowin
f|f|f|f|f|f|t|f|f|f|nowin
t|f|t|f|f|t|f|f|t|t|won
t|f|t|t|f|f|f|f|f|f|nowin
f|f|f|f|f|f|t|f|t|t|nowin
f|t|f|f|f|t|f|f|t|t|won
f|f|f|f|f|t|f|f|f|f|won
f|t|f|f|t|f|f|f|t|t|won
f|t|t|f|t|f|t|f|f|t|nowin
f|f|f|f|f|t|f|f|t|t|won
f|f|f|f|t|f|f|f|t|t|won
f|t|t|f|f|f|f|f|f|f|nowin
f|t|f|f|f|t|t|f|f|t|won
t|f|t|f|t|f|t|f|f|t|won
t|t|t|f|f|f|f|f|f|f|nowin
t|f|f|t|f|f|f|f|f|f|nowin
f|f|t|f|t|f|t|f|f|t|won
f|t|f|f|t|f|t|f|f|t|nowin
t|t|t|f|f|f|f|f|t|t|nowin
f|t|t|f|f|f|f|f|t|t|nowin
f|f|t|f|f|f|f|f|f|f|won
t|f|t|f|f|f|f|f|f|f|won
f|t|f|f|t|t|f|f|f|t|won
f|t|f|f|f|f|f|f|f|f|nowin
t|f|t|f|f|f|f|f|t|t|nowin
f|f|f|f|t|f|t|f|f|t|won
f|t|t|f|f|f|t|f|f|t|nowin
t|f|f|f|f|f|f|f|f|f|nowin
f|t|f|f|f|f|f|f|t|t|nowin
f|f|f|f|f|f|f|f|f|f|nowin
f|f|t|f|f|f|t|f|f|t|won
t|f|t|f|f|f|t|f|f|t|won
f|t|t|f|f|t|f|f|f|t|won
f|f|f|f|f|f|f|f|t|t|nowin
f|t|t|f|t|f|f|f|f|t|won
t|f|t|f|f|t|f|f|f|t|won
f|t|f|f|f|f|t|f|f|t|nowin
f|f|t|f|f|t|f|f|f|t|won
f|f|f|f|f|f|t|f|f|t|nowin
f|f|t|f|t|f|f|f|f|t|won
f|t|f|f|f|t|f|f|f|t|won
f|t|f|f|t|f|f|f|f|t|nowin
f|f|f|f|f|t|f|f|f|t|won
f|f|f|f|t|f|f|f|f|t|won
t|t|t|f|f|f|f|f|f|t|nowin
f|t|t|f|f|f|f|f|f|t|nowin
t|f|t|f|f|f|f|f|f|t|won
f|f|t|f|f|f|f|f|f|t|won
f|t|f|f|f|f|f|f|f|t|nowin
f|f|f|f|f|f|f|f|f|t|won

## JRip

Decision list:

rules | predicted class
---|---
(bxqsq = t) and (rimmx = f)|nowin (668.0/0.0)
(wknck = t) and (rimmx = f) and (r2ar8 = t) and (wkovl = t)|nowin (263.0/0.0)
(wkpos = f) and (cntxt = f) and (rimmx = f) and (bknwy = f)|nowin (98.0/0.0)
(wknck = t) and (rimmx = f) and (bkxcr = t)|nowin (106.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (wkcti = f) and (bkblk = f) and (bxqsq = f)|nowin (52.0/0.0)
(mulch = t) and (rimmx = f) and (katri = n)|nowin (47.0/0.0)
(katri = b) and (bkblk = f) and (bkxbq = f)|nowin (32.0/0.0)
(skrxp = t) and (rimmx = f) and (wknck = t)|nowin (29.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (rimmx = f) and (bkblk = f) and (reskr = t)|nowin (17.0/0.0)
(rxmsq = t) and (qxmsq = f) and (bkxbq = f) and (r2ar8 = t) and (bxqsq = f)|nowin (17.0/0.0)
(wkovl = f) and (wknck = t) and (rimmx = f) and (bkona = t)|nowin (10.0/0.0)
(wkpos = f) and (hdchk = t)|nowin (6.0/0.0)
(thrsk = t) and (rimmx = f) and (wknck = t)|nowin (7.0/0.0)
(wkpos = f) and (cntxt = f) and (rimmx = f) and (simpl = t)|nowin (3.0/0.0)
(wkpos = f) and (skach = t) and (bkblk = f)|nowin (3.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (wknck = f) and (bkblk = f) and (r2ar8 = t)|nowin (4.0/0.0)
(bkon8 = t) and (wknck = t) and (rimmx = f)|nowin (3.0/0.0)
|won (1509.0/9.0)


## PART

Decision list:

rules | predicted class
---|---
rimmx = f AND bxqsq = t|nowin (668.0)
stlmt = f AND rimmx = t|won (525.0)
wknck = t AND r2ar8 = t AND wkovl = t|nowin (263.0)
wkna8 = t AND bknwy = f|nowin (98.0)
wknck = f AND hdchk = f AND bkxbq = t|won (536.0)
wknck = t AND bkxcr = t|nowin (106.0)
mulch = t|nowin (53.0/2.0)
bkon8 = f AND bkona = t AND bkxbq = t|nowin (22.0)
bkon8 = f AND wkpos = t AND skrxp = f AND katri = n AND rxmsq = f AND thrsk = f AND wknck = f|won (210.0/1.0)
bkon8 = f AND katri = w|won (86.0)
qxmsq = f AND bkblk = t AND bkon8 = f AND cntxt = t|won (54.0/3.0)
qxmsq = f AND bkxbq = f AND cntxt = t AND wkcti = f|nowin (86.0/1.0)
qxmsq = t|won (29.0/1.0)
reskr = f AND bkon8 = f AND bkxbq = t|won (26.0/1.0)
reskr = t|nowin (19.0)
bkon8 = f AND skach = f AND rxmsq = t AND r2ar8 = t|nowin (15.0)
bkon8 = f AND skach = f AND rxmsq = f AND dwipd = l AND skrxp = t|nowin (14.0/1.0)
bkon8 = f AND skach = f AND skrxp = f AND bkspr = f AND blxwp = f AND bkblk = f AND reskd = f AND rxmsq = f AND r2ar8 = f AND thrsk = f|won (17.0/1.0)
wknck = f AND wkpos = t|won (19.0/2.0)
rxmsq = f|nowin (26.0/1.0)
|won (2.0)


## J48 Decision Tree

* rimmx = f
	* bxqsq = f
		* wknck = f
			* wkna8 = f
				* bkxbq = f
					* wkpos = t
						* katri = n
							* rxmsq = f: won (231.0/2.0)
							* rxmsq = t
								* qxmsq = f: nowin (14.0)
								* qxmsq = t: won (25.0)
						* katri = w: won (43.0)
						* katri = b
							* bkblk = f: nowin (18.0)
							* bkblk = t: won (10.0/1.0)
					* wkpos = f
						* katri = n
							* bkblk = f: nowin (77.0/4.0)
							* bkblk = t: won (25.0/4.0)
						* katri = w: won (45.0)
						* katri = b
							* bkblk = f: nowin (14.0)
							* bkblk = t: won (25.0/4.0)
				* bkxbq = t: won (536.0)
			* wkna8 = t: nowin (112.0/3.0)
		* wknck = t
			* r2ar8 = t: nowin (335.0/6.0)
			* r2ar8 = f
				* bkxcr = f
					* skrxp = f
						* mulch = f: won (56.0/23.0)
						* mulch = t: nowin (17.0)
					* skrxp = t: nowin (28.0)
				* bkxcr = t: nowin (70.0)
	* bxqsq = t: nowin (668.0)
* rimmx = t: won (525.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* r2ar8=(t)
			* wkovl=(t): nowin(466.0/0.0)
			* wkovl!=(t)
				* bkxcr=(t): nowin(76.0/0.0)
				* bkxcr!=(t)
					* bkona=(t): nowin(17.0/0.0)
					* bkona!=(t): nowin(16.0/6.0)
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
		* bxqsq=(t): nowin(360.0/0.0)
		* bxqsq!=(t)
			* wkna8=(t)
				* bknwy=(f): nowin(98.0/0.0)
				* bknwy!=(f)
					* r2ar8=(t): nowin(7.0/0.0)
					* r2ar8!=(t): nowin(4.0/3.0)
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
										* wtoeg=(t): won(6.0/1.0)
										* wtoeg!=(t): won(12.0/0.0)
									* dwipd!=(g): won(39.0/0.0)
							* dsopp!=(t): won(586.0/0.0)
* rimmx!=(f): won(525.0/0.0)



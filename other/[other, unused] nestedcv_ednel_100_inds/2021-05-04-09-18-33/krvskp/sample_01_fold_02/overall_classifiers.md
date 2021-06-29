# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx!=(f) | won | 0.522648 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx = f and bxqsq != f | nowin | 0.307159 |
| stlmt = f and rimmx != f | won | 0.426829 |
| wknck != f and wkovl = t and bknwy = f | nowin | 0.217496 |
| wkna8 != f and bknwy = f | nowin | 0.092179 |
| wknck = f and hdchk = f and wkna8 = f and bkxbq != f | won | 0.616705 |
| wknck != f and bkxcr != f | nowin | 0.198529 |
| mulch != f and katri != w | nowin | 0.102881 |
| bkon8 = f and bkona != f and bkxbq != f | nowin | 0.048035 |
| bkon8 = f and katri != w and wkpos = t and katri = n and skrxp = f and rxmsq = f and thrsk = f and bkxbq = f and dsopp = f | won | 0.541420 |
| katri = w | won | 0.377510 |
| qxmsq != f and katri = n | won | 0.138889 |
| bkblk != f and bkon8 = f and hdchk = f and cntxt != f | won | 0.251208 |
| cntxt != f and wknck = f and thrsk = f and r2ar8 = t | nowin | 0.506024 |
| reskr = f and bkon8 = f and skach = f and rxmsq != f and wkcti = f | nowin | 0.127660 |
| reskr = f and bkon8 = f and skach = f and wkovl = t and skewr != t | won | 0.313953 |
| reskr = f and skrxp != f and dwipd = l | nowin | 0.214286 |
| reskr != f | nowin | 0.179104 |
| bkon8 = f and bkxcr != f | nowin | 0.067797 |
| bkon8 != f | nowin | 0.067797 |
| skach = f and reskd != f and bknwy = f | nowin | 0.023810 |
| skach = f and reskd = f and bkblk = f and blxwp = f and bkxbq != f | won | 0.511111 |
| skach != f | nowin | 0.085714 |
| bkxbq = f and reskd = f and bkblk != f and r2ar8 = t | nowin | 0.058824 |
| bkxbq = f and reskd = f and rxmsq = f and dsopp != f and dwipd = l | won | 0.370370 |
| bkxbq = f and reskd = f and rxmsq = f and wkovl = t and dwipd = l | won | 0.150000 |
| bkxbq = f and reskd = f and rxmsq = f and wtoeg = n and wkpos = t | won | 0.260870 |
| rxmsq = f and dsopp = f and reskd = f and simpl != f and bknwy != f | nowin | 0.187500 |
| rxmsq = f and dsopp = f and reskd = f and wkcti != f and wknck = f | won | 0.071429 |
| rxmsq = f and dsopp = f and reskd = f and wkcti = f and wknck = f and cntxt = f | won | 0.263158 |
| wkcti = f | nowin | 0.625000 |
| reskd = f | won | 0.510204 |
|  | nowin | 0.800000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| bxqsq = t and rimmx = f | nowin | 0.307159 |
| wknck = t and rimmx = f and wkovl = t and bknwy = f | nowin | 0.153021 |
| wkpos = f and cntxt = f and rimmx = f and bknwy = f | nowin | 0.061914 |
| wknck = t and rimmx = f and bkxcr = t | nowin | 0.067164 |
| wkpos = f and katri = n and bkxbq = f and wkcti = f and bkblk = f and bkon8 = f | nowin | 0.030381 |
| mulch = t and rimmx = f and katri = n | nowin | 0.029754 |
| katri = b and bkblk = f and bkxbq = f | nowin | 0.021526 |
| skrxp = t and rimmx = f and wknck = t | nowin | 0.017682 |
| wkpos = f and katri = n and bkxbq = f and rimmx = f and bkblk = f and r2ar8 = t | nowin | 0.009247 |
| wkovl = f and wkpos = f and hdchk = t | nowin | 0.003984 |
| rxmsq = t and qxmsq = f and bkxbq = f and dsopp = f and bxqsq = f | nowin | 0.008592 |
| wkovl = f and wknck = t and rimmx = f and bkona = t | nowin | 0.007937 |
| wkovl = f and wkpos = f and katri = n and bkxbq = f and rimmx = f and reskr = t | nowin | 0.003984 |
| thrsk = t and rimmx = f and wknck = t | nowin | 0.003984 |
| wkna8 = t and rimmx = f and simpl = t | nowin | 0.001996 |
| skach = t and bkblk = f | nowin | 0.001996 |
| bkon8 = t and wknck = t and rimmx = f | nowin | 0.001996 |
|  | won | 0.994695 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(bxqsq = t) and (rimmx = f)|nowin (665.0/0.0)
(wknck = t) and (rimmx = f) and (wkovl = t) and (bknwy = f)|nowin (271.0/0.0)
(wkpos = f) and (cntxt = f) and (rimmx = f) and (bknwy = f)|nowin (99.0/0.0)
(wknck = t) and (rimmx = f) and (bkxcr = t)|nowin (108.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (wkcti = f) and (bkblk = f) and (bkon8 = f)|nowin (47.0/0.0)
(mulch = t) and (rimmx = f) and (katri = n)|nowin (46.0/0.0)
(katri = b) and (bkblk = f) and (bkxbq = f)|nowin (33.0/0.0)
(skrxp = t) and (rimmx = f) and (wknck = t)|nowin (27.0/0.0)
(wkpos = f) and (katri = n) and (bkxbq = f) and (rimmx = f) and (bkblk = f) and (r2ar8 = t)|nowin (14.0/0.0)
(wkovl = f) and (wkpos = f) and (hdchk = t)|nowin (6.0/0.0)
(rxmsq = t) and (qxmsq = f) and (bkxbq = f) and (dsopp = f) and (bxqsq = f)|nowin (13.0/0.0)
(wkovl = f) and (wknck = t) and (rimmx = f) and (bkona = t)|nowin (12.0/0.0)
(wkovl = f) and (wkpos = f) and (katri = n) and (bkxbq = f) and (rimmx = f) and (reskr = t)|nowin (6.0/0.0)
(thrsk = t) and (rimmx = f) and (wknck = t)|nowin (6.0/0.0)
(wkna8 = t) and (rimmx = f) and (simpl = t)|nowin (3.0/0.0)
(skach = t) and (bkblk = f)|nowin (3.0/0.0)
(bkon8 = t) and (wknck = t) and (rimmx = f)|nowin (3.0/0.0)
|won (1508.0/8.0)


## PART

Decision list:

rules | predicted class
---|---
rimmx = f AND bxqsq != f|nowin (665.0)
stlmt = f AND rimmx != f|won (525.0)
wknck != f AND wkovl = t AND bknwy = f|nowin (271.0)
wkna8 != f AND bknwy = f|nowin (99.0)
wknck = f AND hdchk = f AND wkna8 = f AND bkxbq != f|won (539.0)
wknck != f AND bkxcr != f|nowin (108.0)
mulch != f AND katri != w|nowin (50.0)
bkon8 = f AND bkona != f AND bkxbq != f|nowin (22.0)
bkon8 = f AND katri != w AND wkpos = t AND katri = n AND skrxp = f AND rxmsq = f AND thrsk = f AND bkxbq = f AND dsopp = f|won (183.0)
katri = w|won (94.0)
qxmsq != f AND katri = n|won (25.0)
bkblk != f AND bkon8 = f AND hdchk = f AND cntxt != f|won (52.0)
cntxt != f AND wknck = f AND thrsk = f AND r2ar8 = t|nowin (84.0)
reskr = f AND bkon8 = f AND skach = f AND rxmsq != f AND wkcti = f|nowin (12.0)
reskr = f AND bkon8 = f AND skach = f AND wkovl = t AND skewr != t|won (27.0)
reskr = f AND skrxp != f AND dwipd = l|nowin (15.0)
reskr != f|nowin (12.0)
bkon8 = f AND bkxcr != f|nowin (4.0)
bkon8 != f|nowin (4.0)
skach = f AND reskd != f AND bknwy = f|nowin (3.0/1.0)
skach = f AND reskd = f AND bkblk = f AND blxwp = f AND bkxbq != f|won (23.0)
skach != f|nowin (3.0)
bkxbq = f AND reskd = f AND bkblk != f AND r2ar8 = t|nowin (2.0)
bkxbq = f AND reskd = f AND rxmsq = f AND dsopp != f AND dwipd = l|won (10.0)
bkxbq = f AND reskd = f AND rxmsq = f AND wkovl = t AND dwipd = l|won (3.0)
bkxbq = f AND reskd = f AND rxmsq = f AND wtoeg = n AND wkpos = t|won (6.0)
rxmsq = f AND dsopp = f AND reskd = f AND simpl != f AND bknwy != f|nowin (3.0)
rxmsq = f AND dsopp = f AND reskd = f AND wkcti != f AND wknck = f|won (4.0/2.0)
rxmsq = f AND dsopp = f AND reskd = f AND wkcti = f AND wknck = f AND cntxt = f|won (5.0)
wkcti = f|nowin (10.0)
reskd = f|won (5.0)
|nowin (2.0)


## SimpleCart Decision Tree

* rimmx=(f)
	* wknck=(t)
		* wkovl=(t)
			* bknwy=(f): nowin(461.0/0.0)
			* bknwy!=(f): nowin(19.0/2.0)
		* wkovl!=(t)
			* bkxcr=(t): nowin(180.0/0.0)
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
		* bxqsq=(t): nowin(366.0/0.0)
		* bxqsq!=(t)
			* wkna8=(t)
				* bknwy=(f): nowin(99.0/0.0)
				* bknwy!=(f): nowin(11.0/3.0)
			* wkna8!=(t)
				* wkpos=(f)
					* bkxbq=(f)
							* katri=(n)|(b)
							* bkblk=(f)
								* r2ar8=(t): nowin(62.0/0.0)
								* r2ar8!=(t)
									* wkcti=(f): nowin(13.0/0.0)
									* wkcti!=(f): nowin(9.0/3.0)
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
							* qxmsq!=(f): won(26.0/0.0)
						* rxmsq!=(t)
							* dsopp=(t): won(58.0/2.0)
							* dsopp!=(t): won(591.0/0.0)
* rimmx!=(f): won(525.0/0.0)



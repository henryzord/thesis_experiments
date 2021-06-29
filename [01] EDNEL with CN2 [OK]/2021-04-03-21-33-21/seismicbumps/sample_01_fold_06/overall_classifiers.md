# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| shift = W and gdenergy = all and gdpuls = all and nbumps <= 1.5 and nbumps4 <= 0.5 and nbumps6 = all and nbumps7 = all and nbumps89 = all | 0 | 0.859266 |
| shift = N and gdenergy = all and gdpuls = all and nbumps <= 1.5 and nbumps4 <= 0.5 and nbumps6 = all and nbumps7 = all and nbumps89 = all | 0 | 0.834909 |
| shift = W and gdenergy = all and gdpuls = all and nbumps > 1.5 and nbumps4 <= 0.5 and nbumps6 = all and nbumps7 = all and nbumps89 = all | 0 | 0.615250 |
| shift = W and gdenergy = all and gdpuls = all and nbumps > 1.5 and nbumps4 > 0.5 and nbumps6 = all and nbumps7 = all and nbumps89 = all | 0 | 0.299262 |
| shift = W and gdenergy = all and gdpuls = all and nbumps <= 1.5 and nbumps4 > 0.5 and nbumps6 = all and nbumps7 = all and nbumps89 = all | 0 | 0.186170 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy < -29.5 and nbumps2 >= 0.5 | 1 | 0.004910 |
| shift = N and gdenergy = all and gdpuls = all and nbumps > 1.5 and nbumps4 <= 0.5 and nbumps6 = all and nbumps7 = all and nbumps89 = all | 0 | 0.118910 |
| shift = N and gdenergy = all and gdpuls = all and nbumps <= 1.5 and nbumps4 > 0.5 and nbumps6 = all and nbumps7 = all and nbumps89 = all | 0 | 0.034459 |
| nbumps >= 1.5 and gpuls >= 740.5 and gdenergy >= -29.5 | 0 | 0.415728 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 | 0 | 0.919840 |
| nbumps3 <= 3.5 and gpuls <= 740.5 and gpuls > 98.5 and genergy > 21865.0 and gdpuls <= 41.0 and genergy > 29405.0 and genergy <= 108930.0 and seismoacoustic != b | 0 | 0.276555 |
| nbumps2 > 0.5 and genergy <= 304420.0 and gpuls <= 1451.5 and gpuls <= 740.5 and genergy <= 108930.0 and gpuls > 98.5 and gdpuls <= 11.0 and gdpuls <= 0.0 | 0 | 0.235119 |
| nbumps3 <= 3.5 and gpuls <= 740.5 and gdpuls > 0.5 and gdpuls > 10.5 | 0 | 0.229496 |
| gpuls > 338.0 and nbumps2 <= 0.5 | 0 | 0.162011 |
| gpuls > 338.0 and gdenergy > -29.5 and gdpuls > -23.5 and gpuls > 759.5 and gdpuls > -10.5 and energy > 1850.0 and energy <= 38550.0 and energy <= 22350.0 and gdpuls > 4.5 and gdpuls > 36.5 | 0 | 0.106509 |
| genergy > 19195.0 and gpuls > 338.0 and gdenergy > -29.5 and gdpuls > -23.5 and gpuls > 759.5 and gpuls <= 2211.5 and energy <= 36050.0 and energy <= 5750.0 | 0 | 0.145594 |
| gpuls <= 338.0 | 0 | 0.081090 |
| energy > 40650.0 | 0 | 0.063678 |
| genergy <= 799855.0 and genergy <= 534535.0 and gdenergy <= -29.5 | 1 | 0.511816 |
| gdpuls > -23.5 and nbumps > 3.5 | 0 | 0.081984 |
| gdpuls > -23.5 | 1 | 0.804505 |
|  | 0 | 0.793103 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

shift|gdenergy|gdpuls|nbumps|nbumps4|nbumps6|nbumps7|nbumps89|class
---|---|---|---|---|---|---|---|---
n|all|all|(1.5-inf)|(0.5-inf)|all|all|all|1
w|all|all|(1.5-inf)|(0.5-inf)|all|all|all|0
n|all|all|(-inf-1.5]|(0.5-inf)|all|all|all|0
w|all|all|(-inf-1.5]|(0.5-inf)|all|all|all|0
w|all|all|(1.5-inf)|(-inf-0.5]|all|all|all|0
n|all|all|(1.5-inf)|(-inf-0.5]|all|all|all|0
n|all|all|(-inf-1.5]|(-inf-0.5]|all|all|all|0
w|all|all|(-inf-1.5]|(-inf-0.5]|all|all|all|0

## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5|0 (1855.0/63.0)
nbumps3 <= 3.5 AND gpuls <= 740.5 AND gpuls > 98.5 AND genergy > 21865.0 AND gdpuls <= 41.0 AND genergy > 29405.0 AND genergy <= 108930.0 AND seismoacoustic != b|0 (75.0/7.0)
nbumps2 > 0.5 AND genergy <= 304420.0 AND gpuls <= 1451.5 AND gpuls <= 740.5 AND genergy <= 108930.0 AND gpuls > 98.5 AND gdpuls <= 11.0 AND gdpuls <= 0.0|0 (76.0/15.0)
nbumps3 <= 3.5 AND gpuls <= 740.5 AND gdpuls > 0.5 AND gdpuls > 10.5|0 (62.0/3.0)
gpuls > 338.0 AND nbumps2 <= 0.5|0 (55.0/6.0)
gpuls > 338.0 AND gdenergy > -29.5 AND gdpuls > -23.5 AND gpuls > 759.5 AND gdpuls > -10.5 AND energy > 1850.0 AND energy <= 38550.0 AND energy <= 22350.0 AND gdpuls > 4.5 AND gdpuls > 36.5|0 (30.0/6.0)
genergy > 19195.0 AND gpuls > 338.0 AND gdenergy > -29.5 AND gdpuls > -23.5 AND gpuls > 759.5 AND gpuls <= 2211.5 AND energy <= 36050.0 AND energy <= 5750.0|0 (46.0/8.0)
gpuls <= 338.0|0 (28.0/1.0)
energy > 40650.0|0 (18.0/4.0)
genergy <= 799855.0 AND genergy <= 534535.0 AND gdenergy <= -29.5|1 (17.0/5.0)
gdpuls > -23.5 AND nbumps > 3.5|0 (30.0/12.0)
gdpuls > -23.5|1 (24.0/8.0)
|0 (10.0)


## J48 Decision Tree

* : 0 (2326.0/153.0)


## SimpleCart Decision Tree

* nbumps < 1.5
	* gpuls < 1342.5
		* genergy < 16885.0: 0(784.0/10.0)
		* genergy >= 16885.0: 0(945.0/39.0)
	* gpuls >= 1342.5
		* nbumps3 < 0.5: 0(54.0/6.0)
		* nbumps3 >= 0.5: 0(9.0/8.0)
* nbumps >= 1.5
	* gpuls < 740.5: 0(234.0/36.0)
	* gpuls >= 740.5
		* gdenergy < -29.5
			* nbumps2 < 0.5: 0(9.0/2.0)
			* nbumps2 >= 0.5: 1(15.0/6.0)
		* gdenergy >= -29.5: 0(132.0/37.0)



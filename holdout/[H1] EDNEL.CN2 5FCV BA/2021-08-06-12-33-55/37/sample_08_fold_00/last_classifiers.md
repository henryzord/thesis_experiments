# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| plas <= 123 and pedi <= 0.66 and mass <= 26.4 | 0 | 0.270643 |
| plas <= 123 and pedi <= 0.66 and mass > 26.4 and plas <= 94 | 0 | 0.244457 |
| plas > 123 and age > 24 and skin <= 41 and plas > 154 | 1 | 0.119099 |
| plas <= 123 and pedi <= 0.66 and mass > 26.4 and plas > 94 and skin > 14 and age <= 28 | 0 | 0.170068 |
| plas > 123 and age <= 24 and mass <= 32.8 | 0 | 0.102222 |
| plas <= 123 and pedi > 0.66 and mass <= 26.6 | 0 | 0.070313 |
| plas > 123 and age > 24 and skin > 41 | 1 | 0.041322 |
| plas > 123 and age > 24 and skin <= 41 and plas <= 154 and mass > 26.1 and plas <= 150 and skin <= 33 and pedi > 0.491 | 1 | 0.039683 |
| plas <= 123 and pedi > 0.66 and mass > 26.6 and preg <= 7 and pedi > 0.871 | 0 | 0.060112 |
| plas > 123 and age > 24 and skin <= 41 and plas <= 154 and mass > 26.1 and plas <= 150 and skin <= 33 and pedi <= 0.491 and age <= 40 and preg > 3 | 0 | 0.047732 |
| plas <= 123 and pedi <= 0.66 and mass > 26.4 and plas > 94 and skin > 14 and age > 28 and pedi <= 0.238 | 0 | 0.046620 |
| plas > 123 and age > 24 and skin <= 41 and plas <= 154 and mass > 26.1 and plas <= 150 and skin > 33 | 1 | 0.022753 |
| plas > 123 and age > 24 and skin <= 41 and plas <= 154 and mass <= 26.1 | 0 | 0.038154 |
| plas <= 123 and pedi <= 0.66 and mass > 26.4 and plas > 94 and skin <= 14 and mass <= 29.6 | 0 | 0.038154 |
| plas <= 123 and pedi > 0.66 and mass > 26.6 and preg > 7 | 1 | 0.020031 |
| plas <= 123 and pedi <= 0.66 and mass > 26.4 and plas > 94 and skin <= 14 and mass > 29.6 and mass > 33.7 | 0 | 0.033333 |
| plas > 123 and age > 24 and skin <= 41 and plas <= 154 and mass > 26.1 and plas <= 150 and skin <= 33 and pedi <= 0.491 and age > 40 | 1 | 0.018886 |
| plas <= 123 and pedi > 0.66 and mass > 26.6 and preg <= 7 and pedi <= 0.871 and age <= 28 | 0 | 0.032622 |
| plas > 123 and age > 24 and skin <= 41 and plas <= 154 and mass > 26.1 and plas > 150 | 0 | 0.030462 |
| plas > 123 and age <= 24 and mass > 32.8 and insu <= 160 | 1 | 0.015423 |
| plas <= 123 and pedi <= 0.66 and mass > 26.4 and plas > 94 and skin > 14 and age > 28 and pedi > 0.238 and pres <= 75 | 0 | 0.028505 |
| plas <= 123 and pedi > 0.66 and mass > 26.6 and preg <= 7 and pedi <= 0.871 and age > 28 | 1 | 0.014026 |
| plas <= 123 and pedi <= 0.66 and mass > 26.4 and plas > 94 and skin <= 14 and mass > 29.6 and mass <= 33.7 | 1 | 0.014026 |
| plas > 123 and age <= 24 and mass > 32.8 and insu > 160 | 0 | 0.021164 |
| plas > 123 and age > 24 and skin <= 41 and plas <= 154 and mass > 26.1 and plas <= 150 and skin <= 33 and pedi <= 0.491 and age <= 40 and preg <= 3 | 1 | 0.011396 |
| plas <= 123 and pedi <= 0.66 and mass > 26.4 and plas > 94 and skin > 14 and age > 28 and pedi > 0.238 and pres > 75 | 1 | 0.007959 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| plas <= 123.5 and mass <= 26.45 | 0 | 0.308721 |
| plas > 154.5 | 1 | 0.181280 |
| plas <= 99.5 and age > 25.5 | 0 | 0.224223 |
| plas <= 99.5 | 0 | 0.250567 |
| age <= 29.5 and skin > 5.0 and age <= 24.5 and mass <= 41.8 and age > 21.5 | 0 | 0.206285 |
| pedi <= 0.513 | 0 | 0.400834 |
| preg > 7.5 and pedi <= 1.125 | 1 | 0.394836 |
| insu <= 217.5 | 1 | 0.644501 |
|  | 0 | 0.934783 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
plas <= 123.5 AND mass <= 26.45|0 (87.0/2.0)
plas > 154.5|1 (85.0/15.0)
plas <= 99.5 AND age > 25.5|0 (51.0/10.0)
plas <= 99.5|0 (48.0/1.0)
age <= 29.5 AND skin > 5.0 AND age <= 24.5 AND mass <= 41.8 AND age > 21.5|0 (30.0)
pedi <= 0.513|0 (140.0/48.0)
preg > 7.5 AND pedi <= 1.125|1 (18.0)
insu <= 217.5|1 (69.0/32.0)
|0 (6.0)


## J48 Decision Tree

* plas <= 123
	* pedi <= 0.66
		* mass <= 26.4: 0 (71.0/1.0)
		* mass > 26.4
			* plas <= 94: 0 (66.0/3.0)
			* plas > 94
				* skin <= 14
					* mass <= 29.6: 0 (11.0/2.0)
					* mass > 29.6
						* mass <= 33.7: 1 (13.0/5.0)
						* mass > 33.7: 0 (10.0/2.0)
				* skin > 14
					* age <= 28: 0 (42.0/2.0)
					* age > 28
						* pedi <= 0.238: 0 (11.0/1.0)
						* pedi > 0.238
							* pres <= 75: 0 (9.0/2.0)
							* pres > 75: 1 (9.0/4.0)
	* pedi > 0.66
		* mass <= 26.6: 0 (16.0/1.0)
		* mass > 26.6
			* preg <= 7
				* pedi <= 0.871
					* age <= 28: 0 (13.0/4.0)
					* age > 28: 1 (13.0/5.0)
				* pedi > 0.871: 0 (19.0/4.0)
			* preg > 7: 1 (9.0/1.0)
* plas > 123
	* age <= 24
		* mass <= 32.8: 0 (25.0/2.0)
		* mass > 32.8
			* insu <= 160: 1 (9.0/2.0)
			* insu > 160: 0 (9.0/3.0)
	* age > 24
		* skin <= 41
			* plas <= 154
				* mass <= 26.1: 0 (11.0/2.0)
				* mass > 26.1
					* plas <= 150
						* skin <= 33
							* pedi <= 0.491
								* age <= 40
									* preg <= 3: 1 (9.0/3.0)
									* preg > 3: 0 (13.0/2.0)
								* age > 40: 1 (15.0/5.0)
							* pedi > 0.491: 1 (28.0/8.0)
						* skin > 33: 1 (10.0/1.0)
					* plas > 150: 0 (11.0/3.0)
			* plas > 154: 1 (67.0/11.0)
		* skin > 41: 1 (15.0)



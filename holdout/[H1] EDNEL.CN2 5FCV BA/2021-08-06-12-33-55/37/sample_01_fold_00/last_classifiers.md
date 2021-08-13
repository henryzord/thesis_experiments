# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| plas <= 127.0 | 0 | 0.564942 |
| plas > 127.0 and mass > 29.9 | 1 | 0.191524 |
| plas > 127.0 and mass <= 29.9 | 0 | 0.122696 |
| plas < 127.5 and age >= 28.5 and mass >= 26.35 and pedi < 0.5205 and plas >= 93.5 and mass < 36.55 and pedi < 0.384 | 1 | 0.031943 |
| plas < 127.5 and age >= 28.5 and mass >= 26.35 and pedi >= 0.5205 | 1 | 0.037121 |
| plas >= 127.5 and mass >= 29.95 and plas < 165.5 and pres >= 61.0 and age < 30.5 | 0 | 0.054720 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| plas >= 128 and mass >= 30 | 1 | 0.191524 |
| age >= 29 and insu >= 144 | 1 | 0.022165 |
|  | 0 | 0.851942 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(plas >= 128) and (mass >= 30)|1 (147.0/38.0)
(age >= 29) and (insu >= 144)|1 (25.0/9.0)
|0 (365.0/61.0)


## J48 Decision Tree

* plas <= 127.0: 0 (290.0/53.0)
* plas > 127.0
	* mass <= 29.9: 0 (41.0/12.0)
	* mass > 29.9: 1 (130.0/35.0)


## SimpleCart Decision Tree

* plas < 127.5
	* age < 28.5
		* mass < 30.9: 0(104.0/2.0)
		* mass >= 30.9: 0(67.0/14.0)
	* age >= 28.5
		* mass < 26.35: 0(31.0/1.0)
		* mass >= 26.35
			* pedi < 0.5205
				* plas < 93.5: 0(21.0/1.0)
				* plas >= 93.5
					* mass < 36.55
						* pedi < 0.384: 1(21.0/18.0)
						* pedi >= 0.384: 0(10.0/2.0)
					* mass >= 36.55: 0(15.0/2.0)
			* pedi >= 0.5205: 1(21.0/12.0)
* plas >= 127.5
	* mass < 29.95: 0(35.0/13.0)
	* mass >= 29.95
		* plas < 165.5
			* pres < 61.0: 1(11.0/0.0)
			* pres >= 61.0
				* age < 30.5: 0(18.0/13.0)
				* age >= 30.5
					* mass < 34.8: 1(13.0/10.0)
					* mass >= 34.8: 1(24.0/4.0)
		* plas >= 165.5: 1(48.0/6.0)



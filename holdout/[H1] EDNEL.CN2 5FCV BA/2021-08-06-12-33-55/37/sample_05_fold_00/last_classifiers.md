# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.664804 |
| plas < 144.5 and age < 30.5 and mass < 45.4 and preg >= 6.5 | 1 | 0.007428 |
| plas >= 144.5 and pedi < 0.309 and plas >= 160.0 | 1 | 0.031585 |
| preg <= 6.5 and plas > 144.5 and mass > 27.85 and mass <= 42.85 and age <= 30.5 | 1 | 0.027124 |
| plas < 144.5 and age < 30.5 and mass >= 45.4 | 1 | 0.011542 |
| preg > 6.5 and plas > 144.5 and mass <= 27.85 and age > 30.5 | 1 | 0.007428 |
| preg > 6.5 and plas > 144.5 and mass > 27.85 and mass <= 42.85 and age > 30.5 | 1 | 0.052108 |
| preg > 6.5 and plas > 99.5 and plas <= 144.5 and mass > 27.85 and mass <= 42.85 and age > 30.5 | 1 | 0.031571 |
| plas <= 144.5 and plas > 99.5 and pedi > 0.8985 | 1 | 0.035600 |
| preg <= 6.5 and plas > 144.5 and mass > 42.85 and age > 30.5 | 1 | 0.008889 |
| plas < 144.5 and age < 30.5 and mass < 45.4 and preg < 6.5 and plas >= 130.5 and skin < 7.0 | 1 | 0.011542 |
| plas < 144.5 and age >= 30.5 and mass >= 26.95 and pedi >= 0.52 and plas >= 110.0 | 1 | 0.046501 |
| plas >= 144.5 and pedi >= 0.309 and insu < 335.0 and plas >= 154.5 and pres < 92.0 and age >= 48.0 | 1 | 0.017631 |
| preg <= 6.5 and plas > 99.5 and plas <= 144.5 and mass > 42.85 and age > 30.5 | 1 | 0.012465 |
| preg > 6.5 and plas > 144.5 and mass > 42.85 and age > 30.5 | 1 | 0.008333 |
| preg <= 6.5 and plas > 144.5 and mass > 42.85 and age <= 30.5 | 1 | 0.022192 |
| plas >= 144.5 and pedi >= 0.309 and insu < 335.0 and plas < 154.5 and age >= 39.5 | 1 | 0.019231 |
| preg <= 6.5 and plas > 144.5 and mass > 27.85 and mass <= 42.85 and age > 30.5 | 1 | 0.036331 |
| plas > 144.5 | 1 | 0.146920 |
| plas < 144.5 and age < 30.5 and mass < 45.4 and preg < 6.5 and plas < 130.5 and pedi >= 0.6775 and mass >= 30.15 and insu >= 67.5 and mass < 34.849999999999994 | 1 | 0.013812 |
| plas < 144.5 and age >= 30.5 and mass >= 26.95 and pedi >= 0.52 and plas < 110.0 and preg >= 4.0 | 1 | 0.017212 |
| preg > 6.5 and plas > 99.5 and plas <= 144.5 and mass > 42.85 and age > 30.5 | 1 | 0.013812 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| plas <= 144 and mass > 26.4 and mass <= 45.4 and pedi <= 0.719 and preg <= 6 and age <= 33 | 0 | 0.404984 |
| mass <= 26.4 and plas <= 150 | 0 | 0.359953 |
| plas > 159 | 1 | 0.302166 |
| age > 24 and plas > 96 and mass <= 42.8 and pedi > 0.73 | 1 | 0.161317 |
| mass > 42.8 | 1 | 0.134606 |
| age > 24 and pedi > 0.222 and pres <= 85 and plas <= 96 | 0 | 0.167130 |
| pedi <= 0.722 and pedi <= 0.222 | 0 | 0.176098 |
| pedi <= 0.722 and pres <= 84 and pres <= 78 and mass <= 36.1 and preg <= 8 and plas > 134 | 0 | 0.176098 |
| pedi <= 0.722 and pres <= 84 and plas <= 139 and preg <= 8 and pres <= 74 | 1 | 0.328659 |
| pedi <= 0.682 and pedi <= 0.444 and insu <= 115 | 0 | 0.313043 |
| pedi <= 0.682 | 1 | 0.450682 |
|  | 0 | 0.894737 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| plas >= 155 and pedi >= 0.314 and pedi <= 0.588 | 1 | 0.062992 |
| plas >= 128 and mass >= 30.3 and pedi >= 0.719 and pedi <= 1.072 | 1 | 0.053050 |
| plas >= 128 and mass >= 42 and preg >= 1 | 1 | 0.032520 |
| age >= 31 and mass >= 27.9 and pedi >= 0.465 and preg >= 8 and pres <= 80 | 1 | 0.024590 |
| plas >= 161 and age <= 25 and pres >= 52 | 1 | 0.024590 |
| age >= 31 and mass >= 27.9 and plas >= 109 and preg <= 1 and age <= 42 | 1 | 0.024590 |
| age >= 41 and plas >= 144 and pres >= 82 and plas <= 161 | 1 | 0.019231 |
| age >= 41 and mass >= 27.9 and mass <= 30.5 and age <= 53 and pedi >= 0.158 | 1 | 0.024590 |
| skin <= 0 and mass >= 32 and mass <= 32.9 and plas >= 119 | 1 | 0.016529 |
| mass >= 33.3 and age >= 40 and skin >= 41 and pres >= 68 | 1 | 0.013812 |
| plas >= 102 and mass >= 42.6 and preg >= 5 | 1 | 0.011080 |
|  | 0 | 0.843972 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

preg|plas|mass|age|target
---|---|---|---|---
(6.5-inf)|(144.5-inf)|(42.85-inf)|(30.5-inf)|1
(-inf-6.5]|(144.5-inf)|(42.85-inf)|(30.5-inf)|1
(6.5-inf)|(99.5-144.5]|(42.85-inf)|(30.5-inf)|1
(-inf-6.5]|(99.5-144.5]|(42.85-inf)|(30.5-inf)|1
(6.5-inf)|(-inf-99.5]|(42.85-inf)|(30.5-inf)|0
(-inf-6.5]|(-inf-99.5]|(42.85-inf)|(30.5-inf)|0
(6.5-inf)|(144.5-inf)|(27.85-42.85]|(30.5-inf)|1
(-inf-6.5]|(144.5-inf)|(27.85-42.85]|(30.5-inf)|1
(-inf-6.5]|(144.5-inf)|(42.85-inf)|(-inf-30.5]|1
(6.5-inf)|(99.5-144.5]|(27.85-42.85]|(30.5-inf)|1
(-inf-6.5]|(99.5-144.5]|(27.85-42.85]|(30.5-inf)|0
(-inf-6.5]|(144.5-inf)|(-inf-27.85]|(30.5-inf)|0
(-inf-6.5]|(99.5-144.5]|(42.85-inf)|(-inf-30.5]|0
(6.5-inf)|(-inf-99.5]|(27.85-42.85]|(30.5-inf)|0
(-inf-6.5]|(-inf-99.5]|(27.85-42.85]|(30.5-inf)|0
(6.5-inf)|(144.5-inf)|(-inf-27.85]|(30.5-inf)|1
(-inf-6.5]|(-inf-99.5]|(42.85-inf)|(-inf-30.5]|0
(6.5-inf)|(99.5-144.5]|(-inf-27.85]|(30.5-inf)|0
(-inf-6.5]|(99.5-144.5]|(-inf-27.85]|(30.5-inf)|0
(-inf-6.5]|(144.5-inf)|(27.85-42.85]|(-inf-30.5]|1
(6.5-inf)|(-inf-99.5]|(-inf-27.85]|(30.5-inf)|0
(6.5-inf)|(99.5-144.5]|(27.85-42.85]|(-inf-30.5]|0
(-inf-6.5]|(99.5-144.5]|(27.85-42.85]|(-inf-30.5]|0
(-inf-6.5]|(-inf-99.5]|(-inf-27.85]|(30.5-inf)|0
(-inf-6.5]|(144.5-inf)|(-inf-27.85]|(-inf-30.5]|0
(-inf-6.5]|(-inf-99.5]|(27.85-42.85]|(-inf-30.5]|0
(6.5-inf)|(99.5-144.5]|(-inf-27.85]|(-inf-30.5]|1
(-inf-6.5]|(99.5-144.5]|(-inf-27.85]|(-inf-30.5]|0
(-inf-6.5]|(-inf-99.5]|(-inf-27.85]|(-inf-30.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(plas >= 155) and (pedi >= 0.314) and (pedi <= 0.588)|1 (24.0/0.0)
(plas >= 128) and (mass >= 30.3) and (pedi >= 0.719) and (pedi <= 1.072)|1 (20.0/0.0)
(plas >= 128) and (mass >= 42) and (preg >= 1)|1 (12.0/0.0)
(age >= 31) and (mass >= 27.9) and (pedi >= 0.465) and (preg >= 8) and (pres <= 80)|1 (9.0/0.0)
(plas >= 161) and (age <= 25) and (pres >= 52)|1 (9.0/0.0)
(age >= 31) and (mass >= 27.9) and (plas >= 109) and (preg <= 1) and (age <= 42)|1 (9.0/0.0)
(age >= 41) and (plas >= 144) and (pres >= 82) and (plas <= 161)|1 (7.0/0.0)
(age >= 41) and (mass >= 27.9) and (mass <= 30.5) and (age <= 53) and (pedi >= 0.158)|1 (9.0/0.0)
(skin <= 0) and (mass >= 32) and (mass <= 32.9) and (plas >= 119)|1 (6.0/0.0)
(mass >= 33.3) and (age >= 40) and (skin >= 41) and (pres >= 68)|1 (5.0/0.0)
(plas >= 102) and (mass >= 42.6) and (preg >= 5)|1 (4.0/0.0)
|0 (423.0/66.0)


## PART

Decision list:

rules | predicted class
---|---
plas <= 144 AND mass > 26.4 AND mass <= 45.4 AND pedi <= 0.719 AND preg <= 6 AND age <= 33|0 (155.0/18.0)
mass <= 26.4 AND plas <= 150|0 (109.0/4.0)
plas > 159|1 (74.0/14.0)
age > 24 AND plas > 96 AND mass <= 42.8 AND pedi > 0.73|1 (34.0/6.0)
mass > 42.8|1 (26.0/5.0)
age > 24 AND pedi > 0.222 AND pres <= 85 AND plas <= 96|0 (23.0/6.0)
pedi <= 0.722 AND pedi <= 0.222|0 (19.0/3.0)
pedi <= 0.722 AND pres <= 84 AND pres <= 78 AND mass <= 36.1 AND preg <= 8 AND plas > 134|0 (17.0/4.0)
pedi <= 0.722 AND pres <= 84 AND plas <= 139 AND preg <= 8 AND pres <= 74|1 (17.0/3.0)
pedi <= 0.682 AND pedi <= 0.444 AND insu <= 115|0 (31.0/8.0)
pedi <= 0.682|1 (21.0/7.0)
|0 (11.0)


## J48 Decision Tree

* plas <= 144.5
	* plas <= 99.5: 0 (92.0/4.0)
	* plas > 99.5
		* pedi <= 0.8985: 0 (177.0/47.0)
		* pedi > 0.8985: 1 (17.0/3.0)
* plas > 144.5: 1 (72.0/17.0)


## SimpleCart Decision Tree

* plas < 144.5
	* age < 30.5
		* mass < 45.4
			* preg < 6.5
				* plas < 130.5
					* pedi < 0.6775
						* mass < 30.95
							* preg < 5.5: 0(96.0/0.0)
							* preg >= 5.5: 0(4.0/1.0)
						* mass >= 30.95: 0(78.0/9.0)
					* pedi >= 0.6775
						* mass < 30.15: 0(13.0/1.0)
						* mass >= 30.15
							* insu < 67.5: 0(9.0/1.0)
							* insu >= 67.5
								* mass < 34.849999999999994: 1(5.0/0.0)
								* mass >= 34.849999999999994: 0(3.0/1.0)
				* plas >= 130.5
					* skin < 7.0: 1(5.0/1.0)
					* skin >= 7.0
						* mass < 33.75: 0(12.0/0.0)
						* mass >= 33.75: 0(3.0/3.0)
			* preg >= 6.5: 1(4.0/2.0)
		* mass >= 45.4: 1(5.0/1.0)
	* age >= 30.5
		* mass < 26.95
			* plas < 131.5: 0(28.0/0.0)
			* plas >= 131.5: 0(3.0/1.0)
		* mass >= 26.95
			* pedi < 0.52
				* plas < 96.5: 0(16.0/2.0)
				* plas >= 96.5: 0(41.0/27.0)
			* pedi >= 0.52
				* plas < 110.0
					* preg < 4.0: 0(6.0/2.0)
					* preg >= 4.0: 1(9.0/4.0)
				* plas >= 110.0: 1(20.0/3.0)
* plas >= 144.5
	* pedi < 0.309
		* plas < 160.0: 0(12.0/5.0)
		* plas >= 160.0: 1(17.0/8.0)
	* pedi >= 0.309
		* insu < 335.0
			* plas < 154.5
				* age < 39.5
					* mass < 42.849999999999994: 0(6.0/1.0)
					* mass >= 42.849999999999994: 1(4.0/0.0)
				* age >= 39.5: 1(7.0/0.0)
			* plas >= 154.5
				* pres < 92.0
					* age < 48.0: 1(37.0/0.0)
					* age >= 48.0: 1(8.0/2.0)
				* pres >= 92.0: 0(2.0/2.0)
		* insu >= 335.0: 0(4.0/3.0)



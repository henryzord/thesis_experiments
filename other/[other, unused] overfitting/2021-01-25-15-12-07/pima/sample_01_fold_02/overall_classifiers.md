# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Plas < 127.5 | tested_negative | 0.560030 |
| Plas > 129.0 and Mass > 29.9 | tested_positive | 0.174110 |
| Plas >= 127.5 and Mass < 29.95 | tested_negative | 0.122125 |
| Preg > 6.5 and Plas > 99.5 and Plas <= 123.5 and Mass > 27.35 and Age > 28.5 | tested_positive | 0.029115 |
| Plas >= 127.5 and Mass >= 29.95 and Plas < 157.5 and Age < 30.5 and Pres >= 61.0 and Mass < 41.8 | tested_negative | 0.067522 |
| Preg <= 6.5 and Plas > 123.5 and Plas <= 157.5 and Mass > 27.35 and Age > 28.5 | tested_positive | 0.040562 |
| Preg > 6.5 and Plas > 123.5 and Plas <= 157.5 and Mass > 27.35 and Age > 28.5 | tested_positive | 0.040199 |
| Preg > 6.5 and Plas > 157.5 and Mass <= 27.35 and Age > 28.5 | tested_positive | 0.007064 |
| Plas >= 127.5 and Mass >= 29.95 and Plas < 157.5 and Age < 30.5 and Pres < 61.0 | tested_positive | 0.019608 |
| Plas <= 129.0 and Age > 28.0 and Mass > 26.2 and Plas > 107.0 and Pedi > 0.56 and Preg <= 3.0 and Plas > 121.0 | tested_positive | 0.009178 |
| Plas <= 129.0 and Age > 28.0 and Mass > 26.2 and Plas > 107.0 and Pedi > 0.56 and Preg > 3.0 | tested_positive | 0.026515 |
| Preg <= 6.5 and Plas > 157.5 and Mass > 27.35 and Age > 28.5 | tested_positive | 0.048853 |
| Plas >= 127.5 and Mass >= 29.95 and Plas < 157.5 and Age < 30.5 and Pres >= 61.0 and Mass >= 41.8 | tested_positive | 0.009912 |
| Plas <= 129.0 and Age > 28.0 and Mass > 26.2 and Plas > 107.0 and Pedi <= 0.56 | tested_negative | 0.074727 |
| Preg <= 6.5 and Plas > 123.5 and Plas <= 157.5 and Mass > 27.35 and Age <= 28.5 | tested_negative | 0.087972 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Plas <= 123.0 and Mass > 26.4 and Preg <= 6.0 and Age <= 29.0 | tested_negative | 0.343249 |
| Mass <= 27.3 and Plas <= 151.0 | tested_negative | 0.370908 |
| Plas > 157.0 | tested_positive | 0.298844 |
| Plas <= 94.0 | tested_negative | 0.105646 |
| Preg > 6.0 and Pedi > 0.514 and Preg > 7.0 | tested_positive | 0.150893 |
|  | tested_negative | 0.507463 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Plas >= 155 and Pedi >= 0.328 and Pres <= 76 and Pedi <= 0.615 | tested_positive | 0.050633 |
| Mass >= 30 and Plas >= 158 and Pres >= 72 and Mass <= 40 and Pres <= 92 | tested_positive | 0.060543 |
| Plas >= 124 and Mass >= 41.8 and Insu <= 250 and Pedi >= 0.431 | tested_positive | 0.034335 |
| Plas >= 124 and Age <= 54 and Age >= 41 and Mass <= 34.4 and Plas <= 133 | tested_positive | 0.021739 |
| Plas >= 128 and Preg >= 7 and Age >= 41 and Mass >= 34.9 | tested_positive | 0.030172 |
| Age >= 29 and Plas >= 108 and Mass >= 27.9 and Pedi >= 0.734 and Mass <= 36.5 and Pres >= 76 | tested_positive | 0.023861 |
| Plas >= 113 and Mass >= 28.9 and Insu <= 0 and Pres <= 76 and Age >= 38 and Pres >= 72 | tested_positive | 0.013158 |
| Plas >= 113 and Mass >= 41.8 and Skin >= 37 and Age >= 27 | tested_positive | 0.019608 |
| Pres <= 0 and Plas >= 131 | tested_positive | 0.019608 |
| Age >= 29 and Plas >= 100 and Pres <= 70 and Skin >= 23 and Skin <= 32 and Age <= 33 and Mass <= 39.1 | tested_positive | 0.017467 |
|  | tested_negative | 0.812274 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

preg|plas|mass|age|class
---|---|---|---|---
(6.5-inf)|(157.5-inf)|(27.35-inf)|(28.5-inf)|tested_positive
(-inf-6.5]|(157.5-inf)|(27.35-inf)|(28.5-inf)|tested_positive
(6.5-inf)|(123.5-157.5]|(27.35-inf)|(28.5-inf)|tested_positive
(-inf-6.5]|(123.5-157.5]|(27.35-inf)|(28.5-inf)|tested_positive
(-inf-6.5]|(157.5-inf)|(-inf-27.35]|(28.5-inf)|tested_negative
(6.5-inf)|(157.5-inf)|(-inf-27.35]|(28.5-inf)|tested_positive
(6.5-inf)|(99.5-123.5]|(27.35-inf)|(28.5-inf)|tested_positive
(-inf-6.5]|(99.5-123.5]|(27.35-inf)|(28.5-inf)|tested_negative
(6.5-inf)|(123.5-157.5]|(-inf-27.35]|(28.5-inf)|tested_negative
(-inf-6.5]|(-inf-99.5]|(27.35-inf)|(28.5-inf)|tested_negative
(6.5-inf)|(-inf-99.5]|(27.35-inf)|(28.5-inf)|tested_negative
(-inf-6.5]|(157.5-inf)|(27.35-inf)|(-inf-28.5]|tested_positive
(-inf-6.5]|(123.5-157.5]|(-inf-27.35]|(28.5-inf)|tested_negative
(-inf-6.5]|(123.5-157.5]|(27.35-inf)|(-inf-28.5]|tested_negative
(6.5-inf)|(99.5-123.5]|(-inf-27.35]|(28.5-inf)|tested_negative
(-inf-6.5]|(99.5-123.5]|(-inf-27.35]|(28.5-inf)|tested_negative
(6.5-inf)|(99.5-123.5]|(27.35-inf)|(-inf-28.5]|tested_negative
(6.5-inf)|(-inf-99.5]|(-inf-27.35]|(28.5-inf)|tested_negative
(-inf-6.5]|(157.5-inf)|(-inf-27.35]|(-inf-28.5]|tested_negative
(-inf-6.5]|(-inf-99.5]|(-inf-27.35]|(28.5-inf)|tested_negative
(-inf-6.5]|(99.5-123.5]|(27.35-inf)|(-inf-28.5]|tested_negative
(-inf-6.5]|(-inf-99.5]|(27.35-inf)|(-inf-28.5]|tested_negative
(-inf-6.5]|(123.5-157.5]|(-inf-27.35]|(-inf-28.5]|tested_negative
(6.5-inf)|(99.5-123.5]|(-inf-27.35]|(-inf-28.5]|tested_negative
(-inf-6.5]|(99.5-123.5]|(-inf-27.35]|(-inf-28.5]|tested_negative
(-inf-6.5]|(-inf-99.5]|(-inf-27.35]|(-inf-28.5]|tested_negative

## JRip

Decision list:

rules | predicted class
---|---
(Plas >= 155) and (Pedi >= 0.328) and (Pres <= 76) and (Pedi <= 0.615)|tested_positive (24.0/0.0)
(Mass >= 30) and (Plas >= 158) and (Pres >= 72) and (Mass <= 40) and (Pres <= 92)|tested_positive (29.0/0.0)
(Plas >= 124) and (Mass >= 41.8) and (Insu <= 250) and (Pedi >= 0.431)|tested_positive (16.0/0.0)
(Plas >= 124) and (Age <= 54) and (Age >= 41) and (Mass <= 34.4) and (Plas <= 133)|tested_positive (10.0/0.0)
(Plas >= 128) and (Preg >= 7) and (Age >= 41) and (Mass >= 34.9)|tested_positive (14.0/0.0)
(Age >= 29) and (Plas >= 108) and (Mass >= 27.9) and (Pedi >= 0.734) and (Mass <= 36.5) and (Pres >= 76)|tested_positive (11.0/0.0)
(Plas >= 113) and (Mass >= 28.9) and (Insu <= 0) and (Pres <= 76) and (Age >= 38) and (Pres >= 72)|tested_positive (6.0/0.0)
(Plas >= 113) and (Mass >= 41.8) and (Skin >= 37) and (Age >= 27)|tested_positive (9.0/0.0)
(Pres <= 0) and (Plas >= 131)|tested_positive (9.0/0.0)
(Age >= 29) and (Plas >= 100) and (Pres <= 70) and (Skin >= 23) and (Skin <= 32) and (Age <= 33) and (Mass <= 39.1)|tested_positive (8.0/0.0)
|tested_negative (554.0/104.0)


## PART

Decision list:

rules | predicted class
---|---
Plas <= 123.0 AND Mass > 26.4 AND Preg <= 6.0 AND Age <= 29.0|tested_negative (160.0/19.0)
Mass <= 27.3 AND Plas <= 151.0|tested_negative (155.0/7.0)
Plas > 157.0|tested_positive (100.0/18.0)
Plas <= 94.0|tested_negative (29.0/4.0)
Preg > 6.0 AND Pedi > 0.514 AND Preg > 7.0|tested_positive (26.0/1.0)
|tested_negative (220.0/103.0)


## J48 Decision Tree

* Plas <= 129.0
	* Age <= 28.0: tested_negative (197.0/17.0)
	* Age > 28.0
		* Mass <= 26.2: tested_negative (28.0/2.0)
		* Mass > 26.2
			* Plas <= 107.0: tested_negative (54.0/14.0)
			* Plas > 107.0
				* Pedi <= 0.56: tested_negative (41.0/19.0)
				* Pedi > 0.56
					* Preg <= 3.0
						* Plas <= 121.0: tested_negative (5.0/2.0)
						* Plas > 121.0: tested_positive (5.0/1.0)
					* Preg > 3.0: tested_positive (12.0)
* Plas > 129.0
	* Mass <= 29.9: tested_negative (46.0/15.0)
	* Mass > 29.9: tested_positive (130.0/35.0)


## SimpleCart Decision Tree

* Plas < 127.5: tested_negative(353.0/85.0)
* Plas >= 127.5
	* Mass < 29.95: tested_negative(47.0/21.0)
	* Mass >= 29.95
		* Plas < 157.5
			* Age < 30.5
				* Pres < 61.0: tested_positive(9.0/0.0)
				* Pres >= 61.0
					* Mass < 41.8: tested_negative(22.0/6.0)
					* Mass >= 41.8: tested_positive(6.0/2.0)
			* Age >= 30.5: tested_positive(40.0/15.0)
		* Plas >= 157.5: tested_positive(73.0/11.0)



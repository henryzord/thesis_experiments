# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Pulse5 > 0.041 and Pulse3 > 0.101 and Pulse4 > -0.542 and Pulse6 > -0.227 | g | 0.619773 |
| Pulse5 < 0.2275 | b | 0.235350 |
| Pulse5 >= 0.2275 and Pulse27 >= 0.999 | b | 0.119469 |
| Pulse5 >= 0.2275 and Pulse27 < 0.999 | g | 0.607101 |
| Pulse5 > 0.041 and Pulse3 > 0.101 and Pulse4 > -0.542 and Pulse6 <= -0.227 | b | 0.047115 |
| Pulse5 > 0.041 and Pulse3 > 0.101 and Pulse4 <= -0.542 | b | 0.048518 |
| Pulse29 > 0.997 and Pulse30 > -0.9145 and Pulse30 <= 0.9305 | g | 0.063689 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Pulse5 > 0.041 and Pulse1 > 0 and Pulse3 > 0.214 and Pulse8 > -0.399 and Pulse16 <= 0.863 and Pulse5 > 0.413 | g | 0.604638 |
| Pulse5 <= 0.041 | b | 0.722892 |
| Pulse27 > 0.925 | b | 0.611864 |
| Pulse7 > 0.014 and Pulse10 > 0.449 | g | 0.387821 |
| Pulse21 <= 0.249 | b | 0.443223 |
|  | g | 0.705882 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

pulse29|pulse30|class
---|---|---
(0.997-inf)|(0.9305-inf)|b
(0.068-0.997]|(0.9305-inf)|g
(-inf--0.912]|(0.9305-inf)|b
(0.997-inf)|(-0.9145-0.9305]|g
(-inf--0.912]|(-0.9145-0.9305]|b
(-0.0015-0.068]|(-0.9145-0.9305]|b
(-0.912--0.0015]|(-0.9145-0.9305]|g
(0.068-0.997]|(-0.9145-0.9305]|g
(-0.912--0.0015]|(-inf--0.9145]|b
(0.997-inf)|(-inf--0.9145]|b
(-inf--0.912]|(-inf--0.9145]|b
(0.068-0.997]|(-inf--0.9145]|g

## PART

Decision list:

rules | predicted class
---|---
Pulse5 > 0.041 AND Pulse1 > 0 AND Pulse3 > 0.214 AND Pulse8 > -0.399 AND Pulse16 <= 0.863 AND Pulse5 > 0.413|g (184.0/5.0)
Pulse5 <= 0.041|b (60.0)
Pulse27 > 0.925|b (40.0/2.0)
Pulse7 > 0.014 AND Pulse10 > 0.449|g (10.0)
Pulse21 <= 0.249|b (12.0/2.0)
|g (10.0/1.0)


## J48 Decision Tree

* Pulse5 <= 0.041: b (52.0)
* Pulse5 > 0.041
	* Pulse3 <= 0.101: b (16.0)
	* Pulse3 > 0.101
		* Pulse4 <= -0.542: b (12.0/1.0)
		* Pulse4 > -0.542
			* Pulse6 <= -0.227: b (13.0/4.0)
			* Pulse6 > -0.227: g (160.0/3.0)


## SimpleCart Decision Tree

* Pulse5 < 0.2275: b(65.0/3.0)
* Pulse5 >= 0.2275
	* Pulse27 < 0.999: g(187.0/13.0)
	* Pulse27 >= 0.999: b(36.0/12.0)



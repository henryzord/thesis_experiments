# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Node-caps = no | no-recurrence-events | 0.646446 |
| Node-caps = yes and Deg-malig = 3 | recurrence-events | 0.083761 |
| Node-caps = yes and Deg-malig = 2 | no-recurrence-events | 0.134419 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Deg-malig != 3 | no-recurrence-events | 0.624443 |
| Inv-nodes != 6-8 and Tumor-size != 40-44 and Breast-quad != right_up and Age != 30-39 and Inv-nodes = 0-2 | no-recurrence-events | 0.125707 |
|  | recurrence-events | 0.836957 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

node-caps|deg-malig|class
---|---|---
yes|3|recurrence-events
no|3|no-recurrence-events
?|3|no-recurrence-events
?|2|no-recurrence-events
yes|2|no-recurrence-events
no|2|no-recurrence-events
?|1|recurrence-events
no|1|no-recurrence-events

## PART

Decision list:

rules | predicted class
---|---
Deg-malig != 3|no-recurrence-events (159.0/31.0)
Inv-nodes != 6-8 AND Tumor-size != 40-44 AND Breast-quad != right_up AND Age != 30-39 AND Inv-nodes = 0-2|no-recurrence-events (25.88/7.88)
|recurrence-events (44.13/14.0)


## J48 Decision Tree

* Node-caps = yes
	* Deg-malig = 1: recurrence-events (0.83/0.21)
	* Deg-malig = 2: no-recurrence-events (25.21/8.0)
	* Deg-malig = 3: recurrence-events (27.42/6.42)
* Node-caps = no: no-recurrence-events (203.54/47.38)


## SimpleCart Decision Tree

* : no-recurrence-events(180.0/77.0)



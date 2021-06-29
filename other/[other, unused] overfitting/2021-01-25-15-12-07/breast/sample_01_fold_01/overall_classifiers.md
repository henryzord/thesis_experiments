# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | no-recurrence-events | 0.700389 |
| Node-caps = yes and Deg-malig = 3 | recurrence-events | 0.083761 |
| Inv-nodes != 0-2 and Deg-malig != 3 and Breast = left and Age != 50-59 | recurrence-events | 0.027799 |
| Inv-nodes != 0-2 and Deg-malig = 3 | recurrence-events | 0.093788 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Node-caps = no and Inv-nodes = 0-2 | no-recurrence-events | 0.622628 |
|  | recurrence-events | 0.681416 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

node-caps|deg-malig|class
---|---|---
?|3|no-recurrence-events
yes|3|recurrence-events
no|3|no-recurrence-events
?|2|no-recurrence-events
yes|2|no-recurrence-events
no|2|no-recurrence-events
?|1|recurrence-events
no|1|no-recurrence-events

## PART

Decision list:

rules | predicted class
---|---
Node-caps = no AND Inv-nodes = 0-2|no-recurrence-events (156.32/31.55)
|recurrence-events (72.68/35.23)


## J48 Decision Tree

* Inv-nodes = 0-2: no-recurrence-events (190.0/40.0)
* Inv-nodes != 0-2
	* Deg-malig = 3: recurrence-events (34.0/9.0)
	* Deg-malig != 3
		* Breast = left
			* Age = 50-59: no-recurrence-events (6.0/1.0)
			* Age != 50-59: recurrence-events (7.0/1.0)
		* Breast != left: no-recurrence-events (20.0/5.0)


## SimpleCart Decision Tree

* : no-recurrence-events(180.0/77.0)



# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 and Age <= -0.228 and Class > -1.87 and Class <= 0.0214 and Class > -0.923 | -1.0 | 0.312966 |
| Sex > -1.92 and Age <= -0.228 and Class > -1.87 and Class > -0.923 | -1.0 | 0.431742 |
| Sex > -1.92 and Class > -1.87 and Age <= -0.228 | -1.0 | 0.088012 |
| Sex <= -1.92 and Class <= -0.923 and Class <= -1.87 | 1.0 | 0.327353 |
| Sex > -1.92 and Age <= -0.228 | -1.0 | 0.088499 |
| Class <= -0.923 and Age <= -0.228 | 1.0 | 0.442668 |
| Class > -0.923 and Class <= 0.0214 and Sex <= -1.92 and Age <= -0.228 | -1.0 | 0.120495 |
| Class > -0.923 and Class <= 0.0214 and Sex > -1.92 | -1.0 | 0.029199 |
| Class > -0.923 and Class <= 0.0214 | -1.0 | 0.006181 |
| Class <= -0.923 | 1.0 | 0.556842 |
|  | 1.0 | 0.954424 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
Sex > -1.92 AND Age <= -0.228 AND Class > -1.87 AND Class <= 0.0214 AND Class > -0.923|-1.0 (408.0/66.0)
Sex > -1.92 AND Age <= -0.228 AND Class > -1.87 AND Class > -0.923|-1.0 (784.0/177.0)
Sex > -1.92 AND Class > -1.87 AND Age <= -0.228|-1.0 (145.0/12.0)
Sex <= -1.92 AND Class <= -0.923 AND Class <= -1.87|1.0 (130.0/2.0)
Sex > -1.92 AND Age <= -0.228|-1.0 (157.0/50.0)
Class <= -0.923 AND Age <= -0.228|1.0 (84.0/13.0)
Class > -0.923 AND Class <= 0.0214 AND Sex <= -1.92 AND Age <= -0.228|-1.0 (155.0/69.0)
Class > -0.923 AND Class <= 0.0214 AND Sex > -1.92|-1.0 (46.0/13.0)
Class > -0.923 AND Class <= 0.0214|-1.0 (29.0/13.0)
Class <= -0.923|1.0 (23.0)
|1.0 (20.0/2.0)



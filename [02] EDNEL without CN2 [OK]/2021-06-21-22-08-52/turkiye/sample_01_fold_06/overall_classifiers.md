# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| instr = 1 and difficulty != 4 and difficulty != 5 and Q16 != 1 | 10 | 0.044166 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 = 1 | 13 | 0.009438 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty = 1 | 6 | 0.008593 |
| instr != 1 and instr != 2 and difficulty = 2 | 13 | 0.008784 |
| instr != 1 and instr = 2 and difficulty = 4 and Q15 != 1 and Q6 != 2 and Q8 != 2 and Q6 != 1 and Q15 != 2 and Q11 != 2 and Q3 != 2 and attendance != 0 | 11 | 0.008282 |
| instr = 2 and difficulty = 3 and Q21 = 4 | 6 | 0.007497 |
| instr = 3 and difficulty = 1 and Q21 = 3 | 3 | 0.006955 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat != 1 and Q11 != 1 and Q14 != 1 and Q15 != 1 and Q22 != 1 and Q19 != 1 and Q5 != 5 | 9 | 0.005964 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 != 2 and Q1 != 1 and Q9 != 5 and Q15 != 5 and Q6 != 2 and Q20 != 2 and Q26 != 2 and Q17 != 2 and difficulty != 1 and attendance != 0 and Q11 != 2 | 3 | 0.005587 |
| instr!=(3) and instr = 3 and difficulty != 4 and difficulty!=(2) and difficulty != 5 and attendance!=(1) and Q4 != 2 and Q6!=(3) and Q5!=(2) and Q12!=(2) and Q26!=(4) and Q9 = 3 and Q13!=(3) and Q23 != 2 | 13 | 0.007126 |
| instr = 3 and difficulty = 4 and Q21 = 4 | 5 | 0.003936 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance = 4 and Q2 != 1 and Q23 != 1 and Q27 != 1 and Q1 != 1 and Q14 != 2 and Q15 != 2 and Q6 != 2 and Q1 != 2 and Q16 != 2 | 3 | 0.004496 |
| instr = 2 and difficulty = 3 and Q21 = 3 | 6 | 0.004400 |
| instr = 2 and difficulty = 3 and Q21 = 5 | 6 | 0.004297 |
| instr = 1 and difficulty != 4 and difficulty = 5 and attendance != 4 and Q11 != 4 | 7 | 0.004060 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat != 1 and Q11 = 1 | 13 | 0.003816 |
| instr = 2 and difficulty = 2 and Q21 = 4 | 6 | 0.003844 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty = 5 and Q3 != 2 and nb.repeat != 2 | 11 | 0.003613 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty = 3 and Q1 != 1 and Q20 != 5 and Q16 != 2 and Q24 != 2 and Q20 != 2 and Q22 != 2 and Q18 != 2 and Q11 != 2 and Q7 != 2 and Q23 != 2 and Q8 != 2 and attendance = 2 | 3 | 0.003245 |
| instr != 1 and instr = 2 and difficulty = 4 and Q15 != 1 and Q6 = 2 | 11 | 0.003377 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 = 2 | 3 | 0.003947 |
| instr = 3 and difficulty = 3 and Q21 = 5 | 8 | 0.002925 |
| instr = 3 and difficulty = 5 and Q21 = 1 | 3 | 0.002313 |
| instr = 1 and difficulty = 4 and nb.repeat != 3 and Q18 != 2 and Q4 = 2 | 7 | 0.003160 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 = 1 | 5 | 0.003522 |
| instr = 3 and difficulty = 1 and Q21 = 4 | 3 | 0.003093 |
| instr = 2 and difficulty = 2 and Q21 = 3 | 6 | 0.002760 |
| instr = 1 and difficulty = 4 and nb.repeat = 3 | 7 | 0.002582 |
| instr = 1 and difficulty = 1 and Q21 = 1 | 10 | 0.002743 |
| instr = 3 and difficulty = 1 and Q21 = 5 | 13 | 0.002372 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 != 2 and Q16 != 3 and Q18 != 3 and Q8 != 2 and Q11 != 2 and Q11 != 3 and Q4 != 2 and Q24 != 3 and Q1 != 2 and Q15 = 5 and Q13 != 4 and Q9 != 3 and Q9 != 4 and Q4 != 4 and Q3 != 3 and Q1 != 4 and Q24 = 5 and difficulty != 5 and Q7 != 4 and attendance != 2 | 5 | 0.001908 |
| instr = 3 and difficulty = 4 and Q21 = 5 | 8 | 0.001895 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 = 2 | 6 | 0.003089 |
| instr = 1 and difficulty = 4 and nb.repeat != 3 and Q18 != 2 and Q4 != 2 and Q5 != 2 and Q16 != 2 and Q10 != 2 and Q12 != 2 and Q24 != 3 and Q22 != 3 and Q1 != 3 and Q4 != 3 and Q1 != 2 and Q1 != 4 | 2 | 0.001927 |
| instr = 3 and difficulty = 4 and Q21 = 3 | 3 | 0.005019 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 = 1 and Q3 != 5 and Q5 != 4 and Q6 != 4 and Q22 != 2 and Q10 != 4 and Q7 != 3 and Q17 != 2 | 8 | 0.001946 |
| instr = 3 and difficulty = 2 and Q21 = 4 | 8 | 0.001328 |
| instr = 2 and difficulty = 2 and Q21 = 5 | 6 | 0.001915 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat != 1 and Q11 != 1 and Q14 != 1 and Q15 != 1 and Q22 != 1 and Q19 != 1 and Q5 = 5 | 13 | 0.001803 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance = 4 and Q2 != 1 and Q23 != 1 and Q27 != 1 and Q1 != 1 and Q14 != 2 and Q15 != 2 and Q6 != 2 and Q1 = 2 | 8 | 0.002050 |
| instr = 1 and difficulty != 4 and difficulty = 5 and attendance = 4 | 10 | 0.001768 |
| instr = 3 and difficulty = 3 and Q21 = 3 | 3 | 0.002788 |
| instr != 1 and instr = 2 and difficulty = 4 and Q15 != 1 and Q6 != 2 and Q8 != 2 and Q6 != 1 and Q15 != 2 and Q11 != 2 and Q3 != 2 and attendance = 0 and Q13 != 5 | 11 | 0.001538 |
| instr = 2 and difficulty = 4 and Q21 = 1 | 6 | 0.001629 |
| instr != 1 and instr = 2 and difficulty = 4 and Q15 != 1 and Q6 != 2 and Q8 != 2 and Q6 = 1 | 11 | 0.001462 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 = 2 | 11 | 0.001209 |
| instr = 3 and difficulty = 3 and Q21 = 4 | 3 | 0.003465 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 = 1 | 8 | 0.001381 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 != 1 and Q27 != 1 and attendance != 0 and Q1 != 1 and Q2 != 2 and Q1 != 2 and difficulty != 2 and nb.repeat != 2 and Q16 != 4 and Q13 != 4 and Q12 != 4 and Q10 != 4 and Q6 != 4 and nb.repeat = 1 and Q19 != 4 and attendance = 2 and Q1 = 3 | 11 | 0.000892 |
| instr = 1 and difficulty = 4 and Q21 = 4 | 7 | 0.002393 |
| instr = 1 and difficulty = 4 and nb.repeat != 3 and Q18 != 2 and Q4 != 2 and Q5 != 2 and Q16 != 2 and Q10 != 2 and Q12 != 2 and Q24 != 3 and Q22 != 3 and Q1 != 3 and Q4 != 3 and Q1 != 2 and Q1 = 4 | 10 | 0.001235 |
| instr = 3 and difficulty = 4 and Q21 = 2 | 3 | 0.001907 |
| instr = 1 and difficulty = 4 and nb.repeat != 3 and Q18 != 2 and Q4 != 2 and Q5 != 2 and Q16 != 2 and Q10 != 2 and Q12 != 2 and Q24 = 3 and attendance != 1 | 10 | 0.001395 |
| instr = 1 and difficulty = 4 and Q21 = 3 | 7 | 0.002886 |
| instr = 3 and difficulty = 5 and Q21 = 5 | 3 | 0.001306 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 = 2 | 11 | 0.000941 |
| instr = 3 and difficulty = 5 and Q21 = 3 | 3 | 0.004312 |
| instr = 3 and difficulty = 3 and Q21 = 2 | 3 | 0.001179 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 = 1 | 9 | 0.000850 |
| instr = 1 and difficulty = 3 and Q21 = 1 | 10 | 0.001423 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 = 3 | 5 | 0.000864 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 != 2 and Q16 != 3 and Q18 != 3 and Q8 != 2 and Q11 != 2 and Q11 != 3 and Q4 != 2 and Q24 != 3 and Q1 != 2 and Q15 = 5 and Q13 != 4 and Q9 != 3 and Q9 != 4 and Q4 != 4 and Q3 != 3 and Q1 != 4 and Q24 = 5 and difficulty = 5 and attendance = 3 | 5 | 0.000772 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance = 4 and Q2 != 1 and Q23 != 1 and Q27 != 1 and Q1 != 1 and Q14 = 2 | 5 | 0.000922 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 = 1 and Q3 != 5 and Q5 != 4 and Q6 != 4 and Q22 = 2 and Q17 = 4 | 4 | 0.000792 |
| instr = 3 and difficulty = 4 and Q21 = 1 | 3 | 0.000829 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 != 1 and Q27 != 1 and attendance != 0 and Q1 != 1 and Q2 != 2 and Q1 != 2 and difficulty != 2 and nb.repeat != 2 and Q16 != 4 and Q13 != 4 and Q12 != 4 and Q10 != 4 and Q6 != 4 and nb.repeat = 1 and Q19 != 4 and attendance != 2 and Q2 != 3 and Q14 = 5 and attendance = 4 and Q1 = 5 | 1 | 0.000648 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 = 2 | 11 | 0.000854 |
| instr = 3 and difficulty = 1 and Q21 = 2 | 3 | 0.002935 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 = 1 | 9 | 0.000744 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 = 5 | 5 | 0.001081 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 != 1 and Q27 != 1 and attendance != 0 and Q1 != 1 and Q2 != 2 and Q1 != 2 and difficulty = 2 and Q2 = 4 and Q17 = 5 | 1 | 0.000808 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 = 2 and attendance != 1 and Q27 != 2 | 9 | 0.000749 |
| instr = 1 and difficulty = 5 and Q21 = 5 | 2 | 0.000416 |
| instr = 2 and difficulty = 3 and Q21 = 1 | 6 | 0.001132 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 = 1 and Q9 != 4 and Q1 != 5 and Q19 != 4 and Q11 = 1 and Q2 != 3 and Q1 = 1 and attendance != 3 and nb.repeat = 1 and difficulty != 2 | 1 | 0.000505 |
| instr = 2 and difficulty = 5 and Q21 = 1 | 6 | 0.000587 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 = 1 and Q3 != 5 and Q5 != 4 and Q6 != 4 and Q22 = 2 and Q17 != 4 | 13 | 0.000577 |
| instr = 1 and difficulty != 4 and difficulty = 5 and attendance != 4 and Q11 = 4 and attendance != 1 | 10 | 0.000830 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance = 4 and Q2 != 1 and Q23 != 1 and Q27 != 1 and Q1 != 1 and Q14 != 2 and Q15 != 2 and Q6 = 2 | 8 | 0.001027 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty = 5 and Q3 = 2 | 11 | 0.000747 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat != 1 and Q11 != 1 and Q14 = 1 | 5 | 0.000599 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 = 5 | 5 | 0.000576 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 != 2 and Q16 != 3 and Q18 != 3 and Q8 != 2 and Q11 = 2 | 5 | 0.000691 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty = 3 and Q1 != 1 and Q20 != 5 and Q16 != 2 and Q24 != 2 and Q20 != 2 and Q22 != 2 and Q18 = 2 | 5 | 0.000648 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 = 2 | 1 | 0.000404 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 = 2 | 11 | 0.000523 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 = 2 | 1 | 0.000562 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 != 2 and Q1 != 1 and Q9 != 5 and Q15 != 5 and Q6 != 2 and Q20 != 2 and Q26 != 2 and Q17 != 2 and difficulty != 1 and attendance = 0 and Q16 != 3 and difficulty != 4 | 13 | 0.000672 |
| instr != 1 and instr = 2 and difficulty = 4 and Q15 != 1 and Q6 != 2 and Q8 = 2 | 11 | 0.000627 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 = 2 | 1 | 0.000455 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 = 1 and Q9 != 4 and Q1 = 5 | 11 | 0.000627 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 = 2 | 11 | 0.000376 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 = 1 | 1 | 0.000364 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 != 1 and Q27 != 1 and attendance != 0 and Q1 != 1 and Q2 != 2 and Q1 != 2 and difficulty != 2 and nb.repeat != 2 and Q16 != 4 and Q13 != 4 and Q12 != 4 and Q10 != 4 and Q6 = 4 | 1 | 0.000606 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 != 1 and Q27 != 1 and attendance != 0 and Q1 != 1 and Q2 = 2 | 1 | 0.000303 |
| instr = 1 and difficulty = 4 and nb.repeat != 3 and Q18 != 2 and Q4 != 2 and Q5 != 2 and Q16 != 2 and Q10 != 2 and Q12 = 2 | 10 | 0.000553 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance = 4 and Q2 != 1 and Q23 != 1 and Q27 = 1 | 5 | 0.000576 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 != 2 and Q16 != 3 and Q18 != 3 and Q8 != 2 and Q11 != 2 and Q11 != 3 and Q4 != 2 and Q24 != 3 and Q1 != 2 and Q15 != 5 | 5 | 0.000600 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 = 1 and Q3 != 5 and Q5 != 4 and Q6 = 4 and Q20 = 4 | 9 | 0.000486 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 = 1 and Q9 != 4 and Q1 != 5 and Q19 != 4 and Q11 = 1 and Q2 != 3 and Q1 = 1 and attendance != 3 and nb.repeat = 1 and difficulty = 2 | 6 | 0.000636 |
| instr != 1 and instr = 2 and difficulty = 4 and Q15 != 1 and Q6 != 2 and Q8 != 2 and Q6 != 1 and Q15 = 2 | 6 | 0.000847 |
| instr = 1 and difficulty != 4 and difficulty != 5 and Q16 = 1 and Q11 = 3 | 7 | 0.000594 |
| instr = 1 and difficulty != 4 and difficulty != 5 and Q16 = 1 and Q11 != 3 and nb.repeat = 1 and Q3 = 1 and Q4 = 1 and difficulty != 2 and Q1 = 1 and Q23 = 1 and difficulty != 1 and attendance = 2 | 7 | 0.000594 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 != 2 and Q16 != 3 and Q18 != 3 and Q8 != 2 and Q11 != 2 and Q11 != 3 and Q4 != 2 and Q24 != 3 and Q1 != 2 and Q15 = 5 and Q13 != 4 and Q9 != 3 and Q9 = 4 | 13 | 0.000807 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 = 2 | 1 | 0.000294 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 = 2 | 3 | 0.000907 |
| instr = 1 and difficulty = 4 and nb.repeat != 3 and Q18 = 2 | 10 | 0.000577 |
| instr = 1 and difficulty = 4 and Q21 = 2 | 2 | 0.000286 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance = 1 | 5 | 0.000425 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 = 2 | 11 | 0.000436 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat != 1 and Q11 != 1 and Q14 != 1 and Q15 != 1 and Q22 != 1 and Q19 = 1 | 9 | 0.000486 |
| instr = 1 and difficulty = 2 and Q21 = 1 | 10 | 0.000553 |
| instr = 3 and difficulty = 5 and Q21 = 4 | 3 | 0.001764 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty = 3 and Q1 != 1 and Q20 != 5 and Q16 != 2 and Q24 != 2 and Q20 != 2 and Q22 != 2 and Q18 != 2 and Q11 = 2 | 5 | 0.000486 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 = 1 | 5 | 0.000486 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty = 3 and Q1 != 1 and Q20 != 5 and Q16 = 2 and Q18 = 3 | 5 | 0.000486 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 != 2 and Q1 != 1 and Q9 != 5 and Q15 != 5 and Q6 != 2 and Q20 != 2 and Q26 != 2 and Q17 != 2 and difficulty = 1 and attendance != 3 and Q19 != 3 and Q22 = 3 | 5 | 0.000389 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance = 4 and Q2 = 1 | 5 | 0.000389 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 != 2 and Q1 != 1 and Q9 != 5 and Q15 != 5 and Q6 != 2 and Q20 != 2 and Q26 != 2 and Q17 != 2 and difficulty = 1 and attendance = 3 and Q1 != 3 | 9 | 0.000382 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 = 1 | 13 | 0.000577 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 != 1 and Q27 != 1 and attendance != 0 and Q1 != 1 and Q2 != 2 and Q1 != 2 and difficulty != 2 and nb.repeat != 2 and Q16 != 4 and Q13 = 4 | 11 | 0.000269 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 = 2 | 11 | 0.000470 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 != 1 and Q27 != 1 and attendance != 0 and Q1 != 1 and Q2 != 2 and Q1 != 2 and difficulty != 2 and nb.repeat != 2 and Q16 != 4 and Q13 != 4 and Q12 = 4 and attendance != 2 | 1 | 0.000364 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 = 2 | 1 | 0.000364 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 = 1 and Q3 != 5 and Q5 != 4 and Q6 != 4 and Q22 != 2 and Q10 != 4 and Q7 = 3 | 9 | 0.000409 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 = 1 and Q9 != 4 and Q20 != 3 | 5 | 0.000432 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 = 1 | 5 | 0.000384 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 != 2 and Q16 != 3 and Q18 != 3 and Q8 != 2 and Q11 != 2 and Q11 != 3 and Q4 != 2 and Q24 != 3 and Q1 != 2 and Q15 = 5 and Q13 != 4 and Q9 != 3 and Q9 != 4 and Q4 != 4 and Q3 != 3 and Q1 = 4 | 5 | 0.000432 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 != 2 and Q1 != 1 and Q9 = 5 | 5 | 0.000432 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 = 1 | 9 | 0.000425 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 != 2 and Q16 != 3 and Q18 != 3 and Q8 != 2 and Q11 != 2 and Q11 != 3 and Q4 != 2 and Q24 != 3 and Q1 != 2 and Q15 = 5 and Q13 != 4 and Q9 != 3 and Q9 != 4 and Q4 != 4 and Q3 != 3 and Q1 != 4 and Q24 = 5 and difficulty != 5 and Q7 != 4 and attendance = 2 | 3 | 0.000455 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 != 2 and Q1 = 1 and difficulty != 4 and Q2 != 3 | 13 | 0.000448 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty = 3 and Q1 != 1 and Q20 = 5 | 13 | 0.000448 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 = 1 and Q9 = 4 | 13 | 0.000448 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 = 5 | 8 | 0.000373 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 = 1 | 8 | 0.000671 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance = 4 and Q2 != 1 and Q23 != 1 and Q27 != 1 and Q1 != 1 and Q14 != 2 and Q15 != 2 and Q6 != 2 and Q1 != 2 and Q16 = 2 | 8 | 0.000629 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 = 1 and Q9 != 4 and Q1 != 5 and Q19 != 4 and Q11 = 1 and Q2 = 3 | 11 | 0.000418 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 = 5 | 13 | 0.000401 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 != 1 and Q27 != 1 and attendance != 0 and Q1 != 1 and Q2 != 2 and Q1 != 2 and difficulty != 2 and nb.repeat != 2 and Q16 != 4 and Q13 != 4 and Q12 != 4 and Q10 != 4 and Q6 != 4 and nb.repeat = 1 and Q19 = 4 | 11 | 0.000279 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 = 1 and Q9 != 4 and Q1 != 5 and Q19 = 4 | 11 | 0.000418 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 != 2 and Q16 != 3 and Q18 = 3 | 3 | 0.000680 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 = 5 | 9 | 0.000382 |
| instr = 1 and difficulty != 4 and difficulty != 5 and Q16 = 1 and Q11 != 3 and nb.repeat != 1 | 2 | 0.000262 |
| instr = 3 and difficulty = 5 and Q21 = 2 | 3 | 0.000951 |
| instr = 1 and difficulty = 4 and Q21 = 1 | 7 | 0.000549 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 = 1 and Q3 = 5 | 8 | 0.000559 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 != 1 and Q27 != 1 and attendance != 0 and Q1 != 1 and Q2 != 2 and Q1 != 2 and difficulty != 2 and nb.repeat = 2 and attendance = 2 | 11 | 0.000376 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 = 5 and difficulty = 1 | 3 | 0.000340 |
| instr = 2 and difficulty = 3 and Q21 = 2 | 6 | 0.002111 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 = 2 | 8 | 0.000315 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 = 2 | 8 | 0.000236 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 = 1 | 8 | 0.000236 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance = 4 and Q2 != 1 and Q23 != 1 and Q27 != 1 and Q1 = 1 and Q19 != 5 and Q3 = 3 | 9 | 0.000283 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty = 3 and Q1 != 1 and Q20 != 5 and Q16 != 2 and Q24 != 2 and Q20 != 2 and Q22 = 2 | 9 | 0.000283 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 != 2 and Q16 != 3 and Q18 != 3 and Q8 != 2 and Q11 != 2 and Q11 != 3 and Q4 != 2 and Q24 != 3 and Q1 != 2 and Q15 = 5 and Q13 != 4 and Q9 != 3 and Q9 != 4 and Q4 != 4 and Q3 != 3 and Q1 != 4 and Q24 != 5 | 9 | 0.000283 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 != 2 and Q1 != 1 and Q9 != 5 and Q15 != 5 and Q6 != 2 and Q20 != 2 and Q26 != 2 and Q17 = 2 | 13 | 0.000299 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 != 2 and Q16 != 3 and Q18 != 3 and Q8 != 2 and Q11 != 2 and Q11 = 3 | 13 | 0.000504 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 = 2 and attendance != 1 and Q27 = 2 and Q5 = 3 and Q8 = 3 | 8 | 0.000280 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 = 2 | 8 | 0.000280 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty = 3 and Q1 != 1 and Q20 != 5 and Q16 != 2 and Q24 = 2 | 8 | 0.000280 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 = 2 and attendance != 1 and Q27 = 2 and Q5 != 3 | 8 | 0.000280 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 = 1 | 8 | 0.000210 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 != 1 and Q27 != 1 and attendance != 0 and Q1 != 1 and Q2 != 2 and Q1 != 2 and difficulty != 2 and nb.repeat = 2 and attendance != 2 and attendance = 3 | 11 | 0.000279 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 != 1 and Q27 != 1 and attendance != 0 and Q1 != 1 and Q2 != 2 and Q1 != 2 and difficulty != 2 and nb.repeat != 2 and Q16 != 4 and Q13 != 4 and Q12 != 4 and Q10 != 4 and Q6 != 4 and nb.repeat = 1 and Q19 != 4 and attendance != 2 and Q2 != 3 and Q14 != 5 | 11 | 0.000279 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 = 3 | 3 | 0.000182 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 = 5 | 4 | 0.000198 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 != 1 and Q27 != 1 and attendance != 0 and Q1 = 1 | 1 | 0.000202 |
| instr = 1 and difficulty != 4 and difficulty = 5 and attendance != 4 and Q11 = 4 and attendance = 1 | 2 | 0.000442 |
| instr != 1 and instr = 2 and difficulty = 4 and Q15 != 1 and Q6 != 2 and Q8 != 2 and Q6 != 1 and Q15 != 2 and Q11 != 2 and Q3 = 2 | 6 | 0.000283 |
| instr = 1 and difficulty = 4 and nb.repeat != 3 and Q18 != 2 and Q4 != 2 and Q5 != 2 and Q16 != 2 and Q10 != 2 and Q12 != 2 and Q24 != 3 and Q22 != 3 and Q1 = 3 | 7 | 0.001077 |
| instr!=(3) and instr != 3 and difficulty = 4 and Q1 != 4 and Q8 != 4 and Q22 != 2 and Q6!=(2) and nb.repeat != 2 and Q14 != 2 and Q13 != 2 and difficulty != 3 and Q1!=(2) and Q3 != 2 and attendance != 2 and Q1 != 5 | 2 | 0.000154 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 = 1 and Q3 != 5 and Q5 != 4 and Q6 != 4 and Q22 != 2 and Q10 = 4 | 5 | 0.000216 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 = 1 and Q3 != 5 and Q5 = 4 | 5 | 0.000576 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 != 2 and Q1 != 1 and Q9 != 5 and Q15 != 5 and Q6 != 2 and Q20 != 2 and Q26 = 2 | 5 | 0.000389 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 != 2 and Q1 != 1 and Q9 != 5 and Q15 = 5 | 5 | 0.000432 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 != 2 and Q1 != 1 and Q9 != 5 and Q15 != 5 and Q6 != 2 and Q20 != 2 and Q26 != 2 and Q17 != 2 and difficulty != 1 and attendance != 0 and Q11 = 2 | 5 | 0.000648 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 = 1 and Q13 != 4 and attendance = 3 | 13 | 0.000448 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty = 3 and Q1 != 1 and Q20 != 5 and Q16 != 2 and Q24 != 2 and Q20 != 2 and Q22 != 2 and Q18 != 2 and Q11 != 2 and Q7 != 2 and Q23 != 2 and Q8 = 2 | 8 | 0.000210 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 = 1 and Q3 != 5 and Q5 != 4 and Q6 = 4 and Q20 != 4 | 8 | 0.000559 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance = 4 and Q2 != 1 and Q23 = 1 | 8 | 0.000210 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 = 2 | 8 | 0.000419 |
| instr != 1 and instr = 2 and difficulty = 4 and Q15 != 1 and Q6 != 2 and Q8 != 2 and Q6 != 1 and Q15 != 2 and Q11 != 2 and Q3 != 2 and attendance = 0 and Q13 = 5 | 1 | 0.000202 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 = 2 and attendance != 1 and Q27 = 2 and Q5 = 3 and Q8 != 3 | 3 | 0.001134 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 != 2 and Q16 != 3 and Q18 != 3 and Q8 != 2 and Q11 != 2 and Q11 != 3 and Q4 != 2 and Q24 != 3 and Q1 != 2 and Q15 = 5 and Q13 != 4 and Q9 != 3 and Q9 != 4 and Q4 != 4 and Q3 != 3 and Q1 != 4 and Q24 = 5 and difficulty != 5 and Q7 = 4 | 3 | 0.000113 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 != 2 and Q16 != 3 and Q18 != 3 and Q8 != 2 and Q11 != 2 and Q11 != 3 and Q4 = 2 | 3 | 0.000454 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 = 1 | 4 | 0.000159 |
| instr!=(3) and instr != 3 and difficulty = 4 and Q1 != 4 and Q8 != 4 and Q22 != 2 and Q6!=(2) and nb.repeat != 2 and Q14 != 2 and Q13 = 2 | 2 | 0.000065 |
| instr = 1 and difficulty != 4 and difficulty != 5 and Q16 = 1 and Q11 != 3 and nb.repeat = 1 and Q3 = 1 and Q4 = 1 and difficulty != 2 and Q1 != 1 | 2 | 0.000098 |
| instr = 1 and difficulty != 4 and difficulty != 5 and Q16 = 1 and Q11 != 3 and nb.repeat = 1 and Q3 = 1 and Q4 = 1 and difficulty != 2 and Q1 = 1 and Q23 != 1 | 2 | 0.000098 |
| instr = 2 and difficulty = 2 and Q21 = 1 | 6 | 0.000482 |
| instr!=(3) and instr != 3 and difficulty = 4 and Q1 = 4 and Q9 != 3 and attendance != 2 and Q7!=(3) and Q5 != 4 | 7 | 0.000317 |
| instr!=(3) and instr != 3 and difficulty = 4 and Q1 != 4 and Q8 != 4 and Q22 = 2 and attendance!=(2) and Q3 != 5 and attendance != 1 | 7 | 0.000119 |
| instr!=(3) and instr != 3 and difficulty != 4 and Q8 != 2 and Q10!=(3) and Q1 = 2 and difficulty = 5 and Q14 != 3 | 10 | 0.000069 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 != 2 and Q1 != 1 and Q9 != 5 and Q15 != 5 and Q6 != 2 and Q20 != 2 and Q26 != 2 and Q17 != 2 and difficulty != 1 and attendance = 0 and Q16 != 3 and difficulty = 4 | 4 | 0.000113 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 != 2 and Q1 = 1 and difficulty = 4 | 5 | 0.000486 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 = 1 | 5 | 0.000288 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 != 3 and Q7 != 2 and Q16 != 3 and Q18 != 3 and Q8 != 2 and Q11 != 2 and Q11 != 3 and Q4 != 2 and Q24 != 3 and Q1 != 2 and Q15 = 5 and Q13 = 4 | 13 | 0.000299 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance = 4 and Q2 != 1 and Q23 != 1 and Q27 != 1 and Q1 = 1 and Q19 = 5 | 13 | 0.000299 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 = 1 | 13 | 0.000504 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 != 2 and Q16 != 2 and Q18 != 2 and Q23 != 2 and Q20 != 2 and Q24 != 2 and Q10 != 2 and Q9 != 2 and Q11 != 2 and Q27 != 2 and Q12 != 2 and Q5 != 2 and Q6 != 2 and Q3 != 2 and Q7 != 2 and Q8 != 2 and Q12 != 1 and Q7 != 1 and Q4 != 1 and Q27 != 1 and attendance != 0 and Q1 != 1 and Q2 != 2 and Q1 != 2 and difficulty != 2 and nb.repeat != 2 and Q16 != 4 and Q13 != 4 and Q12 != 4 and Q10 != 4 and Q6 != 4 and nb.repeat != 1 | 1 | 0.000101 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 = 1 and Q9 != 4 and Q20 = 3 | 3 | 0.000510 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty = 3 and Q1 != 1 and Q20 != 5 and Q16 != 2 and Q24 != 2 and Q20 != 2 and Q22 != 2 and Q18 != 2 and Q11 != 2 and Q7 = 2 | 4 | 0.000088 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 = 1 and Q9 = 4 | 4 | 0.000099 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty = 3 and Q1 != 1 and Q20 != 5 and Q16 != 2 and Q24 != 2 and Q20 = 2 | 4 | 0.000099 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty = 3 and Q1 != 1 and Q20 != 5 and Q16 != 2 and Q24 != 2 and Q20 != 2 and Q22 != 2 and Q18 != 2 and Q11 != 2 and Q7 != 2 and Q23 = 2 | 4 | 0.000066 |
| instr!=(3) and instr != 3 and difficulty != 4 and Q8 != 2 and Q10!=(3) and Q1 != 2 and Q6 = 2 and Q3 != 3 | 2 | 0.000034 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty = 5 and Q3 != 2 and nb.repeat = 2 | 6 | 0.000678 |
| instr = 1 and difficulty = 5 and Q21 = 3 | 7 | 0.001100 |
| instr!=(3) and instr != 3 and difficulty = 4 and Q1 != 4 and Q8 != 4 and Q22 != 2 and Q6!=(2) and nb.repeat != 2 and Q14 != 2 and Q13 != 2 and difficulty != 3 and Q1!=(2) and Q3 != 2 and attendance = 2 and Q23 = 5 | 10 | 0.000035 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 = 5 | 5 | 0.000675 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 = 5 and Q27 != 1 and Q5 != 2 and Q18 != 1 and Q13 != 1 and Q16 != 2 and Q2 != 1 and Q27 != 2 and Q14 != 3 and Q13 != 3 and Q27 != 3 and attendance != 1 and Q2 = 3 | 5 | 0.000494 |
| instr!=(3) and instr = 3 and difficulty != 4 and difficulty!=(2) and difficulty = 5 and Q6 != 4 and Q3 = 4 and Q5 != 3 | 13 | 0.000082 |
| instr != 1 and instr = 2 and difficulty = 4 and Q15 != 1 and Q6 != 2 and Q8 != 2 and Q6 != 1 and Q15 != 2 and Q11 = 2 | 6 | 0.000071 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance = 4 and Q2 != 1 and Q23 != 1 and Q27 != 1 and Q1 != 1 and Q14 != 2 and Q15 = 2 | 4 | 0.000050 |
| instr!=(3) and instr != 3 and difficulty = 4 and Q1 != 4 and Q8 != 4 and Q22 != 2 and Q6!=(2) and nb.repeat != 2 and Q14 != 2 and Q13 = 4 | 2 | 0.000028 |
| instr = 1 and difficulty = 5 and Q21 = 2 | 7 | 0.000693 |
| instr!=(3) and instr != 3 and difficulty != 4 and Q8 = 2 and Q16 != 2 and difficulty = 3 | 7 | 0.000033 |
| instr = 2 and difficulty = 5 and Q21 = 5 | 11 | 0.001209 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and difficulty != 1 and Q14 != 2 and Q22 != 2 and Q17 != 2 and Q28 = 2 | 6 | 0.000944 |
| instr = 2 and difficulty = 4 and Q21 = 5 | 11 | 0.002405 |
| instr != 1 and instr = 2 and difficulty = 4 and Q15 = 1 | 6 | 0.001412 |
| instr = 3 and difficulty = 1 and Q21 = 1 | 13 | 0.007242 |
| instr!=(3) and instr != 3 and difficulty != 4 and Q8 != 2 and Q10!=(3) and Q1 = 2 and difficulty != 5 and Q2 != 2 | 2 | 0.000014 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 = 5 and difficulty != 1 | 8 | 0.000959 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty != 3 and Q14 != 5 and Q3 != 2 and Q5 != 2 and Q1 != 2 and Q2 != 2 and Q1 != 1 and Q9 != 5 and Q15 != 5 and Q6 != 2 and Q20 = 2 | 3 | 0.001417 |
| instr = 1 and difficulty = 5 and Q21 = 1 | 7 | 0.001521 |
| instr!=(3) and instr != 3 and difficulty = 4 and Q1 != 4 and Q8 != 4 and Q22 != 2 and Q6!=(2) and nb.repeat != 2 and Q14 != 2 and Q13 != 2 and difficulty != 3 and Q1!=(2) and Q3 != 2 and attendance = 2 and Q23 != 5 and attendance != 0 | 10 | 0.000044 |
| instr!=(3) and instr != 3 and difficulty = 4 and Q1 != 4 and Q8 != 4 and Q22 != 2 and Q6!=(2) and nb.repeat != 2 and Q14 != 2 and Q13 != 2 and difficulty != 3 and Q1!=(2) and Q3 != 2 and attendance != 2 and Q1 = 5 and attendance = 4 | 7 | 0.000013 |
| instr = 3 and difficulty = 3 and Q21 = 1 | 13 | 0.001506 |
| instr!=(3) and instr != 3 and difficulty = 4 and Q1 = 4 and Q9 != 3 and attendance = 2 and Q20 != 1 and Q13!=(5) | 10 | 0.000059 |
| instr = 1 and difficulty = 4 and Q21 = 5 | 2 | 0.001291 |
| instr!=(3) and instr != 3 and difficulty = 4 and Q1 != 4 and Q8 != 4 and Q22 != 2 and Q6!=(2) and nb.repeat != 2 and Q14 != 2 and Q13 != 2 and difficulty != 3 and Q1!=(2) and Q3 != 2 and attendance != 2 and Q1 = 5 and attendance = 3 | 7 | 0.000008 |
| instr!=(3) and instr != 3 and difficulty != 4 and Q8 = 2 and Q16 != 2 and difficulty != 3 | 2 | 0.000014 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty = 3 and Q1 != 1 and Q20 != 5 and Q16 = 2 and Q18 != 3 | 3 | 0.000530 |
| instr!=(3) and instr != 3 and difficulty != 4 and Q8 != 2 and Q10!=(3) and Q1 != 2 and Q6 != 2 and Q3!=(5) and attendance = 3 and difficulty = 5 and attendance != 1 | 10 | 0.000063 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 = 5 | 3 | 0.000606 |
| instr!=(3) and instr != 3 and difficulty != 4 and Q8 != 2 and Q10!=(3) and Q1 != 2 and Q6 != 2 and Q3!=(5) and attendance != 3 | 10 | 0.010616 |
| instr = 2 and difficulty = 4 and Q21 = 3 | 11 | 0.005408 |
| instr != 1 and instr != 2 and difficulty != 2 and nb.repeat = 1 and Q17 != 1 and Q4 != 1 and Q5 != 1 and Q11 != 1 and attendance != 4 and Q26 != 1 and Q6 != 1 and Q25 != 5 and Q13 != 1 and Q28 != 1 and Q19 != 1 and Q8 != 1 and Q18 != 1 and Q24 != 5 and Q21 != 5 and Q23 != 1 and Q22 != 5 and Q12 != 1 and Q3 != 1 and Q2 != 1 and Q17 != 5 and Q10 != 5 and Q11 != 5 and Q7 != 5 and Q5 != 5 and Q9 != 1 and Q16 != 5 and difficulty = 3 and Q1 != 1 and Q20 != 5 and Q16 != 2 and Q24 != 2 and Q20 != 2 and Q22 != 2 and Q18 != 2 and Q11 != 2 and Q7 != 2 and Q23 != 2 and Q8 != 2 and attendance != 2 and Q1 != 5 and Q11 = 3 | 13 | 0.001604 |
| instr!=(3) and instr != 3 and difficulty = 4 and Q1 = 4 and Q9 != 3 and attendance != 2 and Q7!=(3) and Q5 != 2 | 7 | 0.000491 |
| instr!=(3) and instr = 3 and difficulty != 4 and difficulty!=(2) and difficulty != 5 and attendance!=(1) and Q4 != 2 and Q6!=(3) and Q5!=(2) and Q12!=(2) and Q26!=(4) and Q9 = 3 and Q13!=(3) and Q23 != 5 | 13 | 0.007283 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| instr = 1 and difficulty = 1 | 10 | 0.016166 |
| instr = 1 and difficulty = 3 and Q18 = 4 | 10 | 0.011312 |
| instr = 1 and difficulty = 3 and Q13 = 5 | 10 | 0.005887 |
| instr = 1 and difficulty = 2 | 10 | 0.007850 |
| instr = 1 and difficulty = 3 and Q24 = 3 and Q26 = 3 | 10 | 0.005057 |
| instr = 1 and nb.repeat = 3 | 7 | 0.003190 |
| instr = 1 and Q1 = 1 and Q9 = 1 and Q4 = 1 and Q5 = 1 and Q20 = 1 and difficulty = 5 | 7 | 0.001237 |
| instr = 1 and Q1 = 5 and Q19 = 5 | 2 | 0.005117 |
| instr = 1 and Q17 = 5 and attendance = 4 and Q23 = 5 | 7 | 0.001557 |
| instr = 1 and difficulty = 3 and Q24 = 1 | 10 | 0.001344 |
| instr = 1 and attendance = 0 | 10 | 0.000626 |
| instr = 1 and difficulty = 3 and Q24 = 2 and Q9 = 2 | 10 | 0.000844 |
| instr = 1 and Q6 = 1 | 7 | 0.003722 |
| instr = 1 and Q17 = 2 and Q16 = 2 and Q8 = 3 | 10 | 0.001274 |
| instr = 1 and Q1 = 2 and Q24 = 4 | 7 | 0.001524 |
| instr = 1 and Q22 = 1 | 2 | 0.002851 |
| instr = 1 and Q25 = 2 and Q28 = 2 and Q23 = 2 | 2 | 0.001052 |
| instr = 1 and Q10 = 3 and Q4 = 3 and Q1 = 3 and Q23 = 3 and Q17 = 3 and difficulty = 4 | 10 | 0.000914 |
| instr = 1 and Q10 = 2 | 7 | 0.001652 |
| instr = 1 and Q2 = 4 and Q1 = 4 and Q23 = 4 and Q28 = 4 and Q21 = 4 and Q9 = 4 and attendance = 3 | 2 | 0.001023 |
| instr = 1 and Q2 = 4 and Q1 = 4 and Q6 = 4 and Q23 = 4 and Q18 = 4 and Q12 = 4 | 10 | 0.001315 |
| instr = 1 and Q2 = 2 | 7 | 0.000923 |
| instr = 1 and nb.repeat = 1 and difficulty = 3 and Q24 = 4 | 10 | 0.000409 |
| instr = 1 and Q1 = 3 | 7 | 0.002980 |
| instr = 1 and Q9 = 4 | 10 | 0.000723 |
| instr = 1 and attendance = 1 | 2 | 0.002774 |
| instr = 1 and Q13 = 4 | 10 | 0.000058 |
| instr = 1 and attendance = 2 | 2 | 0.001261 |
| instr = 2 and difficulty = 5 and nb.repeat = 1 | 11 | 0.005120 |
| instr = 2 and difficulty = 5 | 6 | 0.003417 |
| instr = 2 and difficulty = 4 and Q27 = 1 and Q2 = 1 | 6 | 0.001572 |
| instr = 2 and difficulty = 4 and Q8 = 3 | 11 | 0.006220 |
| instr = 2 and difficulty = 4 and Q13 = 4 | 11 | 0.007405 |
| instr = 2 and difficulty = 2 and nb.repeat = 2 and Q4 = 2 and attendance = 1 | 11 | 0.000483 |
| instr = 2 and difficulty = 2 and Q14 = 2 and Q5 = 2 | 6 | 0.001610 |
| instr = 2 and difficulty = 2 and Q14 = 4 and Q22 = 3 | 6 | 0.001370 |
| instr = 2 and difficulty = 3 and attendance = 0 and Q27 = 3 | 6 | 0.001399 |
| instr = 2 and difficulty = 3 and Q6 = 5 and Q11 = 5 and Q15 = 5 and Q2 = 5 and attendance = 4 and Q13 = 5 | 1 | 0.000816 |
| instr = 2 and difficulty = 3 and Q6 = 5 and Q11 = 5 and Q5 = 5 | 6 | 0.005634 |
| instr = 2 and difficulty = 2 and Q14 = 4 and Q22 = 5 and Q13 = 4 | 6 | 0.000807 |
| instr = 1 | 7 | 0.003548 |
| instr = 2 and difficulty = 3 and Q21 = 2 and Q9 = 4 and attendance = 2 | 1 | 0.000492 |
| instr = 2 and difficulty = 3 and Q21 = 2 | 6 | 0.002724 |
| instr = 2 and difficulty = 2 and Q14 = 4 and Q22 = 4 and Q24 = 4 and Q13 = 4 and Q4 = 4 and Q5 = 4 | 6 | 0.002248 |
| instr = 2 and difficulty = 3 and Q22 = 2 and Q1 = 1 | 11 | 0.000334 |
| instr = 2 and difficulty = 3 and Q21 = 1 | 6 | 0.001361 |
| instr = 2 and difficulty = 3 and Q6 = 1 | 11 | 0.002832 |
| instr = 2 and difficulty = 3 and Q24 = 4 and nb.repeat = 1 and Q21 = 3 | 11 | 0.000804 |
| instr = 2 and difficulty = 3 and Q24 = 4 and Q21 = 5 and Q16 = 4 | 11 | 0.000754 |
| instr = 2 and difficulty = 3 and Q24 = 4 and nb.repeat = 1 and Q11 = 3 and Q10 = 3 and Q16 = 4 | 6 | 0.002166 |
| instr = 2 and difficulty = 2 and Q1 = 4 and Q27 = 4 | 6 | 0.000122 |
| instr = 2 and difficulty = 2 and Q1 = 4 and Q27 = 3 | 6 | 0.001026 |
| instr = 2 and Q12 = 4 and Q11 = 3 and difficulty = 3 | 1 | 0.000566 |
| instr = 2 and Q12 = 4 and Q11 = 4 and Q6 = 5 | 6 | 0.002077 |
| instr = 2 and Q12 = 4 and Q11 = 5 | 11 | 0.000829 |
| instr = 2 and Q12 = 4 and Q26 = 3 and Q2 = 4 and Q1 = 4 | 6 | 0.000804 |
| instr = 2 and Q12 = 4 and Q26 = 3 and Q2 = 3 | 6 | 0.000686 |
| instr = 2 and Q12 = 4 and Q26 = 3 | 13 | 0.000422 |
| instr = 2 and Q12 = 4 and Q7 = 3 and Q3 = 4 | 11 | 0.000581 |
| instr = 2 and Q12 = 4 and Q7 = 3 | 6 | 0.000496 |
| instr = 2 and Q12 = 4 and Q5 = 4 and Q2 = 4 and Q8 = 4 and Q4 = 4 and Q1 = 4 | 6 | 0.008120 |
| instr = 2 and Q6 = 2 and Q1 = 4 and Q9 = 4 | 11 | 0.000830 |
| instr = 2 and Q6 = 2 and Q5 = 3 and Q11 = 2 | 11 | 0.000692 |
| instr = 2 and Q6 = 2 and Q5 = 3 and Q11 = 3 | 6 | 0.000922 |
| instr = 2 and Q6 = 2 and Q5 = 2 and Q13 = 3 and Q8 = 2 | 1 | 0.001661 |
| instr = 2 and Q6 = 2 and Q5 = 3 | 11 | 0.000722 |
| instr = 2 and Q6 = 4 and nb.repeat = 1 and Q7 = 2 | 13 | 0.000539 |
| instr = 2 and Q12 = 4 and nb.repeat = 1 and Q7 = 4 | 1 | 0.007605 |
| instr = 2 and Q12 = 4 and Q17 = 4 | 6 | 0.000545 |
| instr = 2 and Q12 = 5 and Q6 = 4 | 1 | 0.001741 |
| instr = 2 and Q12 = 5 and nb.repeat = 2 | 1 | 0.000523 |
| instr = 2 and attendance = 1 and Q18 = 3 and Q21 = 3 | 6 | 0.003376 |
| instr = 2 and Q12 = 4 | 11 | 0.012024 |
| instr = 2 and Q4 = 5 and Q17 = 5 and Q3 = 5 | 6 | 0.003085 |
| instr = 2 and Q2 = 5 and Q11 = 5 | 6 | 0.000108 |
| instr = 2 and Q7 = 5 | 13 | 0.000882 |
| instr = 2 and Q6 = 5 and Q23 = 4 | 6 | 0.000406 |
| instr = 2 and Q6 = 5 and Q21 = 4 | 1 | 0.000622 |
| instr = 2 and difficulty = 4 and Q5 = 2 | 11 | 0.001748 |
| instr = 2 and Q6 = 2 and nb.repeat = 1 and Q7 = 2 and Q5 = 2 and Q4 = 2 and Q21 = 2 | 11 | 0.001368 |
| instr = 2 and Q6 = 2 and Q1 = 1 | 6 | 0.001431 |
| instr = 2 and Q6 = 2 and Q28 = 4 and difficulty = 3 and Q14 = 4 | 1 | 0.001096 |
| instr = 2 and Q6 = 3 and Q8 = 2 and Q18 = 4 and Q16 = 3 | 6 | 0.000613 |
| instr = 2 and Q6 = 3 and Q8 = 2 | 11 | 0.001352 |
| instr = 2 and Q22 = 2 and difficulty = 1 | 6 | 0.001516 |
| instr = 2 and Q7 = 2 and Q19 = 3 and Q26 = 3 | 1 | 0.000992 |
| instr = 2 and Q14 = 2 and Q2 = 1 | 11 | 0.000414 |
| instr = 2 and Q27 = 2 and Q15 = 2 | 6 | 0.000176 |
| instr = 2 and Q7 = 2 and Q19 = 4 | 13 | 0.000526 |
| instr = 2 and Q6 = 2 and Q8 = 2 | 11 | 0.000647 |
| instr = 2 and Q6 = 3 and Q10 = 3 and Q4 = 3 and Q12 = 3 and Q27 = 4 and Q15 = 4 and nb.repeat = 1 | 6 | 0.000439 |
| instr = 2 and Q6 = 3 and Q10 = 3 and Q4 = 3 and Q24 = 4 and Q14 = 4 | 11 | 0.000970 |
| instr = 2 and Q2 = 2 | 6 | 0.001112 |
| instr = 2 and Q24 = 4 and attendance = 1 | 6 | 0.001100 |
| instr = 2 and Q13 = 2 and Q3 = 3 | 11 | 0.000040 |
| instr = 2 and Q13 = 5 | 6 | 0.000302 |
| instr = 2 and Q16 = 5 and Q7 = 3 | 11 | 0.001162 |
| instr = 2 and Q9 = 2 | 1 | 0.002061 |
| instr = 2 and Q16 = 4 and Q21 = 4 and Q20 = 4 and Q7 = 3 | 1 | 0.001622 |
| instr = 2 and Q16 = 4 and Q4 = 3 and Q10 = 3 | 13 | 0.000770 |
| instr = 2 and Q4 = 4 and Q6 = 4 and Q14 = 4 | 13 | 0.001870 |
| instr = 2 and Q16 = 4 and Q4 = 3 | 1 | 0.000423 |
| instr = 2 and Q16 = 4 and Q14 = 4 | 13 | 0.000368 |
| instr = 2 and Q24 = 3 and Q28 = 3 and Q16 = 3 and Q9 = 3 and Q7 = 3 and Q1 = 3 and attendance = 3 and nb.repeat = 1 | 6 | 0.002411 |
| instr = 2 and Q16 = 3 and Q24 = 3 and Q28 = 3 and Q27 = 3 and Q12 = 3 and Q3 = 3 and Q1 = 3 and attendance = 0 and difficulty = 1 | 1 | 0.001268 |
| instr = 2 and Q16 = 3 and Q24 = 3 and Q28 = 3 and Q27 = 3 | 11 | 0.006265 |
| instr = 2 and Q24 = 3 and Q14 = 3 | 1 | 0.006167 |
| instr = 2 and Q17 = 1 | 6 | 0.002455 |
| nb.repeat = 3 and Q11 = 5 and Q1 = 5 and Q14 = 5 and Q23 = 5 and attendance = 4 | 13 | 0.001068 |
| nb.repeat = 3 and Q11 = 5 and Q1 = 5 and Q14 = 5 and Q23 = 5 | 8 | 0.001259 |
| difficulty = 2 and Q14 = 2 and Q2 = 2 | 13 | 0.004621 |
| difficulty = 5 and nb.repeat = 2 and Q16 = 2 | 3 | 0.001169 |
| difficulty = 5 and Q4 = 5 and nb.repeat = 1 | 5 | 0.002071 |
| difficulty = 2 and Q14 = 2 and Q1 = 1 | 8 | 0.000992 |
| difficulty = 2 and Q17 = 2 and Q5 = 2 | 13 | 0.000217 |
| difficulty = 5 and Q16 = 5 | 13 | 0.001188 |
| Q21 = 1 and Q23 = 2 and Q16 = 1 | 13 | 0.001440 |
| difficulty = 5 and Q11 = 1 and Q17 = 3 and nb.repeat = 1 | 5 | 0.001570 |
| difficulty = 5 and Q11 = 5 | 8 | 0.000717 |
| difficulty = 5 and Q1 = 4 and Q2 = 4 and Q27 = 4 and attendance = 3 | 3 | 0.001194 |
| difficulty = 5 and Q9 = 5 and Q10 = 1 | 8 | 0.000753 |
| difficulty = 5 and Q9 = 5 | 5 | 0.000049 |
| difficulty = 5 and Q11 = 1 and Q9 = 3 | 13 | 0.000727 |
| difficulty = 5 and Q21 = 1 and Q26 = 1 and Q9 = 1 and Q25 = 1 and nb.repeat = 1 and Q2 = 1 | 3 | 0.002857 |
| difficulty = 2 and Q17 = 1 | 13 | 0.003291 |
| difficulty = 1 and Q20 = 2 and Q13 = 3 and Q10 = 2 | 9 | 0.001247 |
| difficulty = 1 and Q20 = 2 and Q27 = 3 and Q4 = 2 | 13 | 0.001173 |
| difficulty = 1 and Q20 = 2 and Q26 = 3 and Q5 = 3 | 5 | 0.001488 |
| difficulty = 1 and Q20 = 2 and Q26 = 1 | 13 | 0.000368 |
| difficulty = 1 and Q20 = 2 and Q16 = 2 and Q11 = 2 and Q22 = 2 and nb.repeat = 1 and Q2 = 2 | 3 | 0.003185 |
| difficulty = 5 and nb.repeat = 2 and attendance = 0 | 3 | 0.001463 |
| difficulty = 5 and nb.repeat = 2 and attendance = 4 | 3 | 0.000690 |
| difficulty = 1 and Q20 = 2 and Q16 = 2 and Q22 = 2 and attendance = 0 and Q1 = 2 | 9 | 0.000647 |
| difficulty = 1 and Q7 = 1 and Q11 = 2 | 13 | 0.000839 |
| difficulty = 1 and Q7 = 1 and Q11 = 3 and attendance = 0 | 5 | 0.000363 |
| difficulty = 1 and Q7 = 1 and Q11 = 3 | 13 | 0.000995 |
| difficulty = 1 and Q3 = 1 and Q1 = 1 and Q11 = 2 | 13 | 0.001332 |
| difficulty = 1 and Q7 = 1 and Q11 = 5 and Q16 = 1 | 8 | 0.000625 |
| difficulty = 1 and Q7 = 1 and Q2 = 2 | 13 | 0.000996 |
| difficulty = 1 and Q15 = 1 and Q17 = 1 and Q10 = 1 and Q8 = 1 and Q19 = 1 and Q1 = 1 and Q4 = 1 and attendance = 4 | 13 | 0.001038 |
| difficulty = 1 and Q15 = 1 and Q17 = 1 and Q10 = 1 and Q19 = 1 and Q8 = 1 and Q1 = 1 and Q4 = 1 and attendance = 1 and nb.repeat = 1 | 3 | 0.000225 |
| difficulty = 1 and Q15 = 1 and Q17 = 1 and Q10 = 1 and Q19 = 1 and Q8 = 1 and Q1 = 1 and Q4 = 1 and attendance = 0 and Q26 = 1 and nb.repeat = 1 and Q6 = 1 and Q21 = 1 and Q13 = 1 | 3 | 0.007249 |
| nb.repeat = 3 and Q9 = 1 | 13 | 0.002288 |
| nb.repeat = 3 and Q18 = 5 and Q12 = 5 | 13 | 0.000564 |
| nb.repeat = 3 and Q18 = 5 | 5 | 0.000101 |
| nb.repeat = 3 and Q9 = 5 | 13 | 0.000192 |
| nb.repeat = 3 and Q10 = 1 and Q5 = 1 | 8 | 0.001244 |
| nb.repeat = 3 and Q10 = 3 and Q8 = 3 and Q7 = 3 and Q1 = 3 and Q26 = 3 and difficulty = 2 | 9 | 0.000928 |
| nb.repeat = 3 and Q10 = 3 and Q8 = 3 and Q7 = 3 and Q1 = 3 and Q26 = 3 and attendance = 1 | 9 | 0.000660 |
| difficulty = 5 and nb.repeat = 2 and Q6 = 3 | 13 | 0.001157 |
| difficulty = 5 and Q21 = 5 | 8 | 0.000346 |
| difficulty = 5 and Q1 = 3 and Q24 = 3 and Q11 = 3 and Q7 = 3 and nb.repeat = 1 and Q15 = 3 | 3 | 0.005833 |
| difficulty = 1 and Q20 = 1 and Q12 = 3 | 13 | 0.000587 |
| difficulty = 1 and Q22 = 1 and Q12 = 1 and Q10 = 1 and Q8 = 1 and Q4 = 2 and Q6 = 1 | 5 | 0.000871 |
| difficulty = 1 and Q22 = 1 and Q12 = 1 and Q10 = 1 and Q7 = 1 | 13 | 0.012776 |
| nb.repeat = 3 and Q10 = 3 and Q8 = 3 and Q7 = 3 and Q1 = 3 and Q26 = 3 and attendance = 2 and difficulty = 3 | 9 | 0.000389 |
| difficulty = 1 and Q15 = 1 and Q17 = 1 and Q7 = 2 and nb.repeat = 1 | 13 | 0.000705 |
| nb.repeat = 3 and Q10 = 3 and Q3 = 4 | 9 | 0.000585 |
| difficulty = 1 and Q15 = 1 and Q17 = 1 | 3 | 0.000581 |
| difficulty = 1 and Q15 = 1 and Q9 = 2 | 13 | 0.000526 |
| difficulty = 1 and Q15 = 3 and attendance = 2 | 3 | 0.000753 |
| difficulty = 5 and Q22 = 4 and Q7 = 3 | 3 | 0.001114 |
| difficulty = 1 and Q15 = 3 and attendance = 4 and Q28 = 3 | 3 | 0.000940 |
| difficulty = 1 and Q15 = 1 | 4 | 0.000247 |
| difficulty = 1 and Q24 = 1 and Q8 = 1 and Q10 = 2 | 13 | 0.001190 |
| difficulty = 1 and Q24 = 1 and Q7 = 1 | 3 | 0.000037 |
| difficulty = 1 and Q24 = 1 | 9 | 0.004191 |
| difficulty = 1 and Q6 = 3 and Q8 = 2 and Q22 = 2 and Q21 = 2 | 3 | 0.001775 |
| instr = 2 and Q1 = 1 | 1 | 0.004687 |
| nb.repeat = 3 and difficulty = 2 and Q21 = 4 | 8 | 0.001773 |
| difficulty = 1 and Q27 = 1 and Q22 = 5 | 8 | 0.001261 |
| nb.repeat = 3 and Q27 = 5 | 8 | 0.000188 |
| nb.repeat = 3 and Q11 = 2 and attendance = 0 | 13 | 0.001284 |
| nb.repeat = 3 and Q11 = 2 and Q1 = 2 | 9 | 0.000405 |
| difficulty = 1 and Q28 = 5 and Q21 = 4 | 3 | 0.001090 |
| difficulty = 1 and Q28 = 1 | 5 | 0.006302 |
| difficulty = 1 and Q24 = 5 and Q27 = 5 and Q4 = 4 and Q22 = 5 | 13 | 0.001669 |
| difficulty = 1 and Q8 = 3 and Q7 = 2 | 3 | 0.000923 |
| difficulty = 1 and Q17 = 5 and Q15 = 4 and Q3 = 4 | 9 | 0.000941 |
| difficulty = 1 and Q17 = 5 and Q16 = 5 and Q12 = 5 and Q3 = 5 and attendance = 0 and nb.repeat = 1 | 5 | 0.001790 |
| nb.repeat = 3 and Q7 = 1 | 13 | 0.000095 |
| nb.repeat = 3 and Q11 = 1 | 4 | 0.000023 |
| nb.repeat = 3 and difficulty = 1 and Q3 = 3 | 9 | 0.001040 |
| nb.repeat = 3 and difficulty = 4 | 3 | 0.002671 |
| difficulty = 1 and Q8 = 3 and Q3 = 2 | 3 | 0.000804 |
| difficulty = 1 and Q19 = 1 and Q5 = 2 | 3 | 0.000449 |
| difficulty = 1 and Q9 = 1 and Q26 = 4 | 5 | 0.000970 |
| difficulty = 1 and Q8 = 1 and Q4 = 1 and Q10 = 1 | 13 | 0.000098 |
| difficulty = 1 and Q8 = 1 and Q13 = 2 | 9 | 0.001346 |
| nb.repeat = 2 and Q11 = 1 and Q8 = 1 | 13 | 0.002596 |
| nb.repeat = 3 and difficulty = 3 and attendance = 0 | 9 | 0.001727 |
| difficulty = 1 and Q8 = 3 and Q10 = 4 and Q2 = 4 | 13 | 0.001537 |
| difficulty = 1 and Q9 = 5 and Q8 = 3 | 13 | 0.000288 |
| difficulty = 1 and Q9 = 5 and Q12 = 4 and Q10 = 4 | 5 | 0.000788 |
| difficulty = 1 and Q9 = 5 and Q12 = 5 and Q2 = 5 and Q28 = 5 and attendance = 4 | 3 | 0.000814 |
| difficulty = 1 and Q9 = 5 and Q12 = 5 and Q2 = 5 and Q28 = 5 and attendance = 3 | 5 | 0.000293 |
| difficulty = 1 and Q9 = 5 and Q12 = 5 and Q18 = 4 | 5 | 0.000494 |
| difficulty = 1 and Q9 = 5 | 13 | 0.004018 |
| difficulty = 1 and Q22 = 5 and attendance = 0 and Q19 = 5 | 13 | 0.000092 |
| difficulty = 1 and Q22 = 5 and Q7 = 2 | 8 | 0.001368 |
| difficulty = 1 and Q8 = 5 and Q6 = 4 | 5 | 0.000596 |
| difficulty = 1 and Q8 = 5 and Q2 = 3 | 4 | 0.000519 |
| difficulty = 1 and Q8 = 5 and Q28 = 4 | 3 | 0.000843 |
| difficulty = 1 and attendance = 1 and Q25 = 3 | 3 | 0.001299 |
| difficulty = 1 and attendance = 1 and Q1 = 3 | 8 | 0.000192 |
| difficulty = 1 and attendance = 4 | 5 | 0.002180 |
| difficulty = 1 and Q12 = 5 and Q23 = 3 | 4 | 0.000524 |
| difficulty = 1 and Q16 = 5 and Q28 = 4 | 5 | 0.000450 |
| nb.repeat = 2 and Q14 = 5 and Q27 = 5 and difficulty = 3 | 8 | 0.001541 |
| difficulty = 1 and Q16 = 2 and Q27 = 2 and Q22 = 2 | 3 | 0.000179 |
| difficulty = 1 and Q17 = 2 and Q24 = 2 | 5 | 0.007304 |
| difficulty = 1 and Q16 = 2 and Q27 = 3 | 13 | 0.000671 |
| difficulty = 1 and Q16 = 2 | 9 | 0.000561 |
| difficulty = 1 and Q19 = 5 | 3 | 0.004229 |
| difficulty = 1 and Q12 = 5 | 5 | 0.000028 |
| difficulty = 1 and Q15 = 2 and Q8 = 2 | 13 | 0.002166 |
| difficulty = 1 and Q6 = 2 and Q25 = 3 and Q23 = 3 | 9 | 0.000229 |
| difficulty = 1 and Q6 = 2 and Q16 = 3 and Q25 = 2 | 5 | 0.001040 |
| difficulty = 1 and Q6 = 2 | 8 | 0.002094 |
| difficulty = 1 and Q19 = 2 and Q23 = 2 | 4 | 0.001025 |
| difficulty = 1 and Q10 = 2 and Q2 = 2 | 9 | 0.000888 |
| difficulty = 1 and Q11 = 3 and Q5 = 3 and Q12 = 3 and Q18 = 3 and Q28 = 3 and Q2 = 3 and Q1 = 3 and attendance = 0 | 3 | 0.010048 |
| nb.repeat = 3 and Q1 = 2 and Q11 = 3 | 8 | 0.000834 |
| nb.repeat = 3 and Q1 = 3 and Q14 = 3 | 13 | 0.001983 |
| nb.repeat = 2 and Q14 = 1 | 5 | 0.001244 |
| nb.repeat = 2 and Q11 = 1 and Q21 = 3 | 3 | 0.000249 |
| nb.repeat = 2 and Q11 = 1 | 5 | 0.000130 |
| nb.repeat = 2 and attendance = 4 and Q16 = 3 | 9 | 0.000719 |
| nb.repeat = 2 and attendance = 4 | 3 | 0.000900 |
| nb.repeat = 2 and Q10 = 1 | 4 | 0.000114 |
| nb.repeat = 2 and attendance = 0 and Q8 = 2 and Q9 = 2 | 3 | 0.000748 |
| nb.repeat = 2 and attendance = 0 and Q8 = 3 | 9 | 0.002574 |
| nb.repeat = 2 and attendance = 0 and Q8 = 5 and difficulty = 4 | 13 | 0.000643 |
| nb.repeat = 2 and attendance = 0 | 13 | 0.001874 |
| nb.repeat = 2 and attendance = 2 and Q26 = 4 and Q8 = 4 | 13 | 0.001102 |
| difficulty = 1 and Q11 = 3 and Q8 = 3 and Q1 = 3 and Q12 = 3 | 13 | 0.010338 |
| difficulty = 1 and nb.repeat = 1 and attendance = 3 and Q26 = 4 | 9 | 0.000750 |
| difficulty = 1 and nb.repeat = 1 and attendance = 0 and Q11 = 3 and Q5 = 3 and Q3 = 3 and Q22 = 3 | 9 | 0.004112 |
| difficulty = 1 and attendance = 1 | 3 | 0.000152 |
| difficulty = 1 and Q11 = 3 and Q5 = 3 | 3 | 0.000178 |
| difficulty = 1 and Q11 = 3 | 5 | 0.004743 |
| difficulty = 1 and Q5 = 2 and Q18 = 3 | 3 | 0.001487 |
| difficulty = 1 and Q5 = 3 and Q7 = 4 and Q26 = 4 | 9 | 0.002037 |
| difficulty = 1 and Q5 = 3 and Q2 = 2 | 8 | 0.000510 |
| difficulty = 1 and Q5 = 4 and Q11 = 4 and Q9 = 4 and Q18 = 4 and Q13 = 4 | 3 | 0.007577 |
| difficulty = 1 and Q5 = 4 and Q3 = 4 and Q15 = 4 and Q6 = 4 | 4 | 0.002112 |
| difficulty = 1 and Q13 = 2 | 3 | 0.000218 |
| difficulty = 1 and Q20 = 3 and Q14 = 3 | 5 | 0.000521 |
| difficulty = 1 and Q20 = 4 and Q5 = 4 | 5 | 0.003749 |
| difficulty = 1 and Q17 = 3 | 3 | 0.000219 |
| difficulty = 1 and Q20 = 4 | 13 | 0.002236 |
| difficulty = 5 and Q22 = 2 and Q5 = 2 and Q8 = 2 | 3 | 0.002813 |
| difficulty = 4 and attendance = 2 and Q1 = 4 and Q8 = 4 and Q23 = 4 | 5 | 0.002606 |
| difficulty = 4 and attendance = 2 and Q11 = 1 and Q2 = 1 | 3 | 0.001556 |
| difficulty = 4 and attendance = 2 and Q11 = 2 and Q1 = 2 | 3 | 0.001553 |
| difficulty = 4 and attendance = 2 and Q11 = 1 | 5 | 0.001687 |
| difficulty = 5 and Q21 = 2 and Q12 = 2 | 5 | 0.001047 |
| difficulty = 1 | 9 | 0.007490 |
| difficulty = 4 and attendance = 4 and Q4 = 4 and Q15 = 2 | 5 | 0.000283 |
| difficulty = 4 and attendance = 4 and Q4 = 4 and Q10 = 4 and Q15 = 4 and Q16 = 4 | 3 | 0.001964 |
| attendance = 4 and Q4 = 1 and Q22 = 4 | 8 | 0.003651 |
| difficulty = 4 and attendance = 4 and Q27 = 4 | 8 | 0.003867 |
| difficulty = 4 and Q21 = 2 and Q8 = 4 | 3 | 0.000884 |
| difficulty = 4 and Q21 = 2 and Q8 = 1 | 4 | 0.000409 |
| difficulty = 4 and Q21 = 2 and Q23 = 2 and Q27 = 2 and attendance = 3 | 3 | 0.001930 |
| difficulty = 4 and attendance = 1 and Q2 = 5 and Q1 = 5 | 3 | 0.001638 |
| difficulty = 4 and Q21 = 2 and Q28 = 3 and Q15 = 4 | 9 | 0.001704 |
| difficulty = 4 and Q21 = 2 and Q17 = 2 | 13 | 0.003108 |
| difficulty = 4 and Q21 = 2 and Q11 = 2 | 3 | 0.002139 |
| difficulty = 4 and Q21 = 2 | 5 | 0.001918 |
| difficulty = 4 and Q21 = 5 and Q23 = 4 and Q13 = 3 | 8 | 0.001327 |
| difficulty = 4 and Q1 = 4 and Q2 = 5 and Q11 = 4 | 5 | 0.002460 |
| difficulty = 4 and Q11 = 5 and Q22 = 5 and Q26 = 5 and nb.repeat = 1 and Q9 = 5 | 5 | 0.002184 |
| difficulty = 4 and Q11 = 5 and Q22 = 4 | 8 | 0.001659 |
| difficulty = 4 and Q11 = 5 and Q26 = 5 and Q13 = 5 | 9 | 0.001023 |
| difficulty = 4 and Q11 = 5 and Q22 = 5 and Q26 = 4 | 5 | 0.001194 |
| difficulty = 5 and Q21 = 2 | 13 | 0.000706 |
| difficulty = 5 and Q2 = 1 and Q11 = 1 | 3 | 0.001393 |
| difficulty = 5 and Q2 = 1 and Q27 = 3 | 8 | 0.002427 |
| difficulty = 4 and Q11 = 5 and Q22 = 5 | 8 | 0.001964 |
| difficulty = 4 and Q14 = 2 and Q11 = 1 | 3 | 0.001663 |
| difficulty = 2 and Q23 = 1 and Q9 = 1 | 9 | 0.001511 |
| difficulty = 2 and Q23 = 5 and Q19 = 5 and attendance = 1 | 13 | 0.003270 |
| difficulty = 4 and Q14 = 2 and Q11 = 4 | 8 | 0.003672 |
| difficulty = 4 and Q13 = 5 and Q15 = 5 | 5 | 0.000829 |
| difficulty = 4 and Q13 = 5 and Q8 = 4 | 3 | 0.001324 |
| difficulty = 5 and Q22 = 1 and Q1 = 2 and Q4 = 1 | 13 | 0.001826 |
| difficulty = 5 and Q22 = 4 and Q18 = 4 and Q13 = 4 and Q4 = 4 and Q6 = 4 and nb.repeat = 1 and attendance = 4 | 3 | 0.001272 |
| difficulty = 5 and Q22 = 1 | 5 | 0.001404 |
| difficulty = 5 and Q22 = 4 and Q18 = 4 and Q6 = 4 and Q1 = 4 and attendance = 2 | 5 | 0.000933 |
| difficulty = 5 and Q22 = 4 and Q18 = 4 and Q4 = 4 and Q1 = 4 and attendance = 0 | 13 | 0.000924 |
| difficulty = 5 and Q22 = 4 and Q7 = 2 and attendance = 3 | 8 | 0.001882 |
| difficulty = 5 and Q2 = 4 and Q4 = 4 | 3 | 0.001658 |
| difficulty = 5 and Q22 = 4 and Q17 = 4 | 5 | 0.001289 |
| difficulty = 4 and Q13 = 1 and Q9 = 1 and attendance = 3 and Q8 = 1 | 3 | 0.000531 |
| difficulty = 4 and Q13 = 1 and Q24 = 1 and Q9 = 1 and attendance = 0 | 5 | 0.000360 |
| difficulty = 4 and Q13 = 1 and Q9 = 1 and Q26 = 1 and attendance = 1 | 3 | 0.001798 |
| difficulty = 4 and Q14 = 2 and Q22 = 3 and Q1 = 1 | 9 | 0.001267 |
| difficulty = 4 and Q13 = 1 and attendance = 3 and Q1 = 1 | 3 | 0.000237 |
| difficulty = 4 and Q13 = 1 and Q1 = 1 | 9 | 0.002494 |
| difficulty = 4 and Q14 = 2 and Q1 = 3 | 8 | 0.000967 |
| difficulty = 4 and Q14 = 5 and Q13 = 4 | 5 | 0.000284 |
| difficulty = 4 and Q14 = 1 and Q1 = 2 | 5 | 0.001433 |
| difficulty = 4 and Q14 = 4 and Q11 = 1 | 5 | 0.001066 |
| difficulty = 4 and Q14 = 4 and Q11 = 2 and Q28 = 3 | 4 | 0.001048 |
| difficulty = 4 and Q14 = 4 and Q21 = 3 and Q3 = 3 | 3 | 0.002692 |
| difficulty = 4 and Q14 = 2 | 9 | 0.002176 |
| difficulty = 4 and Q14 = 4 and Q2 = 1 and nb.repeat = 1 | 8 | 0.001181 |
| difficulty = 4 and Q14 = 4 and Q11 = 2 and Q28 = 5 and Q3 = 4 | 5 | 0.002579 |
| difficulty = 4 and Q16 = 5 and attendance = 2 | 9 | 0.000649 |
| difficulty = 4 and Q16 = 1 and Q9 = 1 | 9 | 0.000125 |
| difficulty = 4 and Q16 = 1 and Q9 = 3 | 4 | 0.000474 |
| difficulty = 4 and Q16 = 2 and Q23 = 2 | 8 | 0.002162 |
| difficulty = 4 and Q16 = 1 | 13 | 0.001975 |
| difficulty = 4 and Q1 = 1 and Q28 = 5 | 4 | 0.000870 |
| difficulty = 4 and Q1 = 1 and Q2 = 1 | 9 | 0.000147 |
| difficulty = 4 and Q1 = 1 and Q2 = 2 | 9 | 0.000958 |
| difficulty = 4 and Q1 = 4 and Q2 = 4 and Q25 = 4 and Q17 = 4 and Q13 = 4 | 5 | 0.005100 |
| difficulty = 4 and Q1 = 4 and Q2 = 4 and Q13 = 4 | 5 | 0.000276 |
| difficulty = 4 and Q1 = 1 | 5 | 0.001258 |
| difficulty = 4 and Q3 = 2 and Q24 = 3 and Q15 = 3 | 3 | 0.002851 |
| difficulty = 4 and Q3 = 2 and Q15 = 4 | 5 | 0.002365 |
| difficulty = 5 and attendance = 2 and Q15 = 4 | 4 | 0.000557 |
| Q17 = 1 and Q21 = 1 | 13 | 0.004965 |
| Q17 = 2 and Q16 = 1 | 9 | 0.001387 |
| Q17 = 1 | 4 | 0.000175 |
| Q21 = 1 and Q6 = 2 | 9 | 0.000571 |
| Q21 = 1 and Q15 = 1 and Q22 = 1 | 4 | 0.000069 |
| Q21 = 1 | 5 | 0.000859 |
| Q14 = 1 and Q7 = 2 | 8 | 0.001802 |
| difficulty = 4 and Q3 = 1 | 3 | 0.000842 |
| Q22 = 2 and attendance = 2 | 3 | 0.003668 |
| Q22 = 5 and Q7 = 1 and Q9 = 3 | 13 | 0.000938 |
| Q5 = 1 and Q2 = 3 | 8 | 0.002237 |
| Q5 = 1 and Q3 = 4 | 9 | 0.002344 |
| difficulty = 5 and attendance = 3 and Q17 = 3 | 3 | 0.000307 |
| Q3 = 1 and Q12 = 1 | 4 | 0.000289 |
| difficulty = 5 and attendance = 2 | 8 | 0.000498 |
| Q14 = 2 and Q15 = 3 and Q22 = 3 | 13 | 0.001289 |
| Q14 = 2 and Q16 = 2 and Q6 = 2 and Q1 = 2 | 3 | 0.003235 |
| Q14 = 2 and Q24 = 1 | 9 | 0.001951 |
| Q14 = 1 | 13 | 0.000143 |
| Q23 = 1 | 13 | 0.000302 |
| Q1 = 5 and Q10 = 4 | 3 | 0.001012 |
| Q21 = 5 and Q14 = 3 and Q6 = 3 and Q1 = 3 | 9 | 0.002363 |
| Q14 = 2 and Q13 = 3 and Q3 = 3 | 3 | 0.000608 |
| Q14 = 2 and Q7 = 3 | 9 | 0.001739 |
| Q21 = 2 and Q3 = 2 and Q6 = 2 | 5 | 0.002604 |
| Q6 = 1 and Q12 = 3 | 13 | 0.001484 |
| Q1 = 1 and Q11 = 1 and Q4 = 1 | 13 | 0.000157 |
| Q1 = 1 and Q11 = 4 and Q23 = 3 | 8 | 0.002717 |
| Q23 = 2 and attendance = 3 | 4 | 0.002878 |
| difficulty = 2 and Q5 = 2 and Q1 = 1 and Q25 = 3 | 4 | 0.000914 |
| difficulty = 2 and Q5 = 2 and Q10 = 3 and Q1 = 2 | 9 | 0.001716 |
| difficulty = 2 and Q5 = 5 and Q27 = 5 and nb.repeat = 1 | 3 | 0.000994 |
| difficulty = 2 and attendance = 4 | 8 | 0.002791 |
| difficulty = 2 and Q8 = 5 | 13 | 0.000837 |
| difficulty = 2 and Q25 = 3 and Q28 = 3 and Q2 = 3 and nb.repeat = 1 | 13 | 0.007205 |
| difficulty = 2 and Q12 = 2 and Q22 = 4 | 8 | 0.001204 |
| difficulty = 2 and Q12 = 2 | 13 | 0.000725 |
| Q12 = 1 and Q6 = 4 | 5 | 0.002483 |
| Q25 = 2 and Q3 = 3 and Q22 = 2 | 9 | 0.000796 |
| Q12 = 1 and Q28 = 3 and Q5 = 3 | 5 | 0.000621 |
| Q12 = 1 and Q28 = 4 | 8 | 0.000934 |
| Q12 = 1 and Q28 = 5 | 8 | 0.000873 |
| Q12 = 1 | 9 | 0.003271 |
| difficulty = 2 and Q16 = 4 and Q18 = 4 and Q10 = 4 | 13 | 0.002025 |
| difficulty = 2 and Q17 = 5 and Q23 = 4 | 3 | 0.000426 |
| difficulty = 2 and Q16 = 3 and Q23 = 3 and attendance = 1 | 9 | 0.001269 |
| Q14 = 5 and Q7 = 3 and Q11 = 5 | 8 | 0.003731 |
| Q14 = 5 and Q4 = 3 | 3 | 0.001538 |
| Q14 = 2 | 5 | 0.000736 |
| difficulty = 2 and nb.repeat = 2 and attendance = 2 | 3 | 0.000691 |
| difficulty = 2 and Q27 = 4 | 9 | 0.004236 |
| Q14 = 5 and attendance = 0 and Q2 = 5 | 8 | 0.002617 |
| Q14 = 5 and attendance = 3 | 13 | 0.003381 |
| Q14 = 5 and Q11 = 4 and Q13 = 5 | 9 | 0.001230 |
| Q1 = 1 and Q18 = 3 | 8 | 0.002387 |
| Q1 = 1 and Q14 = 3 | 3 | 0.000957 |
| Q1 = 1 and Q9 = 3 | 8 | 0.001810 |
| Q1 = 1 and Q12 = 2 | 5 | 0.000664 |
| Q1 = 3 and Q20 = 5 | 8 | 0.004015 |
| nb.repeat = 2 and attendance = 2 | 8 | 0.000888 |
| Q1 = 3 and Q12 = 4 and Q20 = 4 and Q4 = 4 | 9 | 0.002616 |
| Q1 = 3 and Q8 = 4 and Q14 = 3 | 3 | 0.001401 |
| Q1 = 1 | 3 | 0.001288 |
| Q1 = 3 and Q9 = 1 | 5 | 0.001183 |
| Q1 = 3 and Q8 = 4 and Q27 = 4 | 8 | 0.000740 |
| Q1 = 3 and Q8 = 2 and Q16 = 3 and Q23 = 4 | 8 | 0.002873 |
| nb.repeat = 3 and Q14 = 4 | 8 | 0.000583 |
| nb.repeat = 2 and attendance = 3 and difficulty = 4 and Q13 = 3 and Q1 = 3 | 9 | 0.001606 |
| nb.repeat = 2 and attendance = 3 and Q4 = 4 | 13 | 0.000727 |
| Q1 = 3 and Q8 = 4 | 3 | 0.000902 |
| Q1 = 3 and Q8 = 2 and Q16 = 2 | 5 | 0.001164 |
| Q1 = 3 and Q8 = 2 and Q9 = 2 | 9 | 0.001603 |
| Q1 = 3 and Q8 = 3 and nb.repeat = 2 and Q15 = 3 and Q12 = 3 and attendance = 1 | 13 | 0.002739 |
| Q1 = 3 and Q8 = 3 and Q12 = 4 and Q20 = 3 | 9 | 0.002893 |
| Q1 = 3 and Q8 = 3 and nb.repeat = 2 and Q22 = 3 and difficulty = 3 | 8 | 0.001367 |
| Q1 = 3 and Q8 = 3 and Q17 = 3 and Q4 = 3 and Q6 = 3 and nb.repeat = 1 and attendance = 2 | 3 | 0.009671 |
| Q1 = 3 and Q8 = 3 and Q16 = 4 and Q9 = 3 and attendance = 1 and difficulty = 4 | 3 | 0.003098 |
| Q1 = 4 and Q3 = 3 and Q28 = 4 and Q6 = 4 | 5 | 0.002162 |
| Q1 = 4 and Q3 = 3 and Q2 = 3 | 8 | 0.001074 |
| Q1 = 4 and Q3 = 3 and Q6 = 3 | 3 | 0.000883 |
| Q1 = 3 and Q8 = 3 and Q16 = 3 and Q20 = 3 and Q13 = 3 and nb.repeat = 1 and Q6 = 3 and Q3 = 3 and attendance = 1 | 5 | 0.006826 |
| Q1 = 4 and Q3 = 4 and Q2 = 3 and Q8 = 3 | 8 | 0.002913 |
| Q1 = 4 and Q3 = 2 | 4 | 0.000400 |
| Q1 = 4 and Q5 = 4 and Q19 = 4 and Q11 = 4 and Q12 = 4 and nb.repeat = 1 | 3 | 0.017422 |
| Q1 = 4 and Q22 = 3 and Q8 = 4 | 5 | 0.001794 |
| Q1 = 4 and Q22 = 2 | 3 | 0.001133 |
| Q1 = 4 and Q8 = 5 | 13 | 0.001253 |
| Q1 = 4 and Q5 = 4 and Q19 = 3 | 5 | 0.001628 |
| Q1 = 4 and Q17 = 4 and Q4 = 3 | 8 | 0.000117 |
| Q1 = 4 and Q20 = 3 | 8 | 0.001258 |
| Q1 = 4 and Q11 = 3 | 3 | 0.000079 |
| Q1 = 4 and Q5 = 3 and Q7 = 2 | 9 | 0.001389 |
| Q1 = 4 and Q5 = 4 and Q12 = 3 | 9 | 0.003650 |
| Q1 = 4 and Q5 = 4 | 8 | 0.013013 |
| Q1 = 2 and Q27 = 5 and Q21 = 5 | 8 | 0.003793 |
| Q1 = 3 and Q8 = 3 and Q16 = 3 and Q20 = 3 and Q13 = 3 and nb.repeat = 1 and Q6 = 3 and Q3 = 3 and attendance = 3 and difficulty = 4 | 3 | 0.002073 |
| Q1 = 3 and Q8 = 3 and Q16 = 3 and Q20 = 3 and Q13 = 3 and Q6 = 3 and nb.repeat = 1 and Q3 = 3 | 13 | 0.009583 |
| attendance = 0 and Q6 = 4 and Q23 = 3 | 8 | 0.001998 |
| attendance = 0 and Q6 = 3 and Q20 = 4 | 8 | 0.001782 |
| attendance = 4 and Q1 = 2 | 8 | 0.008629 |
| attendance = 4 and Q4 = 5 | 13 | 0.000833 |
| Q14 = 5 and attendance = 1 | 5 | 0.000611 |
| Q14 = 5 | 13 | 0.002902 |
| Q4 = 5 and Q2 = 5 | 5 | 0.001239 |
| Q12 = 5 | 8 | 0.000658 |
| Q11 = 2 and Q5 = 3 and Q1 = 2 | 5 | 0.002463 |
| Q11 = 2 | 3 | 0.002293 |
| Q12 = 2 and Q10 = 3 | 8 | 0.002496 |
| Q3 = 5 and Q4 = 3 | 5 | 0.002830 |
| Q11 = 4 and Q1 = 2 and Q12 = 3 and Q27 = 3 | 9 | 0.004194 |
| Q11 = 4 and Q17 = 4 and Q2 = 4 | 3 | 0.001330 |
| Q11 = 5 | 9 | 0.010731 |
| Q20 = 2 and Q27 = 3 | 9 | 0.002377 |
| Q20 = 3 and Q9 = 3 and Q15 = 3 and Q21 = 3 and Q4 = 3 and Q2 = 3 and attendance = 3 | 4 | 0.001349 |
| Q20 = 3 and Q9 = 3 and Q15 = 3 and Q21 = 3 and Q4 = 3 and Q8 = 3 and Q2 = 3 | 3 | 0.014955 |
| Q20 = 3 and Q9 = 2 | 5 | 0.003295 |
| Q14 = 3 and Q17 = 4 and Q3 = 4 | 3 | 0.001759 |
| Q14 = 3 and Q24 = 4 and Q3 = 2 | 4 | 0.002759 |
| Q14 = 3 and Q24 = 3 and Q10 = 3 and Q5 = 3 and Q4 = 3 | 4 | 0.004980 |
| Q20 = 3 and Q8 = 3 and Q26 = 3 | 9 | 0.016703 |
| Q20 = 3 and Q1 = 3 | 5 | 0.032495 |
| Q20 = 3 and Q7 = 2 | 4 | 0.002541 |
| Q20 = 4 and Q16 = 3 and Q6 = 4 | 8 | 0.002470 |
| Q20 = 3 | 3 | 0.000484 |
| Q16 = 2 | 4 | 0.001389 |
| Q16 = 3 and difficulty = 3 | 13 | 0.003568 |
| Q16 = 3 and Q21 = 3 | 3 | 0.000153 |
| Q16 = 4 and Q17 = 4 and Q10 = 3 and Q1 = 3 | 5 | 0.004480 |
| Q1 = 2 and Q6 = 4 | 9 | 0.005222 |
| Q2 = 3 and Q1 = 3 | 3 | 0.000858 |
| Q12 = 3 and difficulty = 4 | 4 | 0.001059 |
| Q12 = 3 | 8 | 0.020164 |
|  | 13 | 0.129983 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| instr = 1 and Q25 = 5 and difficulty = 4 and Q6 = 5 and attendance = 3 | 2 | 0.000962 |
| instr = 1 and difficulty = 4 and nb.repeat = 3 and attendance = 0 | 7 | 0.001584 |
| instr = 1 and difficulty = 4 and Q1 = 2 and Q9 = 3 and Q4 = 2 | 7 | 0.001980 |
| instr = 1 and difficulty = 4 and attendance = 1 and Q26 = 3 | 7 | 0.001604 |
| instr = 1 and difficulty = 5 and Q3 = 3 and Q15 = 4 | 7 | 0.001584 |
| instr = 1 and difficulty = 4 and Q25 = 4 and Q3 = 3 and Q15 = 4 | 7 | 0.001584 |
| instr = 1 and Q7 = 1 and difficulty = 5 | 7 | 0.001765 |
| instr = 1 and difficulty = 4 and Q11 = 5 and Q3 = 4 | 7 | 0.001079 |
| instr = 2 and Q12 = 5 and Q6 = 4 | 1 | 0.001206 |
| instr = 1 and difficulty = 1 and Q6 = 4 | 10 | 0.005461 |
| instr = 1 and difficulty = 3 and Q25 = 4 and Q14 = 4 and Q11 = 4 and attendance = 3 | 10 | 0.004899 |
| instr = 1 and difficulty = 1 and Q12 = 2 | 10 | 0.003368 |
| instr = 1 and difficulty = 3 and Q25 = 4 and attendance = 2 | 10 | 0.002543 |
| instr = 1 and difficulty = 2 and Q4 = 2 | 10 | 0.002528 |
| instr = 1 and difficulty = 3 and Q26 = 3 and Q9 = 4 | 10 | 0.001500 |
| instr = 1 and difficulty = 3 and Q2 = 3 and Q17 = 4 | 10 | 0.001476 |
| instr = 1 and difficulty = 1 and Q12 = 3 and Q2 = 3 | 10 | 0.002948 |
| instr = 1 and difficulty = 3 and attendance = 3 and Q10 = 5 | 10 | 0.003570 |
| instr = 1 and difficulty = 2 and Q26 = 3 and nb.repeat = 1 | 10 | 0.002318 |
| instr = 1 and difficulty = 3 and Q8 = 3 and Q2 = 3 and attendance = 3 and Q20 = 3 | 10 | 0.001708 |
| instr = 1 and difficulty = 3 and Q5 = 4 | 10 | 0.003895 |
| instr = 1 and difficulty = 1 and Q9 = 5 | 10 | 0.003454 |
| instr = 1 and difficulty = 2 and Q18 = 4 | 10 | 0.002374 |
| instr = 1 and difficulty = 3 and Q26 = 3 and attendance = 2 | 10 | 0.001350 |
| instr = 1 and attendance = 4 and Q15 = 2 | 10 | 0.001476 |
| instr = 1 and difficulty = 3 and Q16 = 2 | 10 | 0.001406 |
| instr = 1 and Q17 = 1 | 10 | 0.004665 |
| instr = 1 and Q1 = 4 and Q26 = 3 | 10 | 0.001424 |
| instr = 1 and attendance = 4 and Q1 = 5 | 10 | 0.002177 |
| instr = 2 and difficulty = 4 and Q13 = 4 and Q6 = 2 | 11 | 0.002277 |
| instr = 2 and difficulty = 4 and Q13 = 4 | 11 | 0.006799 |
| instr = 2 and difficulty = 4 and Q21 = 3 | 11 | 0.004947 |
| instr = 2 and difficulty = 5 and Q20 = 5 and nb.repeat = 1 | 11 | 0.001898 |
| instr = 2 and difficulty = 3 and Q27 = 4 and Q21 = 5 | 11 | 0.001459 |
| instr = 2 and difficulty = 3 and Q18 = 4 and Q26 = 3 and Q20 = 3 | 11 | 0.001595 |
| instr = 2 and difficulty = 5 and nb.repeat = 1 and attendance = 1 | 11 | 0.001326 |
| instr = 2 and difficulty = 3 and Q10 = 3 and Q4 = 4 and Q3 = 4 | 11 | 0.001396 |
| instr = 3 and attendance = 4 and Q1 = 2 and Q3 = 4 and Q2 = 4 | 8 | 0.001678 |
| instr = 3 and Q21 = 4 and Q1 = 1 and Q5 = 1 and Q23 = 1 and nb.repeat = 1 | 8 | 0.001887 |
| instr = 3 and attendance = 4 and Q10 = 3 and Q12 = 2 and Q15 = 4 | 8 | 0.002122 |
| instr = 3 and Q21 = 5 and Q14 = 4 and Q4 = 3 | 8 | 0.001815 |
| instr = 2 and attendance = 1 and Q9 = 3 and Q22 = 4 and Q3 = 3 | 6 | 0.001949 |
| instr = 2 and difficulty = 2 and Q18 = 4 and Q11 = 3 | 6 | 0.002474 |
| instr = 2 and attendance = 1 and Q1 = 1 | 6 | 0.002517 |
| instr = 2 and Q3 = 5 and attendance = 2 | 6 | 0.002247 |
| instr = 2 and Q4 = 4 and Q6 = 5 | 6 | 0.001825 |
| instr = 2 and Q28 = 2 and Q4 = 3 | 6 | 0.001625 |
| instr = 2 and Q7 = 4 and Q12 = 3 and Q28 = 4 and Q27 = 4 | 6 | 0.002006 |
| instr = 2 and Q12 = 4 and difficulty = 2 | 6 | 0.002653 |
| instr = 2 and difficulty = 3 and attendance = 0 and Q18 = 5 | 6 | 0.002166 |
| instr = 2 and difficulty = 3 and Q17 = 2 | 6 | 0.001938 |
| instr = 2 and Q12 = 4 and Q1 = 4 and Q24 = 5 | 6 | 0.001394 |
| instr = 2 and Q9 = 3 and Q27 = 2 and Q24 = 3 | 6 | 0.001475 |
| instr = 2 and Q3 = 5 and Q25 = 4 | 6 | 0.001339 |
| instr = 3 and nb.repeat = 2 and Q8 = 3 and Q24 = 4 | 9 | 0.001791 |
| instr = 3 and nb.repeat = 1 and difficulty = 4 and Q1 = 4 and attendance = 2 | 5 | 0.002266 |
| instr = 3 and nb.repeat = 1 and difficulty = 4 and Q13 = 4 and Q17 = 3 | 5 | 0.001493 |
| instr = 3 and nb.repeat = 1 and difficulty = 4 and Q2 = 3 and Q11 = 1 | 5 | 0.001493 |
| instr = 3 and nb.repeat = 1 and Q13 = 4 and Q4 = 3 and Q3 = 2 | 5 | 0.001257 |
| instr = 3 and nb.repeat = 1 and Q6 = 4 and Q22 = 3 and Q9 = 2 | 5 | 0.001571 |
| instr = 3 and Q6 = 1 and difficulty = 2 | 13 | 0.003515 |
| instr = 3 and Q17 = 1 and Q7 = 3 | 13 | 0.001735 |
| instr = 3 and Q6 = 1 and difficulty = 1 and Q10 = 2 | 13 | 0.001578 |
| instr = 3 and Q11 = 1 and difficulty = 1 and Q24 = 2 | 13 | 0.001329 |
|  | 3 | 0.184384 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

instr|difficulty|q21|class
---|---|---|---
2|5|5|11
1|5|5|2
3|5|5|3
2|4|5|11
1|4|5|2
3|4|5|8
2|5|4|11
2|3|5|6
1|3|5|10
1|5|4|10
3|5|4|3
3|3|5|8
1|2|5|10
2|4|4|11
2|2|5|6
1|4|4|7
3|2|5|13
3|4|4|5
2|5|3|11
1|5|3|7
2|3|4|6
2|1|5|6
1|1|5|10
1|3|4|10
3|5|3|3
3|3|4|3
3|1|5|13
2|4|3|11
2|2|4|6
1|4|3|7
1|2|4|10
3|2|4|8
3|4|3|3
1|5|2|7
2|5|2|11
2|3|3|6
2|1|4|6
1|1|4|10
1|3|3|10
3|5|2|3
3|1|4|3
3|3|3|3
1|2|3|10
2|4|2|11
2|2|3|6
3|2|3|13
1|4|2|2
3|4|2|3
2|3|2|6
2|5|1|6
2|1|3|6
1|5|1|7
1|3|2|10
1|1|3|10
3|5|1|3
3|3|2|3
3|1|3|3
2|4|1|6
1|2|2|10
2|2|2|6
1|4|1|7
3|4|1|3
3|2|2|13
2|1|2|6
2|3|1|6
1|3|1|10
1|1|2|10
3|3|1|13
3|1|2|3
2|2|1|6
1|2|1|10
3|2|1|13
1|1|1|10
2|1|1|6
3|1|1|13

## JRip

Decision list:

rules | predicted class
---|---
(instr = 1) and (Q25 = 5) and (difficulty = 4) and (Q6 = 5) and (attendance = 3)|2 (10.0/3.0)
(instr = 1) and (difficulty = 4) and (nb.repeat = 3) and (attendance = 0)|7 (8.0/0.0)
(instr = 1) and (difficulty = 4) and (Q1 = 2) and (Q9 = 3) and (Q4 = 2)|7 (10.0/0.0)
(instr = 1) and (difficulty = 4) and (attendance = 1) and (Q26 = 3)|7 (10.0/1.0)
(instr = 1) and (difficulty = 5) and (Q3 = 3) and (Q15 = 4)|7 (8.0/0.0)
(instr = 1) and (difficulty = 4) and (Q25 = 4) and (Q3 = 3) and (Q15 = 4)|7 (8.0/0.0)
(instr = 1) and (Q7 = 1) and (difficulty = 5)|7 (22.0/8.0)
(instr = 1) and (difficulty = 4) and (Q11 = 5) and (Q3 = 4)|7 (9.0/2.0)
(instr = 2) and (Q12 = 5) and (Q6 = 4)|1 (17.0/7.0)
(instr = 1) and (difficulty = 1) and (Q6 = 4)|10 (26.0/0.0)
(instr = 1) and (difficulty = 3) and (Q25 = 4) and (Q14 = 4) and (Q11 = 4) and (attendance = 3)|10 (29.0/3.0)
(instr = 1) and (difficulty = 1) and (Q12 = 2)|10 (16.0/0.0)
(instr = 1) and (difficulty = 3) and (Q25 = 4) and (attendance = 2)|10 (14.0/1.0)
(instr = 1) and (difficulty = 2) and (Q4 = 2)|10 (12.0/0.0)
(instr = 1) and (difficulty = 3) and (Q26 = 3) and (Q9 = 4)|10 (9.0/1.0)
(instr = 1) and (difficulty = 3) and (Q2 = 3) and (Q17 = 4)|10 (7.0/0.0)
(instr = 1) and (difficulty = 1) and (Q12 = 3) and (Q2 = 3)|10 (14.0/0.0)
(instr = 1) and (difficulty = 3) and (attendance = 3) and (Q10 = 5)|10 (26.0/5.0)
(instr = 1) and (difficulty = 2) and (Q26 = 3) and (nb.repeat = 1)|10 (11.0/0.0)
(instr = 1) and (difficulty = 3) and (Q8 = 3) and (Q2 = 3) and (attendance = 3) and (Q20 = 3)|10 (10.0/1.0)
(instr = 1) and (difficulty = 3) and (Q5 = 4)|10 (47.0/16.0)
(instr = 1) and (difficulty = 1) and (Q9 = 5)|10 (22.0/3.0)
(instr = 1) and (difficulty = 2) and (Q18 = 4)|10 (15.0/2.0)
(instr = 1) and (difficulty = 3) and (Q26 = 3) and (attendance = 2)|10 (10.0/2.0)
(instr = 1) and (attendance = 4) and (Q15 = 2)|10 (7.0/0.0)
(instr = 1) and (difficulty = 3) and (Q16 = 2)|10 (14.0/4.0)
(instr = 1) and (Q17 = 1)|10 (69.0/32.0)
(instr = 1) and (Q1 = 4) and (Q26 = 3)|10 (10.0/1.0)
(instr = 1) and (attendance = 4) and (Q1 = 5)|10 (28.0/11.0)
(instr = 2) and (difficulty = 4) and (Q13 = 4) and (Q6 = 2)|11 (10.0/0.0)
(instr = 2) and (difficulty = 4) and (Q13 = 4)|11 (75.0/29.0)
(instr = 2) and (difficulty = 4) and (Q21 = 3)|11 (62.0/25.0)
(instr = 2) and (difficulty = 5) and (Q20 = 5) and (nb.repeat = 1)|11 (12.0/2.0)
(instr = 2) and (difficulty = 3) and (Q27 = 4) and (Q21 = 5)|11 (10.0/2.0)
(instr = 2) and (difficulty = 3) and (Q18 = 4) and (Q26 = 3) and (Q20 = 3)|11 (7.0/0.0)
(instr = 2) and (difficulty = 5) and (nb.repeat = 1) and (attendance = 1)|11 (10.0/2.0)
(instr = 2) and (difficulty = 3) and (Q10 = 3) and (Q4 = 4) and (Q3 = 4)|11 (8.0/1.0)
(instr = 3) and (attendance = 4) and (Q1 = 2) and (Q3 = 4) and (Q2 = 4)|8 (9.0/1.0)
(instr = 3) and (Q21 = 4) and (Q1 = 1) and (Q5 = 1) and (Q23 = 1) and (nb.repeat = 1)|8 (8.0/0.0)
(instr = 3) and (attendance = 4) and (Q10 = 3) and (Q12 = 2) and (Q15 = 4)|8 (9.0/0.0)
(instr = 3) and (Q21 = 5) and (Q14 = 4) and (Q4 = 3)|8 (13.0/3.0)
(instr = 2) and (attendance = 1) and (Q9 = 3) and (Q22 = 4) and (Q3 = 3)|6 (8.0/0.0)
(instr = 2) and (difficulty = 2) and (Q18 = 4) and (Q11 = 3)|6 (14.0/2.0)
(instr = 2) and (attendance = 1) and (Q1 = 1)|6 (30.0/12.0)
(instr = 2) and (Q3 = 5) and (attendance = 2)|6 (20.0/6.0)
(instr = 2) and (Q4 = 4) and (Q6 = 5)|6 (19.0/7.0)
(instr = 2) and (Q28 = 2) and (Q4 = 3)|6 (12.0/3.0)
(instr = 2) and (Q7 = 4) and (Q12 = 3) and (Q28 = 4) and (Q27 = 4)|6 (12.0/2.0)
(instr = 2) and (Q12 = 4) and (difficulty = 2)|6 (42.0/20.0)
(instr = 2) and (difficulty = 3) and (attendance = 0) and (Q18 = 5)|6 (9.0/0.0)
(instr = 2) and (difficulty = 3) and (Q17 = 2)|6 (20.0/7.0)
(instr = 2) and (Q12 = 4) and (Q1 = 4) and (Q24 = 5)|6 (11.0/3.0)
(instr = 2) and (Q9 = 3) and (Q27 = 2) and (Q24 = 3)|6 (7.0/0.0)
(instr = 2) and (Q3 = 5) and (Q25 = 4)|6 (16.0/6.0)
(instr = 3) and (nb.repeat = 2) and (Q8 = 3) and (Q24 = 4)|9 (14.0/4.0)
(instr = 3) and (nb.repeat = 1) and (difficulty = 4) and (Q1 = 4) and (attendance = 2)|5 (29.0/13.0)
(instr = 3) and (nb.repeat = 1) and (difficulty = 4) and (Q13 = 4) and (Q17 = 3)|5 (11.0/3.0)
(instr = 3) and (nb.repeat = 1) and (difficulty = 4) and (Q2 = 3) and (Q11 = 1)|5 (11.0/3.0)
(instr = 3) and (nb.repeat = 1) and (Q13 = 4) and (Q4 = 3) and (Q3 = 2)|5 (10.0/3.0)
(instr = 3) and (nb.repeat = 1) and (Q6 = 4) and (Q22 = 3) and (Q9 = 2)|5 (8.0/1.0)
(instr = 3) and (Q6 = 1) and (difficulty = 2)|13 (34.0/13.0)
(instr = 3) and (Q17 = 1) and (Q7 = 3)|13 (10.0/2.0)
(instr = 3) and (Q6 = 1) and (difficulty = 1) and (Q10 = 2)|13 (11.0/3.0)
(instr = 3) and (Q11 = 1) and (difficulty = 1) and (Q24 = 2)|13 (10.0/3.0)
|3 (4117.0/3321.0)


## PART

Decision list:

rules | predicted class
---|---
instr = 1 AND difficulty = 1|10 (119.0/22.0)
instr = 1 AND difficulty = 3 AND Q18 = 4|10 (89.0/19.0)
instr = 1 AND difficulty = 3 AND Q13 = 5|10 (68.0/24.0)
instr = 1 AND difficulty = 2|10 (58.0/11.0)
instr = 1 AND difficulty = 3 AND Q24 = 3 AND Q26 = 3|10 (52.0/16.0)
instr = 1 AND nb.repeat = 3|7 (26.0/6.0)
instr = 1 AND Q1 = 1 AND Q9 = 1 AND Q4 = 1 AND Q5 = 1 AND Q20 = 1 AND difficulty = 5|7 (17.0/7.0)
instr = 1 AND Q1 = 5 AND Q19 = 5|2 (34.0/15.0)
instr = 1 AND Q17 = 5 AND attendance = 4 AND Q23 = 5|7 (8.0)
instr = 1 AND difficulty = 3 AND Q24 = 1|10 (19.0/8.0)
instr = 1 AND attendance = 0|10 (18.0/8.0)
instr = 1 AND difficulty = 3 AND Q24 = 2 AND Q9 = 2|10 (7.0/1.0)
instr = 1 AND Q6 = 1|7 (23.0/9.0)
instr = 1 AND Q17 = 2 AND Q16 = 2 AND Q8 = 3|10 (5.0)
instr = 1 AND Q1 = 2 AND Q24 = 4|7 (14.0/4.0)
instr = 1 AND Q22 = 1|2 (4.0/1.0)
instr = 1 AND Q25 = 2 AND Q28 = 2 AND Q23 = 2|2 (9.0/3.0)
instr = 1 AND Q10 = 3 AND Q4 = 3 AND Q1 = 3 AND Q23 = 3 AND Q17 = 3 AND difficulty = 4|10 (17.0/8.0)
instr = 1 AND Q10 = 2|7 (13.0/4.0)
instr = 1 AND Q2 = 4 AND Q1 = 4 AND Q23 = 4 AND Q28 = 4 AND Q21 = 4 AND Q9 = 4 AND attendance = 3|2 (14.0/7.0)
instr = 1 AND Q2 = 4 AND Q1 = 4 AND Q6 = 4 AND Q23 = 4 AND Q18 = 4 AND Q12 = 4|10 (19.0/10.0)
instr = 1 AND Q2 = 2|7 (6.0)
instr = 1 AND nb.repeat = 1 AND difficulty = 3 AND Q24 = 4|10 (5.0)
instr = 1 AND Q1 = 3|7 (23.0/10.0)
instr = 1 AND Q9 = 4|10 (17.0/7.0)
instr = 1 AND attendance = 1|2 (3.0/1.0)
instr = 1 AND Q13 = 4|10 (2.0)
instr = 1 AND attendance = 2|2 (2.0)
instr = 2 AND difficulty = 5 AND nb.repeat = 1|11 (64.0/27.0)
instr = 2 AND difficulty = 5|6 (11.0/4.0)
instr = 2 AND difficulty = 4 AND Q27 = 1 AND Q2 = 1|6 (10.0/2.0)
instr = 2 AND difficulty = 4 AND Q8 = 3|11 (75.0/31.0)
instr = 2 AND difficulty = 4 AND Q13 = 4|11 (73.0/24.0)
instr = 2 AND difficulty = 2 AND nb.repeat = 2 AND Q4 = 2 AND attendance = 1|11 (8.0/4.0)
instr = 2 AND difficulty = 2 AND Q14 = 2 AND Q5 = 2|6 (6.0)
instr = 2 AND difficulty = 2 AND Q14 = 4 AND Q22 = 3|6 (9.0/2.0)
instr = 2 AND difficulty = 3 AND attendance = 0 AND Q27 = 3|6 (18.0/8.0)
instr = 2 AND difficulty = 3 AND Q6 = 5 AND Q11 = 5 AND Q15 = 5 AND Q2 = 5 AND attendance = 4 AND Q13 = 5|1 (24.0/15.0)
instr = 2 AND difficulty = 3 AND Q6 = 5 AND Q11 = 5 AND Q5 = 5|6 (53.0/20.0)
instr = 2 AND difficulty = 2 AND Q14 = 4 AND Q22 = 5 AND Q13 = 4|6 (5.0/1.0)
instr = 1|7 (2.0)
instr = 2 AND difficulty = 3 AND Q21 = 2 AND Q9 = 4 AND attendance = 2|1 (2.0)
instr = 2 AND difficulty = 3 AND Q21 = 2|6 (27.0/10.0)
instr = 2 AND difficulty = 2 AND Q14 = 4 AND Q22 = 4 AND Q24 = 4 AND Q13 = 4 AND Q4 = 4 AND Q5 = 4|6 (29.0/13.0)
instr = 2 AND difficulty = 3 AND Q22 = 2 AND Q1 = 1|11 (3.0/1.0)
instr = 2 AND difficulty = 3 AND Q21 = 1|6 (26.0/14.0)
instr = 2 AND difficulty = 3 AND Q6 = 1|11 (18.0/7.0)
instr = 2 AND difficulty = 3 AND Q24 = 4 AND nb.repeat = 1 AND Q21 = 3|11 (5.0/1.0)
instr = 2 AND difficulty = 3 AND Q24 = 4 AND Q21 = 5 AND Q16 = 4|11 (3.0)
instr = 2 AND difficulty = 3 AND Q24 = 4 AND nb.repeat = 1 AND Q11 = 3 AND Q10 = 3 AND Q16 = 4|6 (20.0/7.0)
instr = 2 AND difficulty = 2 AND Q1 = 4 AND Q27 = 4|6 (5.0/2.0)
instr = 2 AND difficulty = 2 AND Q1 = 4 AND Q27 = 3|6 (4.0)
instr = 2 AND Q12 = 4 AND Q11 = 3 AND difficulty = 3|1 (3.0)
instr = 2 AND Q12 = 4 AND Q11 = 4 AND Q6 = 5|6 (10.0/1.0)
instr = 2 AND Q12 = 4 AND Q11 = 5|11 (10.0/4.0)
instr = 2 AND Q12 = 4 AND Q26 = 3 AND Q2 = 4 AND Q1 = 4|6 (7.0/3.0)
instr = 2 AND Q12 = 4 AND Q26 = 3 AND Q2 = 3|6 (3.0)
instr = 2 AND Q12 = 4 AND Q26 = 3|13 (4.0/1.0)
instr = 2 AND Q12 = 4 AND Q7 = 3 AND Q3 = 4|11 (5.0/1.0)
instr = 2 AND Q12 = 4 AND Q7 = 3|6 (3.0/1.0)
instr = 2 AND Q12 = 4 AND Q5 = 4 AND Q2 = 4 AND Q8 = 4 AND Q4 = 4 AND Q1 = 4|6 (147.0/82.0)
instr = 2 AND Q6 = 2 AND Q1 = 4 AND Q9 = 4|11 (3.0/1.0)
instr = 2 AND Q6 = 2 AND Q5 = 3 AND Q11 = 2|11 (6.0/2.0)
instr = 2 AND Q6 = 2 AND Q5 = 3 AND Q11 = 3|6 (6.0/1.0)
instr = 2 AND Q6 = 2 AND Q5 = 2 AND Q13 = 3 AND Q8 = 2|1 (8.0/1.0)
instr = 2 AND Q6 = 2 AND Q5 = 3|11 (6.0)
instr = 2 AND Q6 = 4 AND nb.repeat = 1 AND Q7 = 2|13 (4.0/1.0)
instr = 2 AND Q12 = 4 AND nb.repeat = 1 AND Q7 = 4|1 (28.0/13.0)
instr = 2 AND Q12 = 4 AND Q17 = 4|6 (5.0/1.0)
instr = 2 AND Q12 = 5 AND Q6 = 4|1 (14.0/4.0)
instr = 2 AND Q12 = 5 AND nb.repeat = 2|1 (5.0/2.0)
instr = 2 AND attendance = 1 AND Q18 = 3 AND Q21 = 3|6 (41.0/19.0)
instr = 2 AND Q12 = 4|11 (3.0)
instr = 2 AND Q4 = 5 AND Q17 = 5 AND Q3 = 5|6 (89.0/53.0)
instr = 2 AND Q2 = 5 AND Q11 = 5|6 (7.0/1.0)
instr = 2 AND Q7 = 5|13 (8.0/4.0)
instr = 2 AND Q6 = 5 AND Q23 = 4|6 (2.0)
instr = 2 AND Q6 = 5 AND Q21 = 4|1 (4.0/1.0)
instr = 2 AND difficulty = 4 AND Q5 = 2|11 (8.0)
instr = 2 AND Q6 = 2 AND nb.repeat = 1 AND Q7 = 2 AND Q5 = 2 AND Q4 = 2 AND Q21 = 2|11 (15.0/9.0)
instr = 2 AND Q6 = 2 AND Q1 = 1|6 (12.0/4.0)
instr = 2 AND Q6 = 2 AND Q28 = 4 AND difficulty = 3 AND Q14 = 4|1 (8.0/2.0)
instr = 2 AND Q6 = 3 AND Q8 = 2 AND Q18 = 4 AND Q16 = 3|6 (4.0/1.0)
instr = 2 AND Q6 = 3 AND Q8 = 2|11 (8.0/2.0)
instr = 2 AND Q22 = 2 AND difficulty = 1|6 (9.0/3.0)
instr = 2 AND Q7 = 2 AND Q19 = 3 AND Q26 = 3|1 (5.0/1.0)
instr = 2 AND Q14 = 2 AND Q2 = 1|11 (3.0)
instr = 2 AND Q27 = 2 AND Q15 = 2|6 (3.0/1.0)
instr = 2 AND Q7 = 2 AND Q19 = 4|13 (5.0/2.0)
instr = 2 AND Q6 = 2 AND Q8 = 2|11 (3.0)
instr = 2 AND Q6 = 3 AND Q10 = 3 AND Q4 = 3 AND Q12 = 3 AND Q27 = 4 AND Q15 = 4 AND nb.repeat = 1|6 (6.0/2.0)
instr = 2 AND Q6 = 3 AND Q10 = 3 AND Q4 = 3 AND Q24 = 4 AND Q14 = 4|11 (6.0/2.0)
instr = 2 AND Q2 = 2|6 (15.0/6.0)
instr = 2 AND Q24 = 4 AND attendance = 1|6 (8.0/1.0)
instr = 2 AND Q13 = 2 AND Q3 = 3|11 (2.0/1.0)
instr = 2 AND Q13 = 5|6 (8.0/4.0)
instr = 2 AND Q16 = 5 AND Q7 = 3|11 (4.0)
instr = 2 AND Q9 = 2|1 (6.0/2.0)
instr = 2 AND Q16 = 4 AND Q21 = 4 AND Q20 = 4 AND Q7 = 3|1 (4.0/2.0)
instr = 2 AND Q16 = 4 AND Q4 = 3 AND Q10 = 3|13 (4.0)
instr = 2 AND Q4 = 4 AND Q6 = 4 AND Q14 = 4|13 (5.0/2.0)
instr = 2 AND Q16 = 4 AND Q4 = 3|1 (3.0)
instr = 2 AND Q16 = 4 AND Q14 = 4|13 (4.0/1.0)
instr = 2 AND Q24 = 3 AND Q28 = 3 AND Q16 = 3 AND Q9 = 3 AND Q7 = 3 AND Q1 = 3 AND attendance = 3 AND nb.repeat = 1|6 (17.0/6.0)
instr = 2 AND Q16 = 3 AND Q24 = 3 AND Q28 = 3 AND Q27 = 3 AND Q12 = 3 AND Q3 = 3 AND Q1 = 3 AND attendance = 0 AND difficulty = 1|1 (44.0/30.0)
instr = 2 AND Q16 = 3 AND Q24 = 3 AND Q28 = 3 AND Q27 = 3|11 (63.0/36.0)
instr = 2 AND Q24 = 3 AND Q14 = 3|1 (8.0/1.0)
instr = 2 AND Q17 = 1|6 (65.0/40.0)
nb.repeat = 3 AND Q11 = 5 AND Q1 = 5 AND Q14 = 5 AND Q23 = 5 AND attendance = 4|13 (10.0/4.0)
nb.repeat = 3 AND Q11 = 5 AND Q1 = 5 AND Q14 = 5 AND Q23 = 5|8 (20.0/10.0)
difficulty = 2 AND Q14 = 2 AND Q2 = 2|13 (34.0/13.0)
difficulty = 5 AND nb.repeat = 2 AND Q16 = 2|3 (7.0/2.0)
difficulty = 5 AND Q4 = 5 AND nb.repeat = 1|5 (40.0/24.0)
difficulty = 2 AND Q14 = 2 AND Q1 = 1|8 (3.0)
difficulty = 2 AND Q17 = 2 AND Q5 = 2|13 (4.0/1.0)
difficulty = 5 AND Q16 = 5|13 (14.0/6.0)
Q21 = 1 AND Q23 = 2 AND Q16 = 1|13 (8.0/2.0)
difficulty = 5 AND Q11 = 1 AND Q17 = 3 AND nb.repeat = 1|5 (8.0/2.0)
difficulty = 5 AND Q11 = 5|8 (8.0/2.0)
difficulty = 5 AND Q1 = 4 AND Q2 = 4 AND Q27 = 4 AND attendance = 3|3 (8.0/3.0)
difficulty = 5 AND Q9 = 5 AND Q10 = 1|8 (4.0/1.0)
difficulty = 5 AND Q9 = 5|5 (4.0/2.0)
difficulty = 5 AND Q11 = 1 AND Q9 = 3|13 (7.0/3.0)
difficulty = 5 AND Q21 = 1 AND Q26 = 1 AND Q9 = 1 AND Q25 = 1 AND nb.repeat = 1 AND Q2 = 1|3 (48.0/28.0)
difficulty = 2 AND Q17 = 1|13 (21.0/7.0)
difficulty = 1 AND Q20 = 2 AND Q13 = 3 AND Q10 = 2|9 (7.0/2.0)
difficulty = 1 AND Q20 = 2 AND Q27 = 3 AND Q4 = 2|13 (5.0/1.0)
difficulty = 1 AND Q20 = 2 AND Q26 = 3 AND Q5 = 3|5 (6.0/1.0)
difficulty = 1 AND Q20 = 2 AND Q26 = 1|13 (4.0/2.0)
difficulty = 1 AND Q20 = 2 AND Q16 = 2 AND Q11 = 2 AND Q22 = 2 AND nb.repeat = 1 AND Q2 = 2|3 (51.0/30.0)
difficulty = 5 AND nb.repeat = 2 AND attendance = 0|3 (12.0/6.0)
difficulty = 5 AND nb.repeat = 2 AND attendance = 4|3 (7.0/3.0)
difficulty = 1 AND Q20 = 2 AND Q16 = 2 AND Q22 = 2 AND attendance = 0 AND Q1 = 2|9 (9.0/4.0)
difficulty = 1 AND Q7 = 1 AND Q11 = 2|13 (4.0/1.0)
difficulty = 1 AND Q7 = 1 AND Q11 = 3 AND attendance = 0|5 (3.0/1.0)
difficulty = 1 AND Q7 = 1 AND Q11 = 3|13 (4.0/1.0)
difficulty = 1 AND Q3 = 1 AND Q1 = 1 AND Q11 = 2|13 (6.0/2.0)
difficulty = 1 AND Q7 = 1 AND Q11 = 5 AND Q16 = 1|8 (4.0/1.0)
difficulty = 1 AND Q7 = 1 AND Q2 = 2|13 (5.0/1.0)
difficulty = 1 AND Q15 = 1 AND Q17 = 1 AND Q10 = 1 AND Q8 = 1 AND Q19 = 1 AND Q1 = 1 AND Q4 = 1 AND attendance = 4|13 (7.0/2.0)
difficulty = 1 AND Q15 = 1 AND Q17 = 1 AND Q10 = 1 AND Q19 = 1 AND Q8 = 1 AND Q1 = 1 AND Q4 = 1 AND attendance = 1 AND nb.repeat = 1|3 (4.0/2.0)
difficulty = 1 AND Q15 = 1 AND Q17 = 1 AND Q10 = 1 AND Q19 = 1 AND Q8 = 1 AND Q1 = 1 AND Q4 = 1 AND attendance = 0 AND Q26 = 1 AND nb.repeat = 1 AND Q6 = 1 AND Q21 = 1 AND Q13 = 1|3 (182.0/121.0)
nb.repeat = 3 AND Q9 = 1|13 (41.0/25.0)
nb.repeat = 3 AND Q18 = 5 AND Q12 = 5|13 (3.0)
nb.repeat = 3 AND Q18 = 5|5 (3.0/1.0)
nb.repeat = 3 AND Q9 = 5|13 (6.0/3.0)
nb.repeat = 3 AND Q10 = 1 AND Q5 = 1|8 (4.0/1.0)
nb.repeat = 3 AND Q10 = 3 AND Q8 = 3 AND Q7 = 3 AND Q1 = 3 AND Q26 = 3 AND difficulty = 2|9 (10.0/5.0)
nb.repeat = 3 AND Q10 = 3 AND Q8 = 3 AND Q7 = 3 AND Q1 = 3 AND Q26 = 3 AND attendance = 1|9 (5.0/1.0)
difficulty = 5 AND nb.repeat = 2 AND Q6 = 3|13 (6.0/2.0)
difficulty = 5 AND Q21 = 5|8 (10.0/4.0)
difficulty = 5 AND Q1 = 3 AND Q24 = 3 AND Q11 = 3 AND Q7 = 3 AND nb.repeat = 1 AND Q15 = 3|3 (54.0/25.0)
difficulty = 1 AND Q20 = 1 AND Q12 = 3|13 (5.0/2.0)
difficulty = 1 AND Q22 = 1 AND Q12 = 1 AND Q10 = 1 AND Q8 = 1 AND Q4 = 2 AND Q6 = 1|5 (3.0)
difficulty = 1 AND Q22 = 1 AND Q12 = 1 AND Q10 = 1 AND Q7 = 1|13 (26.0/10.0)
nb.repeat = 3 AND Q10 = 3 AND Q8 = 3 AND Q7 = 3 AND Q1 = 3 AND Q26 = 3 AND attendance = 2 AND difficulty = 3|9 (4.0/2.0)
difficulty = 1 AND Q15 = 1 AND Q17 = 1 AND Q7 = 2 AND nb.repeat = 1|13 (4.0/2.0)
nb.repeat = 3 AND Q10 = 3 AND Q3 = 4|9 (5.0/2.0)
difficulty = 1 AND Q15 = 1 AND Q17 = 1|3 (7.0/4.0)
difficulty = 1 AND Q15 = 1 AND Q9 = 2|13 (2.0)
difficulty = 1 AND Q15 = 3 AND attendance = 2|3 (4.0/1.0)
difficulty = 5 AND Q22 = 4 AND Q7 = 3|3 (4.0/1.0)
difficulty = 1 AND Q15 = 3 AND attendance = 4 AND Q28 = 3|3 (4.0/1.0)
difficulty = 1 AND Q15 = 1|4 (2.0/1.0)
difficulty = 1 AND Q24 = 1 AND Q8 = 1 AND Q10 = 2|13 (3.0)
difficulty = 1 AND Q24 = 1 AND Q7 = 1|3 (3.0/1.0)
difficulty = 1 AND Q24 = 1|9 (7.0/2.0)
difficulty = 1 AND Q6 = 3 AND Q8 = 2 AND Q22 = 2 AND Q21 = 2|3 (4.0)
instr = 2 AND Q1 = 1|1 (2.0/1.0)
nb.repeat = 3 AND difficulty = 2 AND Q21 = 4|8 (6.0/1.0)
difficulty = 1 AND Q27 = 1 AND Q22 = 5|8 (5.0/1.0)
nb.repeat = 3 AND Q27 = 5|8 (4.0/1.0)
nb.repeat = 3 AND Q11 = 2 AND attendance = 0|13 (6.0/2.0)
nb.repeat = 3 AND Q11 = 2 AND Q1 = 2|9 (6.0/3.0)
difficulty = 1 AND Q28 = 5 AND Q21 = 4|3 (9.0/4.0)
difficulty = 1 AND Q28 = 1|5 (3.0/1.0)
difficulty = 1 AND Q24 = 5 AND Q27 = 5 AND Q4 = 4 AND Q22 = 5|13 (4.0)
difficulty = 1 AND Q8 = 3 AND Q7 = 2|3 (10.0/5.0)
difficulty = 1 AND Q17 = 5 AND Q15 = 4 AND Q3 = 4|9 (6.0/2.0)
difficulty = 1 AND Q17 = 5 AND Q16 = 5 AND Q12 = 5 AND Q3 = 5 AND attendance = 0 AND nb.repeat = 1|5 (88.0/67.0)
nb.repeat = 3 AND Q7 = 1|13 (4.0/2.0)
nb.repeat = 3 AND Q11 = 1|4 (3.0/2.0)
nb.repeat = 3 AND difficulty = 1 AND Q3 = 3|9 (10.0/5.0)
nb.repeat = 3 AND difficulty = 4|3 (25.0/13.0)
difficulty = 1 AND Q8 = 3 AND Q3 = 2|3 (8.0/3.0)
difficulty = 1 AND Q19 = 1 AND Q5 = 2|3 (3.0/1.0)
difficulty = 1 AND Q9 = 1 AND Q26 = 4|5 (4.0/1.0)
difficulty = 1 AND Q8 = 1 AND Q4 = 1 AND Q10 = 1|13 (4.0/1.0)
difficulty = 1 AND Q8 = 1 AND Q13 = 2|9 (3.0)
nb.repeat = 2 AND Q11 = 1 AND Q8 = 1|13 (20.0/9.0)
nb.repeat = 3 AND difficulty = 3 AND attendance = 0|9 (8.0/4.0)
difficulty = 1 AND Q8 = 3 AND Q10 = 4 AND Q2 = 4|13 (6.0/1.0)
difficulty = 1 AND Q9 = 5 AND Q8 = 3|13 (3.0/1.0)
difficulty = 1 AND Q9 = 5 AND Q12 = 4 AND Q10 = 4|5 (4.0/1.0)
difficulty = 1 AND Q9 = 5 AND Q12 = 5 AND Q2 = 5 AND Q28 = 5 AND attendance = 4|3 (9.0/5.0)
difficulty = 1 AND Q9 = 5 AND Q12 = 5 AND Q2 = 5 AND Q28 = 5 AND attendance = 3|5 (5.0/3.0)
difficulty = 1 AND Q9 = 5 AND Q12 = 5 AND Q18 = 4|5 (6.0/3.0)
difficulty = 1 AND Q9 = 5|13 (27.0/15.0)
difficulty = 1 AND Q22 = 5 AND attendance = 0 AND Q19 = 5|13 (4.0)
difficulty = 1 AND Q22 = 5 AND Q7 = 2|8 (3.0)
difficulty = 1 AND Q8 = 5 AND Q6 = 4|5 (3.0/1.0)
difficulty = 1 AND Q8 = 5 AND Q2 = 3|4 (2.0)
difficulty = 1 AND Q8 = 5 AND Q28 = 4|3 (2.0)
difficulty = 1 AND attendance = 1 AND Q25 = 3|3 (13.0/7.0)
difficulty = 1 AND attendance = 1 AND Q1 = 3|8 (3.0/1.0)
difficulty = 1 AND attendance = 4|5 (13.0/7.0)
difficulty = 1 AND Q12 = 5 AND Q23 = 3|4 (2.0)
difficulty = 1 AND Q16 = 5 AND Q28 = 4|5 (3.0/1.0)
nb.repeat = 2 AND Q14 = 5 AND Q27 = 5 AND difficulty = 3|8 (17.0/9.0)
difficulty = 1 AND Q16 = 2 AND Q27 = 2 AND Q22 = 2|3 (5.0/3.0)
difficulty = 1 AND Q17 = 2 AND Q24 = 2|5 (4.0/1.0)
difficulty = 1 AND Q16 = 2 AND Q27 = 3|13 (4.0/1.0)
difficulty = 1 AND Q16 = 2|9 (4.0/1.0)
difficulty = 1 AND Q19 = 5|3 (3.0)
difficulty = 1 AND Q12 = 5|5 (3.0/2.0)
difficulty = 1 AND Q15 = 2 AND Q8 = 2|13 (3.0/1.0)
difficulty = 1 AND Q6 = 2 AND Q25 = 3 AND Q23 = 3|9 (5.0/3.0)
difficulty = 1 AND Q6 = 2 AND Q16 = 3 AND Q25 = 2|5 (3.0)
difficulty = 1 AND Q6 = 2|8 (6.0/3.0)
difficulty = 1 AND Q19 = 2 AND Q23 = 2|4 (3.0/1.0)
difficulty = 1 AND Q10 = 2 AND Q2 = 2|9 (5.0/1.0)
difficulty = 1 AND Q11 = 3 AND Q5 = 3 AND Q12 = 3 AND Q18 = 3 AND Q28 = 3 AND Q2 = 3 AND Q1 = 3 AND attendance = 0|3 (148.0/92.0)
nb.repeat = 3 AND Q1 = 2 AND Q11 = 3|8 (2.0)
nb.repeat = 3 AND Q1 = 3 AND Q14 = 3|13 (9.0/4.0)
nb.repeat = 2 AND Q14 = 1|5 (9.0/4.0)
nb.repeat = 2 AND Q11 = 1 AND Q21 = 3|3 (2.0/1.0)
nb.repeat = 2 AND Q11 = 1|5 (2.0)
nb.repeat = 2 AND attendance = 4 AND Q16 = 3|9 (3.0/1.0)
nb.repeat = 2 AND attendance = 4|3 (10.0/5.0)
nb.repeat = 2 AND Q10 = 1|4 (3.0/2.0)
nb.repeat = 2 AND attendance = 0 AND Q8 = 2 AND Q9 = 2|3 (4.0/1.0)
nb.repeat = 2 AND attendance = 0 AND Q8 = 3|9 (21.0/11.0)
nb.repeat = 2 AND attendance = 0 AND Q8 = 5 AND difficulty = 4|13 (3.0/1.0)
nb.repeat = 2 AND attendance = 0|13 (21.0/13.0)
nb.repeat = 2 AND attendance = 2 AND Q26 = 4 AND Q8 = 4|13 (7.0/3.0)
difficulty = 1 AND Q11 = 3 AND Q8 = 3 AND Q1 = 3 AND Q12 = 3|13 (20.0/11.0)
difficulty = 1 AND nb.repeat = 1 AND attendance = 3 AND Q26 = 4|9 (5.0/2.0)
difficulty = 1 AND nb.repeat = 1 AND attendance = 0 AND Q11 = 3 AND Q5 = 3 AND Q3 = 3 AND Q22 = 3|9 (6.0/3.0)
difficulty = 1 AND attendance = 1|3 (3.0/1.0)
difficulty = 1 AND Q11 = 3 AND Q5 = 3|3 (6.0/3.0)
difficulty = 1 AND Q11 = 3|5 (7.0/3.0)
difficulty = 1 AND Q5 = 2 AND Q18 = 3|3 (3.0)
difficulty = 1 AND Q5 = 3 AND Q7 = 4 AND Q26 = 4|9 (3.0)
difficulty = 1 AND Q5 = 3 AND Q2 = 2|8 (3.0/1.0)
difficulty = 1 AND Q5 = 4 AND Q11 = 4 AND Q9 = 4 AND Q18 = 4 AND Q13 = 4|3 (103.0/65.0)
difficulty = 1 AND Q5 = 4 AND Q3 = 4 AND Q15 = 4 AND Q6 = 4|4 (5.0/1.0)
difficulty = 1 AND Q13 = 2|3 (3.0/1.0)
difficulty = 1 AND Q20 = 3 AND Q14 = 3|5 (3.0)
difficulty = 1 AND Q20 = 4 AND Q5 = 4|5 (3.0)
difficulty = 1 AND Q17 = 3|3 (2.0)
difficulty = 1 AND Q20 = 4|13 (2.0)
difficulty = 5 AND Q22 = 2 AND Q5 = 2 AND Q8 = 2|3 (20.0/9.0)
difficulty = 4 AND attendance = 2 AND Q1 = 4 AND Q8 = 4 AND Q23 = 4|5 (19.0/10.0)
difficulty = 4 AND attendance = 2 AND Q11 = 1 AND Q2 = 1|3 (8.0/3.0)
difficulty = 4 AND attendance = 2 AND Q11 = 2 AND Q1 = 2|3 (12.0/6.0)
difficulty = 4 AND attendance = 2 AND Q11 = 1|5 (11.0/4.0)
difficulty = 5 AND Q21 = 2 AND Q12 = 2|5 (5.0)
difficulty = 1|9 (2.0)
difficulty = 4 AND attendance = 4 AND Q4 = 4 AND Q15 = 2|5 (2.0/1.0)
difficulty = 4 AND attendance = 4 AND Q4 = 4 AND Q10 = 4 AND Q15 = 4 AND Q16 = 4|3 (16.0/8.0)
attendance = 4 AND Q4 = 1 AND Q22 = 4|8 (7.0)
difficulty = 4 AND attendance = 4 AND Q27 = 4|8 (13.0/4.0)
difficulty = 4 AND Q21 = 2 AND Q8 = 4|3 (5.0/2.0)
difficulty = 4 AND Q21 = 2 AND Q8 = 1|4 (3.0/1.0)
difficulty = 4 AND Q21 = 2 AND Q23 = 2 AND Q27 = 2 AND attendance = 3|3 (10.0/4.0)
difficulty = 4 AND attendance = 1 AND Q2 = 5 AND Q1 = 5|3 (8.0/3.0)
difficulty = 4 AND Q21 = 2 AND Q28 = 3 AND Q15 = 4|9 (3.0)
difficulty = 4 AND Q21 = 2 AND Q17 = 2|13 (21.0/11.0)
difficulty = 4 AND Q21 = 2 AND Q11 = 2|3 (7.0/1.0)
difficulty = 4 AND Q21 = 2|5 (6.0/2.0)
difficulty = 4 AND Q21 = 5 AND Q23 = 4 AND Q13 = 3|8 (3.0)
difficulty = 4 AND Q1 = 4 AND Q2 = 5 AND Q11 = 4|5 (6.0/1.0)
difficulty = 4 AND Q11 = 5 AND Q22 = 5 AND Q26 = 5 AND nb.repeat = 1 AND Q9 = 5|5 (47.0/33.0)
difficulty = 4 AND Q11 = 5 AND Q22 = 4|8 (7.0/2.0)
difficulty = 4 AND Q11 = 5 AND Q26 = 5 AND Q13 = 5|9 (5.0/1.0)
difficulty = 4 AND Q11 = 5 AND Q22 = 5 AND Q26 = 4|5 (6.0/2.0)
difficulty = 5 AND Q21 = 2|13 (6.0/3.0)
difficulty = 5 AND Q2 = 1 AND Q11 = 1|3 (4.0/1.0)
difficulty = 5 AND Q2 = 1 AND Q27 = 3|8 (4.0)
difficulty = 4 AND Q11 = 5 AND Q22 = 5|8 (5.0/1.0)
difficulty = 4 AND Q14 = 2 AND Q11 = 1|3 (5.0/2.0)
difficulty = 2 AND Q23 = 1 AND Q9 = 1|9 (2.0)
difficulty = 2 AND Q23 = 5 AND Q19 = 5 AND attendance = 1|13 (7.0)
difficulty = 4 AND Q14 = 2 AND Q11 = 4|8 (5.0)
difficulty = 4 AND Q13 = 5 AND Q15 = 5|5 (19.0/10.0)
difficulty = 4 AND Q13 = 5 AND Q8 = 4|3 (3.0)
difficulty = 5 AND Q22 = 1 AND Q1 = 2 AND Q4 = 1|13 (3.0)
difficulty = 5 AND Q22 = 4 AND Q18 = 4 AND Q13 = 4 AND Q4 = 4 AND Q6 = 4 AND nb.repeat = 1 AND attendance = 4|3 (8.0/4.0)
difficulty = 5 AND Q22 = 1|5 (6.0/3.0)
difficulty = 5 AND Q22 = 4 AND Q18 = 4 AND Q6 = 4 AND Q1 = 4 AND attendance = 2|5 (5.0/2.0)
difficulty = 5 AND Q22 = 4 AND Q18 = 4 AND Q4 = 4 AND Q1 = 4 AND attendance = 0|13 (5.0/2.0)
difficulty = 5 AND Q22 = 4 AND Q7 = 2 AND attendance = 3|8 (3.0)
difficulty = 5 AND Q2 = 4 AND Q4 = 4|3 (12.0/5.0)
difficulty = 5 AND Q22 = 4 AND Q17 = 4|5 (8.0/3.0)
difficulty = 4 AND Q13 = 1 AND Q9 = 1 AND attendance = 3 AND Q8 = 1|3 (10.0/7.0)
difficulty = 4 AND Q13 = 1 AND Q24 = 1 AND Q9 = 1 AND attendance = 0|5 (5.0/3.0)
difficulty = 4 AND Q13 = 1 AND Q9 = 1 AND Q26 = 1 AND attendance = 1|3 (5.0/1.0)
difficulty = 4 AND Q14 = 2 AND Q22 = 3 AND Q1 = 1|9 (2.0)
difficulty = 4 AND Q13 = 1 AND attendance = 3 AND Q1 = 1|3 (3.0/1.0)
difficulty = 4 AND Q13 = 1 AND Q1 = 1|9 (5.0/2.0)
difficulty = 4 AND Q14 = 2 AND Q1 = 3|8 (3.0/1.0)
difficulty = 4 AND Q14 = 5 AND Q13 = 4|5 (4.0/2.0)
difficulty = 4 AND Q14 = 1 AND Q1 = 2|5 (4.0/1.0)
difficulty = 4 AND Q14 = 4 AND Q11 = 1|5 (10.0/5.0)
difficulty = 4 AND Q14 = 4 AND Q11 = 2 AND Q28 = 3|4 (4.0/1.0)
difficulty = 4 AND Q14 = 4 AND Q21 = 3 AND Q3 = 3|3 (10.0/3.0)
difficulty = 4 AND Q14 = 2|9 (3.0)
difficulty = 4 AND Q14 = 4 AND Q2 = 1 AND nb.repeat = 1|8 (3.0)
difficulty = 4 AND Q14 = 4 AND Q11 = 2 AND Q28 = 5 AND Q3 = 4|5 (4.0)
difficulty = 4 AND Q16 = 5 AND attendance = 2|9 (2.0)
difficulty = 4 AND Q16 = 1 AND Q9 = 1|9 (3.0/1.0)
difficulty = 4 AND Q16 = 1 AND Q9 = 3|4 (2.0/1.0)
difficulty = 4 AND Q16 = 2 AND Q23 = 2|8 (4.0/1.0)
difficulty = 4 AND Q16 = 1|13 (2.0)
difficulty = 4 AND Q1 = 1 AND Q28 = 5|4 (6.0/2.0)
difficulty = 4 AND Q1 = 1 AND Q2 = 1|9 (3.0/1.0)
difficulty = 4 AND Q1 = 1 AND Q2 = 2|9 (3.0/1.0)
difficulty = 4 AND Q1 = 4 AND Q2 = 4 AND Q25 = 4 AND Q17 = 4 AND Q13 = 4|5 (52.0/35.0)
difficulty = 4 AND Q1 = 4 AND Q2 = 4 AND Q13 = 4|5 (7.0/2.0)
difficulty = 4 AND Q1 = 1|5 (4.0)
difficulty = 4 AND Q3 = 2 AND Q24 = 3 AND Q15 = 3|3 (10.0/5.0)
difficulty = 4 AND Q3 = 2 AND Q15 = 4|5 (5.0/1.0)
difficulty = 5 AND attendance = 2 AND Q15 = 4|4 (4.0/1.0)
Q17 = 1 AND Q21 = 1|13 (32.0/18.0)
Q17 = 2 AND Q16 = 1|9 (6.0/3.0)
Q17 = 1|4 (4.0/2.0)
Q21 = 1 AND Q6 = 2|9 (5.0/2.0)
Q21 = 1 AND Q15 = 1 AND Q22 = 1|4 (3.0/1.0)
Q21 = 1|5 (12.0/6.0)
Q14 = 1 AND Q7 = 2|8 (3.0)
difficulty = 4 AND Q3 = 1|3 (5.0/3.0)
Q22 = 2 AND attendance = 2|3 (13.0/5.0)
Q22 = 5 AND Q7 = 1 AND Q9 = 3|13 (3.0/1.0)
Q5 = 1 AND Q2 = 3|8 (7.0/2.0)
Q5 = 1 AND Q3 = 4|9 (7.0/2.0)
difficulty = 5 AND attendance = 3 AND Q17 = 3|3 (6.0/3.0)
Q3 = 1 AND Q12 = 1|4 (6.0/1.0)
difficulty = 5 AND attendance = 2|8 (3.0)
Q14 = 2 AND Q15 = 3 AND Q22 = 3|13 (5.0/2.0)
Q14 = 2 AND Q16 = 2 AND Q6 = 2 AND Q1 = 2|3 (20.0/11.0)
Q14 = 2 AND Q24 = 1|9 (5.0/1.0)
Q14 = 1|13 (3.0/1.0)
Q23 = 1|13 (5.0/2.0)
Q1 = 5 AND Q10 = 4|3 (6.0/2.0)
Q21 = 5 AND Q14 = 3 AND Q6 = 3 AND Q1 = 3|9 (5.0/1.0)
Q14 = 2 AND Q13 = 3 AND Q3 = 3|3 (3.0/1.0)
Q14 = 2 AND Q7 = 3|9 (11.0/4.0)
Q21 = 2 AND Q3 = 2 AND Q6 = 2|5 (8.0/3.0)
Q6 = 1 AND Q12 = 3|13 (5.0/1.0)
Q1 = 1 AND Q11 = 1 AND Q4 = 1|13 (3.0/1.0)
Q1 = 1 AND Q11 = 4 AND Q23 = 3|8 (10.0/4.0)
Q23 = 2 AND attendance = 3|4 (15.0/6.0)
difficulty = 2 AND Q5 = 2 AND Q1 = 1 AND Q25 = 3|4 (3.0/1.0)
difficulty = 2 AND Q5 = 2 AND Q10 = 3 AND Q1 = 2|9 (3.0)
difficulty = 2 AND Q5 = 5 AND Q27 = 5 AND nb.repeat = 1|3 (12.0/7.0)
difficulty = 2 AND attendance = 4|8 (11.0/4.0)
difficulty = 2 AND Q8 = 5|13 (7.0/4.0)
difficulty = 2 AND Q25 = 3 AND Q28 = 3 AND Q2 = 3 AND nb.repeat = 1|13 (21.0/8.0)
difficulty = 2 AND Q12 = 2 AND Q22 = 4|8 (3.0/1.0)
difficulty = 2 AND Q12 = 2|13 (4.0/1.0)
Q12 = 1 AND Q6 = 4|5 (8.0/2.0)
Q25 = 2 AND Q3 = 3 AND Q22 = 2|9 (3.0)
Q12 = 1 AND Q28 = 3 AND Q5 = 3|5 (3.0/1.0)
Q12 = 1 AND Q28 = 4|8 (8.0/4.0)
Q12 = 1 AND Q28 = 5|8 (3.0)
Q12 = 1|9 (4.0/1.0)
difficulty = 2 AND Q16 = 4 AND Q18 = 4 AND Q10 = 4|13 (24.0/15.0)
difficulty = 2 AND Q17 = 5 AND Q23 = 4|3 (3.0/1.0)
difficulty = 2 AND Q16 = 3 AND Q23 = 3 AND attendance = 1|9 (10.0/5.0)
Q14 = 5 AND Q7 = 3 AND Q11 = 5|8 (8.0/1.0)
Q14 = 5 AND Q4 = 3|3 (7.0/2.0)
Q14 = 2|5 (5.0/2.0)
difficulty = 2 AND nb.repeat = 2 AND attendance = 2|3 (3.0/1.0)
difficulty = 2 AND Q27 = 4|9 (8.0/2.0)
Q14 = 5 AND attendance = 0 AND Q2 = 5|8 (5.0/3.0)
Q14 = 5 AND attendance = 3|13 (20.0/11.0)
Q14 = 5 AND Q11 = 4 AND Q13 = 5|9 (3.0)
Q1 = 1 AND Q18 = 3|8 (6.0/2.0)
Q1 = 1 AND Q14 = 3|3 (7.0/3.0)
Q1 = 1 AND Q9 = 3|8 (5.0/2.0)
Q1 = 1 AND Q12 = 2|5 (4.0/1.0)
Q1 = 3 AND Q20 = 5|8 (12.0/2.0)
nb.repeat = 2 AND attendance = 2|8 (10.0/6.0)
Q1 = 3 AND Q12 = 4 AND Q20 = 4 AND Q4 = 4|9 (7.0/1.0)
Q1 = 3 AND Q8 = 4 AND Q14 = 3|3 (4.0/1.0)
Q1 = 1|3 (3.0/2.0)
Q1 = 3 AND Q9 = 1|5 (2.0)
Q1 = 3 AND Q8 = 4 AND Q27 = 4|8 (5.0/2.0)
Q1 = 3 AND Q8 = 2 AND Q16 = 3 AND Q23 = 4|8 (4.0)
nb.repeat = 3 AND Q14 = 4|8 (6.0/4.0)
nb.repeat = 2 AND attendance = 3 AND difficulty = 4 AND Q13 = 3 AND Q1 = 3|9 (5.0/2.0)
nb.repeat = 2 AND attendance = 3 AND Q4 = 4|13 (8.0/5.0)
Q1 = 3 AND Q8 = 4|3 (4.0/1.0)
Q1 = 3 AND Q8 = 2 AND Q16 = 2|5 (3.0)
Q1 = 3 AND Q8 = 2 AND Q9 = 2|9 (3.0/1.0)
Q1 = 3 AND Q8 = 3 AND nb.repeat = 2 AND Q15 = 3 AND Q12 = 3 AND attendance = 1|13 (10.0/5.0)
Q1 = 3 AND Q8 = 3 AND Q12 = 4 AND Q20 = 3|9 (4.0)
Q1 = 3 AND Q8 = 3 AND nb.repeat = 2 AND Q22 = 3 AND difficulty = 3|8 (6.0/3.0)
Q1 = 3 AND Q8 = 3 AND Q17 = 3 AND Q4 = 3 AND Q6 = 3 AND nb.repeat = 1 AND attendance = 2|3 (56.0/30.0)
Q1 = 3 AND Q8 = 3 AND Q16 = 4 AND Q9 = 3 AND attendance = 1 AND difficulty = 4|3 (4.0/1.0)
Q1 = 4 AND Q3 = 3 AND Q28 = 4 AND Q6 = 4|5 (4.0/1.0)
Q1 = 4 AND Q3 = 3 AND Q2 = 3|8 (5.0/2.0)
Q1 = 4 AND Q3 = 3 AND Q6 = 3|3 (4.0/1.0)
Q1 = 3 AND Q8 = 3 AND Q16 = 3 AND Q20 = 3 AND Q13 = 3 AND nb.repeat = 1 AND Q6 = 3 AND Q3 = 3 AND attendance = 1|5 (42.0/27.0)
Q1 = 4 AND Q3 = 4 AND Q2 = 3 AND Q8 = 3|8 (3.0)
Q1 = 4 AND Q3 = 2|4 (2.0/1.0)
Q1 = 4 AND Q5 = 4 AND Q19 = 4 AND Q11 = 4 AND Q12 = 4 AND nb.repeat = 1|3 (100.0/64.0)
Q1 = 4 AND Q22 = 3 AND Q8 = 4|5 (4.0/1.0)
Q1 = 4 AND Q22 = 2|3 (2.0)
Q1 = 4 AND Q8 = 5|13 (5.0/2.0)
Q1 = 4 AND Q5 = 4 AND Q19 = 3|5 (5.0/1.0)
Q1 = 4 AND Q17 = 4 AND Q4 = 3|8 (3.0/2.0)
Q1 = 4 AND Q20 = 3|8 (4.0)
Q1 = 4 AND Q11 = 3|3 (2.0/1.0)
Q1 = 4 AND Q5 = 3 AND Q7 = 2|9 (2.0/1.0)
Q1 = 4 AND Q5 = 4 AND Q12 = 3|9 (7.0/3.0)
Q1 = 4 AND Q5 = 4|8 (5.0/2.0)
Q1 = 2 AND Q27 = 5 AND Q21 = 5|8 (5.0/1.0)
Q1 = 3 AND Q8 = 3 AND Q16 = 3 AND Q20 = 3 AND Q13 = 3 AND nb.repeat = 1 AND Q6 = 3 AND Q3 = 3 AND attendance = 3 AND difficulty = 4|3 (22.0/15.0)
Q1 = 3 AND Q8 = 3 AND Q16 = 3 AND Q20 = 3 AND Q13 = 3 AND Q6 = 3 AND nb.repeat = 1 AND Q3 = 3|13 (57.0/40.0)
attendance = 0 AND Q6 = 4 AND Q23 = 3|8 (3.0)
attendance = 0 AND Q6 = 3 AND Q20 = 4|8 (5.0/2.0)
attendance = 4 AND Q1 = 2|8 (17.0/6.0)
attendance = 4 AND Q4 = 5|13 (13.0/8.0)
Q14 = 5 AND attendance = 1|5 (8.0/5.0)
Q14 = 5|13 (7.0/3.0)
Q4 = 5 AND Q2 = 5|5 (4.0)
Q12 = 5|8 (4.0/2.0)
Q11 = 2 AND Q5 = 3 AND Q1 = 2|5 (4.0)
Q11 = 2|3 (11.0/6.0)
Q12 = 2 AND Q10 = 3|8 (10.0/3.0)
Q3 = 5 AND Q4 = 3|5 (4.0/1.0)
Q11 = 4 AND Q1 = 2 AND Q12 = 3 AND Q27 = 3|9 (5.0/1.0)
Q11 = 4 AND Q17 = 4 AND Q2 = 4|3 (6.0/2.0)
Q11 = 5|9 (4.0)
Q20 = 2 AND Q27 = 3|9 (3.0/1.0)
Q20 = 3 AND Q9 = 3 AND Q15 = 3 AND Q21 = 3 AND Q4 = 3 AND Q2 = 3 AND attendance = 3|4 (9.0/5.0)
Q20 = 3 AND Q9 = 3 AND Q15 = 3 AND Q21 = 3 AND Q4 = 3 AND Q8 = 3 AND Q2 = 3|3 (8.0/4.0)
Q20 = 3 AND Q9 = 2|5 (4.0)
Q14 = 3 AND Q17 = 4 AND Q3 = 4|3 (3.0)
Q14 = 3 AND Q24 = 4 AND Q3 = 2|4 (2.0)
Q14 = 3 AND Q24 = 3 AND Q10 = 3 AND Q5 = 3 AND Q4 = 3|4 (3.0)
Q20 = 3 AND Q8 = 3 AND Q26 = 3|9 (9.0/4.0)
Q20 = 3 AND Q1 = 3|5 (3.0/1.0)
Q20 = 3 AND Q7 = 2|4 (2.0)
Q20 = 4 AND Q16 = 3 AND Q6 = 4|8 (4.0/1.0)
Q20 = 3|3 (2.0/1.0)
Q16 = 2|4 (2.0/1.0)
Q16 = 3 AND difficulty = 3|13 (2.0)
Q16 = 3 AND Q21 = 3|3 (2.0)
Q16 = 4 AND Q17 = 4 AND Q10 = 3 AND Q1 = 3|5 (8.0/4.0)
Q1 = 2 AND Q6 = 4|9 (10.0/4.0)
Q2 = 3 AND Q1 = 3|3 (5.0/1.0)
Q12 = 3 AND difficulty = 4|4 (3.0)
Q12 = 3|8 (2.0/1.0)
|13 (3.0/1.0)


## J48 Decision Tree

* instr = 1
	* difficulty = 4
		* nb.repeat = 3: 7 (11.0/1.0)
		* nb.repeat != 3
			* Q18 = 2: 10 (9.0/4.0)
			* Q18 != 2
				* Q4 = 2: 7 (14.0)
				* Q4 != 2
					* Q5 = 2: 7 (4.0)
					* Q5 != 2
						* Q16 = 2: 7 (5.0/1.0)
						* Q16 != 2
							* Q10 = 2: 7 (3.0/1.0)
							* Q10 != 2
								* Q12 = 2: 10 (4.0/1.0)
								* Q12 != 2
									* Q24 = 3
										* attendance = 1: 7 (3.0/1.0)
										* attendance != 1: 10 (18.0/7.0)
									* Q24 != 3
										* Q22 = 3: 7 (2.0)
										* Q22 != 3
											* Q1 = 3: 7 (8.0/2.0)
											* Q1 != 3
												* Q4 = 3: 7 (2.0/1.0)
												* Q4 != 3
													* Q1 = 2: 7 (3.0/1.0)
													* Q1 != 2
														* Q1 = 4: 10 (30.0/18.0)
														* Q1 != 4: 2 (27.0/12.0)
	* difficulty != 4
		* difficulty = 5
			* attendance = 4: 10 (21.0/9.0)
			* attendance != 4
				* Q11 = 4
					* attendance = 1: 2 (4.0/1.0)
					* attendance != 1: 10 (6.0/2.0)
				* Q11 != 4: 7 (49.0/18.0)
		* difficulty != 5
			* Q16 = 1
				* Q11 = 3: 7 (3.0)
				* Q11 != 3
					* nb.repeat = 1
						* Q3 = 1
							* Q4 = 1
								* difficulty = 2: 10 (4.0/1.0)
								* difficulty != 2
									* Q1 = 1
										* Q23 = 1
											* difficulty = 1: 10 (29.0/14.0)
											* difficulty != 1
												* attendance = 2: 7 (2.0)
												* attendance != 2: 10 (9.0/3.0)
										* Q23 != 1: 2 (2.0/1.0)
									* Q1 != 1: 2 (2.0/1.0)
							* Q4 != 1: 10 (2.0)
						* Q3 != 1: 10 (4.0)
					* nb.repeat != 1: 2 (3.0/1.0)
			* Q16 != 1: 10 (334.0/78.0)
* instr != 1
	* instr = 2
		* difficulty = 4
			* Q15 = 1: 6 (11.0/3.0)
			* Q15 != 1
				* Q6 = 2: 11 (19.0/2.0)
				* Q6 != 2
					* Q8 = 2: 11 (11.0/6.0)
					* Q8 != 2
						* Q6 = 1: 11 (7.0)
						* Q6 != 1
							* Q15 = 2: 6 (4.0)
							* Q15 != 2
								* Q11 = 2: 6 (3.0/2.0)
								* Q11 != 2
									* Q3 = 2: 6 (3.0/1.0)
									* Q3 != 2
										* attendance = 0
											* Q13 = 5: 1 (2.0/1.0)
											* Q13 != 5: 11 (9.0)
										* attendance != 0: 11 (122.0/57.0)
		* difficulty != 4
			* difficulty = 5
				* Q3 = 2: 11 (4.0)
				* Q3 != 2
					* nb.repeat = 2: 6 (4.0/1.0)
					* nb.repeat != 2: 11 (57.0/28.0)
			* difficulty != 5
				* difficulty = 1: 6 (282.0/184.0)
				* difficulty != 1
					* Q14 = 2: 6 (41.0/19.0)
					* Q14 != 2
						* Q22 = 2: 1 (9.0/4.0)
						* Q22 != 2
							* Q17 = 2: 1 (5.0/2.0)
							* Q17 != 2
								* Q28 = 2: 6 (10.0/4.0)
								* Q28 != 2
									* Q16 = 2: 11 (11.0/4.0)
									* Q16 != 2
										* Q18 = 2: 11 (5.0/2.0)
										* Q18 != 2
											* Q23 = 2: 6 (7.0/2.0)
											* Q23 != 2
												* Q20 = 2: 11 (4.0/1.0)
												* Q20 != 2
													* Q24 = 2: 1 (16.0/10.0)
													* Q24 != 2
														* Q10 = 2: 11 (9.0/4.0)
														* Q10 != 2
															* Q9 = 2: 1 (9.0/5.0)
															* Q9 != 2
																* Q11 = 2: 6 (2.0)
																* Q11 != 2
																	* Q27 = 2: 6 (11.0/5.0)
																	* Q27 != 2
																		* Q12 = 2: 11 (16.0/8.0)
																		* Q12 != 2
																			* Q5 = 2: 1 (8.0/4.0)
																			* Q5 != 2
																				* Q6 = 2: 11 (12.0/4.0)
																				* Q6 != 2
																					* Q3 = 2: 6 (2.0)
																					* Q3 != 2
																						* Q7 = 2: 6 (4.0/2.0)
																						* Q7 != 2
																							* Q8 = 2: 11 (10.0/6.0)
																							* Q8 != 2
																								* Q12 = 1
																									* Q9 = 4: 13 (2.0)
																									* Q9 != 4
																										* Q1 = 5: 11 (3.0)
																										* Q1 != 5
																											* Q19 = 4: 11 (2.0)
																											* Q19 != 4
																												* Q11 = 1
																													* Q2 = 3: 11 (2.0)
																													* Q2 != 3
																														* Q1 = 1
																															* attendance = 3: 6 (4.0/2.0)
																															* attendance != 3
																																* nb.repeat = 1
																																	* difficulty = 2: 6 (3.0)
																																	* difficulty != 2: 1 (8.0/4.0)
																																* nb.repeat != 1: 6 (4.0/2.0)
																														* Q1 != 1: 6 (2.0/1.0)
																												* Q11 != 1: 6 (2.0/1.0)
																								* Q12 != 1
																									* Q7 = 1: 6 (2.0)
																									* Q7 != 1
																										* Q4 = 1: 1 (3.0/1.0)
																										* Q4 != 1
																											* Q27 = 1: 6 (3.0/2.0)
																											* Q27 != 1
																												* attendance = 0: 6 (47.0/20.0)
																												* attendance != 0
																													* Q1 = 1: 1 (8.0/5.0)
																													* Q1 != 1
																														* Q2 = 2: 1 (6.0/3.0)
																														* Q2 != 2
																															* Q1 = 2: 6 (19.0/9.0)
																															* Q1 != 2
																																* difficulty = 2
																																	* Q2 = 4
																																		* Q17 = 5: 1 (3.0)
																																		* Q17 != 5: 6 (26.0/10.0)
																																	* Q2 != 4: 6 (35.0/19.0)
																																* difficulty != 2
																																	* nb.repeat = 2
																																		* attendance = 2: 11 (5.0/2.0)
																																		* attendance != 2
																																			* attendance = 3: 11 (2.0/1.0)
																																			* attendance != 3: 6 (14.0/5.0)
																																	* nb.repeat != 2
																																		* Q16 = 4: 6 (97.0/54.0)
																																		* Q16 != 4
																																			* Q13 = 4: 11 (6.0/3.0)
																																			* Q13 != 4
																																				* Q12 = 4
																																					* attendance = 2: 6 (3.0/1.0)
																																					* attendance != 2: 1 (2.0/1.0)
																																				* Q12 != 4
																																					* Q10 = 4: 6 (4.0)
																																					* Q10 != 4
																																						* Q6 = 4: 1 (2.0)
																																						* Q6 != 4
																																							* nb.repeat = 1
																																								* Q19 = 4: 11 (3.0/1.0)
																																								* Q19 != 4
																																									* attendance = 2
																																										* Q1 = 3: 11 (13.0/7.0)
																																										* Q1 != 3: 6 (6.0/1.0)
																																									* attendance != 2
																																										* Q2 = 3: 6 (35.0/16.0)
																																										* Q2 != 3
																																											* Q14 = 5
																																												* attendance = 4
																																													* Q1 = 5: 1 (16.0/9.0)
																																													* Q1 != 5: 6 (3.0/1.0)
																																												* attendance != 4: 6 (24.0/13.0)
																																											* Q14 != 5: 11 (3.0/1.0)
																																							* nb.repeat != 1: 1 (2.0/1.0)
	* instr != 2
		* difficulty = 2: 13 (229.0/143.0)
		* difficulty != 2
			* nb.repeat = 1
				* Q17 = 1: 13 (333.0/222.0)
				* Q17 != 1
					* Q4 = 1
						* Q3 = 5: 8 (4.0)
						* Q3 != 5
							* Q5 = 4: 5 (6.0/2.0)
							* Q5 != 4
								* Q6 = 4
									* Q20 = 4: 9 (4.0/1.0)
									* Q20 != 4: 8 (4.0/1.0)
								* Q6 != 4
									* Q22 = 2
										* Q17 = 4: 4 (8.0/3.0)
										* Q17 != 4: 13 (14.0/8.0)
									* Q22 != 2
										* Q10 = 4: 5 (4.0/2.0)
										* Q10 != 4
											* Q7 = 3: 9 (13.0/8.0)
											* Q7 != 3
												* Q17 = 2: 3 (3.0/1.0)
												* Q17 != 2: 8 (76.0/50.0)
					* Q4 != 1
						* Q5 = 1: 8 (37.0/25.0)
						* Q5 != 1
							* Q11 = 1: 5 (65.0/35.0)
							* Q11 != 1
								* attendance = 4
									* Q2 = 1: 5 (3.0)
									* Q2 != 1
										* Q23 = 1: 8 (3.0/1.0)
										* Q23 != 1
											* Q27 = 1: 5 (6.0/2.0)
											* Q27 != 1
												* Q1 = 1
													* Q19 = 5: 13 (2.0)
													* Q19 != 5
														* Q3 = 3: 9 (2.0/1.0)
														* Q3 != 3: 3 (6.0/3.0)
												* Q1 != 1
													* Q14 = 2: 5 (18.0/9.0)
													* Q14 != 2
														* Q15 = 2: 4 (3.0/2.0)
														* Q15 != 2
															* Q6 = 2: 8 (7.0/1.0)
															* Q6 != 2
																* Q1 = 2: 8 (22.0/8.0)
																* Q1 != 2
																	* Q16 = 2: 8 (2.0)
																	* Q16 != 2: 3 (151.0/102.0)
								* attendance != 4
									* Q26 = 1: 9 (10.0/5.0)
									* Q26 != 1
										* Q6 = 1: 13 (13.0/8.0)
										* Q6 != 1
											* Q25 = 5
												* Q27 = 1: 8 (5.0/1.0)
												* Q27 != 1
													* Q5 = 2: 8 (4.0/1.0)
													* Q5 != 2
														* Q18 = 1: 8 (2.0)
														* Q18 != 1
															* Q13 = 1: 9 (2.0)
															* Q13 != 1
																* Q16 = 2: 8 (3.0/1.0)
																* Q16 != 2
																	* Q2 = 1: 13 (4.0/1.0)
																	* Q2 != 1
																		* Q27 = 2: 3 (8.0/2.0)
																		* Q27 != 2
																			* Q14 = 3: 8 (3.0/1.0)
																			* Q14 != 3
																				* Q13 = 3: 3 (3.0/2.0)
																				* Q13 != 3
																					* Q27 = 3: 5 (9.0/3.0)
																					* Q27 != 3
																						* attendance = 1: 5 (23.0/16.0)
																						* attendance != 1
																							* Q2 = 3: 5 (7.0/3.0)
																							* Q2 != 3
																								* Q7 = 2: 8 (2.0)
																								* Q7 != 2
																									* Q16 = 3: 8 (3.0/1.0)
																									* Q16 != 3
																										* Q18 = 3: 3 (3.0)
																										* Q18 != 3
																											* Q8 = 2: 8 (3.0/1.0)
																											* Q8 != 2
																												* Q11 = 2: 5 (3.0)
																												* Q11 != 2
																													* Q11 = 3: 13 (4.0/1.0)
																													* Q11 != 3
																														* Q4 = 2: 3 (2.0)
																														* Q4 != 2
																															* Q24 = 3: 8 (2.0/1.0)
																															* Q24 != 3
																																* Q1 = 2: 3 (2.0/1.0)
																																* Q1 != 2
																																	* Q15 = 5
																																		* Q13 = 4: 13 (2.0)
																																		* Q13 != 4
																																			* Q9 = 3: 8 (3.0/1.0)
																																			* Q9 != 3
																																				* Q9 = 4: 13 (9.0/3.0)
																																				* Q9 != 4
																																					* Q4 = 4: 8 (2.0/1.0)
																																					* Q4 != 4
																																						* Q3 = 3: 8 (2.0/1.0)
																																						* Q3 != 3
																																							* Q1 = 4: 5 (2.0)
																																							* Q1 != 4
																																								* Q24 = 5
																																									* difficulty = 5
																																										* attendance = 3: 5 (6.0/1.0)
																																										* attendance != 3: 3 (8.0/4.0)
																																									* difficulty != 5
																																										* Q7 = 4: 3 (2.0/1.0)
																																										* Q7 != 4
																																											* attendance = 2: 3 (16.0/11.0)
																																											* attendance != 2: 5 (112.0/81.0)
																																								* Q24 != 5: 9 (2.0)
																																	* Q15 != 5: 5 (7.0/2.0)
											* Q25 != 5
												* Q13 = 1: 4 (5.0/3.0)
												* Q13 != 1
													* Q28 = 1: 5 (4.0/1.0)
													* Q28 != 1
														* Q19 = 1: 3 (6.0/3.0)
														* Q19 != 1
															* Q8 = 1: 5 (9.0/5.0)
															* Q8 != 1
																* Q18 = 1: 9 (16.0/8.0)
																* Q18 != 1
																	* Q24 = 5: 5 (16.0/9.0)
																	* Q24 != 5
																		* Q21 = 5
																			* difficulty = 1: 3 (3.0/1.0)
																			* difficulty != 1: 8 (11.0/4.0)
																		* Q21 != 5
																			* Q23 = 1: 5 (3.0/1.0)
																			* Q23 != 1
																				* Q22 = 5: 5 (7.0/3.0)
																				* Q22 != 5
																					* Q12 = 1
																						* Q9 = 4: 4 (2.0/1.0)
																						* Q9 != 4
																							* Q20 = 3: 3 (3.0/1.0)
																							* Q20 != 3: 5 (8.0/4.0)
																					* Q12 != 1
																						* Q3 = 1
																							* Q13 = 4: 3 (2.0/1.0)
																							* Q13 != 4
																								* attendance = 3: 13 (2.0)
																								* attendance != 3: 3 (2.0/1.0)
																						* Q3 != 1
																							* Q2 = 1: 8 (7.0/4.0)
																							* Q2 != 1
																								* Q17 = 5: 3 (16.0/11.0)
																								* Q17 != 5
																									* Q10 = 5: 13 (13.0/8.0)
																									* Q10 != 5
																										* Q11 = 5: 8 (9.0/5.0)
																										* Q11 != 5
																											* Q7 = 5: 3 (5.0/3.0)
																											* Q7 != 5
																												* Q5 = 5: 9 (5.0/2.0)
																												* Q5 != 5
																													* Q9 = 1: 8 (4.0/2.0)
																													* Q9 != 1
																														* Q16 = 5: 5 (6.0/2.0)
																														* Q16 != 5
																															* difficulty = 3
																																* Q1 = 1: 3 (5.0/3.0)
																																* Q1 != 1
																																	* Q20 = 5: 13 (2.0)
																																	* Q20 != 5
																																		* Q16 = 2
																																			* Q18 = 3: 5 (3.0/1.0)
																																			* Q18 != 3: 3 (19.0/12.0)
																																		* Q16 != 2
																																			* Q24 = 2: 8 (3.0/1.0)
																																			* Q24 != 2
																																				* Q20 = 2: 4 (2.0/1.0)
																																				* Q20 != 2
																																					* Q22 = 2: 9 (3.0/1.0)
																																					* Q22 != 2
																																						* Q18 = 2: 5 (3.0)
																																						* Q18 != 2
																																							* Q11 = 2: 5 (4.0/1.0)
																																							* Q11 != 2
																																								* Q7 = 2: 4 (8.0/6.0)
																																								* Q7 != 2
																																									* Q23 = 2: 4 (2.0/1.0)
																																									* Q23 != 2
																																										* Q8 = 2: 8 (4.0/2.0)
																																										* Q8 != 2
																																											* attendance = 2: 3 (59.0/30.0)
																																											* attendance != 2
																																												* Q1 = 5: 3 (3.0/2.0)
																																												* Q1 != 5
																																													* Q11 = 3: 13 (64.0/44.0)
																																													* Q11 != 3: 3 (62.0/44.0)
																															* difficulty != 3
																																* Q14 = 5: 4 (4.0/2.0)
																																* Q14 != 5
																																	* Q3 = 2: 3 (111.0/69.0)
																																	* Q3 != 2
																																		* Q5 = 2: 3 (27.0/19.0)
																																		* Q5 != 2
																																			* Q1 = 2
																																				* attendance = 1: 3 (4.0/3.0)
																																				* attendance != 1
																																					* Q27 = 2
																																						* Q5 = 3
																																							* Q8 = 3: 8 (2.0/1.0)
																																							* Q8 != 3: 3 (5.0)
																																						* Q5 != 3: 8 (3.0/1.0)
																																					* Q27 != 2: 9 (22.0/13.0)
																																			* Q1 != 2
																																				* Q2 = 2: 8 (8.0/5.0)
																																				* Q2 != 2
																																					* Q1 = 1
																																						* difficulty = 4: 5 (4.0/1.0)
																																						* difficulty != 4
																																							* Q2 = 3: 3 (2.0/1.0)
																																							* Q2 != 3: 13 (2.0)
																																					* Q1 != 1
																																						* Q9 = 5: 5 (2.0)
																																						* Q9 != 5
																																							* Q15 = 5: 5 (2.0)
																																							* Q15 != 5
																																								* Q6 = 2: 3 (9.0/7.0)
																																								* Q6 != 2
																																									* Q20 = 2: 3 (14.0/4.0)
																																									* Q20 != 2
																																										* Q26 = 2: 5 (5.0/2.0)
																																										* Q26 != 2
																																											* Q17 = 2: 13 (3.0/1.0)
																																											* Q17 != 2
																																												* difficulty = 1
																																													* attendance = 3
																																														* Q1 = 3: 13 (11.0/6.0)
																																														* Q1 != 3: 9 (3.0)
																																													* attendance != 3
																																														* Q19 = 3: 3 (151.0/93.0)
																																														* Q19 != 3
																																															* Q22 = 3: 5 (2.0)
																																															* Q22 != 3: 3 (95.0/63.0)
																																												* difficulty != 1
																																													* attendance = 0
																																														* Q16 = 3: 3 (14.0/8.0)
																																														* Q16 != 3
																																															* difficulty = 4: 4 (7.0/5.0)
																																															* difficulty != 4: 13 (2.0)
																																													* attendance != 0
																																														* Q11 = 2: 5 (3.0)
																																														* Q11 != 2: 3 (174.0/112.0)
			* nb.repeat != 1
				* Q11 = 1: 13 (79.0/42.0)
				* Q11 != 1
					* Q14 = 1: 5 (12.0/6.0)
					* Q14 != 1
						* Q15 = 1: 3 (2.0/1.0)
						* Q15 != 1
							* Q22 = 1: 3 (4.0/2.0)
							* Q22 != 1
								* Q19 = 1: 9 (7.0/3.0)
								* Q19 != 1
									* Q5 = 5: 13 (64.0/45.0)
									* Q5 != 5: 9 (280.0/198.0)


## SimpleCart Decision Tree

* instr=(3)
		* nb.repeat=(3)|(2)
				* Q10=(4)|(3)|(2)
			* Q12=(3)
					* difficulty=(4)|(3)
							* Q25=(4)|(3)|(2)
							* Q2=(3)|(5)
									* Q3=(3)|(2)|(5)
										* Q15=(4)|(3)|(1): 9(28.0/45.0)
										* Q15!=(4)|(3)|(1): 3(2.0/0.0)
									* Q3!=(3)|(2)|(5): 3(3.0/2.0)
							* Q2!=(3)|(5)
							* Q18=(3)
											* Q3=(4)|(3)|(1)|(5): 13(3.0/1.0)
											* Q3!=(4)|(3)|(1)|(5)
											* attendance=(3)|(2)|(4): 3(1.0/1.0)
											* attendance!=(3)|(2)|(4): 9(2.0/0.0)
							* Q18!=(3): 9(11.0/3.0)
							* Q25!=(4)|(3)|(2)
						* attendance=(1): 9(1.0/1.0)
						* attendance!=(1): 8(4.0/0.0)
					* difficulty!=(4)|(3)
					* Q15=(4): 9(3.0/1.0)
					* Q15!=(4)
						* Q11=(4): 3(2.0/0.0)
						* Q11!=(4)
							* Q25=(2): 13(3.0/0.0)
							* Q25!=(2)
								* nb.repeat=(3): 9(12.0/15.0)
								* nb.repeat!=(3)
									* attendance=(1)
										* difficulty=(2): 8(2.0/4.0)
										* difficulty!=(2)
														* difficulty=(5)|(2)|(3)|(4): 13(3.0/2.0)
														* difficulty!=(5)|(2)|(3)|(4): 13(2.0/1.0)
									* attendance!=(1)
													* Q1=(4)|(3)|(1)|(5): 3(9.0/17.0)
													* Q1!=(4)|(3)|(1)|(5): 5(1.0/1.0)
			* Q12!=(3)
							* Q15=(5)|(4)|(3)|(2)
							* Q11=(5)|(4)|(3)
							* Q1=(5)|(4)
									* difficulty=(5)|(3)|(2)
									* attendance=(3)|(2)
										* Q15=(5)|(3): 3(4.0/0.0)
										* Q15!=(5)|(3)
													* attendance=(3)|(0)|(1)|(4)
													* difficulty=(3)|(1)|(4): 13(3.0/4.0)
													* difficulty!=(3)|(1)|(4)
												* difficulty=(5): 3(1.0/2.0)
												* difficulty!=(5): 3(1.0/3.0)
													* attendance!=(3)|(0)|(1)|(4)
														* difficulty=(5)|(3)|(1)|(4)
												* nb.repeat=(3): 13(2.0/0.0)
												* nb.repeat!=(3): 13(2.0/1.0)
														* difficulty!=(5)|(3)|(1)|(4): 9(2.0/0.0)
									* attendance!=(3)|(2)
											* Q23=(5)|(4)|(1)
												* Q2=(4)|(1)|(2): 8(12.0/14.0)
												* Q2!=(4)|(1)|(2): 9(2.0/0.0)
											* Q23!=(5)|(4)|(1)
											* nb.repeat=(3)|(1): 4(1.0/1.0)
											* nb.repeat!=(3)|(1): 13(2.0/0.0)
									* difficulty!=(5)|(3)|(2)
										* Q22=(4)|(1)|(2)
												* Q13=(4)|(1)|(2)|(5)
										* nb.repeat=(3): 3(5.0/4.0)
										* nb.repeat!=(3)
													* attendance=(4)|(2)|(1): 9(3.0/7.0)
													* attendance!=(4)|(2)|(1): 5(2.0/1.0)
												* Q13!=(4)|(1)|(2)|(5): 9(2.0/0.0)
										* Q22!=(4)|(1)|(2): 3(3.0/1.0)
							* Q1!=(5)|(4)
							* Q8=(4)
								* Q4=(5): 8(2.0/0.0)
								* Q4!=(5)
										* Q26=(5)|(3): 5(4.0/1.0)
										* Q26!=(5)|(3)
												* attendance=(3)|(1)|(4)
												* nb.repeat=(3)|(1): 8(1.0/1.0)
												* nb.repeat!=(3)|(1): 4(1.0/1.0)
												* attendance!=(3)|(1)|(4): 13(3.0/1.0)
							* Q8!=(4)
									* difficulty=(5)|(4)
										* Q7=(5)|(3): 9(7.0/1.0)
										* Q7!=(5)|(3)
													* Q7=(4)|(2)|(3)|(5)
													* Q1=(2)|(4)|(5)
												* Q15=(4): 9(2.0/0.0)
												* Q15!=(4): 3(2.0/1.0)
													* Q1!=(2)|(4)|(5): 8(2.0/0.0)
													* Q7!=(4)|(2)|(3)|(5): 4(2.0/0.0)
									* difficulty!=(5)|(4)
											* Q28=(4)|(3)|(1)
											* Q21=(5)|(2): 9(4.0/1.0)
											* Q21!=(5)|(2)
													* Q5=(3)|(2)|(5)
														* Q27=(4)|(2)|(5)
															* attendance=(3)|(2)|(1): 8(6.0/0.0)
															* attendance!=(3)|(2)|(1): 3(1.0/1.0)
														* Q27!=(4)|(2)|(5)
													* attendance=(3): 3(1.0/1.0)
													* attendance!=(3)
																* difficulty=(3)|(4)|(5): 8(2.0/1.0)
																* difficulty!=(3)|(4)|(5): 9(2.0/0.0)
													* Q5!=(3)|(2)|(5)
														* Q3=(4)|(1)|(5): 9(3.0/0.0)
														* Q3!=(4)|(1)|(5): 4(2.0/0.0)
											* Q28!=(4)|(3)|(1): 8(8.0/1.0)
							* Q11!=(5)|(4)|(3)
							* difficulty=(3)|(2)
										* Q11=(2)|(3)|(4)|(5)
								* Q20=(4): 3(3.0/0.0)
								* Q20!=(4)
										* attendance=(2)|(1): 13(12.0/8.0)
										* attendance!=(2)|(1): 8(4.0/3.0)
										* Q11!=(2)|(3)|(4)|(5)
											* attendance=(2)|(1)|(3)|(4): 4(2.0/0.0)
											* attendance!=(2)|(1)|(3)|(4): 5(2.0/0.0)
							* difficulty!=(3)|(2)
							* Q16=(4): 13(4.0/0.0)
							* Q16!=(4)
									* attendance=(4)|(2)
									* difficulty=(5): 3(1.0/1.0)
									* difficulty!=(5): 8(4.0/2.0)
									* attendance!=(4)|(2)
									* Q7=(3): 8(2.0/0.0)
									* Q7!=(3)
												* Q3=(5)|(4)|(3): 3(5.0/1.0)
												* Q3!=(5)|(4)|(3)
											* Q19=(3): 3(2.0/0.0)
											* Q19!=(3)
													* Q26=(5)|(3): 13(2.0/0.0)
													* Q26!=(5)|(3): 9(11.0/12.0)
							* Q15!=(5)|(4)|(3)|(2): 5(4.0/1.0)
				* Q10!=(4)|(3)|(2)
			* difficulty=(5)
				* Q9=(2): 4(2.0/0.0)
				* Q9!=(2)
							* Q19=(5)|(3)|(2)
							* attendance=(3)|(2): 8(2.0/1.0)
							* attendance!=(3)|(2)
									* Q1=(5)|(2)|(4)
								* attendance=(1): 3(1.0/1.0)
								* attendance!=(1)
										* nb.repeat=(3)|(1)
													* attendance=(4)|(1)|(2)|(3): 13(5.0/2.0)
													* attendance!=(4)|(1)|(2)|(3): 13(2.0/0.0)
										* nb.repeat!=(3)|(1): 13(2.0/1.0)
									* Q1!=(5)|(2)|(4): 13(5.0/0.0)
							* Q19!=(5)|(3)|(2)
							* nb.repeat=(3)|(1)
							* attendance=(4): 3(1.0/3.0)
							* attendance!=(4)
								* attendance=(1): 3(1.0/1.0)
								* attendance!=(1): 13(4.0/1.0)
							* nb.repeat!=(3)|(1): 3(5.0/2.0)
			* difficulty!=(5)
					* Q5=(3)|(2): 13(8.0/1.0)
					* Q5!=(3)|(2)
					* Q11=(3): 5(3.0/1.0)
					* Q11!=(3)
							* Q28=(5)|(3)
							* attendance=(4)
									* nb.repeat=(3)|(1): 13(3.0/3.0)
									* nb.repeat!=(3)|(1): 3(3.0/0.0)
							* attendance!=(4)
											* Q21=(5)|(4)|(3)|(1): 8(18.0/34.0)
											* Q21!=(5)|(4)|(3)|(1): 9(3.0/0.0)
							* Q28!=(5)|(3)
								* Q1=(5)|(2): 13(7.0/1.0)
								* Q1!=(5)|(2)
									* Q22=(5)|(3): 9(2.0/1.0)
									* Q22!=(5)|(3)
									* attendance=(2): 13(5.0/1.0)
									* attendance!=(2)
											* difficulty=(4)|(2)
												* attendance=(4)|(3): 9(2.0/0.0)
												* attendance!=(4)|(3)
												* difficulty=(4)
													* nb.repeat=(3): 3(1.0/1.0)
													* nb.repeat!=(3)
																	* attendance=(1)|(2)|(3)|(4): 13(2.0/1.0)
																	* attendance!=(1)|(2)|(3)|(4): 3(1.0/2.0)
												* difficulty!=(4)
													* nb.repeat=(3): 9(2.0/2.0)
													* nb.repeat!=(3): 13(4.0/3.0)
											* difficulty!=(4)|(2)
												* nb.repeat=(3)|(1): 8(8.0/10.0)
												* nb.repeat!=(3)|(1)
													* attendance=(3)|(1): 8(2.0/1.0)
													* attendance!=(3)|(1): 13(4.0/4.0)
		* nb.repeat!=(3)|(2)
			* Q21=(5)|(4)
				* Q1=(5)|(4)
						* Q11=(5)|(4)|(3)
						* Q12=(3)|(2)
								* attendance=(3)|(2)|(1)
								* Q24=(5)|(3)
										* Q13=(4)|(1)|(2)
												* Q23=(5)|(4)|(1)|(2): 5(5.0/0.0)
												* Q23!=(5)|(4)|(1)|(2): 8(2.0/1.0)
										* Q13!=(4)|(1)|(2)
									* attendance=(2): 13(2.0/0.0)
									* attendance!=(2)
													* Q2=(5)|(1)|(2)|(3): 3(1.0/2.0)
													* Q2!=(5)|(1)|(2)|(3): 8(3.0/0.0)
								* Q24!=(5)|(3)
								* Q17=(5): 9(6.0/1.0)
								* Q17!=(5)
												* Q12=(3)|(1)|(4)|(5)
													* Q14=(4)|(1)|(2)|(5)
													* difficulty=(4)|(1)|(5)
															* Q6=(4)|(1)|(2)|(5): 5(2.0/0.0)
															* Q6!=(4)|(1)|(2)|(5): 5(1.0/1.0)
													* difficulty!=(4)|(1)|(5): 9(2.0/1.0)
													* Q14!=(4)|(1)|(2)|(5): 3(1.0/1.0)
												* Q12!=(3)|(1)|(4)|(5): 12(2.0/0.0)
								* attendance!=(3)|(2)|(1)
									* difficulty=(4)|(3)|(2): 8(10.0/3.0)
									* difficulty!=(4)|(3)|(2): 3(4.0/1.0)
						* Q12!=(3)|(2)
								* attendance=(4)|(3)|(2)
								* difficulty=(3)|(2)
										* Q10=(5)|(4)|(1)
									* Q24=(5)
												* Q2=(5)|(2)|(3)
														* attendance=(4)|(3)|(0)|(1): 3(8.0/20.0)
														* attendance!=(4)|(3)|(0)|(1): 13(4.0/2.0)
												* Q2!=(5)|(2)|(3): 13(5.0/1.0)
									* Q24!=(5)
												* Q6=(5)|(4)|(1)
											* Q1=(5): 5(3.0/1.0)
											* Q1!=(5)
												* attendance=(4): 5(8.0/15.0)
												* attendance!=(4): 3(25.0/41.0)
												* Q6!=(5)|(4)|(1): 3(4.0/0.0)
										* Q10!=(5)|(4)|(1): 5(4.0/0.0)
								* difficulty!=(3)|(2)
											* Q4=(5)|(4)|(1)|(2)
									* Q6=(3): 8(3.0/1.0)
									* Q6!=(3)
												* Q27=(5)|(4)|(2)
											* Q9=(3): 8(2.0/0.0)
											* Q9!=(3)
															* Q10=(5)|(4)|(1)|(2)
															* difficulty=(4)|(2)|(3): 3(32.0/71.0)
															* difficulty!=(4)|(2)|(3)
																	* Q27=(5)|(1)|(2)|(3)
																		* attendance=(4)|(3)|(0)|(1)
																			* Q10=(5)|(1)|(2)|(3): 5(13.0/18.0)
																			* Q10!=(5)|(1)|(2)|(3): 5(3.0/0.0)
																		* attendance!=(4)|(3)|(0)|(1): 3(6.0/1.0)
																	* Q27!=(5)|(1)|(2)|(3)
															* attendance=(3)
																			* difficulty=(5)|(2)|(3)|(4): 3(4.0/1.0)
																			* difficulty!=(5)|(2)|(3)|(4): 9(3.0/1.0)
															* attendance!=(3)
																		* Q6=(4)|(1)|(3): 5(6.0/8.0)
																		* Q6!=(4)|(1)|(3): 3(2.0/0.0)
															* Q10!=(5)|(4)|(1)|(2)
														* Q8=(5)|(3): 5(1.0/2.0)
														* Q8!=(5)|(3)
																	* attendance=(4)|(3)|(0)|(1): 9(3.0/0.0)
																	* attendance!=(4)|(3)|(0)|(1): 3(1.0/1.0)
												* Q27!=(5)|(4)|(2): 5(5.0/2.0)
											* Q4!=(5)|(4)|(1)|(2): 5(5.0/1.0)
								* attendance!=(4)|(3)|(2)
									* Q24=(5)|(4)|(2)
								* difficulty=(2): 13(8.0/9.0)
								* difficulty!=(2)
										* Q8=(5)|(3)
												* Q13=(5)|(4)|(2)
														* Q8=(5)|(1)|(2)|(4)
												* Q27=(3): 5(3.0/0.0)
												* Q27!=(3)
															* Q2=(5)|(4)|(3)
																* Q19=(5)|(4)|(1)
															* Q7=(4)
																			* Q10=(5)|(1)|(2)|(3): 8(2.0/0.0)
																			* Q10!=(5)|(1)|(2)|(3): 3(2.0/0.0)
															* Q7!=(4)
																		* Q2=(5)|(1)|(2)
																	* attendance=(1)
																					* difficulty=(5)|(4)|(3)|(2): 5(6.0/7.0)
																					* difficulty!=(5)|(4)|(3)|(2): 4(1.0/1.0)
																	* attendance!=(1)
																					* Q24=(5)|(1)|(2)|(3): 3(24.0/77.0)
																					* Q24!=(5)|(1)|(2)|(3): 13(4.0/2.0)
																		* Q2!=(5)|(1)|(2): 5(3.0/0.0)
																* Q19!=(5)|(4)|(1): 3(2.0/0.0)
															* Q2!=(5)|(4)|(3): 13(2.0/0.0)
														* Q8!=(5)|(1)|(2)|(4): 13(4.0/1.0)
												* Q13!=(5)|(4)|(2): 9(3.0/0.0)
										* Q8!=(5)|(3)
											* difficulty=(5)|(3)
													* Q16=(4)|(1)|(2)
															* attendance=(1)|(2)|(3)|(4): 8(7.0/10.0)
															* attendance!=(1)|(2)|(3)|(4)
															* Q6=(4)|(1)|(2)
														* difficulty=(5): 13(3.0/0.0)
														* difficulty!=(5): 13(4.0/7.0)
															* Q6!=(4)|(1)|(2): 3(1.0/1.0)
													* Q16!=(4)|(1)|(2): 9(2.0/0.0)
											* difficulty!=(5)|(3)
											* Q10=(5): 8(2.0/0.0)
											* Q10!=(5)
												* Q5=(3): 3(3.0/0.0)
												* Q5!=(3)
													* Q16=(3): 9(2.0/0.0)
													* Q16!=(3)
															* Q6=(5)|(3): 5(3.0/1.0)
															* Q6!=(5)|(3)
																	* Q16=(5)|(4)|(3)
																			* Q7=(5)|(4)|(1)|(2): 3(35.0/79.0)
																			* Q7!=(5)|(4)|(1)|(2): 3(2.0/0.0)
																	* Q16!=(5)|(4)|(3): 13(2.0/1.0)
									* Q24!=(5)|(4)|(2)
										* Q19=(5)|(4)|(1)
											* Q7=(5)|(4)|(1): 9(5.0/0.0)
											* Q7!=(5)|(4)|(1): 8(2.0/1.0)
										* Q19!=(5)|(4)|(1): 5(2.0/0.0)
						* Q11!=(5)|(4)|(3)
							* attendance=(3)|(2)|(1): 5(14.0/3.0)
							* attendance!=(3)|(2)|(1)
							* Q7=(5)|(2): 13(2.0/0.0)
							* Q7!=(5)|(2): 3(1.0/2.0)
				* Q1!=(5)|(4)
						* Q11=(5)|(4)|(3)
						* Q16=(5)|(4)
						* Q19=(3)
							* Q2=(2): 3(1.0/3.0)
							* Q2!=(2): 8(9.0/1.0)
						* Q19!=(3)
										* Q6=(5)|(4)|(3)|(2)
								* Q21=(5)
											* Q13=(4)|(3)|(2)
											* Q27=(4)|(2)
													* Q9=(4)|(3)|(1): 9(3.0/0.0)
													* Q9!=(4)|(3)|(1): 3(2.0/1.0)
											* Q27!=(4)|(2): 8(11.0/2.0)
											* Q13!=(4)|(3)|(2)
										* difficulty=(4)
													* attendance=(3)|(2)|(1): 5(5.0/0.0)
													* attendance!=(3)|(2)|(1): 13(2.0/1.0)
										* difficulty!=(4)
											* Q4=(2)
															* Q18=(5)|(1)|(2)|(3): 3(3.0/2.0)
															* Q18!=(5)|(1)|(2)|(3): 9(4.0/1.0)
											* Q4!=(2)
														* Q5=(5)|(4)|(2)
														* attendance=(3)|(2)
																* Q2=(5)|(3)|(2): 8(3.0/0.0)
																* Q2!=(5)|(3)|(2)
																	* Q6=(4)|(1)|(3): 8(1.0/1.0)
																	* Q6!=(4)|(1)|(3): 13(2.0/0.0)
														* attendance!=(3)|(2)
																* Q2=(4)|(3)|(1): 13(6.0/1.0)
																* Q2!=(4)|(3)|(1)
																		* attendance=(4)|(1)|(2)|(3): 5(1.0/2.0)
																		* attendance!=(4)|(1)|(2)|(3): 3(1.0/1.0)
														* Q5!=(5)|(4)|(2)
															* Q12=(4)|(3)|(2): 8(5.0/1.0)
															* Q12!=(4)|(3)|(2): 5(1.0/1.0)
								* Q21!=(5)
										* Q28=(5)|(3)
										* Q4=(4): 5(4.0/1.0)
										* Q4!=(4)
													* Q9=(4)|(3)|(1): 3(11.0/3.0)
													* Q9!=(4)|(3)|(1): 4(1.0/2.0)
										* Q28!=(5)|(3)
												* Q20=(5)|(4)|(1)
													* Q4=(5)|(4)|(2)
												* difficulty=(5): 3(3.0/0.0)
												* difficulty!=(5)
													* Q6=(5): 8(3.0/0.0)
													* Q6!=(5)
																	* Q4=(4)|(1)|(3)|(5)
															* Q22=(5): 3(2.0/0.0)
															* Q22!=(5)
																* attendance=(3)
																				* difficulty=(4)|(3)|(1)|(5): 5(3.0/1.0)
																				* difficulty!=(4)|(3)|(1)|(5): 8(1.0/1.0)
																* attendance!=(3)
																				* Q1=(3)|(2)|(4)|(5)
																			* Q8=(5)|(2)
																						* Q3=(4)|(1)|(2)|(5): 13(2.0/0.0)
																						* Q3!=(4)|(1)|(2)|(5): 5(2.0/0.0)
																			* Q8!=(5)|(2)
																						* Q6=(4)|(1)|(2)|(5)
																							* Q2=(4)|(1)|(2)|(5)
																					* difficulty=(4): 3(2.0/0.0)
																					* difficulty!=(4)
																									* Q5=(4)|(1)|(2)|(5): 8(2.0/3.0)
																									* Q5!=(4)|(1)|(2)|(5): 9(3.0/1.0)
																							* Q2!=(4)|(1)|(2)|(5): 9(3.0/0.0)
																						* Q6!=(4)|(1)|(2)|(5): 8(2.0/0.0)
																				* Q1!=(3)|(2)|(4)|(5): 9(3.0/0.0)
																	* Q4!=(4)|(1)|(3)|(5)
															* attendance=(3)
																* difficulty=(4): 5(1.0/2.0)
																* difficulty!=(4): 3(3.0/1.0)
															* attendance!=(3)
																		* Q27=(4)|(3)|(1): 8(6.0/1.0)
																		* Q27!=(4)|(3)|(1): 3(1.0/1.0)
													* Q4!=(5)|(4)|(2)
														* Q5=(4)|(3)|(5)
															* Q8=(3)|(2)|(5)
																* Q10=(3)|(1)|(5)
																		* attendance=(4)|(3)|(2)|(1)
																* Q6=(4): 5(3.0/0.0)
																* Q6!=(4): 5(5.0/5.0)
																		* attendance!=(4)|(3)|(2)|(1): 3(1.0/1.0)
																* Q10!=(3)|(1)|(5): 9(3.0/1.0)
															* Q8!=(3)|(2)|(5): 5(7.0/2.0)
														* Q5!=(4)|(3)|(5): 8(3.0/1.0)
												* Q20!=(5)|(4)|(1): 9(5.0/1.0)
										* Q6!=(5)|(4)|(3)|(2): 13(4.0/0.0)
						* Q16!=(5)|(4)
							* Q12=(5)|(3)
							* Q14=(3)
									* attendance=(2)|(1): 3(7.0/2.0)
									* attendance!=(2)|(1)
									* Q4=(2): 13(2.0/0.0)
									* Q4!=(2)
													* Q24=(5)|(4)|(3)|(1)
											* Q1=(2): 8(3.0/0.0)
											* Q1!=(2): 9(3.0/3.0)
													* Q24!=(5)|(4)|(3)|(1): 5(3.0/1.0)
							* Q14!=(3)
									* Q6=(5)|(3)
										* Q3=(5)|(3)
											* attendance=(4)|(2): 8(5.0/0.0)
											* attendance!=(4)|(2)
											* Q21=(5): 3(1.0/1.0)
											* Q21!=(5): 4(3.0/0.0)
										* Q3!=(5)|(3)
												* Q13=(4)|(1)|(5)
													* Q2=(3)|(2)|(5): 5(6.0/1.0)
													* Q2!=(3)|(2)|(5)
														* attendance=(2)|(1)|(4): 4(1.0/1.0)
														* attendance!=(2)|(1)|(4): 3(2.0/0.0)
												* Q13!=(4)|(1)|(5): 9(4.0/0.0)
									* Q6!=(5)|(3)
									* Q2=(2)
										* Q17=(5): 8(3.0/1.0)
										* Q17!=(5): 9(4.0/1.0)
									* Q2!=(2): 8(17.0/4.0)
							* Q12!=(5)|(3)
							* Q2=(2)
									* Q6=(4)|(2)
											* Q15=(4)|(1)|(5)
										* Q1=(2): 5(1.0/1.0)
										* Q1!=(2): 9(4.0/0.0)
											* Q15!=(4)|(1)|(5): 13(4.0/1.0)
									* Q6!=(4)|(2)
										* Q9=(5)|(2): 4(1.0/1.0)
										* Q9!=(5)|(2): 8(6.0/0.0)
							* Q2!=(2): 8(33.0/6.0)
						* Q11!=(5)|(4)|(3)
						* attendance=(2)|(1)
								* difficulty=(5)|(4)|(3)
										* Q5=(4)|(3)|(2)|(5)
										* Q10=(5)|(3)|(2)
											* Q9=(5)|(4)|(2)
										* Q3=(4): 5(1.0/1.0)
										* Q3!=(4): 3(7.0/1.0)
											* Q9!=(5)|(4)|(2)
										* Q6=(4): 3(2.0/0.0)
										* Q6!=(4): 5(6.0/1.0)
										* Q10!=(5)|(3)|(2): 5(4.0/0.0)
										* Q5!=(4)|(3)|(2)|(5): 9(3.0/1.0)
								* difficulty!=(5)|(4)|(3): 13(5.0/1.0)
						* attendance!=(2)|(1)
							* Q16=(3)|(2)
									* Q28=(5)|(3)|(2)
									* Q4=(5)|(2): 5(7.0/0.0)
									* Q4!=(5)|(2)
												* Q2=(4)|(3)|(1)|(5)
													* Q7=(3)|(2)|(4)|(5): 3(1.0/2.0)
													* Q7!=(3)|(2)|(4)|(5): 5(2.0/0.0)
												* Q2!=(4)|(3)|(1)|(5): 13(2.0/0.0)
									* Q28!=(5)|(3)|(2)
								* Q7=(3)
									* Q5=(3): 3(2.0/0.0)
									* Q5!=(3): 5(3.0/0.0)
								* Q7!=(3)
											* Q6=(5)|(4)|(2): 8(9.0/0.0)
											* Q6!=(5)|(4)|(2): 4(1.0/1.0)
							* Q16!=(3)|(2)
								* Q27=(3)|(2)
										* difficulty=(5)|(4)|(3): 13(4.0/0.0)
										* difficulty!=(5)|(4)|(3): 4(2.0/0.0)
								* Q27!=(3)|(2)
								* Q20=(4)
											* Q5=(3)|(2)|(5)
										* Q3=(3): 3(2.0/0.0)
										* Q3!=(3): 4(3.0/3.0)
											* Q5!=(3)|(2)|(5)
												* Q10=(4)|(2)|(5): 13(2.0/0.0)
												* Q10!=(4)|(2)|(5): 5(2.0/0.0)
								* Q20!=(4)
									* Q6=(2): 8(4.0/1.0)
									* Q6!=(2)
											* Q5=(4)|(2): 3(4.0/0.0)
											* Q5!=(4)|(2)
													* Q14=(4)|(3)|(2): 8(3.0/0.0)
													* Q14!=(4)|(3)|(2): 13(2.0/1.0)
			* Q21!=(5)|(4)
						* Q17=(5)|(4)|(3)|(2)
				* difficulty=(2)
							* Q20=(3)|(2)|(5)
							* Q11=(5)|(4)
										* Q1=(5)|(3)|(2)|(4): 3(1.0/2.0)
										* Q1!=(5)|(3)|(2)|(4): 4(2.0/0.0)
							* Q11!=(5)|(4): 13(26.0/17.0)
							* Q20!=(3)|(2)|(5)
						* attendance=(2): 13(2.0/0.0)
						* attendance!=(2)
								* Q14=(5)|(2): 8(2.0/0.0)
								* Q14!=(5)|(2): 9(5.0/0.0)
				* difficulty!=(2)
						* attendance=(4)|(3)
						* Q15=(5): 5(6.0/0.0)
						* Q15!=(5)
									* Q4=(4)|(3)|(2)
										* Q26=(4)|(3)|(2)
										* Q8=(5)|(4)
											* Q16=(5)|(4)
													* difficulty=(4)|(2)|(5): 5(2.0/1.0)
													* difficulty!=(4)|(2)|(5): 9(3.0/0.0)
											* Q16!=(5)|(4)
											* Q3=(3): 8(2.0/1.0)
											* Q3!=(3)
															* Q5=(5)|(4)|(1)|(3): 5(6.0/0.0)
															* Q5!=(5)|(4)|(1)|(3): 3(1.0/1.0)
										* Q8!=(5)|(4)
												* difficulty=(5)|(4)|(2)
														* Q1=(4)|(3)|(2)|(5)
														* Q23=(4)|(3)|(2)
															* Q20=(3)|(2)|(5)
															* Q6=(3)|(2)
															* Q25=(4)
																			* attendance=(4)|(0)|(1)|(2): 5(2.0/0.0)
																			* attendance!=(4)|(0)|(1)|(2): 4(2.0/0.0)
															* Q25!=(4)
																* Q28=(4): 3(2.0/0.0)
																* Q28!=(4)
																	* Q3=(4): 9(2.0/1.0)
																	* Q3!=(4)
																		* Q4=(4): 5(2.0/0.0)
																		* Q4!=(4)
																			* Q13=(2)
																				* attendance=(4): 5(3.0/5.0)
																				* attendance!=(4)
																					* Q1=(3): 13(2.0/0.0)
																					* Q1!=(3)
																								* Q16=(2)|(4)|(5): 3(4.0/3.0)
																								* Q16!=(2)|(4)|(5): 4(1.0/1.0)
																			* Q13!=(2): 3(25.0/49.0)
															* Q6!=(3)|(2)
																	* Q2=(3)|(1)|(5): 13(2.0/1.0)
																	* Q2!=(3)|(1)|(5): 8(3.0/0.0)
															* Q20!=(3)|(2)|(5)
														* Q17=(5): 4(1.0/1.0)
														* Q17!=(5): 3(6.0/0.0)
														* Q23!=(4)|(3)|(2): 5(3.0/0.0)
														* Q1!=(4)|(3)|(2)|(5): 3(7.0/1.0)
												* difficulty!=(5)|(4)|(2)
													* Q7=(4)|(3)|(2)
														* Q4=(3)|(1)|(5)
													* attendance=(4)
															* Q13=(3)|(5)
																		* Q15=(3)|(1)|(4)|(5)
																		* Q1=(4)|(3)|(5): 3(8.0/10.0)
																		* Q1!=(4)|(3)|(5): 8(2.0/1.0)
																		* Q15!=(3)|(1)|(4)|(5): 4(1.0/1.0)
															* Q13!=(3)|(5): 13(3.0/1.0)
													* attendance!=(4)
																* Q2=(3)|(1)|(5)
																* Q11=(4)|(2): 5(2.0/0.0)
																* Q11!=(4)|(2): 13(18.0/18.0)
																* Q2!=(3)|(1)|(5): 4(1.0/2.0)
														* Q4!=(3)|(1)|(5)
														* Q26=(4)|(3)
														* attendance=(4): 8(2.0/0.0)
														* attendance!=(4)
																	* Q27=(4)|(3)|(5)
																			* Q3=(4)|(3)|(1)|(5): 5(6.0/0.0)
																			* Q3!=(4)|(3)|(1)|(5): 5(1.0/1.0)
																	* Q27!=(4)|(3)|(5): 8(1.0/1.0)
														* Q26!=(4)|(3)
															* Q19=(5)|(2)
																		* attendance=(4)|(0)|(1)|(2)
																* Q9=(3): 5(2.0/0.0)
																* Q9!=(3): 3(4.0/3.0)
																		* attendance!=(4)|(0)|(1)|(2)
																			* difficulty=(3)|(2)|(4)|(5): 9(3.0/2.0)
																			* difficulty!=(3)|(2)|(4)|(5): 13(2.0/1.0)
															* Q19!=(5)|(2)
																		* difficulty=(3)|(2)|(4)|(5): 3(7.0/0.0)
																		* difficulty!=(3)|(2)|(4)|(5): 3(1.0/1.0)
													* Q7!=(4)|(3)|(2): 9(3.0/0.0)
										* Q26!=(4)|(3)|(2)
											* Q17=(5)|(3)|(1)
										* Q14=(4): 4(2.0/0.0)
										* Q14!=(4)
											* Q16=(3): 3(1.0/1.0)
											* Q16!=(3): 8(7.0/0.0)
											* Q17!=(5)|(3)|(1)
											* Q23=(5)|(2)
														* attendance=(4)|(0)|(1)|(2): 5(2.0/0.0)
														* attendance!=(4)|(0)|(1)|(2): 8(1.0/1.0)
											* Q23!=(5)|(2): 9(4.0/1.0)
									* Q4!=(4)|(3)|(2)
									* Q10=(4)|(2)
											* Q17=(4)|(3)|(1)
										* Q14=(3)
													* Q3=(4)|(2)|(5): 13(2.0/0.0)
													* Q3!=(4)|(2)|(5): 5(1.0/1.0)
										* Q14!=(3): 4(6.0/2.0)
											* Q17!=(4)|(3)|(1): 13(6.0/1.0)
									* Q10!=(4)|(2)
										* Q27=(3)|(2)
													* Q3=(5)|(3)|(2)|(4): 8(4.0/0.0)
													* Q3!=(5)|(3)|(2)|(4): 5(1.0/1.0)
										* Q27!=(3)|(2)
											* Q26=(4)|(3): 9(5.0/1.0)
											* Q26!=(4)|(3)
												* Q3=(4)|(2): 4(3.0/1.0)
												* Q3!=(4)|(2)
													* Q26=(5)|(2): 5(1.0/2.0)
													* Q26!=(5)|(2): 3(3.0/1.0)
						* attendance!=(4)|(3)
							* Q7=(5)|(3)
									* Q6=(5)|(3)|(1)
									* difficulty=(5)|(4)
										* Q18=(3)|(5)
													* Q4=(3)|(2)|(4)|(5)
														* attendance=(2)|(1)|(3)|(4): 3(30.0/45.0)
														* attendance!=(2)|(1)|(3)|(4)
														* Q12=(3)|(1)|(5)
																* difficulty=(5)|(1)|(2)|(3): 3(7.0/1.0)
																* difficulty!=(5)|(1)|(2)|(3): 3(3.0/5.0)
														* Q12!=(3)|(1)|(5): 4(1.0/1.0)
													* Q4!=(3)|(2)|(4)|(5): 9(2.0/0.0)
										* Q18!=(3)|(5): 3(7.0/1.0)
									* difficulty!=(5)|(4)
									* Q22=(4): 5(3.0/0.0)
									* Q22!=(4)
												* Q12=(5)|(3)|(2)
													* Q10=(5)|(3)|(1)
													* Q24=(3)|(2)
														* Q26=(4)|(2)
																* Q3=(3)|(1)|(5)
															* Q1=(3): 3(2.0/0.0)
															* Q1!=(3): 9(2.0/1.0)
																* Q3!=(3)|(1)|(5): 8(2.0/0.0)
														* Q26!=(4)|(2)
														* Q25=(4): 4(2.0/0.0)
														* Q25!=(4)
															* Q18=(2): 5(2.0/0.0)
															* Q18!=(2)
																	* Q27=(3)|(1): 3(86.0/146.0)
																	* Q27!=(3)|(1): 3(4.0/0.0)
													* Q24!=(3)|(2): 3(4.0/0.0)
													* Q10!=(5)|(3)|(1)
														* Q2=(3)|(1)|(5)
													* Q9=(3): 9(2.0/1.0)
													* Q9!=(3): 5(4.0/0.0)
														* Q2!=(3)|(1)|(5): 3(3.0/1.0)
												* Q12!=(5)|(3)|(2)
												* Q4=(4)|(3)
														* Q16=(3)|(1)|(5)
															* Q3=(3)|(2)|(5): 4(3.0/0.0)
															* Q3!=(3)|(2)|(5): 8(1.0/1.0)
														* Q16!=(3)|(1)|(5): 5(2.0/0.0)
												* Q4!=(4)|(3): 9(3.0/0.0)
									* Q6!=(5)|(3)|(1)
										* Q10=(4)|(3)|(2)
											* Q14=(4)|(3)|(1)
										* Q9=(2): 5(3.0/3.0)
										* Q9!=(2)
													* Q3=(4)|(3)|(1): 9(10.0/3.0)
													* Q3!=(4)|(3)|(1)
															* attendance=(1)|(2)|(3)|(4): 13(2.0/0.0)
															* attendance!=(1)|(2)|(3)|(4): 4(1.0/1.0)
											* Q14!=(4)|(3)|(1)
												* Q27=(3)|(1)|(5)
													* attendance=(1)|(3)|(4): 9(1.0/1.0)
													* attendance!=(1)|(3)|(4): 8(2.0/0.0)
												* Q27!=(3)|(1)|(5): 3(3.0/1.0)
										* Q10!=(4)|(3)|(2)
									* difficulty=(4): 3(2.0/0.0)
									* difficulty!=(4): 13(3.0/0.0)
							* Q7!=(5)|(3)
							* Q1=(4)
								* Q17=(4)
												* Q19=(4)|(1)|(2)|(5): 3(5.0/0.0)
												* Q19!=(4)|(1)|(2)|(5): 13(2.0/1.0)
								* Q17!=(4)
									* Q24=(4): 3(1.0/1.0)
									* Q24!=(4)
											* Q12=(4)|(2)
											* Q2=(3): 3(2.0/0.0)
											* Q2!=(3)
												* Q14=(4): 3(1.0/1.0)
												* Q14!=(4): 5(4.0/0.0)
											* Q12!=(4)|(2): 5(7.0/0.0)
							* Q1!=(4)
									* Q5=(4)|(2)
												* Q6=(5)|(4)|(3)|(2)
													* Q11=(4)|(3)|(2)|(5)
												* Q28=(4)|(3)
													* Q8=(2)|(5)
													* Q1=(3): 5(2.0/1.0)
													* Q1!=(3)
																	* Q12=(4)|(3)|(2)|(5)
																		* Q25=(4)|(3)|(1)|(5)
																		* Q18=(3)|(2)|(5)
																	* difficulty=(3): 9(2.0/0.0)
																	* difficulty!=(3)
																					* Q16=(3)|(1)|(4)|(5)
																			* Q12=(3): 3(2.0/0.0)
																			* Q12!=(3): 9(3.0/8.0)
																					* Q16!=(3)|(1)|(4)|(5): 3(3.0/0.0)
																		* Q18!=(3)|(2)|(5): 5(2.0/1.0)
																		* Q25!=(4)|(3)|(1)|(5): 9(3.0/0.0)
																	* Q12!=(4)|(3)|(2)|(5): 9(3.0/0.0)
													* Q8!=(2)|(5)
													* Q10=(3)
														* Q11=(4): 9(2.0/1.0)
														* Q11!=(4)
																		* Q15=(3)|(1)|(4)|(5): 3(2.0/1.0)
																		* Q15!=(3)|(1)|(4)|(5): 8(1.0/1.0)
													* Q10!=(3): 3(9.0/1.0)
												* Q28!=(4)|(3)
												* difficulty=(4)
															* Q12=(2)|(4)|(5)
														* Q3=(3): 3(2.0/0.0)
														* Q3!=(3)
															* attendance=(2): 9(2.0/3.0)
															* attendance!=(2)
																			* attendance=(1)|(2)|(3)|(4): 13(3.0/2.0)
																			* attendance!=(1)|(2)|(3)|(4): 13(3.0/0.0)
															* Q12!=(2)|(4)|(5): 9(2.0/0.0)
												* difficulty!=(4)
													* Q1=(3): 5(7.0/4.0)
													* Q1!=(3)
														* Q14=(3)
																		* Q6=(4)|(3)|(1)|(5): 4(1.0/2.0)
																		* Q6!=(4)|(3)|(1)|(5): 5(3.0/0.0)
														* Q14!=(3)
															* Q27=(3): 13(2.0/0.0)
															* Q27!=(3): 3(30.0/35.0)
													* Q11!=(4)|(3)|(2)|(5)
											* Q12=(2): 3(2.0/0.0)
											* Q12!=(2): 5(7.0/2.0)
												* Q6!=(5)|(4)|(3)|(2)
											* Q10=(3)|(2): 13(5.0/0.0)
											* Q10!=(3)|(2): 3(5.0/1.0)
									* Q5!=(4)|(2)
												* difficulty=(5)|(4)|(3)|(2)
											* Q1=(5)|(2)
											* Q25=(3)
												* Q4=(3): 4(2.0/0.0)
												* Q4!=(3): 5(1.0/2.0)
											* Q25!=(3): 5(6.0/0.0)
											* Q1!=(5)|(2)
												* Q12=(4)|(3)
														* Q6=(3)|(2)|(5): 3(4.0/0.0)
														* Q6!=(3)|(2)|(5): 13(2.0/0.0)
												* Q12!=(4)|(3)
												* Q14=(4): 8(3.0/1.0)
												* Q14!=(4)
														* Q9=(5)|(3)
																	* Q11=(3)|(2)|(4)|(5): 4(3.0/0.0)
																	* Q11!=(3)|(2)|(4)|(5): 8(2.0/1.0)
														* Q9!=(5)|(3)
															* Q10=(3)|(2): 5(3.0/0.0)
															* Q10!=(3)|(2)
																* Q17=(5)|(3)
																	* Q11=(5)|(4): 9(2.0/0.0)
																	* Q11!=(5)|(4)
																				* Q26=(3)|(2)|(4)|(5): 4(1.0/1.0)
																				* Q26!=(3)|(2)|(4)|(5): 5(2.0/0.0)
																* Q17!=(5)|(3)
																			* attendance=(2)|(1)|(3)|(4): 3(6.0/0.0)
																			* attendance!=(2)|(1)|(3)|(4): 4(1.0/1.0)
												* difficulty!=(5)|(4)|(3)|(2)
												* Q14=(5)|(3)|(2)
													* Q28=(5)|(4)|(2)
															* Q1=(5)|(3)|(2)|(4)
															* Q11=(4)|(2)|(5): 3(4.0/1.0)
															* Q11!=(4)|(2)|(5): 5(2.0/1.0)
															* Q1!=(5)|(3)|(2)|(4): 5(4.0/1.0)
													* Q28!=(5)|(4)|(2)
													* Q3=(5)|(3): 13(4.0/0.0)
													* Q3!=(5)|(3)
													* Q7=(2): 4(2.0/0.0)
													* Q7!=(2)
																	* Q10=(3)|(2)|(4)|(5): 5(2.0/2.0)
																	* Q10!=(3)|(2)|(4)|(5): 13(2.0/1.0)
												* Q14!=(5)|(3)|(2)
													* Q9=(4)|(3)|(2): 13(7.0/0.0)
													* Q9!=(4)|(3)|(2)
															* Q2=(2)|(3)|(4)|(5): 9(1.0/1.0)
															* Q2!=(2)|(3)|(4)|(5): 3(2.0/0.0)
						* Q17!=(5)|(4)|(3)|(2)
						* Q1=(5)|(3)|(2)
					* difficulty=(4)
								* Q3=(3)|(4)|(5): 5(2.0/1.0)
								* Q3!=(3)|(4)|(5): 3(3.0/0.0)
					* difficulty!=(4)
						* Q10=(5): 9(2.0/0.0)
						* Q10!=(5)
							* Q7=(2)
								* attendance=(3): 3(1.0/1.0)
								* attendance!=(3)
										* Q13=(4)|(2): 13(2.0/0.0)
										* Q13!=(4)|(2): 5(3.0/1.0)
							* Q7!=(2): 13(18.0/4.0)
						* Q1!=(5)|(3)|(2)
					* Q11=(2)
							* Q14=(4)|(2): 4(2.0/0.0)
							* Q14!=(4)|(2): 13(4.0/0.0)
					* Q11!=(2)
							* Q23=(3)|(2): 3(6.0/1.0)
							* Q23!=(3)|(2)
								* Q15=(3)|(2): 13(4.0/0.0)
								* Q15!=(3)|(2)
									* Q11=(5)|(4): 8(2.0/3.0)
									* Q11!=(5)|(4)
									* Q13=(2): 5(2.0/1.0)
									* Q13!=(2)
										* attendance=(1)
												* difficulty=(3)|(2)
															* difficulty=(3)|(1)|(4)|(5): 13(2.0/2.0)
															* difficulty!=(3)|(1)|(4)|(5): 13(2.0/0.0)
												* difficulty!=(3)|(2): 3(11.0/9.0)
										* attendance!=(1)
											* Q3=(2): 4(1.0/2.0)
											* Q3!=(2)
													* Q9=(5)|(3): 3(3.0/1.0)
													* Q9!=(5)|(3)
														* difficulty=(4)|(3)
														* attendance=(4)
																		* difficulty=(4)|(1)|(2)|(5): 9(2.0/2.0)
																		* difficulty!=(4)|(1)|(2)|(5): 13(3.0/0.0)
														* attendance!=(4): 5(6.0/20.0)
														* difficulty!=(4)|(3)
														* Q6=(2): 13(2.0/0.0)
														* Q6!=(2)
															* Q26=(2): 13(2.0/0.0)
															* Q26!=(2)
																	* Q14=(5)|(2): 5(2.0/1.0)
																	* Q14!=(5)|(2): 3(81.0/157.0)
* instr!=(3)
		* instr=(2)|(3)
			* difficulty=(5)|(4)
						* Q21=(5)|(4)|(3)|(2)
						* Q6=(5)|(4)|(3)
							* attendance=(4)|(3)|(2)
						* Q19=(2): 6(3.0/0.0)
						* Q19!=(2)
							* nb.repeat=(3): 1(2.0/1.0)
							* nb.repeat!=(3)
										* Q28=(5)|(4)|(3)
												* Q5=(5)|(4)|(3)|(1)
													* Q14=(5)|(4)|(3)|(1)
														* Q23=(5)|(4)|(3)|(1)
												* Q13=(4)
															* Q20=(4)|(1)|(2)
																	* Q8=(5)|(4)|(3)|(1)
																	* Q12=(4)|(1)|(5): 11(19.0/22.0)
																	* Q12!=(4)|(1)|(5): 11(4.0/0.0)
																	* Q8!=(5)|(4)|(3)|(1): 6(2.0/0.0)
															* Q20!=(4)|(1)|(2): 11(8.0/0.0)
												* Q13!=(4)
													* Q24=(4): 1(3.0/0.0)
													* Q24!=(4)
														* Q5=(4): 6(4.0/1.0)
														* Q5!=(4)
																		* Q1=(5)|(3)|(1)|(4): 11(30.0/33.0)
																		* Q1!=(5)|(3)|(1)|(4): 1(2.0/1.0)
														* Q23!=(5)|(4)|(3)|(1): 1(1.0/1.0)
													* Q14!=(5)|(4)|(3)|(1): 6(2.0/0.0)
												* Q5!=(5)|(4)|(3)|(1): 6(2.0/0.0)
										* Q28!=(5)|(4)|(3): 11(4.0/0.0)
							* attendance!=(4)|(3)|(2)
							* Q1=(4)|(2): 11(22.0/6.0)
							* Q1!=(4)|(2)
								* Q14=(5)|(4)
								* nb.repeat=(2): 1(2.0/1.0)
								* nb.repeat!=(2)
									* attendance=(1): 6(2.0/0.0)
									* attendance!=(1): 1(2.0/2.0)
								* Q14!=(5)|(4)
										* Q10=(3)|(1)|(5)
												* Q13=(4)|(3)|(1)|(5): 11(17.0/11.0)
												* Q13!=(4)|(3)|(1)|(5): 6(2.0/0.0)
										* Q10!=(3)|(1)|(5): 11(4.0/0.0)
						* Q6!=(5)|(4)|(3)
					* Q10=(2)
						* Q18=(4): 6(2.0/0.0)
						* Q18!=(4): 11(13.0/5.0)
					* Q10!=(2)
						* Q1=(4): 11(3.0/1.0)
						* Q1!=(4): 11(26.0/0.0)
						* Q21!=(5)|(4)|(3)|(2)
							* attendance=(4)|(3)|(2)|(1): 6(15.0/6.0)
							* attendance!=(4)|(3)|(2)|(1): 11(2.0/3.0)
			* difficulty!=(5)|(4)
			* difficulty=(2)
					* Q14=(4)|(2)
							* Q4=(5)|(4)|(2)
						* Q16=(3): 1(3.0/0.0)
						* Q16!=(3)
							* nb.repeat=(2)
										* Q1=(3)|(2)|(5): 11(5.0/3.0)
										* Q1!=(3)|(2)|(5): 1(3.0/2.0)
							* nb.repeat!=(2)
								* Q11=(4)
											* Q28=(4)|(1)|(2)
												* Q6=(4)|(1)|(5): 6(14.0/12.0)
												* Q6!=(4)|(1)|(5): 13(2.0/1.0)
											* Q28!=(4)|(1)|(2): 1(3.0/0.0)
								* Q11!=(4): 6(14.0/2.0)
							* Q4!=(5)|(4)|(2): 6(21.0/3.0)
					* Q14!=(4)|(2)
						* Q7=(4)|(2)
						* Q28=(3): 6(3.0/0.0)
						* Q28!=(3)
								* Q1=(3)|(2)
									* attendance=(3)|(2): 11(3.0/1.0)
									* attendance!=(3)|(2)
												* Q4=(4)|(3)|(1)|(5): 13(3.0/0.0)
												* Q4!=(4)|(3)|(1)|(5): 1(2.0/0.0)
								* Q1!=(3)|(2): 1(6.0/0.0)
						* Q7!=(4)|(2)
							* Q27=(4)|(2): 6(7.0/1.0)
							* Q27!=(4)|(2)
								* Q11=(5)|(2)
								* Q2=(3): 1(3.0/0.0)
								* Q2!=(3)
											* attendance=(4)|(2)|(1)
										* attendance=(2): 6(3.0/0.0)
										* attendance!=(2): 6(3.0/5.0)
											* attendance!=(4)|(2)|(1)
										* attendance=(3): 1(1.0/1.0)
										* attendance!=(3): 1(3.0/1.0)
								* Q11!=(5)|(2)
									* Q3=(5)|(2): 6(5.0/0.0)
									* Q3!=(5)|(2): 6(16.0/21.0)
			* difficulty!=(2)
							* difficulty=(3)|(2)|(4)|(5)
						* Q6=(5)|(4)
									* Q4=(5)|(4)|(3)|(2)
										* Q11=(5)|(4)|(3)|(2)
											* Q14=(5)|(4)|(3)|(2)
										* Q9=(5)|(4)
												* Q24=(5)|(4)|(1)
													* Q12=(5)|(4)|(3)
												* Q2=(3): 6(4.0/0.0)
												* Q2!=(3)
																* Q13=(5)|(4)|(1)|(2)
															* nb.repeat=(3)|(2)
																	* Q1=(4)|(1)|(3)
																			* attendance=(4)|(3)|(1)|(2)
																	* nb.repeat=(3): 6(2.0/0.0)
																	* nb.repeat!=(3): 6(3.0/3.0)
																			* attendance!=(4)|(3)|(1)|(2): 1(1.0/1.0)
																	* Q1!=(4)|(1)|(3): 6(5.0/0.0)
															* nb.repeat!=(3)|(2)
																		* Q5=(5)|(4)|(1)|(2)
																	* Q26=(5)|(3)
																			* attendance=(4)|(3)|(1)
																		* Q20=(4): 6(4.0/0.0)
																		* Q20!=(4)
																						* Q13=(5)|(1)|(2)|(3)
																							* Q2=(5)|(1)|(2)|(3)
																					* attendance=(4): 1(9.0/13.0)
																					* attendance!=(4): 6(12.0/16.0)
																							* Q2!=(5)|(1)|(2)|(3): 6(4.0/2.0)
																						* Q13!=(5)|(1)|(2)|(3): 11(4.0/1.0)
																			* attendance!=(4)|(3)|(1)
																					* Q4=(5)|(1)|(2)|(3)
																						* attendance=(2)|(1)|(3)|(4): 6(5.0/1.0)
																						* attendance!=(2)|(1)|(3)|(4): 6(3.0/0.0)
																					* Q4!=(5)|(1)|(2)|(3): 6(5.0/0.0)
																	* Q26!=(5)|(3)
																	* Q1=(5): 11(5.0/0.0)
																	* Q1!=(5)
																				* Q2=(4)|(1)|(3)
																						* Q7=(4)|(1)|(2)|(5)
																				* Q6=(5): 6(3.0/0.0)
																				* Q6!=(5)
																							* Q1=(4)|(1)|(5): 6(38.0/47.0)
																							* Q1!=(4)|(1)|(5): 1(5.0/4.0)
																						* Q7!=(4)|(1)|(2)|(5): 1(2.0/0.0)
																				* Q2!=(4)|(1)|(3): 1(2.0/0.0)
																		* Q5!=(5)|(4)|(1)|(2): 1(1.0/1.0)
																* Q13!=(5)|(4)|(1)|(2): 11(2.0/0.0)
													* Q12!=(5)|(4)|(3)
														* attendance=(3)|(2)|(0): 13(2.0/0.0)
														* attendance!=(3)|(2)|(0): 11(2.0/0.0)
												* Q24!=(5)|(4)|(1)
											* Q27=(4): 11(3.0/0.0)
											* Q27!=(4)
														* Q1=(5)|(3)|(2): 13(4.0/1.0)
														* Q1!=(5)|(3)|(2)
															* Q13=(5)|(4)|(2)
																	* attendance=(4)|(3)|(0)|(1): 1(2.0/1.0)
																	* attendance!=(4)|(3)|(0)|(1): 6(2.0/0.0)
															* Q13!=(5)|(4)|(2): 1(4.0/0.0)
										* Q9!=(5)|(4)
										* Q28=(3): 11(3.0/1.0)
										* Q28!=(3)
													* Q12=(5)|(3)|(2): 6(13.0/0.0)
													* Q12!=(5)|(3)|(2)
														* Q3=(5)|(4)|(1)
																* Q20=(5)|(4)|(1)|(2)
														* attendance=(2): 1(1.0/1.0)
														* attendance!=(2): 6(4.0/0.0)
																* Q20!=(5)|(4)|(1)|(2): 11(2.0/0.0)
														* Q3!=(5)|(4)|(1): 1(3.0/0.0)
											* Q14!=(5)|(4)|(3)|(2): 11(3.0/0.0)
										* Q11!=(5)|(4)|(3)|(2): 13(2.0/0.0)
									* Q4!=(5)|(4)|(3)|(2): 1(3.0/0.0)
						* Q6!=(5)|(4)
							* Q3=(5)|(4)
										* Q5=(5)|(4)|(3)|(2)
											* Q11=(5)|(4)|(3)|(1)
												* Q11=(5)|(4)|(1)|(2)
										* Q23=(4)
											* Q6=(2): 11(3.0/0.0)
											* Q6!=(2)
														* Q1=(4)|(3)|(5)
													* Q8=(4): 6(1.0/1.0)
													* Q8!=(4): 1(4.0/0.0)
														* Q1!=(4)|(3)|(5): 6(3.0/0.0)
										* Q23!=(4)
											* attendance=(4)
												* Q1=(2): 13(2.0/0.0)
												* Q1!=(2)
															* Q1=(5)|(4)|(2): 1(1.0/1.0)
															* Q1!=(5)|(4)|(2): 11(2.0/0.0)
											* attendance!=(4): 11(13.0/2.0)
												* Q11!=(5)|(4)|(1)|(2): 11(10.0/0.0)
											* Q11!=(5)|(4)|(3)|(1): 1(2.0/0.0)
										* Q5!=(5)|(4)|(3)|(2): 13(2.0/0.0)
							* Q3!=(5)|(4)
							* Q17=(5)
									* Q16=(5)|(3)
												* attendance=(4)|(0)|(1)|(2): 6(3.0/0.0)
												* attendance!=(4)|(0)|(1)|(2): 1(1.0/1.0)
									* Q16!=(5)|(3)
									* Q2=(3): 1(1.0/1.0)
									* Q2!=(3): 11(8.0/0.0)
							* Q17!=(5)
										* Q16=(5)|(4)|(2)
										* Q15=(5)|(3)
										* Q5=(2): 1(5.0/0.0)
										* Q5!=(2): 6(4.0/2.0)
										* Q15!=(5)|(3)
										* Q7=(4)
													* attendance=(2)|(1)|(4): 1(2.0/0.0)
													* attendance!=(2)|(1)|(4): 6(1.0/1.0)
										* Q7!=(4)
												* Q25=(4)|(2)
													* attendance=(3)|(1)
														* Q1=(4)|(3): 11(5.0/2.0)
														* Q1!=(4)|(3)
																	* Q1=(2)|(3)|(4)|(5): 6(4.0/4.0)
																	* Q1!=(2)|(3)|(4)|(5): 6(2.0/0.0)
													* attendance!=(3)|(1)
															* Q5=(3)|(2)|(5): 6(15.0/5.0)
															* Q5!=(3)|(2)|(5): 11(2.0/1.0)
												* Q25!=(4)|(2): 6(6.0/0.0)
										* Q16!=(5)|(4)|(2)
									* Q6=(2)
										* Q1=(3): 1(4.0/0.0)
										* Q1!=(3)
												* Q9=(3)|(2): 13(2.0/1.0)
												* Q9!=(3)|(2): 11(5.0/0.0)
									* Q6!=(2)
										* Q8=(2): 6(3.0/0.0)
										* Q8!=(2)
												* Q13=(4)|(2): 11(3.0/0.0)
												* Q13!=(4)|(2): 6(51.0/65.0)
							* difficulty!=(3)|(2)|(4)|(5)
					* attendance=(1)
								* Q28=(4)|(3)|(2): 6(9.0/3.0)
								* Q28!=(4)|(3)|(2): 1(3.0/4.0)
					* attendance!=(1)
							* Q4=(3)|(2)
							* Q7=(4): 1(5.0/1.0)
							* Q7!=(4)
									* Q10=(5)|(4): 6(4.0/1.0)
									* Q10!=(5)|(4)
									* Q6=(4): 13(2.0/0.0)
									* Q6!=(4)
													* Q7=(3)|(2)|(4)|(5)
											* Q16=(5): 11(2.0/0.0)
											* Q16!=(5)
														* Q18=(4)|(3)|(2)
															* Q9=(3)|(2)|(5)
														* attendance=(2): 11(2.0/1.0)
														* attendance!=(2): 1(26.0/56.0)
															* Q9!=(3)|(2)|(5): 1(3.0/0.0)
														* Q18!=(4)|(3)|(2): 13(2.0/0.0)
													* Q7!=(3)|(2)|(4)|(5): 6(2.0/0.0)
							* Q4!=(3)|(2)
							* Q6=(3)
								* Q5=(3): 1(1.0/1.0)
								* Q5!=(3): 11(4.0/0.0)
							* Q6!=(3)
								* Q5=(2): 6(5.0/0.0)
								* Q5!=(2)
									* Q12=(2)
											* Q8=(4)|(2): 13(2.0/0.0)
											* Q8!=(4)|(2): 11(4.0/0.0)
									* Q12!=(2)
										* Q26=(4)
											* Q6=(5): 6(5.0/1.0)
											* Q6!=(5)
														* Q21=(4)|(1)|(2): 6(17.0/28.0)
														* Q21!=(4)|(1)|(2): 11(3.0/0.0)
										* Q26!=(4)
												* Q9=(4)|(3)
												* Q13=(3): 6(4.0/0.0)
												* Q13!=(3)
														* Q23=(5)|(2): 6(2.0/1.0)
														* Q23!=(5)|(2): 13(3.0/0.0)
												* Q9!=(4)|(3)
													* Q3=(4)|(2): 1(2.0/1.0)
													* Q3!=(4)|(2): 6(36.0/58.0)
		* instr!=(2)|(3)
			* difficulty=(5)|(4)
				* Q1=(5)|(4)
					* Q9=(5)|(3)
						* Q6=(5)|(2)
						* nb.repeat=(3)
							* attendance=(4): 10(2.0/0.0)
							* attendance!=(4): 7(4.0/0.0)
						* nb.repeat!=(3)
							* attendance=(4): 10(5.0/6.0)
							* attendance!=(4): 2(17.0/7.0)
						* Q6!=(5)|(2)
								* attendance=(4)|(3)|(0): 7(6.0/0.0)
								* attendance!=(4)|(3)|(0): 2(1.0/1.0)
					* Q9!=(5)|(3)
							* attendance=(4)|(3)|(2)
							* Q20=(4)|(1)
									* Q22=(4)|(1)|(5)
								* nb.repeat=(3): 10(2.0/0.0)
								* nb.repeat!=(3)
											* Q27=(4)|(1)|(5): 2(11.0/15.0)
											* Q27!=(4)|(1)|(5): 10(2.0/0.0)
									* Q22!=(4)|(1)|(5): 7(2.0/0.0)
							* Q20!=(4)|(1)
							* Q13=(5): 7(1.0/1.0)
							* Q13!=(5): 10(8.0/0.0)
							* attendance!=(4)|(3)|(2)
						* Q7=(3): 10(3.0/0.0)
						* Q7!=(3)
									* Q5=(4)|(1)|(2)
									* nb.repeat=(3)|(2): 7(2.0/0.0)
									* nb.repeat!=(3)|(2)
												* attendance=(1)|(2)|(3)|(4): 7(3.0/3.0)
												* attendance!=(1)|(2)|(3)|(4): 10(2.0/0.0)
									* Q5!=(4)|(1)|(2): 7(4.0/0.0)
				* Q1!=(5)|(4)
					* Q8=(5)|(4)
					* Q4=(4): 7(5.0/2.0)
					* Q4!=(4): 7(21.0/0.0)
					* Q8!=(5)|(4)
						* Q22=(5)|(2)
						* attendance=(2)
							* Q1=(3): 2(1.0/1.0)
							* Q1!=(3): 2(4.0/0.0)
						* attendance!=(2)
									* Q3=(3)|(2)|(5)
									* Q10=(5)|(4): 2(2.0/0.0)
									* Q10!=(5)|(4)
										* attendance=(4)|(1): 10(5.0/0.0)
										* attendance!=(4)|(1)
										* Q1=(3): 10(2.0/0.0)
										* Q1!=(3)
														* attendance=(3)|(1)|(2)|(4): 2(2.0/1.0)
														* attendance!=(3)|(1)|(2)|(4): 7(1.0/1.0)
									* Q3!=(3)|(2)|(5)
											* attendance=(4)|(3)|(1)|(2): 7(3.0/0.0)
											* attendance!=(4)|(3)|(1)|(2): 7(1.0/1.0)
						* Q22!=(5)|(2)
						* Q6=(2)
							* nb.repeat=(2): 7(1.0/1.0)
							* nb.repeat!=(2): 7(10.0/0.0)
						* Q6!=(2)
								* nb.repeat=(3)|(2)
								* difficulty=(5)
									* Q13=(3): 2(1.0/1.0)
									* Q13!=(3): 7(3.0/0.0)
								* difficulty!=(5): 7(7.0/0.0)
								* nb.repeat!=(3)|(2)
									* Q14=(4)|(2)
									* Q20=(3): 10(3.0/1.0)
									* Q20!=(3): 7(6.0/0.0)
									* Q14!=(4)|(2)
										* Q13=(4)|(2): 2(3.0/0.0)
										* Q13!=(4)|(2)
													* difficulty=(5)|(1)|(2)|(3)
													* attendance=(3)|(2)|(1): 7(12.0/7.0)
													* attendance!=(3)|(2)|(1)
												* Q1=(3): 7(2.0/2.0)
												* Q1!=(3)
																* attendance=(4)|(1)|(2)|(3): 10(2.0/2.0)
																* attendance!=(4)|(1)|(2)|(3): 7(2.0/2.0)
													* difficulty!=(5)|(1)|(2)|(3)
											* Q1=(2): 10(2.0/0.0)
											* Q1!=(2)
													* Q3=(4)|(2): 7(2.0/0.0)
													* Q3!=(4)|(2)
															* attendance=(4)|(3)|(2)
																* Q23=(3)|(2)|(5): 10(7.0/4.0)
																* Q23!=(3)|(2)|(5)
																	* attendance=(3)|(0)|(1): 7(3.0/1.0)
																	* attendance!=(3)|(0)|(1): 10(2.0/1.0)
															* attendance!=(4)|(3)|(2)
																	* Q1=(3)|(2)|(4)|(5)
																		* attendance=(1)|(2)|(3)|(4): 7(2.0/1.0)
																		* attendance!=(1)|(2)|(3)|(4): 2(1.0/1.0)
																	* Q1!=(3)|(2)|(4)|(5): 2(1.0/1.0)
			* difficulty!=(5)|(4)
					* Q8=(4)|(3)|(2)
							* Q16=(5)|(4)|(3)|(2)
							* difficulty=(3)|(4)|(5)
								* attendance=(4)|(3)|(2): 10(85.0/18.0)
								* attendance!=(4)|(3)|(2)
							* Q11=(5): 2(1.0/1.0)
							* Q11!=(5): 10(39.0/18.0)
							* difficulty!=(3)|(4)|(5): 10(86.0/5.0)
							* Q16!=(5)|(4)|(3)|(2)
							* difficulty=(3)|(4)|(5): 7(3.0/0.0)
							* difficulty!=(3)|(4)|(5): 2(1.0/1.0)
					* Q8!=(4)|(3)|(2)
				* Q10=(3): 7(4.0/1.0)
				* Q10!=(3)
							* Q1=(5)|(4)|(2)
									* difficulty=(3)|(2)|(4)|(5)
									* Q14=(5)|(3)|(2)
								* Q10=(4): 2(2.0/0.0)
								* Q10!=(4)
									* Q13=(4): 2(1.0/1.0)
									* Q13!=(4)
										* Q2=(4): 10(6.0/0.0)
										* Q2!=(4): 10(41.0/22.0)
									* Q14!=(5)|(3)|(2): 10(6.0/0.0)
									* difficulty!=(3)|(2)|(4)|(5)
										* Q2=(5)|(4)|(2)|(3)
											* attendance=(4)|(3)|(2)|(1): 10(6.0/0.0)
											* attendance!=(4)|(3)|(2)|(1): 10(14.0/3.0)
										* Q2!=(5)|(4)|(2)|(3): 2(1.0/1.0)
							* Q1!=(5)|(4)|(2)
								* Q6=(5)|(3)|(2)
									* Q3=(5)|(2)|(3)
										* attendance=(4)|(0)|(2): 2(1.0/1.0)
										* attendance!=(4)|(0)|(2): 10(2.0/0.0)
									* Q3!=(5)|(2)|(3): 2(4.0/0.0)
								* Q6!=(5)|(3)|(2)
							* Q3=(5): 7(2.0/0.0)
							* Q3!=(5)
									* attendance=(4)|(3)
											* difficulty=(3)|(4)|(5)
													* attendance=(4)|(0)|(1)|(2): 10(3.0/0.0)
													* attendance!=(4)|(0)|(1)|(2): 10(2.0/1.0)
											* difficulty!=(3)|(4)|(5): 10(6.0/0.0)
									* attendance!=(4)|(3): 10(25.0/21.0)



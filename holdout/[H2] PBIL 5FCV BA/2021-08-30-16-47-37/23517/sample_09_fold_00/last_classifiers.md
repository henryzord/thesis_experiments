# J48

![](last_J48_graph.png)

# SimpleCart Decision Tree

attribute_14 < 0.480138

* attribute_9 < 0.262079: 0(3880.0/3239.0)

* attribute_9 >= 0.262079

*   * attribute_1 < 0.5303089999999999

*   *   * attribute_7 < 0.4503795

*   *   *   * attribute_14 < 0.042376: 1(230.0/190.0)

*   *   *   * attribute_14 >= 0.042376: 0(2229.0/1800.0)

*   *   * attribute_7 >= 0.4503795

*   *   *   * attribute_3 < 0.872253

*   *   *   *   * attribute_9 < 0.2893585: 1(101.0/62.0)

*   *   *   *   * attribute_9 >= 0.2893585: 0(2193.0/2044.0)

*   *   *   * attribute_3 >= 0.872253: 1(367.0/296.0)

*   * attribute_1 >= 0.5303089999999999

*   *   * attribute_16 < 0.039795: 0(363.0/266.0)

*   *   * attribute_16 >= 0.039795

*   *   *   * attribute_15 < 0.17037

*   *   *   *   * attribute_6 < 0.243924: 0(169.0/113.0)

*   *   *   *   * attribute_6 >= 0.243924

*   *   *   *   *   * attribute_3 < 0.8964705

*   *   *   *   *   *   * attribute_12 < 0.1201805: 0(713.0/573.0)

*   *   *   *   *   *   * attribute_12 >= 0.1201805

*   *   *   *   *   *   *   * attribute_14 < 0.0917915: 1(334.0/247.0)

*   *   *   *   *   *   *   * attribute_14 >= 0.0917915: 0(588.0/535.0)

*   *   *   *   *   * attribute_3 >= 0.8964705: 1(539.0/472.0)

*   *   *   * attribute_15 >= 0.17037: 1(4749.0/4417.0)

attribute_14 >= 0.480138

* attribute_1 < 0.645016

*   * attribute_13 < 0.539936

*   *   * attribute_4 < 0.0478: 0(212.0/165.0)

*   *   * attribute_4 >= 0.0478: 1(9337.0/8480.0)

*   * attribute_13 >= 0.539936

*   *   * attribute_2 < 0.145932: 0(626.0/489.0)

*   *   * attribute_2 >= 0.145932

*   *   *   * attribute_3 < 0.87196: 0(2531.0/2378.0)

*   *   *   * attribute_3 >= 0.87196: 1(732.0/634.0)

* attribute_1 >= 0.645016: 1(6042.0/5089.0)

# PART

Decision list:

conditions|predicted class
---|---
attribute_15 <= 0.254509 AND attribute_1 <= 0.852722 AND attribute_10 <= 0.839343| 0 (10217.0/4662.0)
attribute_10 > 0.21944 AND attribute_4 <= 0.956715 AND attribute_14 > 0.480138 AND attribute_1 > 0.645016 AND attribute_16 > 0.334079| 1 (7045.0/3116.0)
attribute_4 <= 0.956715 AND attribute_13 <= 0.501411| 1 (25631.0/12391.0)
attribute_4 <= 0.955107 AND attribute_2 > 0.113237 AND attribute_3 <= 0.845488| 0 (14665.0/7140.0)
attribute_2 > 0.140617| 1 (7827.0/3685.0)
| 0 (2039.0/920.0)


# JRip

Decision list:

conditions|predicted class
---|---
(attribute_14 <= 0.479924)|0 (30709.0/14890.0)
(attribute_1 <= 0.644501) and (attribute_13 >= 0.539987) and (attribute_16 <= 0.69864) and (attribute_11 <= 0.443985)|0 (2223.0/1002.0)
|1 (34492.0/16351.0)


# Decision Table

Non matches covered by Majority class

attribute_1|attribute_4|attribute_7|attribute_11|attribute_14|attribute_15|attribute_16|attribute_18|target
---|---|---|---|---|---|---|---|---
(0.648821-inf)|(0.297225-inf)|all|all|(0.480138-inf)|(0.254509-inf)|(0.271738-inf)|all|1
(-inf-0.648821]|(0.297225-inf)|all|all|(0.480138-inf)|(0.254509-inf)|(0.271738-inf)|all|1
(0.648821-inf)|(-inf-0.297225]|all|all|(0.480138-inf)|(0.254509-inf)|(0.271738-inf)|all|1
(-inf-0.648821]|(-inf-0.297225]|all|all|(0.480138-inf)|(0.254509-inf)|(0.271738-inf)|all|1
(0.648821-inf)|(0.297225-inf)|all|all|(-inf-0.480138]|(0.254509-inf)|(0.271738-inf)|all|1
(-inf-0.648821]|(0.297225-inf)|all|all|(-inf-0.480138]|(0.254509-inf)|(0.271738-inf)|all|0
(-inf-0.648821]|(0.297225-inf)|all|all|(0.480138-inf)|(-inf-0.254509]|(0.271738-inf)|all|0
(0.648821-inf)|(-inf-0.297225]|all|all|(-inf-0.480138]|(0.254509-inf)|(0.271738-inf)|all|1
(0.648821-inf)|(0.297225-inf)|all|all|(0.480138-inf)|(-inf-0.254509]|(0.271738-inf)|all|1
(-inf-0.648821]|(-inf-0.297225]|all|all|(-inf-0.480138]|(0.254509-inf)|(0.271738-inf)|all|1
(-inf-0.648821]|(-inf-0.297225]|all|all|(0.480138-inf)|(-inf-0.254509]|(0.271738-inf)|all|0
(0.648821-inf)|(-inf-0.297225]|all|all|(0.480138-inf)|(-inf-0.254509]|(0.271738-inf)|all|1
(-inf-0.648821]|(0.297225-inf)|all|all|(0.480138-inf)|(0.254509-inf)|(-inf-0.271738]|all|1
(0.648821-inf)|(0.297225-inf)|all|all|(0.480138-inf)|(0.254509-inf)|(-inf-0.271738]|all|0
(0.648821-inf)|(-inf-0.297225]|all|all|(0.480138-inf)|(0.254509-inf)|(-inf-0.271738]|all|1
(-inf-0.648821]|(-inf-0.297225]|all|all|(0.480138-inf)|(0.254509-inf)|(-inf-0.271738]|all|0
(-inf-0.648821]|(0.297225-inf)|all|all|(-inf-0.480138]|(-inf-0.254509]|(0.271738-inf)|all|0
(0.648821-inf)|(0.297225-inf)|all|all|(-inf-0.480138]|(-inf-0.254509]|(0.271738-inf)|all|0
(-inf-0.648821]|(0.297225-inf)|all|all|(-inf-0.480138]|(0.254509-inf)|(-inf-0.271738]|all|0
(0.648821-inf)|(0.297225-inf)|all|all|(-inf-0.480138]|(0.254509-inf)|(-inf-0.271738]|all|1
(-inf-0.648821]|(-inf-0.297225]|all|all|(-inf-0.480138]|(-inf-0.254509]|(0.271738-inf)|all|0
(0.648821-inf)|(-inf-0.297225]|all|all|(-inf-0.480138]|(-inf-0.254509]|(0.271738-inf)|all|0
(-inf-0.648821]|(0.297225-inf)|all|all|(0.480138-inf)|(-inf-0.254509]|(-inf-0.271738]|all|0
(0.648821-inf)|(0.297225-inf)|all|all|(0.480138-inf)|(-inf-0.254509]|(-inf-0.271738]|all|0
(0.648821-inf)|(-inf-0.297225]|all|all|(-inf-0.480138]|(0.254509-inf)|(-inf-0.271738]|all|0
(-inf-0.648821]|(-inf-0.297225]|all|all|(-inf-0.480138]|(0.254509-inf)|(-inf-0.271738]|all|0
(-inf-0.648821]|(-inf-0.297225]|all|all|(0.480138-inf)|(-inf-0.254509]|(-inf-0.271738]|all|0
(0.648821-inf)|(-inf-0.297225]|all|all|(0.480138-inf)|(-inf-0.254509]|(-inf-0.271738]|all|0
(0.648821-inf)|(0.297225-inf)|all|all|(-inf-0.480138]|(-inf-0.254509]|(-inf-0.271738]|all|1
(-inf-0.648821]|(0.297225-inf)|all|all|(-inf-0.480138]|(-inf-0.254509]|(-inf-0.271738]|all|0
(0.648821-inf)|(-inf-0.297225]|all|all|(-inf-0.480138]|(-inf-0.254509]|(-inf-0.271738]|all|0
(-inf-0.648821]|(-inf-0.297225]|all|all|(-inf-0.480138]|(-inf-0.254509]|(-inf-0.271738]|all|0



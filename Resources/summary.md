### Title: Assessing pre-training bias in Health data and estimating its impact on machine learning algorithms
### Author: DIEGO DIMER RODRIGUES


#### Bias types
- Measurement Bias: the use of wrong attributes to define some species experience.
- Omitted Attribute Bias: when attributes are left out of the model.
- Representation Bias: the under-representation of some groups due to a lack of information about individuals in these groups.
- Aggregation Bias: when factors that differentiate the individual from the majority of the population (gender or ethnicity) are not taken into consideration.
- Sampling Bias: non-random sampling of subgroups making the model not general enough to work for a new population.
- Longitudinal Data Fallacy: when researchers analyze temporal data and fail to use longitudinal analysis to track cohorts over time.
- Linking Bias: when network attributes are obtained from user connections, activities, or interactions that differ and misrepresent the true behavior of the users.

#### Bias sources:
- Historical: data may be collected at a point in time that does not reflect the current state of society.
- Representation: lack of representation.
- Measurement: comes from how data is measured.
- Aggregation: the mapping from inputs to labels can be inconsistent across different groups.
-  Evaluation: when the benchmark data for an algorithm does not represent the target population.

#### Pre-training metrics 
 - Class imbalance (CI): one one class is more reprented than the other. Ideal is close to zero.
> CI = (na − nd)/(na + nd)
> - na = number of values in facet a
> - nd = number of values in facet d
> - a = feature value that defines a demographic that bias favors
> - d = feature value that defines a demographic that bias disfavors
- Kullback-Leibler (KL) Divergence: measures the divergence between the label distributions for two facets, a and d, represented by Pa(y) and Pd(y).
It works when the output is not binary  but the protected attribute will always be binary (privileged and unprivileged classes).
-  Kolmogorov-Smirnov (KS): finds the most unbalanced label. This metric is equal to the maximum divergence between labels in the distribution for different facets of a dataset. 
-  Conditional Demographic Disparity in Labels (CDDL): provide information about the proportion of negative outcomes in a specific facet of a dataset.


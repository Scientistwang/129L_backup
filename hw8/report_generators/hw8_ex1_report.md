Zipeng Wang #3909934

Physics 129L HW8 Ex1 Report
===========================

Each background pdf has been normalized such that the area under the curve
from $mass = 100(GeV)$ to $mass = 200(GeV)$ is 1. Normalization constants are recorded
in the code "hw8_ex1.py".


Fit 1: Exponential
------------------

In this trial I used the background pdf $e^{-\alpha x}$.

Result: Analyzed by Minos, the fitted value for S is $S = 22.6^{+
8.12}_{-7.5}$. The fitted value for B is $B=177^{+15.1}_{-14.3}$. 

In my opinion, this fit is not very reasonable because there is large
disagreement between $mass = 180$ and $mass = 200$. It seems that the 
background is concave down instead of concave up. 

![Exponential Fit](./ex1_figs/Fit1_exponential.png)

Fit 2: Linear
------------------

In this trial I used a linear background pdf $-kx+b$.

Result: Analyzed by Minos, the fitted value for S is $S = 20.2^{+
7.99}_{-7.39}$. The fitted value for B is $B=180^{+15.2}_{-14.4}$. 

I think this is a good fit since there is no obvious deviation 
between data and fit, though the underlying physics in this 
problem might not be as simple as linear. However, based on
the information at hand, I think this is a good enough fit.

![Linear Fit](./ex1_figs/Fit2_linear.png)

Fit 3: Quadratic
------------------

In this trial I used a quadratic polynomial background pdf 
$-ax^2 +bx+c$.

Result: Analyzed by Minos, the fitted value for S is $S = 18.6^{+
8.81}_{-8.25}$. The fitted value for B is $B=181^{+15.8}_{-14.9}$. 

I think this fit is the best among the three fits I tried. It is
the closest to the binned data. Also, any pdf with some curvature
can be approximated by a quadratic, so I think this fit shows 
some general characteristics for all the concave down background
pdfs. 

![Quadratic Fit](./ex1_figs/Fit3_quadratic.png)

Final Result
------------
Overall, these three different fits gives the value of S ranging from $18.6$
to $22.6$. Therefore, I estimate that the systematic error here is $\pm 2$.

The value of S is $S = 18.6 \pm 8.52 \pm 2$.

+++
title = 'Probability in CS Notes'
date = '2025-12-31'
draft = false
tags = ["math", "programming", "python", "probability"]
+++

# Overview
Here are my notes for my introductory course in probability theory and its applications to computer science. Note this
is from my first course in probability, so the mathematical rigor is...well it's lacking. But I am taking/have taken a 
formal course in probability theory and my notes will be/are available under "probability theory notes". This course was
primarily application focused and as such the notes remain somewhat bare-bones. I have tried to supplement them with
examples(hopefully) that illustrate what the course focused on. I found that the variety and creativity of the 
problems that were designed for the course was the real value which was offered to me as a student.

# Chapter 1: Elements of Probability

### Quick Overview
Probability theory provides a formal framework for reasoning about uncertainty. In computer science, this allows us to model systems where the state of the world is not fully known or deterministic. This chapter establishes the fundamental axioms of probability, defines the rigorous "probability space," and builds up to crucial tools like Conditional Probability and Bayes' Theorem which are essential for machine learning and data analysis.

---

## 1.1 Definition of Probability Space

To speak precisely about probability, we must define the "experiment" and its associated sets. A probability space is defined by three elements: the sample space, the event space, and the probability measure.

**Definition 1.1.1 (Sample Space, $S$ or $\Omega$):**
The Sample Space is the set of all possible outcomes of an experiment.
* **Example (Coin Flip):** $S = \{Heads, Tails\}$.
* **Example (Die Roll):** $S = \{1, 2, 3, 4, 5, 6\}$.
* **Example (Continuous):** For the arrival time of a bus, $S = \{t \mid t \in \mathbb{R}, 0 \le t \le 30\}$.

**Definition 1.1.2 (Event, $E$):**
An Event is a subset of the sample space ($E \subseteq S$) to which we ascribe meaning. An event is said to "occur" if the outcome of the experiment is an element of $E$.
* **Example:** In a die roll, the event "roll is even" is $E = \{2, 4, 6\}$.
* **Example:** In a coin flip, the event "Heads" is $E = \{Heads\}$.

**Definition 1.1.3 (Probability Measure, $P$):**
A function $P$ that maps events to a real number between 0 and 1. It represents the belief or frequency that an event will occur.

---

## 1.2 Axioms and Identities

The entire edifice of probability theory is built upon three fundamental truths, known as the Kolmogorov Axioms.

**Axiom 1.2.1 (Non-negativity):**
For any event $E$, $0 \le P(E) \le 1$.
* Probabilities cannot be negative or exceed 1.

**Axiom 1.2.2 (Completeness):**
$P(S) = 1$
* The probability of the sample space (some outcome happening) is always 1.

**Axiom 1.2.3 (Additivity of Mutually Exclusive Events):**
If events $E$ and $F$ are mutually exclusive (i.e., $E \cap F = \emptyset$), then:
$$P(E \cup F) = P(E) + P(F)$$
This extends to any countable sequence of disjoint events.

### Useful Identities
From these axioms, we can derive several useful properties:
* **Complement Rule:** $P(E^C) = 1 - P(E)$. This is often easier to calculate than $P(E)$ directly.
* **Inclusion-Exclusion Principle:** For any two events $E$ and $F$ (not necessarily disjoint):
    $$P(E \cup F) = P(E) + P(F) - P(E \cap F)$$
    This corrects for the double-counting of outcomes that are in both $E$ and $F$.

### Example: Elephant Gender (Frequency Definition)
To understand probability as a frequency, consider the probability that a newborn elephant is male.
* **Experiment**: A single elephant birth.
* **Data**: Out of 3,070 births, 2,180 were male.
* **Calculation**:
    $$P(Male) \approx \lim_{n \to \infty} \frac{2180}{3070} \approx 0.71$$
* **Insight**: Probabilities often come from limit frequencies of real-world data rather than theoretical equally likely outcomes.

---

## 1.3 Conditional Probability

Conditional probability allows us to update our beliefs when new evidence is available. It is the probability of an event $E$ occurring given that we know event $F$ has already occurred.

**Definition 1.3.1 (Conditional Probability):**
$$P(E|F) = \frac{P(E \cap F)}{P(F)}$$
This is valid only when $P(F) > 0$. Intuitively, we are restricting our sample space to $F$ and checking what fraction of $F$ is also in $E$.

**Theorem 1.3.2 (The Chain Rule):**
Rearranging the definition gives us a way to calculate the probability of "AND":
$$P(E \cap F) = P(E|F)P(F)$$
This generalizes to $n$ events: $P(E_1 \cap \dots \cap E_n) = P(E_1)P(E_2|E_1)\dots P(E_n|E_1\dots E_{n-1})$.

### Example: Netflix Recommendation
Suppose we want to know the probability a user watches a specific movie ($E$) given they watched another movie ($F$).
* **Data**: $P(E) \approx 0.02$ (Prior probability of watching the movie).
* **Observation**: If we know the user watched a related movie (e.g., *Amélie*), the conditional probability $P(E|F)$ might jump significantly (e.g., to 0.42).
* **Interpretation**: Knowing the user's history ($F$) reduces the sample space to "users who watched $F$", where $E$ is much more common than in the general population. This is the basis of recommendation engines.

---

## 1.4 Law of Total Probability

The Law of Total Probability (LOTP) is a strategy for calculating the probability of a complex event $E$ by breaking it down into scenarios based on a set of mutually exclusive background events $B_i$.

**Theorem 1.4.1 (Law of Total Probability):**
If $B_1, B_2, \dots, B_n$ are mutually exclusive and exhaustive events (their union is $S$), then for any event $E$:
$$P(E) = \sum_{i=1}^n P(E|B_i)P(B_i)$$
This is useful when $P(E)$ is hard to calculate directly, but easy to calculate if we know the specific context $B_i$.

### Example: Medical Risk
Calculate the probability a random person tests positive for a disease ($E$). We can split the population into three risk groups ($B_i$):
1.  **High Risk ($B_1$)**: High exposure.
2.  **Medium Risk ($B_2$)**: Family history.
3.  **Low Risk ($B_3$)**: General population.
$$P(E) = P(E|B_1)P(B_1) + P(E|B_2)P(B_2) + P(E|B_3)P(B_3)$$
We can easily estimate $P(E|B_i)$ (likelihood of testing positive given risk level) and $P(B_i)$ (size of risk group) to find the total probability.

---

## 1.5 Bayes' Theorem

Bayes' Theorem is the cornerstone of inference. It provides a way to reverse conditional probabilities: turning $P(Evidence|Belief)$ into $P(Belief|Evidence)$.

**Theorem 1.5.1 (Bayes' Theorem):**
$$P(B|E) = \frac{P(E|B)P(B)}{P(E)}$$
Where:
* $P(B|E)$ is the **Posterior**: Belief after seeing evidence.
* $P(B)$ is the **Prior**: Initial belief.
* $P(E|B)$ is the **Likelihood**: Probability of evidence assuming belief is true.
* $P(E)$ is the **Normalization Constant**: Total probability of the evidence.

### Example: Mammogram Test
We want to know the probability a patient has cancer ($I$) given a positive mammogram test ($E$).
* **Given**:
    * $P(I) = 0.13$ (Prior probability of illness).
    * $P(E|I) = 0.92$ (Sensitivity: True Positive rate).
    * $P(E|I^C) = 0.10$ (False Positive rate).
* **Application**:
    $$P(I | E) = \frac{P(E | I)P(I)}{P(E | I)P(I) + P(E | I^C)P(I^C)}$$
    $$= \frac{0.92 \cdot 0.13}{(0.92 \cdot 0.13) + (0.10 \cdot (1 - 0.13))} \approx 0.58$$
* **Result**: Even with a positive test, the probability of having cancer is only ~58% because the false positive rate acts on a much larger population of healthy people ($I^C$).

---

## 1.6 Independence

Independence simplifies probabilistic models significantly. Two events are independent if knowing one gives no information about the other.

**Definition 1.6.1 (Independence):**
Events $E$ and $F$ are independent if and only if:
$$P(E \cap F) = P(E)P(F)$$
Equivalently, $P(E|F) = P(E)$.

### Example: Parallel Networks
Consider a network path from A to B that works if *at least one* of $n$ parallel routers works.
* Let $F_i$ be the event that router $i$ fails.
* Assume routers fail independently.
* $P(\text{All fail}) = P(F_1 \cap F_2 \dots \cap F_n) = \prod P(F_i)$.
* $P(\text{System works}) = 1 - \prod P(F_i)$.
Independence allows us to simply multiply the failure probabilities to solve the complex system reliability problem.

---

## 1.7 Combinatorics

Counting is a fundamental skill for calculating probabilities, particularly for problems involving equally likely outcomes where $P(E) = \frac{|E|}{|S|}$. We often use shortcuts to count the size of the sample space ($|S|$) and the event space ($|E|$) without listing every element.

**Definition 1.7.1 (Permutations):**
A permutation is an ordered arrangement of objects.
* **Distinct Objects:** The number of ways to order $n$ distinct objects is $n! = n \times (n-1) \times \dots \times 1$.
* **Indistinct Objects:** If there are $n$ objects where $n_1$ are indistinguishable (type 1), $n_2$ are indistinguishable (type 2), etc., the number of unique orderings is:
    $$\frac{n!}{n_1! n_2! \dots n_r!}$$
    This formula corrects for the over-counting that occurs when we treat identical items as distinct.

**Definition 1.7.2 (Combinations):**
A combination is an unordered selection of $r$ objects from a set of $n$ distinct objects. The order of selection does not matter.
$$\binom{n}{r} = \frac{n!}{r!(n-r)!}$$
This is read as "$n$ choose $r$".

### Example: Binary String Permutations
A classic application of combinatorics in computer science is counting binary strings with a fixed number of set bits.

* **Problem:** How many distinct bit strings of length 5 can be formed using exactly three 0's and two 1's?
* **Naive Approach:** If we treated every digit as unique (e.g., $0_a, 0_b, 0_c, 1_a, 1_b$), there would be $5! = 120$ permutations.
* **Correction:** However, the three 0's are indistinguishable, as are the two 1's.
    * We have over-counted the arrangement of 0's by $3! = 6$ times.
    * We have over-counted the arrangement of 1's by $2! = 2$ times.
* **Calculation:** Using the formula for permutations of indistinct objects:
    $$\text{Total} = \frac{5!}{3! \cdot 2!} = \frac{120}{6 \cdot 2} = 10$$
* **Verification:** The 10 strings are: 00011, 00101, 00110, 01001, 01010, 01100, 10001, 10010, 10100, 11000.

# Chapter 2: Random Variables

### Quick Overview
While Chapter 1 dealt with events (subsets of the sample space), Chapter 2 introduces **Random Variables**—a powerful abstraction that allows us to reason about outcomes numerically. Instead of working with abstract outcomes like "Heads, Heads, Tails", we work with variables like $X=2$ (the number of heads). This chapter covers the definitions of discrete and continuous variables, the functions used to describe their probabilities (PMF, PDF, CDF), and summary statistics like Expectation and Variance.

---

## 2.1 Definition and Basic Concepts

A Random Variable (RV) is, confusingly, not a variable but a function. It maps outcomes from the sample space to real numbers.

**Definition 2.1.1 (Random Variable):**
Given a probability space $(\Omega, \mathcal{F}, P)$, a random variable $X$ is a function $X: \Omega \to \mathbb{R}$.
* **Discrete Random Variable:** $X$ can take on a finite or countably infinite number of values (e.g., integers).
* **Continuous Random Variable:** $X$ can take on an uncountably infinite number of values (e.g., real numbers in an interval).

### Example: The Coin Flip
Consider an experiment where we flip 10 coins.
* **Outcomes ($\omega$):** Sequences like $\langle H, H, T, \dots \rangle$.
* **Random Variable ($X$):** Let $X(\omega)$ be the number of heads in the sequence.
* **Value:** If $\omega$ has 4 heads, then $X(\omega) = 4$.
We usually denote the random variable with a capital letter ($X$) and the value it takes with a lowercase letter ($x$).

---

## 2.2 Cumulative Distribution Functions (CDF)

The CDF is a unifying concept that applies to both discrete and continuous variables. It describes the probability that a variable $X$ is less than or equal to a value $x$.

**Definition 2.2.1 (CDF):**
$$F_X(x) \triangleq P(X \le x)$$

**Properties:**
1.  **Bounds:** $0 \le F_X(x) \le 1$.
2.  **Monotonicity:** If $x \le y$, then $F_X(x) \le F_X(y)$.
3.  **Limits:** $\lim_{x \to -\infty} F_X(x) = 0$ and $\lim_{x \to \infty} F_X(x) = 1$.

---

## 2.3 Discrete Random Variables: The PMF

For discrete variables, we describe probability using the Probability Mass Function (PMF). It gives the probability of the variable taking on a specific value.

**Definition 2.3.1 (Probability Mass Function):**
$$p_X(x) \triangleq P(X = x)$$

**Properties:**
* $0 \le p_X(x) \le 1$.
* $\sum_{x \in Val(X)} p_X(x) = 1$ (The sum of probabilities for all possible values must be 1).

### Example: Sum of Two Dice
Let $Y$ be the sum of two 6-sided dice. The value space is $Val(Y) = \{2, 3, \dots, 12\}$.
* $P(Y=2) = 1/36$ (Only outcome (1,1))
* $P(Y=7) = 6/36 = 1/6$ (Outcomes (1,6), (2,5), (3,4), etc.)
This mapping from values ($2 \dots 12$) to probabilities is the PMF of $Y$.


---

## 2.4 Continuous Random Variables: The PDF

For continuous variables (like time or height), the probability of hitting an *exact* value is 0 (e.g., $P(X=2.0000\dots) = 0$). Instead, we measure the probability of falling within a range using the Probability Density Function (PDF).

**Definition 2.4.1 (Probability Density Function):**
The PDF $f_X(x)$ is the derivative of the CDF:
$$f_X(x) \triangleq \frac{dF_X(x)}{dx}$$

**Calculating Probabilities:**
To find the probability that $X$ falls between $a$ and $b$, we integrate the PDF:
$$P(a \le X \le b) = \int_a^b f_X(x) dx$$

**Important Note:** The value $f_X(x)$ is **not** a probability; it is a probability *density*. It can be greater than 1, but the integral over the entire domain must equal 1.

---

## 2.5 Expectation and Variance

We often want to summarize a random variable with a single number representing its "center" or its "spread".

### Expectation (Mean)
The Expectation, $E[X]$, is the weighted average of the values $X$ can take.
* **Discrete:** $E[X] = \sum_{x} x \cdot p_X(x)$
* **Continuous:** $E[X] = \int_{-\infty}^{\infty} x \cdot f_X(x) dx$

**Linearity of Expectation:**
For any constants $a, b$:
$$E[aX + b] = aE[X] + b$$
$$E[X + Y] = E[X] + E[Y]$$
This holds even if $X$ and $Y$ are dependent.

### Variance
The Variance, $Var(X)$, measures how spread out the distribution is from the mean.
$$Var(X) \triangleq E[(X - E[X])^2]$$
**Computational Formula:**
$$Var(X) = E[X^2] - (E[X])^2$$
* **Standard Deviation:** $Std(X) = \sqrt{Var(X)}$ (Same units as $X$).

---

## 2.6 Common Distributions

Probabilities in computer science often follow standard patterns. We call these parametric distributions.

### Discrete Distributions

**1. Bernoulli($p$)**
* **Scenario:** A single coin flip (Success/Failure).
* **PMF:** $P(X=1) = p, P(X=0) = 1-p$.
* **Mean:** $p$
* **Var:** $p(1-p)$.

**2. Binomial($n, p$)**
* **Scenario:** The number of successes in $n$ independent Bernoulli trials.
* **PMF:** $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$.
* **Mean:** $np$
* **Var:** $np(1-p)$
* **Example:** Number of heads in 10 coin flips.

**3. Geometric($p$)**
* **Scenario:** Number of independent trials *until* the first success.
* **PMF:** $P(X=k) = (1-p)^{k-1}p$.
* **Mean:** $1/p$
* **Var:** $(1-p)/p^2$.

**4. Poisson($\lambda$)**
* **Scenario:** Number of rare events occurring in a fixed interval (e.g., server requests per minute).
* **PMF:** $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$.
* **Mean:** $\lambda$
* **Var:** $\lambda$.


### Continuous Distributions

**1. Uniform($a, b$)**
* **Scenario:** All values between $a$ and $b$ are equally likely.
* **PDF:** $f(x) = \frac{1}{b-a}$ for $x \in [a, b]$.
* **Mean:** $\frac{a+b}{2}$
* **Var:** $\frac{(b-a)^2}{12}$.

**2. Exponential($\lambda$)**
* **Scenario:** Time *until* the next event in a Poisson process (memoryless).
* **PDF:** $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$.
* **Mean:** $1/\lambda$
* **Var:** $1/\lambda^2$.

**3. Normal / Gaussian($\mu, \sigma^2$)**
* **Scenario:** The "Bell Curve". Central Limit Theorem states sums of RVs tend toward this.
* **PDF:** $f(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$.
* **Mean:** $\mu$
* **Var:** $\sigma^2$.

---

## 2.7 Binomial Approximation

Calculating exact probabilities for a Binomial distribution $Bin(n, p)$ involves factorials ($n!$), which become computationally intractable for large $n$. In these cases, we approximate the Binomial using either the Poisson or the Normal distribution, depending on the parameters.

### 1. Poisson Approximation
The Poisson distribution is a limiting case of the Binomial where $n \to \infty$ and $p \to 0$ such that $\lambda = np$ remains constant.
* **When to use:** $n$ is large ($>20$) and $p$ is small ($<0.05$).
* **Method:** Set $\lambda = np$ and use $X \sim Poi(\lambda)$.
* **Example:** Sending a bit string of length $n=10^4$ with corruption probability $p=10^{-6}$.
    * Exact: $Bin(10^4, 10^{-6})$. Hard to compute.
    * Approx: $\lambda = 10^4 \cdot 10^{-6} = 0.01$. Use $P(X=k) = \frac{e^{-0.01}0.01^k}{k!}$.

### 2. Normal Approximation
For "moderate" probabilities, the Binomial distribution becomes symmetric and bell-shaped, resembling the Normal distribution.
* **When to use:** $n$ is large and the variance is sufficient: $np(1-p) > 10$.
* **Method:** Approximate $X \sim Bin(n, p)$ with $Y \sim N(\mu, \sigma^2)$ where:
    * $\mu = np$
    * $\sigma^2 = np(1-p)$

**Continuity Correction:**
Since we are approximating a discrete variable (integer steps) with a continuous one (smooth curve), we must adjust the boundaries by 0.5 to capture the "width" of the integer.
* **Discrete:** $P(X = k)$ $\to$ **Continuous:** $P(k - 0.5 < Y < k + 0.5)$
* **Discrete:** $P(X \ge k)$ $\to$ **Continuous:** $P(Y > k - 0.5)$
* **Discrete:** $P(X \le k)$ $\to$ **Continuous:** $P(Y < k + 0.5)$

### Example: Voting
Suppose $n=100$ people vote, with $p=0.5$ for a candidate. What is the probability at least 55 people vote for them ($P(X \ge 55)$)?
1.  **Check:** $np(1-p) = 100(0.5)(0.5) = 25 > 10$. Normal approximation is valid.
2.  **Parameters:** $\mu = 50$, $\sigma^2 = 25 \Rightarrow \sigma = 5$.
3.  **Correction:** We want $P(X \ge 55)$, which covers the integer 55 and up. The continuous range starts at $54.5$.
4.  **Calculation:**
    $$P(X \ge 55) \approx P(Y > 54.5) = 1 - \Phi\left(\frac{54.5 - 50}{5}\right) = 1 - \Phi(0.9)$$
    This is much faster to compute than summing binomial coefficients from 55 to 100.

# Chapter 3: Probabilistic Models

### Quick Overview
Real-world systems rarely involve just one isolated variable. To model complex phenomena—like predicting a disease based on multiple symptoms or determining the authorship of an anonymous text—we need to handle multiple random variables simultaneously. This chapter introduces **Joint Distributions**, which describe how variables interact, and **Probabilistic Inference**, the process of using observed variables to guess hidden ones. We conclude with **Bayesian Networks**, a graphical structure used to represent complex dependencies efficiently.

---

## 3.1 Joint Distributions

To model the relationship between two random variables $X$ and $Y$, we use a joint distribution.

### Discrete: Joint PMF
The Joint Probability Mass Function gives the probability that $X$ takes value $x$ *and* $Y$ takes value $y$ simultaneously.
$$p_{X,Y}(x, y) = P(X=x, Y=y)$$
* **Constraint:** $\sum_x \sum_y p_{X,Y}(x, y) = 1$.

### Continuous: Joint PDF
For continuous variables, we use a 3D surface $f_{X,Y}(x, y)$. The probability is the volume under this surface for a specific region.
$$P(a \le X \le b, c \le Y \le d) = \int_a^b \int_c^d f_{X,Y}(x, y) \, dy \, dx$$
* **Constraint:** $\int_{-\infty}^\infty \int_{-\infty}^\infty f_{X,Y}(x, y) \, dx \, dy = 1$.

---

## 3.2 Marginalization

Often we have a joint distribution (beliefs about everything) but only care about one specific variable. **Marginalization** is the process of "summing out" the variables we don't care about.

**Discrete Marginalization:**
To find the probability of just $X$ (the marginal PMF), sum the joint probabilities over all possible values of $Y$:
$$p_X(x) = \sum_y p_{X,Y}(x, y)$$

**Continuous Marginalization:**
$$f_X(x) = \int_{-\infty}^\infty f_{X,Y}(x, y) \, dy$$

### Example: Robot Localization
Imagine a robot on a 2D grid. The joint distribution $P(X, Y)$ is a heatmap of its likely location. If we only care about how far North it is ($Y$), we sum up the probabilities across all $X$ columns to get the marginal distribution $P(Y)$.

---

## 3.3 Conditional Distributions and Inference

This is the core task of "Inference": updating our belief about a hidden variable $X$ given that we have observed evidence $Y=y$.

**Definition 3.3.1 (Conditional PMF/PDF):**
$$P(X=x | Y=y) = \frac{P(X=x, Y=y)}{P(Y=y)}$$
Using marginalization for the denominator, we get the standard inference equation:
$$P(X=x | Y=y) = \frac{p_{X,Y}(x, y)}{\sum_{x'} p_{X,Y}(x', y)}$$

### Example: Medical Inference
Consider a simple model with a disease $D$ (0 or 1) and a symptom $S$ (0 or 1).
* **Joint Table $P(D, S)$**:
    * $P(D=0, S=0) = 0.80$ (Healthy, No Symptom)
    * $P(D=0, S=1) = 0.10$ (Healthy, Symptom - False Positive)
    * $P(D=1, S=0) = 0.01$ (Sick, No Symptom - False Negative)
    * $P(D=1, S=1) = 0.09$ (Sick, Symptom)

**Inference Task:** We observe a patient has the symptom ($S=1$). What is the probability they are sick ($D=1$)?
1.  **Filter:** Look only at the row where $S=1$.
2.  **Normalize:**
    $$P(D=1 | S=1) = \frac{0.09}{0.09 + 0.10} = \frac{0.09}{0.19} \approx 0.47$$
Despite having the symptom, there is less than a 50% chance they are sick because the "Healthy+Symptom" group is larger than the "Sick+Symptom" group.

---

## 3.4 The Multinomial Distribution

The Multinomial distribution generalizes the Binomial distribution. Instead of 2 outcomes (Heads/Tails), we have $k$ outcomes (e.g., rolling a die, classifying text into categories).

**Definition 3.4.1 (Multinomial):**
Consider $n$ independent trials, where each trial results in one of $m$ outcomes with probabilities $p_1, \dots, p_m$ (where $\sum p_i = 1$). Let $X_i$ be the count of outcome $i$.
$$P(X_1=c_1, \dots, X_m=c_m) = \frac{n!}{c_1! c_2! \dots c_m!} p_1^{c_1} p_2^{c_2} \dots p_m^{c_m}$$

### Example: The Federalist Papers
This is a classic historical application of probabilistic modeling.
* **Context:** The *Federalist Papers* were written by Hamilton, Madison, and Jay to persuade New York to ratify the Constitution. Authorship of 12 essays was disputed between Hamilton and Madison.
* **Model:** We model the writing style as a "Bag of Words." We assume that every word an author writes is drawn independently from a Multinomial distribution specific to that author.
    * **Hamilton's Parameters ($P_H$):** Probabilities for words like "upon", "while", "there".
    * **Madison's Parameters ($P_M$):** Probabilities for the same words (Madison preferred "whilst" over "while").
* **Inference:**
    Given an unknown essay with word counts $X = \{c_{upon}, c_{while}, \dots\}$, we calculate the likelihood of that text under both models:
    $$L(Hamilton) = P(X | \text{Author}=H) = \text{Multinomial}(X; P_H)$$
    $$L(Madison) = P(X | \text{Author}=M) = \text{Multinomial}(X; P_M)$$
* **Result:** By comparing these likelihoods (usually using Log-Likelihoods to avoid underflow), statisticians Mosteller and Wallace (1964) determined that all 12 disputed papers were almost certainly written by Madison.

---

## 3.5 Independence and Covariance

**Independence:**
Two variables are independent if knowing one gives no information about the other.
$$P(X, Y) = P(X)P(Y)$$
$$P(X | Y) = P(X)$$

**Covariance:**
Covariance measures how much two variables vary *together*.
$$Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$$
* **Positive:** As $X$ increases, $Y$ tends to increase.
* **Negative:** As $X$ increases, $Y$ tends to decrease.
* **Zero:** No linear relationship (though they could still be dependent).

**Correlation ($\rho$):**
A normalized version of covariance between -1 and 1.
$$\rho(X, Y) = \frac{Cov(X, Y)}{\sigma_X \sigma_Y}$$

---

## 3.6 Bayesian Networks

A Bayesian Network is a directed acyclic graph (DAG) that represents the dependencies between random variables. It allows us to specify a complex joint distribution using simple local conditional probabilities.

### Structure
* **Nodes:** Random variables.
* **Edges:** Direct influence ($X \to Y$ means $X$ influences $Y$).
* **Factorization:** The joint probability of all variables is the product of each variable conditioned on its parents.
    $$P(X_1, \dots, X_n) = \prod_{i=1}^n P(X_i | \text{Parents}(X_i))$$

### Example: WebMD Symptom Checker
Consider modeling diseases and symptoms. Specifying the full joint table for 4 variables would require $2^4 - 1 = 15$ probabilities. A Bayes Net simplifies this.

**Nodes:**
1.  **Flu ($F$):** (0/1)
2.  **Allergy ($A$):** (0/1)
3.  **Sinus Infection ($S$):** (0/1)
4.  **Headache ($H$):** (0/1)

**Graph:**
* Flu causes Sinus Infection ($F \to S$).
* Allergy causes Sinus Infection ($A \to S$).
* Sinus Infection causes Headache ($S \to H$).



**Joint Probability Calculation:**
To find the probability of a specific state (e.g., You have Flu, No Allergy, Sinus Infection, and Headache), we just multiply the local probabilities:
$$P(F, \neg A, S, H) = P(F) \cdot P(\neg A) \cdot P(S | F, \neg A) \cdot P(H | S)$$
This drastically reduces the number of parameters we need to learn.

### Inference in Bayes Nets
Inference asks: "Given that I have a Headache ($H=1$), what is the probability I have the Flu ($F=1$)?"
$$P(F=1 | H=1) = \frac{P(F=1, H=1)}{P(H=1)}$$
This often involves "summing out" the intermediate variables (like Sinus Infection).

**Concept: Explaining Away**
One unique property of Bayes Nets is "Explaining Away."
* If we know you have a **Sinus Infection**, observing that you have the **Flu** actually *decreases* the probability that you have an **Allergy**.
* Why? Because the Flu "explains" the Sinus Infection, making the Allergy redundant/less likely as a cause. This captures human-like reasoning patterns that simple correlation cannot.

---

## 3.7 Extended Example: Bridge Card Game

Bridge is a cooperative game where players must estimate the strength of their partner's hand based on incomplete information. This scenario provides excellent examples of Expectation, Approximations, and Joint Inference.

**Hand Strength Metric:**
In Bridge, the "strength" of a hand ($H$) is often calculated by a weighted sum of high cards:
* Ace = 4, King = 3, Queen = 2, Jack = 1.
* $H = 4(num aces) + 3(num kings) + 2(num queens) + 1(num jacks)$.

### 1. Expectation of Hand Strength
We can calculate the expected strength of a randomly dealt 13-card hand using Linearity of Expectation.
* Let $X_i$ be the point value of the $i$-th card in your hand.
* The probability of drawing a specific honor card (like an Ace) is $4/52$.
* $E[X_i] = 4(\frac{4}{52}) + 3(\frac{4}{52}) + 2(\frac{4}{52}) + 1(\frac{4}{52}) + 0(\dots) = \frac{10}{13}$.
* Since you hold 13 cards:
    $$E[H] = E[\sum_{i=1}^{13} X_i] = \sum E[X_i] = 13 \cdot \frac{10}{13} = 10$$
* **Insight:** The average hand strength is exactly 10 points.

### 2. Poisson Approximation
Interestingly, the distribution of hand strength closely resembles a Poisson distribution with $\lambda = 10$.
* Why? If we view drawing high cards as "rare events" occurring over the "time" of dealing 13 cards, the Poisson limit applies.
* This approximation simplifies calculations: $P(H=k) \approx \frac{10^k e^{-10}}{k!}$.

### 3. Inference with Joint Distributions
The critical part of Bridge is the dependency between your hand ($H_Y$) and your partner's hand ($H_P$).
* **Independence?** No. There is a fixed pool of high cards. If your hand is very strong (you have many Aces/Kings), your partner's hand is likely weaker.
* **Conditioning:** If you observe that your partner makes a bid indicating a strong hand (e.g., $H_P > 15$), you must update the probability distribution of your own hand $P(H_Y | H_P > 15)$.
* **Result:** This shifts the expected value of your hand $E[H_Y | H_P > 15]$ to be significantly lower than the prior average of 10. This negative correlation is modeled via the joint distribution $P(H_Y, H_P)$.

---

## 3.8 Extended Example: Bayesian Carbon Dating

This example combines exponential decay, binomial probabilities, and Bayesian inference to determine the age of an artifact.

**The Setup:**
* Living things maintain a constant level of Carbon-14 (C14). When they die, C14 decays.
* The time $T$ for a single C14 molecule to decay follows an Exponential distribution: $T \sim Exp(\lambda = 1/8267)$, where 8267 is the mean lifetime in years.

**The Likelihood (Forward Probability):**
Suppose an artifact started with $n=1000$ molecules of C14. We want to find the probability that exactly $m$ molecules remain after $i$ years.
1.  **Probability of Survival:** For one molecule, the probability it survives $i$ years is $p_i = P(T > i) = e^{-\lambda i}$.
2.  **Binomial Model:** Since molecules decay independently, the count of remaining molecules $M$ follows a Binomial distribution:
    $$M | \text{Age}=i \sim Bin(n, p_i)$$
    $$P(M=m | \text{Age}=i) = \binom{n}{m} (p_i)^m (1-p_i)^{n-m}$$

**The Inference (Inverse Probability):**
We observe a measurement of $m=900$ remaining molecules. We want to infer the Age ($A$) of the artifact.
* **Prior:** Assume the artifact is between 0 and 20,000 years old, with a Uniform prior: $P(A=i) = \frac{1}{20000}$.
* **Bayes' Theorem:**
    $$P(A=i | M=900) = \frac{P(M=900 | A=i) P(A=i)}{\sum_{j} P(M=900 | A=j) P(A=j)}$$
* **Calculation:** We compute the likelihood $P(M=900 | A=i)$ for every possible year $i$. The year that maximizes this probability (Maximum A Posteriori) or the weighted average (Expectation) gives us the best estimate of the artifact's age.
* **Visual Intuition:** This creates a "belief distribution" over the age, likely peaking around the year where the expected decay matches the observed 10% loss.

# Chapter 4: Uncertainty Theory

### Quick Overview
In the real world, we rarely know the exact probabilities of events. We work with approximations, limited data, and unknown distributions. This chapter bridges the gap between theoretical probability and applied data science, focusing on how we quantify "surprise" (Information Theory), how we model our own ignorance (Beta Distribution), and how we make decisions when we aren't sure (Thompson Sampling).

---

## 4.1 Sums of Random Variables

A common pattern in probability is aggregating data: summing scores, averaging errors, or counting events. We need tools to understand how the *shape* of randomness changes when we combine variables.

### Convolution
**The Problem:** You have two independent random variables, $X$ and $Y$. What is the distribution of their sum, $Z = X + Y$?

**The Intuition:**
Think of this as a "Reverse Decomposition." If the total is $Z=5$, how could that have happened? Maybe $X=1$ and $Y=4$, or $X=2$ and $Y=3$. Since $X$ and $Y$ are independent, we calculate the probability of *every possible pair* that sums to 5 and add them up.

**Definition 4.1.1 (Convolution):**
* **Discrete:** $P(Z=n) = \sum_{k} P(X=k) \cdot P(Y=n-k)$
* **Continuous:** $f_Z(z) = \int_{-\infty}^{\infty} f_X(x) \cdot f_Y(z-x) \, dx$

### The Central Limit Theorem (CLT)
**The Intuition (The Law of Errors):**
Why is the Normal distribution (Bell Curve) so common in nature? Because most natural phenomena (like human height or measurement error) are the sum of many small, independent factors.
* **Averaging Kills Extremes:** If you sum up enough independent random variables, the "weirdness" of their individual distributions cancels out. The outliers on the left cancel the outliers on the right, leaving a symmetric, bell-shaped mound in the middle.

**Theorem 4.1.2 (Central Limit Theorem):**
Let $X_1, \dots, X_n$ be i.i.d. random variables with mean $\mu$ and variance $\sigma^2$. As $n$ gets large, their sum behaves like a Normal distribution:
$$\sum X_i \sim N(n\mu, n\sigma^2)$$



---

## 4.2 The Beta Distribution

We often need to estimate a probability $p$ (e.g., "how likely is this coin to show Heads?"). But before we flip it, $p$ itself is unknown. The **Beta Distribution** models the "Probability of the Probability."

**Definition 4.2.1 (Beta Distribution):**
The Beta distribution is defined on $[0, 1]$ and represents our *belief* about an unknown probability $p$.
$$X \sim Beta(\alpha, \beta)$$

**Intuition: The "Shape of Belief"**
* **Flat ($Beta(1,1)$):** "I know nothing." Every probability from 0% to 100% is equally likely.
* **Broad Bump ($Beta(3, 3)$):** "I suspect it's fair, but I'm not sure." The curve peaks at 0.5 but is wide.
* **Sharp Peak ($Beta(100, 100)$):** "I am confident it is fair." The curve is a spike at 0.5.

**The Update Rule:**
If you start with a prior belief $Beta(\alpha, \beta)$ and observe $s$ successes and $f$ failures, your new belief is simply:
$$Beta(\alpha + s, \beta + f)$$
This allows us to mathematically transition from "Ignorance" to "Confidence" as we gather data.

---

## 4.3 Algorithmic Analysis (Probabilistic)

Traditional analysis asks "What is the worst that could happen?" Probabilistic analysis asks "What is likely to happen?"

**Intuition:**
Many algorithms rely on randomness to avoid worst-case scenarios. By analyzing the *expectation*, we can show that "bad" runs are incredibly rare.

**Example: Hash Table Collisions**
* **Scenario:** Hashing $n$ items into $m$ buckets.
* **Intuition:** We don't need to know exactly where every item goes. We just need to know that for any *pair* of items, the chance they collide is $1/m$. Linearity of Expectation allows us to sum these small probabilities to find the total expected collisions, ignoring complex dependencies between items.

---

## 4.4 Bootstrapping

**The Problem:** You have a small dataset and calculated a statistic (like the Median). You want to know how accurate that Median is, but there is no simple formula for "Standard Deviation of the Median."

**The Intuition:**
"Pulling yourself up by your bootstraps." Since we don't have the true population to draw more samples from, we treat our *current sample* as if it were the population. We simulate running the experiment again and again by drawing from our own data.

**The Method:**
1.  **Resample:** Create a "fake" dataset by drawing $n$ items from your original data *with replacement*.
2.  **Recalculate:** Compute the median of this fake dataset.
3.  **Repeat:** Do this 10,000 times.
4.  **Result:** The spread of these 10,000 fake medians tells you how much the *actual* median would likely vary if you re-ran the real experiment.

---

## 4.5 Information Theory

Information theory quantifies "Surprise."

**Entropy ($H$):**
Entropy measures the **expected surprise** of a distribution.
$$H(X) = - \sum p(x) \log_2 p(x)$$
* **Intuition:**
    * **Low Entropy:** The sun rising. It happens every day ($p \approx 1$). When it happens, you aren't surprised. The distribution is "boring" or deterministic.
    * **High Entropy:** A fair coin toss. You have no idea what will happen. The outcome is "maximally surprising" on average because you cannot predict it.

**KL Divergence ($D_{KL}$):**
KL Divergence measures the **penalty for being wrong**.
$$D_{KL}(P || Q) = \sum P(x) \log \frac{P(x)}{Q(x)}$$
* **Scenario:** The world works according to distribution $P$ (Truth). However, you *think* the world works according to distribution $Q$ (Your Model).
* **Intuition:**
    * If $P \approx Q$, you are rarely surprised. $D_{KL}$ is close to 0.
    * If $P$ is very different from $Q$, events will happen that you assigned low probability to. You will be constantly "surprised" by reality. $D_{KL}$ measures this "Excess Surprise" or the information you are missing by using the wrong model.

---

## 4.6 Thompson Sampling

Thompson Sampling is a strategy for making decisions when you are unsure which option is best (the Exploration-Exploitation trade-off).

**The Intuition:**
"Don't just pick the winner; pick the *potential* winner."
* If you just pick the option with the highest *average* rating, you might ignore a new option that has few ratings (high uncertainty) but *could* be amazing.
* **Method:** Instead of looking at the average, look at the **distribution** of belief (the Beta distribution). Sample a random value from each option's belief curve.
* **Result:**
    * A solid, mediocre option will always sample near its average.
    * A risky, unknown option has a wide curve. It might randomly sample a huge number (Exploration).
    * If it turns out to be bad, the curve narrows and shifts down, and we stop picking it.
    * This naturally balances "sticking with what works" and "giving the new guy a chance."

# Chapter 5: Machine Learning

### Overview
Machine Learning (ML) is the computational study of algorithms that improve their performance through experience. In the language of probability, "experience" is **Data** ($D$), and "improvement" is finding the most probable **Parameters** ($\theta$) for a model that explains that data. This chapter builds the mathematical foundation of ML, starting from the bedrock of Parameter Estimation, moving to core classification algorithms like Naive Bayes and Logistic Regression, and concluding with the frontiers of Deep Learning and Generative Diffusion Models.

---

## 5.1 Parameter Estimation

Before we can "learn" a complex model, we must understand how to estimate simple probabilities from data. If you flip a coin and get 3 Heads and 7 Tails, why is $0.3$ the "best" estimate for $P(Heads)$? There are two major schools of thought: **Maximum Likelihood Estimation (MLE)** and **Maximum A Posteriori (MAP)**.

### 5.1.1 Maximum Likelihood Estimation (MLE)
**The Philosophy:**
MLE assumes that the world works according to some probability distribution with unknown parameters $\theta$. The "best" $\theta$ is the one that makes the data we actually observed **most likely** to have occurred. It trusts the data completely.

**The Derivation:**
Let's rigorously derive the MLE for a Bernoulli (coin flip) experiment.
1.  **Assumptions:** We have $n$ data points $D = \{x_1, x_2, \dots, x_n\}$ which are Independent and Identically Distributed (I.I.D.).
2.  **Likelihood Function:** The probability of observing this specific sequence of data given a parameter $\theta$ (probability of heads) is the product of their individual probabilities:
    $$L(\theta) = P(D | \theta) = \prod_{i=1}^n P(x_i | \theta) = \theta^{\text{heads}} (1-\theta)^{\text{tails}}$$
3.  **Log-Likelihood:** Maximizing a product is hard (calculus rule for products is messy) and leads to numerical underflow (multiplying tiny numbers gives 0). We take the Log, which turns products into sums. Since $\log$ is monotonic, maximizing $\log(L)$ is the same as maximizing $L$.
    $$LL(\theta) = \log \left( \theta^k (1-\theta)^{n-k} \right) = k \log(\theta) + (n-k) \log(1-\theta)$$
4.  **Optimization:** To find the maximum, we take the derivative with respect to $\theta$ and set it to 0.
    $$\frac{\partial LL}{\partial \theta} = \frac{k}{\theta} - \frac{n-k}{1-\theta} = 0$$
5.  **Solution:**
    $$k(1-\theta) = (n-k)\theta$$
    $$k - k\theta = n\theta - k\theta$$
    $$\theta_{MLE} = \frac{k}{n}$$
**Conclusion:** The MLE estimate is simply the sample mean. If you see 3 heads in 10 tosses, your estimate is exactly $0.3$.

### 5.1.2 Maximum A Posteriori (MAP)
**The Philosophy:**
MLE has a fatal flaw: it overfits small datasets. If you flip a coin once and get Heads, MLE concludes $P(Heads)=1.0$ and that Tails is impossible. MAP fixes this by introducing a **Prior Belief**—mathematically encoding our "common sense" before we see any data.

**The Math:**
We use Bayes' Theorem to flip the condition. We don't just want $P(Data | \theta)$; we want $P(\theta | Data)$.
$$P(\theta | D) = \frac{P(D | \theta) P(\theta)}{P(D)}$$
* **$P(D | \theta)$**: The Likelihood (same as MLE).
* **$P(\theta)$**: The **Prior**. Our belief about $\theta$ *before* the experiment.
* **$P(D)$**: Normalization constant (we ignore this as it doesn't depend on $\theta$).

**The Beta Prior:**
For binomial data, the standard prior is the **Beta Distribution**, $P(\theta) \sim Beta(\alpha, \beta)$. The parameters $\alpha$ and $\beta$ act as "imaginary counts" or "pseudocounts."
* $\alpha-1$: Imaginary heads we've seen before.
* $\beta-1$: Imaginary tails we've seen before.

**The Solution:**
Combining the Binomial Likelihood with the Beta Prior yields a **Posterior** which is also a Beta distribution (this property is called *Conjugacy*).
$$\theta_{MAP} = \text{argmax}_\theta P(\theta | D) = \frac{k + (\alpha - 1)}{n + (\alpha + \beta - 2)}$$

**Comparison Example:**
Scenario: You are estimating the probability a new basketball player makes a shot. You see them take **one** shot and make it ($n=1, k=1$).
* **MLE:** $\theta = 1/1 = 100\%$. (You assume they will never miss).
* **MAP:** You assume most humans shoot around 50%, so you use a prior of $\alpha=5, \beta=5$ (weak belief).
    $$\theta_{MAP} = \frac{1 + 4}{1 + 8} = \frac{5}{9} \approx 55\%$$
    The MAP estimate is much more reasonable ("Regularized"). As $n \to \infty$, the data term $n$ dominates the prior $\alpha+\beta$, and MAP converges to MLE.

---

## 5.2 Naive Bayes Classification

Naive Bayes is a probabilistic classifier based on Generative modeling. It tries to model the world by asking: "If I were a Spam email, what words would I likely contain?" versus "If I were a Ham email, what words would I contain?"

### 5.2.1 The "Naive" Independence Assumption
We want to predict a class label $Y \in \{0, 1\}$ given a vector of features $X = [x_1, x_2, \dots, x_m]$. Using Bayes' Rule:
$$P(Y=1 | X) = \frac{P(X | Y=1) P(Y=1)}{P(X)}$$
The term $P(X | Y=1)$ is the joint probability of all features occurring together given the class. If we have 1000 words in our dictionary, estimating this joint distribution requires parameters for every possible combination of words ($2^{1000}$), which is impossible.

**The Assumption:**
We assume that features are **conditionally independent** given the class.
$$P(x_1, x_2, \dots | Y) \approx P(x_1|Y) \cdot P(x_2|Y) \cdot \dots \cdot P(x_m|Y)$$
This simplifies the problem from $2^m$ parameters to just $m$ parameters per class.

### 5.2.2 The Algorithm
1.  **Training:**
    We calculate two types of probabilities from our training data:
    * **Class Priors:** $P(Y=0)$ and $P(Y=1)$. (How common is spam?)
    * **Feature Likelihoods:** For every word $i$, calculate $P(x_i=1 | Y=1)$ and $P(x_i=1 | Y=0)$.
    * *Note:* We apply **Laplace Smoothing** here. If a word (e.g., "Pokemon") never appears in the Spam dataset, we don't want $P(\text{Pokemon}|Spam) = 0$, because multiplying by 0 kills the entire prediction. We add +1 to the numerator and +2 to the denominator.

2.  **Prediction:**
    For a new email $X$, we calculate the score for each class. We work in **Log-Space** to prevent numerical underflow (multiplying hundreds of small probabilities results in 0 on a computer).
    $$\text{Score}(Spam) = \log P(Y=1) + \sum_{i=1}^m \log P(x_i | Y=1)$$
    $$\text{Score}(Ham) = \log P(Y=0) + \sum_{i=1}^m \log P(x_i | Y=0)$$
    If $\text{Score}(Spam) > \text{Score}(Ham)$, predict Spam.



---

## 5.3 Logistic Regression

While Naive Bayes is a "Generative" model (models $P(X|Y)$), Logistic Regression is a "Discriminative" model. It tries to learn the boundary between classes directly by modeling $P(Y|X)$.

### 5.3.1 The Sigmoid Function
We want to output a probability $p \in [0, 1]$. A standard linear equation $z = \theta^T x$ outputs values in $(-\infty, \infty)$. To map this to a probability, we use the **Sigmoid** (or Logistic) function $\sigma(z)$:
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$
* If $z$ is very large positive, $e^{-z} \approx 0$, so $\sigma(z) \approx 1$.
* If $z$ is very large negative, $e^{-z} \to \infty$, so $\sigma(z) \approx 0$.
* If $z = 0$, $\sigma(z) = 0.5$ (The Decision Boundary).

### 5.3.2 Optimization: Gradient Ascent
Unlike the "counting" approach of Naive Bayes, Logistic Regression has no closed-form solution. We must use optimization to find the best weights $\theta$.

**The Objective:**
Maximize the Log-Likelihood of the correct labels:
$$LL(\theta) = \sum_{i=1}^n y^{(i)} \log(\hat{y}^{(i)}) + (1-y^{(i)}) \log(1-\hat{y}^{(i)})$$

**The Gradient:**
We take the partial derivative of the LL with respect to each weight $\theta_j$. The math simplifies beautifully (a result of the Sigmoid derivative canceling terms):
$$\frac{\partial LL}{\partial \theta_j} = \sum_{i=1}^n \left( y^{(i)} - \sigma(\theta^T x^{(i)}) \right) x_j^{(i)}$$

**Intuitive Explanation of the Gradient:**
$$\text{Gradient} = \text{Sum over data} \left[ (\text{True Label} - \text{Prediction}) \times \text{Input Strength} \right]$$
* **Error term $(y - \hat{y})$:** If we predicted perfectly, this is 0, and we don't change the weight.
* **Direction:** If $y=1$ and prediction is 0.2, the error is positive. We need to *increase* the weight to push the prediction up.
* **Input $x_j$:** If the input $x_j$ was 0, this specific weight $\theta_j$ didn't contribute to the mistake, so we don't update it.

**The Algorithm (Stochastic Gradient Ascent):**
1.  Initialize $\theta$ randomly.
2.  Loop until convergence:
    * For each data point $i$:
        * Calculate prediction $\hat{y} = \sigma(\theta^T x^{(i)})$.
        * Calculate error $E = y^{(i)} - \hat{y}$.
        * Update every weight: $\theta_j \leftarrow \theta_j + \eta \cdot E \cdot x_j^{(i)}$ (where $\eta$ is learning rate).

---

## 5.4 Deep Learning

Deep Learning is the natural evolution of Logistic Regression. If Logistic Regression is a single neuron, a Neural Network is a brain.

### 5.4.1 Limits of Linearity
Logistic Regression is a **Linear Classifier**. It can only solve problems where the classes can be separated by a straight line. It fails on the "XOR" problem (where $(0,0)$ and $(1,1)$ are class 0, but $(0,1)$ and $(1,0)$ are class 1).
To solve this, we stack layers. The first layer learns "features" (non-linear combinations of inputs), and the final layer acts as a Logistic Regression on those learned features.

### 5.4.2 Backpropagation
The core magic of Deep Learning is efficient parameter updates. We have millions of weights. How do we know how to adjust a weight in the very first layer based on an error in the final output?
**The Chain Rule:**
$$\frac{\partial Loss}{\partial \theta_{first}} = \frac{\partial Loss}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial h_{hidden}} \cdot \dots \cdot \frac{\partial h_{1}}{\partial \theta_{first}}$$
Backpropagation computes these gradients layer-by-layer, starting from the end and moving backwards, reusing calculations to be efficient.

---

## 5.5 Generative Models: Diffusion

This represents the cutting edge of probabilistic ML (e.g., Stable Diffusion, DALL-E). Standard models discriminate (Predict Label $Y$ from Image $X$). Generative models create (Predict Image $X$ from Noise).

### 5.5.1 The Core Intuition: Reversing Entropy
It is easy to destroy information. If you take a photograph and iteratively add static (Gaussian noise), you eventually get pure random noise. This is a deterministic process called the **Forward Process**.
Diffusion models rely on the realization that if the steps are small enough, we can **learn to reverse this process**.

### 5.5.2 The Mathematical Framework
1.  **Forward (Destruction):**
    We define a sequence of latent variables $x_0, x_1, \dots, x_T$. At each step, we add a little Gaussian noise.
    $$q(x_t | x_{t-1}) = N(x_t; \sqrt{1-\beta_t} x_{t-1}, \beta_t I)$$
    $x_T$ effectively becomes standard Normal distribution $N(0, I)$.

2.  **Reverse (Creation):**
    We want to sample $q(x_{t-1} | x_t)$. For small steps, this reverse distribution is *also* Gaussian!
    $$p_\theta(x_{t-1} | x_t) = N(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))$$
    The only thing we don't know is the mean $\mu_\theta$.

3.  **The Learning Task:**
    We train a Neural Network to predict the mean. Specifically, it's easier to train the network to **predict the noise** $\epsilon$ that was added to the image.
    * Input: A noisy image $x_t$ and the timestep $t$.
    * Target: The specific noise vector $\epsilon$ that corrupted $x_0$ into $x_t$.
    * Loss: Mean Squared Error $|| \epsilon - \text{Net}(x_t, t) ||^2$.

### 5.5.3 Generating a New Image
1.  Sample a vector of pure random noise $x_T$ from $N(0, 1)$.
2.  Use the trained Neural Network to estimate the noise component.
3.  Subtract a fraction of that noise to take a "step" towards order.
4.  Add a tiny bit of random noise back in (Langevin dynamics) to prevent the process from collapsing to a boring average.
5.  Repeat $T$ times. A detailed image emerges from the white noise.

# Supplementary Section

### Overview

Here are just a few example problems I thought were cool and wanted to share on here.

## Tracking in 2D for Radars

**Problem:**
We want to track the location of an object in 2D space. The object's location is defined by random variables $(X, Y)$. We are not sure exactly where it is, but we have a prior belief. We then make a noisy sensor observation and want to update our belief.

### 1. The Prior
Our prior belief is that the object is located near the point $(3, 3)$. We model $X$ and $Y$ as independent Normal random variables with mean 3 and variance 4:
* $X \sim N(\mu=3, \sigma^2=4)$
* $Y \sim N(\mu=3, \sigma^2=4)$

The joint Probability Density Function (PDF) is the product of the marginals:
$$f_{X,Y}(x, y) = f_X(x) f_Y(y) = K_1 \cdot e^{-\frac{(x-3)^2}{8}} \cdot e^{-\frac{(y-3)^2}{8}}$$
$$f_{X,Y}(x, y) = K_1 \cdot e^{-\frac{(x-3)^2 + (y-3)^2}{8}}$$
*(Note: We wrap all normalization constants like $\frac{1}{\sqrt{2\pi}\sigma}$ into a single constant $K_1$ to simplify algebra).*



### 2. The Observation
We have a sonar sensor at the origin $(0, 0)$ that measures the distance $D$ to the object.
* The true distance is $R = \sqrt{x^2 + y^2}$.
* The sensor is noisy. We model the reading $D$ as the true distance plus Gaussian noise with variance 1: $D \sim N(R, 1)$.

We observe a reading of **$D=4$**.
The likelihood of observing this specific distance given the object is at $(x, y)$ is:
$$f(D=4 | X=x, Y=y) = K_2 \cdot e^{-\frac{(4 - \sqrt{x^2+y^2})^2}{2}}$$
* This function peaks when $\sqrt{x^2+y^2} = 4$ (a circle of radius 4) and drops off as we move away from that ring.

### 3. The Posterior (Bayesian Update)
We want to find the new distribution of the object's location given the sonar data: $f(X=x, Y=y | D=4)$.
Using Bayes' Theorem for densities:
$$f(x, y | D=4) = \frac{f(D=4 | x, y) \cdot f(x, y)}{f(D=4)}$$

Since $f(D=4)$ is just a constant number (it doesn't depend on $x$ or $y$), we can ignore it and focus on the shape:
$$f(x, y | D=4) \propto \text{Likelihood} \times \text{Prior}$$
$$f(x, y | D=4) = K_3 \cdot \underbrace{e^{-\frac{(4 - \sqrt{x^2+y^2})^2}{2}}}_{\text{Ring Shape}} \cdot \underbrace{e^{-\frac{(x-3)^2 + (y-3)^2}{8}}}_{\text{Blob at (3,3)}}$$

Combining the exponents:
$$f(x, y | D=4) = K_3 \cdot e^{-\left[ \frac{(4 - \sqrt{x^2+y^2})^2}{2} + \frac{(x-3)^2 + (y-3)^2}{8} \right]}$$

### 4. Intuition
* **Prior:** A fuzzy blob centered at $(3, 3)$.
* **Likelihood:** A fuzzy ring with radius 4 around the origin $(0, 0)$.
* **Posterior:** The intersection of these two shapes. The math "carves" the ring shape out of the prior blob. The resulting belief is a crescent-like shape near $(3, 3)$ but "pulled" towards the circle of radius 4. This represents our updated knowledge: "We thought it was at (3,3), but the sonar says it's 4 units away, so it's probably slightly closer to the origin than we thought."

## Tank Production Problem

**Historical Context:**
During WWII, the Allies needed to estimate German tank production. Spies estimated 1,400/month. Mathematicians, observing sequential serial numbers on captured tanks, used this probabilistic method to estimate 270/month. [cite_start]Post-war records confirmed the actual number was 276/month! [cite: 90-94]

**Problem:**
A rival factory produces $N$ items with serial numbers $\{1, 2, \dots, N\}$. You capture (sample) $k=5$ items and see serial numbers $\{7, 12, 14, 24, 33\}$. You want to estimate $N$.
* **Observed Data:** The largest serial number seen is $L = 33$.
* **Likelihood:** We assume all sets of 5 items are equally likely to be sampled.

### Part A: Probability of Max=33 given N=100
Suppose we *knew* $N=100$. What is the probability that the largest number in a sample of 5 is exactly 33? 

1.  **Sample Space ($S$):** The number of ways to pick 5 distinct items from 100.
    $$|S| = \binom{100}{5}$$ 
2.  **Event Space ($E$):** To have a max of 33, we must:
    * Pick the number 33 (1 way).
    * Pick 4 other numbers from the range $\{1, \dots, 32\}$.
    $$|E| = \binom{32}{4} \cdot 1$$ 
3.  **Probability:**
    $$P(L=33 | N=100) = \frac{\binom{32}{4}}{\binom{100}{5}}$$

### Part B: Estimating N (Bayesian Update)
Now assume we don't know $N$. We have a **Prior belief** that $N$ is equally likely to be any value between 33 and 100.
* **Prior:** $P(N=n) = \frac{1}{68}$ for $33 \le n \le 100$. 
* **Observation:** We saw $L=33$.

We want the **Posterior**: $P(N=n | L=33)$.
Using Bayes' Theorem:
$$P(N=n | L=33) = \frac{P(L=33 | N=n) P(N=n)}{\sum_{i=33}^{100} P(L=33 | N=i) P(N=i)}$$ 

* **Likelihood:** Generalizing Part A, if the total is $n$, the chance of seeing a max of 33 is:
    $$P(L=33 | N=n) = \frac{\binom{32}{4}}{\binom{n}{5}}$$
* **Calculation:**
    $$P(N=n | L=33) = \frac{\frac{\binom{32}{4}}{\binom{n}{5}} \cdot \frac{1}{68}}{\sum_{i=33}^{100} \frac{\binom{32}{4}}{\binom{i}{5}} \cdot \frac{1}{68}}$$
    Canceling constants ($\binom{32}{4}$ and $\frac{1}{68}$), the posterior is proportional to $\frac{1}{\binom{n}{5}}$. This means smaller values of $N$ (closer to 33) are much more probable than larger values (like 100).

### Part C: Hypothesis Testing
What is the probability that the factory produced fewer than 50 tanks ($N < 50$), given our observation?
We simply sum the posterior probabilities for $n=33$ to $n=49$:
$$P(N < 50 | L=33) = \sum_{n=33}^{49} P(N=n | L=33)$$
This gives us a concrete probability that production is low, helping decision-making in uncertainty.

## Bloom Filters

**Problem:**
A Bloom Filter is a probabilistic data structure used to test whether an element is a member of a set. It is space-efficient but admits **False Positives** (it might say "Yes" when the answer is "No").
* We have a bit array of size $m$ (initially all 0s).
* We have $k$ independent hash functions.
* To insert an element, we hash it $k$ times and set the corresponding bits to 1.
* To check an element, we hash it $k$ times; if *all* corresponding bits are 1, we return "True".

**Question:** Suppose we insert $n$ elements into a filter of size $m$ using $k$ hash functions. What is the probability of a False Positive for a new, uninserted element?

### 1. Analysis of a Single Bit
First, look at a single bit in the array. What is the probability it remains 0 after inserting all $n$ elements?
* Probability a specific bit is chosen by 1 hash function: $1/m$.
* Probability a specific bit is **not** chosen by 1 hash function: $1 - \frac{1}{m}$.
* Since there are $k$ hash functions and $n$ elements, there are $kn$ total independent hash operations.
* Probability the bit remains 0 after $kn$ operations:
    $$P(\text{Bit is 0}) = \left(1 - \frac{1}{m}\right)^{kn}$$

**Approximation:**
Recall the limit definition of $e$: $\lim_{x \to \infty} (1 - \frac{1}{x})^x = e^{-1}$.
We can rewrite our equation:
$$P(\text{Bit is 0}) = \left( (1 - \frac{1}{m})^m \right)^{kn/m} \approx e^{-kn/m}$$

Thus, the probability the bit is **1** (set) is:
$$P(\text{Bit is 1}) = 1 - e^{-kn/m}$$

### 2. False Positive Probability
A False Positive occurs if we check a new element (which was never inserted) and **all $k$** of its hash locations happen to be 1 (set by other elements).
* We assume the status of the $k$ bits are independent (this is an approximation, but accurate for large $m$).
* The probability that *one* specific bucket is 1 is $1 - e^{-kn/m}$.
* The probability that *all $k$* buckets are 1 is:
    $$P(\text{False Positive}) = \left( 1 - e^{-kn/m} \right)^k$$

### 3. Concrete Example
* **Storage ($m$):** 8 billion bits (~1 GB).
* **Items ($n$):** 1 billion URLs (Malicious URL filter).
* **Hashes ($k$):** 5.

**Calculation:**
1.  **Ratio:** $n/m = 1/8 = 0.125$.
2.  **Exponent:** $kn/m = 5 \times 0.125 = 0.625$.
3.  **Bit Probability:** $P(\text{Bit is 1}) = 1 - e^{-0.625} \approx 1 - 0.535 = 0.465$. (About 46% of bits are set).
4.  **Error Rate:**
    $$P(\text{FP}) = (0.465)^5 \approx 0.022$$
**Result:** There is a **2.2%** chance the filter incorrectly flags a safe URL as malicious.

## How Does Shazam See Through the Noise
**Problem:** Shazam is trying to detect a song in a noisy bar. The algorithm extracts 5025 "notes" from the audio: 25 from the actual song and 5000 from background noise.
* **Total Notes:** $N = 5025$.
* **Song Notes:** $S = 25$.
* **Noise Notes:** $5000$.

The algorithm works by examining **pairs** of notes. Every pair votes for which song it thinks is playing. We want to find the probability that the **Correct Song** gets more votes than its **Nearest Neighbor** (the most similar incorrect song).

### 1. Counting Pairs
First, we separate the pairs into two types: "Signal" (both notes from the song) and "Noisy" (at least one note is noise).

* **Total Pairs:** $\binom{5025}{2} \approx 12.6$ million.
* **Signal Pairs ($N_S$):** Both notes must come from the 25 song notes.
    $$N_S = \binom{25}{2} = \frac{25 \times 24}{2} = 300$$
* **Noisy Pairs ($N_N$):** All other pairs.
    $$N_N = \text{Total} - N_S = 12,622,800 - 300 = 12,622,500$$

### 2. Defining the Random Variable
We care about the *difference* in votes: $D = \text{Votes(Correct)} - \text{Votes(Nearest Neighbor)}$.
We want to find $P(D > 0)$.

Let $D_i$ be the contribution of the $i$-th pair to this difference.
* If pair votes Correct, $D_i = +1$.
* If pair votes Nearest Neighbor (NN), $D_i = -1$.
* If pair votes for neither (other songs), $D_i = 0$.

Total difference $D = \sum D_i$.

### 3. Analyzing Signal Pairs
For the 300 signal pairs:
* $P(\text{Vote Correct}) = 0.99 \implies D_i = +1$
* $P(\text{Vote NN}) = 0.01 \implies D_i = -1$

**Expectation:**
$$E[D_{signal}] = (1)(0.99) + (-1)(0.01) = 0.98$$
**Variance:**
$$E[D^2_{signal}] = (1^2)(0.99) + (-1^2)(0.01) = 1.0$$
$$Var(D_{signal}) = E[D^2] - (E[D])^2 = 1.0 - (0.98)^2 = 1.0 - 0.9604 = 0.0396$$

**Total for Signal Pairs ($S_{tot}$):**
$$E[S_{tot}] = 300 \times 0.98 = 294$$
$$Var(S_{tot}) = 300 \times 0.0396 = 11.88$$

### 4. Analyzing Noisy Pairs
For the ~12.6 million noisy pairs:
* $P(\text{Vote Correct}) = 0.001 \implies D_i = +1$
* $P(\text{Vote NN}) = 0.001 \implies D_i = -1$
* $P(\text{Vote Other}) = 0.998 \implies D_i = 0$

**Expectation:**
$$E[D_{noisy}] = (1)(0.001) + (-1)(0.001) + (0)(0.998) = 0$$
*Intuition: The noise is random, so it votes for the correct song and the wrong song equally often. It adds variance but no bias.*

**Variance:**
$$E[D^2_{noisy}] = (1^2)(0.001) + (-1^2)(0.001) + 0 = 0.002$$
$$Var(D_{noisy}) = 0.002 - (0)^2 = 0.002$$

**Total for Noisy Pairs ($N_{tot}$):**
$$E[N_{tot}] = 12,622,500 \times 0 = 0$$
$$Var(N_{tot}) = 12,622,500 \times 0.002 = 25,245$$

### 5. Final Calculation (Normal Approximation)
We sum the Signal and Noisy contributions to get the distribution of the total difference $D$.
* **Mean ($\mu$):** $294 + 0 = 294$
* **Variance ($\sigma^2$):** $11.88 + 25,245 \approx 25,257$
* **Standard Deviation ($\sigma$):** $\sqrt{25,257} \approx 158.92$

By the Central Limit Theorem, $D \sim N(294, 158.92^2)$.

We want $P(D > 0)$. Since $D$ is a sum of integers, we use the **continuity correction** and find $P(D > 0.5)$.

$$Z = \frac{0.5 - \mu}{\sigma} = \frac{0.5 - 294}{158.92} = \frac{-293.5}{158.92} \approx -1.847$$

Using the standard normal CDF ($\Phi$):
$$P(Z > -1.847) = 1 - \Phi(-1.847) = \Phi(1.847) \approx 0.968$$

**Answer:** The probability that Shazam correctly identifies the song is approximately **0.968**.
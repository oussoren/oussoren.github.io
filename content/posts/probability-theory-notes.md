+++
title = 'Probability Theory Notes'
date = '2026-01-01'
draft = false
tags = ["math", "analysis", "probability"]
+++
# Probability spaces and Counting

## Intro

* **Experiment** $\to$ Outcomes ($\Omega$)
    * e.g., Rolling a die $\to \{1, 2, 3, 4, 5, 6\}$
    * Flip a coin $\to \{H, T\}$
    * Draw a card $\to \{1, \dots, 52\}$

* The set of all outcomes is called the **SAMPLE SPACE**.
* The sample space can be **FINITE** or **INFINITE**.

* **Probability measure** on $\Omega$ sample space is a function $P: \Omega \to [0, 1]$ which assigns a probability to each outcome in sample space.

> [!abstract] Axiom
> $P(w)$ s.t. $\sum_{w \in \Omega} P(w) = 1$

### Example: Die Roll
$\Omega = \{1, 2, \dots, 6\}$

One probability measure would be $P(w) = \frac{1}{6}$

Need to check:
$$\sum_{w \in \Omega} P(w) = 1$$For any finite $\Omega$, the probability $P(w) = \frac{1}{|\Omega|}$ gives all outcomes equal probability.

### Philosophical Discussion
**Meaning of a probability — frequentist meaning:**
i.e., if we repeatedly perform the experiment corresponding to $\Omega$ and $P$, then the outcome will occur approximately $P(w)$ proportion of the time, and this approximation will get more accurate as more experiments take place.

* If $P$ is constant on $\Omega$, then it is a **uniform distribution**.
* An **event** is any subset of $\Omega$. The probability of an event $E$:
$$P(E) = \sum_{w \in E} P(w)$$
**Example:** $A$ is the event $A = \{ \text{the result of rolling a die is odd} \} = \{1, 3, 5\}$
$$P(A) = P(1) + P(3) + P(5) = \frac{|A|}{|\Omega|} = \frac{3}{6} = \frac{1}{2}$$

**Ex.** Rolling 2 dice: $\Omega = \{ (i, j) : i, j \in \{1, \dots, 6\} \}$
$P(w) = \frac{1}{36}$
$A = \{ \text{the sum of the rolls is 5} \} = \{ (1, 4), (2, 3), (3, 2), (4, 1) \}$
$$P(A) = \frac{4}{36} = \frac{1}{9}$$

**Ex.** Toss coin 3 times:
$\Omega = \{ (i, j, k) : i, j, k \in \{H, T\} \}$
$|\Omega| = 8 = 2^3$
$P(w) = \frac{1}{8}$

> [!info] 
> \*There are many different probability measures on a sample space\*

**Ex.** Toss coin $n$ times:
$\Omega = \{0, 1\}^n = \{ (e_1, \dots, e_n) : e_i \in \{0, 1\} \}$
$|\Omega| = 2^n \implies P(w) = \frac{1}{2^n}$
$A_k = \text{event that } k \text{ heads appear}$

$$P(A_k) = \sum_{w \in A_k} \frac{1}{|\Omega|} = \frac{|A_k|}{|\Omega|}$$
— *main difficulty lies in counting*
# Fundamental Principle of Counting

Suppose we have $k$ tasks to do, and the $i$-th task can be completed in $n_i$ ways, for $i = 1, 2, \dots, k$. Then there are $\prod_{i=1}^k n_i$ ways to complete the $k$ tasks.

> [!important] Note
> The number of ways for the $i$-th task must be independent of previous choices (though the tasks themselves don't necessarily have to be independent).

### Example: $k=2$
If $n_1 = 2$ and $n_2 = 3$, then the number of ways $= 2 \times 3 = 6$.
*(Visualized as a tree diagram with 2 primary branches, each splitting into 3).*

### Example: Ordering a deck of 52 cards
$$\underbrace{52}_{\text{bottom card}} \times \underbrace{51}_{\text{remaining}} \times \dots \times 1 = 52!$$

### Example: Seating $k$ people on $n$ chairs ($k \le n$)
$$\text{Number of ways} = \underbrace{n}_{\text{1st person}} \times \underbrace{(n-1)}_{\text{2nd person}} \times \dots \times (n-k+1)$$
$$= \frac{n!}{(n-k)!}$$
# Probability Theory: Combinatorics & Inclusion-Exclusion

## Combinations (Choosing $k$ from $n$)
Suppose order doesn't matter. Let $X$ be the number of ways to select $k$ chairs out of $n$.
1. Select $k$ chairs $\to X$ ways.
2. Seat $k$ people in those $k$ chairs $\to k!$ ways.

Total ways to seat $k$ people in $n$ chairs:
$$X \cdot k! = \frac{n!}{(n-k)!}$$
$$\implies X = \frac{n!}{(n-k)!k!} = \binom{n}{k}$$

### Binomial Theorem
$$(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}$$
*Exercise: Prove this using induction.*

---

## Circular Seating
**Problem:** Number of ways to seat $n$ people in a circle of $n$ chairs.
* There are $n!$ ways to seat them in a line.
* In a circle, there are $n$ rotations that are considered the same.
* Total ways $= \frac{n!}{n} = (n-1)!$

> [!tip] Concept: Burnside's Lemma
> This relates to symmetry and counting—essentially "cutting" the circle at one point to turn it into a line.

---

## Probability Examples

### $n$ Coin Tosses
Let event $A_k$ be getting exactly $k$ heads.
* $\Omega = \{0, 1\}^n$, so $|\Omega| = 2^n$.
* A sequence with $k$ heads can be chosen in $\binom{n}{k}$ ways.
$$P(A_k) = \frac{\binom{n}{k}}{2^n}$$
*Note: If you use $\Omega = \{0, 1, \dots, n\}$ (total number of heads), then $P(w) = \frac{1}{n+1}$ is NOT the natural probability measure.*

### The Birthday Problem
In a room of $n$ people, what is the probability that at least 2 people share a birthday?
* Assume 365 days, all equally likely.
* $|\Omega| = 365^n$
* $A^c = \text{No two people share a birthday}$
* $|A^c| = 365 \times 364 \times \dots \times (365 - n + 1)$
$$P(A) = 1 - P(A^c) = 1 - \frac{365!}{ (365-n)! \cdot 365^n }$$
*For $n=40, P(A) \approx 89\%$.*
**Intuition:** The number of *pairs* of people grows much faster than the number of people.

---

## Operations with Events & Inclusion-Exclusion
* **Complements:** $A^c$
* **Union:** $A \cup B$ or $\bigcup_{i=1}^n A_i$
* **Intersection:** $A \cap B$ (A and B)

### Principle of Inclusion-Exclusion
For 2 events:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Generalization for $n$ events:**
$$P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i} P(A_i) - \sum_{i < j} P(A_i \cap A_j) + \sum_{i < j < k} P(A_i \cap A_j \cap A_k) - \dots + (-1)^{n-1} P\left(\bigcap_{i=1}^n A_i\right)$$

---

## The Derangement Problem (Secretary / Mailman Problem)
**Scenario:** A mailman has $n$ letters and $n$ matching mailboxes. If he delivers them at random, what is the probability that at least one letter is correctly delivered?

* $\Omega = \{ \text{permutations of } \{1, \dots, n\} \}$, so $|\Omega| = n!$.
* Let $A_i = \{ \text{i-th letter goes to i-th box} \}$.
* We want $P(A_1 \cup A_2 \cup \dots \cup A_n)$.

**Calculation:**
1. $P(A_{i_1} \cap \dots \cap A_{i_r}) = \frac{(n-r)!}{n!}$ (ways to deliver $r$ pieces correctly).
2. There are $\binom{n}{r}$ terms in the $r$-th sum of the Inclusion-Exclusion formula.
3. $\binom{n}{r} \frac{(n-r)!}{n!} = \frac{n!}{r!(n-r)!} \cdot \frac{(n-r)!}{n!} = \frac{1}{r!}$

**Result:**
$$P(\text{at least one correct}) = \sum_{k=1}^n (-1)^{k-1} \frac{1}{k!} = 1 - \frac{1}{2!} + \frac{1}{3!} - \dots + (-1)^{n-1} \frac{1}{n!}$$

**Limit as $n \to \infty$:**
Using the power series for $e^x$:
$$P(\text{no letters correct}) = 1 - P(\text{at least one}) \xrightarrow{n \to \infty} \frac{1}{e} \approx 0.368$$
### Discrete Sample Spaces
If $\Omega$ is finite or countable, then for any $E \subseteq \Omega$, we have $E = \bigcup_{w \in E} \{w\}$ (where the union is finite or countable).
So:
$$P(E) = \sum_{w \in E} P(\{w\})$$

> [!cite] Definition: Partition
> A **partition** of $\Omega$ is a collection of events $\{E_\lambda\}_{\lambda \in \Lambda}$ such that:
> 1. The events $E_\lambda$ are disjoint ($E_{\lambda_1} \cap E_{\lambda_2} = \emptyset$ for $\lambda_1 \neq \lambda_2$).
> 2. Their union covers the sample space: $\Omega = \bigcup_{\lambda \in \Lambda} E_\lambda$.

**Example (Urn):**
* $E_1 = \{ \text{one marble is red} \}$
* $E_2 = \{ \text{two marbles are red} \}$
* $E_3 = \{ \text{none are red} \}$

---

## Kolmogorov Definition of a Probability Space
A probability space is a triple $(\Omega, \mathcal{F}, P)$ where:
* $\Omega$ is the **sample space**.
* $\mathcal{F}$ is the set of **events** (often $\mathcal{F} = 2^\Omega$, the power set of $\Omega$).
* $P$ is the **probability measure**, a function $P: \mathcal{F} \to [0, 1]$ such that:
    1. $P(\Omega) = 1$
    2. **Countable Additivity:** If $E_1, E_2, \dots$ is a countable collection of disjoint events ($E_i \cap E_j = \emptyset$), then:
    $$P\left(\bigcup_{i=1}^\infty E_i\right) = \sum_{i=1}^\infty P(E_i)$$

---

## Example: Urn Problem
Urn with **30 red**, **20 blue**, and **10 yellow** marbles (60 total).
**Experiment:** Draw 2 marbles without replacement.
**Goal:** Find $P(\text{draw exactly 1 red OR exactly 1 yellow})$.

* $\Omega = \{ \text{subsets of } \{1, \dots, 60\} \text{ of size 2} \}$
* $|\Omega| = \binom{60}{2}$
* $R = \text{event of exactly 1 red}$
* $Y = \text{event of exactly 1 yellow}$

**Probabilities:**
* $P(R) = \frac{30 \times 30}{\binom{60}{2}}$ (30 red options $\times$ 30 non-red options)
* $P(Y) = \frac{10 \times 50}{\binom{60}{2}}$ (10 yellow options $\times$ 50 non-yellow options)
* $P(R \cap Y) = \frac{30 \times 10}{\binom{60}{2}}$ (one red and one yellow)

**Final Calculation:**
$$P(R \cup Y) = P(R) + P(Y) - P(R \cap Y)$$
# Law of Total Probability & Sigma-Algebras

## Alice and Bob Die Game
**Problem:** Alice and Bob play a game by repeatedly rolling a die. Alice rolls first. 
* Alice wins if she rolls a **1 or 2**.
* Bob wins if he rolls a **3, 4, 5, or 6**.
* They take turns.

**Question:** What is the probability that Alice wins in her first two turns?

Let $A$ be the event that Alice wins in her first two turns.
$A = A_1 \cup A_2$
* $A_1$: Alice wins on her 1st turn.
* $A_2$: Alice wins on her 2nd turn.

**Probabilities:**
* $P(A_1) = \frac{2}{6}$
* $P(A_2) = \frac{4}{6} \times \frac{2}{6} \times \frac{2}{6}$ 
    * *(Explanation: Alice fails turn 1 $\to$ Bob fails turn 1 $\to$ Alice wins turn 2)*

Since $A_1$ and $A_2$ form a partition of the "winning within two turns" space:
$$P(A) = P(A_1) + P(A_2)$$
Using the partition logic:
$$P(A) = P(A \cap A_1) + P(A \cap A_2) + P(A \cap (A_1 \cup A_2)^c)$$
Where $P(A \cap (A_1 \cup A_2)^c) = 0$.

---

## Infinite Sample Spaces & Kolmogorov
For games that could theoretically go on forever:
$\Omega = \{ (d_1, d_2, \dots, d_i, \dots) : d_i \in \{1, \dots, 6\} \}$

Note that $P(\{w\}) = \frac{1}{|\Omega|} = 0$ because $\Omega$ is uncountably infinite (massive).

> [!theory] Theorem (Kolmogorov Extension)
> There exists a probability measure on $\Omega$ s.t. for any finite number of rolls $d_1, \dots, d_n$, the probability that the first $n$ rolls are exactly $(d_1, \dots, d_n)$ is:
> $$P(\{e_1, e_2, \dots\} : e_j = d_j \text{ for } j=1, \dots, n) = \frac{1}{6^n}$$

---

## Sigma-Algebras ($\sigma$-algebras)
**Example:** $\Omega = [0, 1]$
An event space $\mathcal{F}$ of "measurable events" forms a $\sigma$-algebra if:
1. If $A_1, A_2, \dots \in \mathcal{F}$, then their countable union $\bigcup_{i=1}^\infty A_i \in \mathcal{F}$.
2. If $A \in \mathcal{F}$, then its complement $A^c \in \mathcal{F}$.

*Note: $\sigma(\text{events})$ is the smallest $\sigma$-algebra containing those events.*

---

## Law of Total Probability
**Corollary:** For any events $A, B$:
$$P(A) = P(A \cap B) + P(A \cap B^c)$$

**General Case:**
If $E_1, E_2, \dots, E_n$ is a finite partition of $\Omega$, then for any event $A$:
$$P(A) = \sum_{i=1}^n P(A \cap E_i)$$
*(This allows us to break the calculation into cases based on the partition).*

### Proof
**Claim:** $A = \bigcup_{i=1}^n (A \cap E_i)$ and these events are disjoint.

1. **Subset $A \subseteq \bigcup (A \cap E_i)$:** Say $w \in A$. Since $\Omega = \bigcup E_i$, there exists $i_0$ s.t. $w \in E_{i_0}$. 
   Thus $w \in A \cap E_{i_0}$, which implies $w \in \bigcup_{i=1}^n (A \cap E_i)$.
2. **Subset $\bigcup (A \cap E_i) \subseteq A$:** Say $w \in \bigcup_{i=1}^n (A \cap E_i)$. Then there exists $i_0$ s.t. $w \in A \cap E_{i_0}$, which implies $w \in A$.
3. **Disjointness:** If $i \neq j$, then $(A \cap E_i) \cap (A \cap E_j) = A \cap (E_i \cap E_j) = A \cap \emptyset = \emptyset$.

Applying **Countable Additivity**:
$$P(A) = P\left(\bigcup_{i=1}^n (A \cap E_i)\right) = \sum_{i=1}^n P(A \cap E_i)$$
# Conditional Probability & Union Bound

## Conditional Probability
> [!info] Definition
> If $P(A) > 0$, we define the **conditional probability** of $B$ given $A$ as:
> $$P(B|A) = \frac{P(A \cap B)}{P(A)}$$

**Intuition (Proportion of Darts):**
* $P(A) \approx$ Proportion of darts that hit $A$.
* $P(A \cap B) \approx$ Proportion of darts that hit $A \cap B$.
* $P(B|A) \approx$ Proportion of darts that hit $B$ *among those that already hit $A$*.

**Multiplication Rule:**
$$P(A \cap B) = P(A) \times P(B|A)$$

---

## Union Bound (Boole's Inequality)
**Proposition:** For any events $E_1, E_2, \dots, E_n$:
$$P\left(\bigcup_{i=1}^n E_i\right) \le \sum_{i=1}^n P(E_i)$$

**Proof:**
Define a sequence of disjoint events $G_i$:
* $G_1 = E_1$
* $G_2 = E_2 - E_1 = E_2 \cap E_1^c$
* $G_3 = E_3 - (E_1 \cup E_2)$
* $G_n = E_n - \left(\bigcup_{i=1}^{n-1} E_i\right)$

By construction, $G_1, \dots, G_n$ are disjoint and $\bigcup_{j=1}^n G_j = \bigcup_{i=1}^n E_i$.
*(Proof of subset both ways: $G_i \subseteq E_i \implies \bigcup G_j \subseteq \bigcup E_i$. Conversely, if $w \in \bigcup E_i$, find the first $i^*$ s.t. $w \in E_{i^*}$. Then $w \in E_{i^*} \cap (E_1 \cup \dots \cup E_{i^*-1})^c = G_{i^*}$, so $w \in \bigcup G_j$).*

Therefore:
$$P\left(\bigcup E_i\right) = P\left(\bigcup G_i\right) = \sum P(G_i)$$
Since $G_i \subseteq E_i$, we have $P(E_i) = P(G_i) + P(E_i - G_i) \ge P(G_i)$ (because $P \ge 0$).
$$\implies \sum P(G_i) \le \sum P(E_i)$$
Thus, $P(\bigcup E_i) \le \sum P(E_i)$.

---

## Example: Bayes' Theorem & Disease Testing
**Scenario:** A disease affects $1/200$ (0.5%) of the population. We have a diagnostic test that is 99% accurate.
**Question:** Given that someone tests positive, what is $P(\text{Disease} | \text{Test Positive})$?

**Variables:**
* $D$: Event person has disease. $P(D) = 0.005$
* $T$: Event person tests positive.
* $P(T|D) = 0.99$ (Accuracy on diseased)
* $P(T|D^c) = 0.01$ (False positive rate, since test is 99% accurate)

**Applying Bayes' Theorem:**
$$P(D|T) = \frac{P(D \cap T)}{P(T)} = \frac{P(T|D)P(D)}{P(T)}$$

Using **Law of Total Probability** for $P(T)$:
$$P(T) = P(T|D)P(D) + P(T|D^c)P(D^c)$$
$$P(T) = (0.99 \times 0.005) + (0.01 \times 0.995)$$

**Final Calculation:**
$$P(D|T) = \frac{0.99 \times 0.005}{(0.99 \times 0.005) + (0.01 \times 0.995)} \approx 33.2\%$$

---

## Quick Exercises (Rolling a Die)
Let $A = \{1\}$, $B = \{5\}$, $C = \{3, 4, 5, 6\}$ (result $\ge 3$).
* $P(B|A) = 0$ (Disjoint events)
* $P(B|C) = \frac{P(B \cap C)}{P(C)} = \frac{1/6}{4/6} = \frac{1}{4}$
# Conditional Probability as a Measure & Independence

## Proof: $Q(B) = P(B|A)$ is a Probability Measure
Suppose $P(A) > 0$. We define a new measure $Q(B) = P(B|A)$.

**1. $Q(\Omega) = 1$**
$$Q(\Omega) = P(\Omega|A) = \frac{P(\Omega \cap A)}{P(A)} = \frac{P(A)}{P(A)} = 1$$

**2. Countable Additivity**
Let $E_1, E_2, \dots$ be disjoint events. Then $(E_1 \cap A), (E_2 \cap A), \dots$ are also disjoint because:
$$(E_i \cap A) \cap (E_j \cap A) = (E_i \cap E_j) \cap A = \emptyset \cap A = \emptyset \text{ if } i \neq j$$

Then:
$$Q\left(\bigcup_{i=1}^\infty E_i\right) = \frac{1}{P(A)} P\left(\left(\bigcup_{i=1}^\infty E_i\right) \cap A\right) = \frac{1}{P(A)} P\left(\bigcup_{i=1}^\infty (E_i \cap A)\right)$$
Using the countable additivity of $P$:
$$= \frac{1}{P(A)} \sum_{i=1}^\infty P(E_i \cap A) = \sum_{i=1}^\infty \frac{P(E_i \cap A)}{P(A)} = \sum_{i=1}^\infty Q(E_i)$$
Thus, $Q$ is a valid probability measure, and $(A, Q)$ is a probability space.

---

## Law of Total Probability (LTP)
If $B_1, B_2, \dots, B_n$ is a partition of $\Omega$, then:
$$P(A) = \sum_{i=1}^n P(A \cap B_i) = \sum_{i=1}^n P(A|B_i)P(B_i)$$
*(Note: This holds as long as $P(B_i) > 0$. If $P(B_i) = 0$, that term just becomes 0 anyway).*

### Conditional Independence
$B$ and $C$ are **conditionally independent** given $A$ if they are independent under the measure $Q(B) = P(B|A)$.
$$B \perp C \text{ under } Q \iff Q(B \cap C) = Q(B)Q(C)$$
$$\iff P(B \cap C | A) = P(B|A)P(C|A)$$

---

## Independence of Events
Two events $A, B$ are **independent** ($A \perp B$) if:
$$P(A \cap B) = P(A)P(B)$$
Equivalently, if $P(A) > 0$:
$$P(B|A) = P(B)$$
*i.e., knowledge of $A$ occurring does not affect the probability of $B$.*

### When is an event $A$ independent of itself?
$$P(A \cap A) = P(A)P(A) \implies P(A) = P(A)^2$$
This only happens if **$P(A) = 0$ or $P(A) = 1$**.

### Independence of Complements
**Theorem:** If $A \perp B$, then $A \perp B^c$ (and $A^c \perp B$, and $A^c \perp B^c$).

**Proof:**
$$P(A \cap B^c) + P(A \cap B) = P(A)$$
$$P(A \cap B^c) = P(A) - P(A \cap B)$$
Since $A \perp B$:
$$P(A \cap B^c) = P(A) - P(A)P(B)$$
$$P(A \cap B^c) = P(A)(1 - P(B)) = P(A)P(B^c)$$
$$\text{Thus, } A \perp B^c$$

---

## Mutual vs. Pairwise Independence

> [!important] Definitions
> **Mutual Independence:** $E_1, \dots, E_n$ are independent if for any subset of indices $\{i_1, \dots, i_k\}$:
> $$P(E_{i_1} \cap \dots \cap E_{i_k}) = \prod_{j=1}^k P(E_{i_j})$$
>
> **Pairwise Independence:** $E_1, \dots, E_n$ are pairwise independent if $P(E_i \cap E_j) = P(E_i)P(E_j)$ for all $i \neq j$.

### Example: The "Pairwise but not Mutual" Case
Toss 2 fair coins.
* $A = \{ \text{1st toss is H} \}$
* $B = \{ \text{2nd toss is H} \}$
* $C = \{ \text{1st and 2nd toss are the same} \}$

**Probabilities:**
$P(A) = 1/2, P(B) = 1/2, P(C) = 1/2$

**Check Pairwise:**
* $P(A \cap B) = P(HH) = 1/4 = P(A)P(B)$
* $P(A \cap C) = P(HH) = 1/4 = P(A)P(C)$
* $P(B \cap C) = P(HH) = 1/4 = P(B)P(C)$
*All pairs are independent.*

**Check Mutual:**
$$P(A \cap B \cap C) = P(HH) = 1/4$$
$$\text{But } P(A)P(B)P(C) = 1/2 \cdot 1/2 \cdot 1/2 = 1/8$$
$$1/4 \neq 1/8 \implies \text{NOT mutually independent.}$$
# Random Variables

> [!definition] 
> A **random variable** $X$ is a function from the sample space to the real numbers:
> $$X: \Omega \to \mathbb{R}$$
> It acts as an assignment of numerical results to events.

### Example: Roll a die twice
$\Omega = \{ (i, j) : i \in \{1, \dots, 6\}, j \in \{1, \dots, 6\} \}$
$P(w) = \frac{1}{36}$ for all $w \in \Omega$.

Define the following random variables:
* $X = \text{"result of first roll"}$
* $Y = \text{"result of second roll"}$
* $Z = \text{"sum of rolls"}$

For any outcome $(i, j)$:
$$X((i, j)) = i, \quad Y((i, j)) = j, \quad Z((i, j)) = i + j = X + Y$$

### Example: Flip $n$ coins
$\Omega = \{ (a_1, \dots, a_n) : a_i \in \{0, 1\} \}$
$X = \text{"number of heads"}$
Define indicator variables $X_j$:
$$X_j = \begin{cases} 1 & \text{if } j\text{-th roll is heads} \\ 0 & \text{otherwise} \end{cases}$$
Then the total number of heads is the sum of these indicators:
$$X = \sum_{j=1}^n X_j \implies X((a_1, \dots, a_n)) = \sum_{j=1}^n X_j((a_1, \dots, a_n))$$

---

## Probability Distributions

For a random variable $X$ and a value $x \in \mathbb{R}$, we consider the event:
$$\{X = x\} = \{ w \in \Omega : X(w) = x \} = X^{-1}(\{x\})$$

The probability is calculated by summing the probabilities of all outcomes that map to $x$:
$$P(X = x) = P(\{w : X(w) = x\}) = \sum_{w: X(w)=x} P(w)$$

If $A \subseteq \mathbb{R}$ is a measurable set (Borel set), then:
$$\{X \in A\} = \{ w \in \Omega : X(w) \in A \}$$

### The Law (Distribution)
> [!info] Definition
> For a probability space $(\Omega, P)$ and a random variable $X$, the **law** or **distribution** of $X$ is the function $P_X$ defined by:
> $$P_X(A) = P(X \in A)$$

**Note:** Two different random variables can have the same law. For example, in the "roll 2 dice" case, $P_X = P_Y$ even though $X$ and $Y$ are different functions (looking at different dice).

### Example: Fruit Dispenser
* $P(\text{banana}) = 1/10$
* $P(\text{orange}) = 4/10$
* $P(\text{apple}) = 1/2$

Define a price function $S$:
$S(\text{banana}) = \$1, \quad S(\text{orange}) = \$0.50, \quad S(\text{apple}) = \$1$

The distribution $P_S$ is:
* $P(S = 1) = P(\{\text{apple, banana}\}) = 1/10 + 1/2 = 6/10$
* $P(S = 0.50) = 4/10$

In general, for $A \subseteq \mathbb{R}$:
$$P_S(A) = \begin{cases} 1 & \text{if } \{1, 0.5\} \subseteq A \\ 0.6 & \text{if } 1 \in A, 0.5 \notin A \\ 0.4 & \text{if } 0.5 \in A, 1 \notin A \\ 0 & \text{otherwise} \end{cases}$$

---

## Discrete Random Variables & PMF

> [!definition] 
> A random variable $X$ is **discrete** if it takes values in a finite or countable set (usually $\mathbb{Z}$).

### Probability Mass Function (PMF)
The PMF of a discrete RV is the function $p_X: \mathbb{Z} \to \mathbb{R}$ defined by:
$$p_X(k) = P(X = k)$$

The PMF completely determines the law/distribution of $X$:
$$P_X(A) = P(X \in A) = \sum_{k \in A \cap \mathbb{Z}} p_X(k)$$

### Example: Number of Heads in $n$ tosses
Compute $p_X(k) = P(X = k)$:
The number of ways to choose $k$ slots for heads out of $n$ total tosses is $\binom{n}{k}$.
$$p_X(k) = \binom{n}{k} \left(\frac{1}{2}\right)^n \quad \text{for } k = 0, 1, \dots, n$$
Otherwise, $p_X(k) = 0$.

**Combinatorial Identity Check:**
$$\sum_{k=0}^n \frac{\binom{n}{k}}{2^n} = \frac{1}{2^n} \sum_{k=0}^n \binom{n}{k} = \frac{2^n}{2^n} = 1$$
# Discrete Random Variables & Independence

## Properties of the PMF
For any discrete random variable $X$:
$$\sum_{k \in \mathbb{Z}} p_X(k) = 1$$
*(This is equivalent to saying $P_X(X \in \mathbb{Z}) = 1$)*.

### The Binomial Law
If $p_X(k) = \binom{n}{k} q^k (1-q)^{n-k}$ for $k = 0, \dots, n$, then $X$ has the **Binomial Distribution**.
* **Interpretation:** The number of successes in $n$ independent trials, where $q$ is the probability of success.
* **Notation:** $X \sim \text{Bin}(n, q)$ or $X \sim f_X$ (meaning $X$ has PMF $f$).

---

## Independence of Discrete Random Variables

> [!definition] 
> We say random variables $X_1, \dots, X_n$ are **independent** if for any $k_1, k_2, \dots, k_n \in \mathbb{Z}$:
> $$P(X_1 = k_1, X_2 = k_2, \dots, X_n = k_n) = P(X_1 = k_1)P(X_2 = k_2)\dots P(X_n = k_n)$$

> [!question] 
> For events, we needed to consider all combinations of subsets for mutual independence. Why is the definition for RVs simpler? 
> *(Hint: Consider how the events $\{X=k\}$ partition the sample space).*

### Theorem: Subcollections are Independent
If $X_1, X_2, \dots, X_n$ are independent, then any subcollection (e.g., $X_1, X_2$) is also independent.

**Proof (for $X_1, X_2$):**
We want to show $P(X_1=k_1, X_2=k_2) = P(X_1=k_1)P(X_2=k_2)$.
Using the Law of Total Probability over all possible values of the other variables $X_3, \dots, X_n$:
$$P(X_1=k_1, X_2=k_2) = \sum_{k_3, \dots, k_n \in \mathbb{Z}} P(X_1=k_1, X_2=k_2, X_3=k_3, \dots, X_n=k_n)$$
By independence of the full set:
$$= \sum_{k_3, \dots, k_n \in \mathbb{Z}} P(X_1=k_1)P(X_2=k_2)P(X_3=k_3)\dots P(X_n=k_n)$$
Factor out the terms not dependent on the summation indices $k_3, \dots, k_n$:
$$= P(X_1=k_1)P(X_2=k_2) \left[ \sum_{k_3 \in \mathbb{Z}} P(X_3=k_3) \right] \dots \left[ \sum_{k_n \in \mathbb{Z}} P(X_n=k_n) \right]$$
Since the sum of a PMF over its support is 1:
$$= P(X_1=k_1)P(X_2=k_2) \cdot (1) \dots (1) = P(X_1=k_1)P(X_2=k_2)$$

---

## Bernoulli Sequences

> [!theory] Theorem (Kolmogorov)
> There exists a probability space with a sequence of independent random variables $X_1, X_2, \dots$ such that each $X_i$ has a Bernoulli PMF:
> $$p_{X_i}(k) = \begin{cases} q & \text{if } k=1 \\ 1-q & \text{if } k=0 \end{cases}$$

### Example: Index of First Success
Let $Y$ be the index of the first "heads" ($X_i = 1$) in a sequence $(X_1, X_2, \dots)$.
$$Y(w) = \min \{ i : X_i(w) = 1 \}$$

**Find the PMF of $Y$:**
The event $\{Y = k\}$ means the first $k-1$ tosses were tails ($0$) and the $k$-th toss was heads ($1$):
$$\{Y = k\} = \{X_1 = 0, X_2 = 0, \dots, X_{k-1} = 0, X_k = 1\}$$
By independence:
$$P(Y = k) = P(X_1=0)P(X_2=0)\dots P(X_{k-1}=0)P(X_k=1)$$
$$P(Y = k) = (1-q)^{k-1} q$$
*(This is the PMF for the **Geometric Distribution**).*

---

## Cumulative Distribution Function (CDF)
* **PMF:** $p_X(k) = P(X = k)$
* **CDF:** $F_X(t) = P(X \le t)$

For a discrete RV, the CDF can be calculated by summing the PMF:
$$F_X(k) = F_X(k-1) + p_X(k)$$

### Distribution Summary
| Name          | Notation                  | PMF $P(X=k)$                                               |
| :------------ | :------------------------ | :--------------------------------------------------------- |
| **Bernoulli** | $X \sim \text{Ber}(p)$    | $p^k(1-p)^{1-k}$ for $k \in \{0, 1\}$                      |
| **Binomial**  | $X \sim \text{Bin}(n, p)$ | $\binom{n}{k} p^k (1-p)^{n-k}$ for $k \in \{0, \dots, n\}$ |
| **Geometric** | $Y \sim \text{Geo}(p)$    | $(1-p)^{k-1} p$ for $k \in \{1, 2, \dots\}$                |
# Poisson Distribution & Joint PMFs

## Geometric Distribution (Recap)
> [!definition] 
> For any RV $Y$, we say $Y \sim \text{Geo}(p)$ if:
> $$P(Y=k) = (1-p)^{k-1}p \quad \text{for } k = 1, 2, 3, \dots$$

**Note:** This derivation is not strictly limited to Bernoulli sequences; it can be proven using the **Chain Rule**:
$$P(X_1=0, \dots, X_{k-1}=0, X_k=1) = P(X_k=1 | X_1=0, \dots, X_{k-1}=0) \dots P(X_1=0)$$

---

## The Poisson Distribution
> [!definition] 
> We say $X \sim \text{Poisson}(\lambda)$ for $\lambda \ge 0$ if:
> $$P(X=k) = e^{-\lambda} \frac{\lambda^k}{k!} \quad \text{for } k = 0, 1, \dots$$

**Sanity Check:**
$$\sum_{k=0}^\infty P(X=k) = e^{-\lambda} \sum_{k=0}^\infty \frac{\lambda^k}{k!} = e^{-\lambda} e^\lambda = 1$$
*(Using the Taylor series expansion $\sum \frac{x^k}{k!} = e^x$).*

---

## Poisson as the Limit of Binomial (Prop A)
**Theorem:** If $X_n \sim \text{Bin}(n, \frac{\lambda}{n})$ for $n=1, 2, \dots$, then for each $k$:
$$P(X_n=k) \xrightarrow{n \to \infty} e^{-\lambda} \frac{\lambda^k}{k!}$$

### Proof:
$$P(X_n=k) = \binom{n}{k} \left(\frac{\lambda}{n}\right)^k \left(1 - \frac{\lambda}{n}\right)^{n-k}$$
$$= \frac{n!}{k!(n-k)!} \frac{\lambda^k}{n^k} \left(1 - \frac{\lambda}{n}\right)^n \left(1 - \frac{\lambda}{n}\right)^{-k}$$
$$= \frac{\lambda^k}{k!} \left[ \frac{n}{n} \cdot \frac{n-1}{n} \cdot \dots \cdot \frac{n-k+1}{n} \right] \left(1 - \frac{\lambda}{n}\right)^n \left(1 - \frac{\lambda}{n}\right)^{-k}$$

As $n \to \infty$:
1. Each of the $k$ factors in the brackets $\to 1$.
2. $(1 - \frac{\lambda}{n})^n \to e^{-\lambda}$.
3. $(1 - \frac{\lambda}{n})^{-k} \to 1^{-k} = 1$.

Result: $P(X_n=k) \to \frac{\lambda^k}{k!} e^{-\lambda}$.

---

## Modeling with Poisson

### Example: Call Center
A center receives 1 call with $P = 1/1000$ every second, independent of other intervals.
* $n = 3600$ seconds in an hour.
* $Y \sim \text{Bin}(3600, 1/1000)$.
* $\lambda = np = 3.6$.

**Calculation:**
$P(Y=10) = \binom{3600}{10} (0.001)^{10} (0.999)^{3590}$
*This is computationally difficult!*
**Poisson Approximation:**
$$P(Y=10) \approx e^{-3.6} \frac{3.6^{10}}{10!}$$

### Common Poisson Applications:
* Number of clicks on a Geiger counter per minute.
* Number of mutations in a DNA strand.
* **Non-homogeneous Poisson:** When events in one interval don't affect the probability in another.

> [!warning] Bad Examples (Where Poisson Fails)
> **Buses at a stop:** Buses often arrive in "bunches" (close to each other). This violates the independence assumption or implies $p$ is not constant across intervals.

---

## Joint Probability Mass Functions (JPMF)
Used to describe the relationship between multiple RVs on the same probability space.

> [!definition] 
> The **Joint PMF** of $X_1, \dots, X_n$ is:
> $$p_{X_1, \dots, X_n}(k_1, \dots, k_n) = P(X_1=k_1, \dots, X_n=k_n)$$

### Marginal PMFs
The **Marginal PMF** of a single variable $X_i$ is recovered by summing out all other variables:
$$p_{X_1}(k_1) = P(X_1=k_1) = \sum_{k_2, k_3, \dots, k_n \in \mathbb{Z}} p_{X_1, \dots, X_n}(k_1, k_2, \dots, k_n)$$
*Intuition: To find the probability $X_1$ takes a certain value, sum over every "valid universe" of the other variables.*
# Joint Distributions & Independence Proofs

## Example: Uniform Discrete Joint Distribution
Consider the set of points $A_n = \{ (i, j) : i > 0, j > 0, i, j \in \mathbb{Z}, i + j \le n \}$.
Pick $(X, Y)$ uniformly from $A_n$.
$$P(X=i, Y=j) = \frac{1}{|A_n|} \text{ if } (i, j) \in A_n, \text{ else } 0$$

**Size of $A_n$:**
The number of points with sum $k$ is $k-1$.
$$|A_n| = \sum_{k=2}^n (k-1) = \frac{n(n-1)}{2}$$

**Marginal Distribution of $X$:**
$$p_X(i) = \sum_{j=1}^{n-i} p_{X,Y}(i, j) = \sum_{j=1}^{n-i} \frac{1}{|A_n|} = \frac{n-i}{|A_n|} = \frac{2(n-i)}{n(n-1)}$$
*Sanity Check:* $\sum_{i=1}^{n-1} p_X(i) = 1$.

---

## Independence & Factorization
> [!theory] Proposition
> $X_1, \dots, X_n$ are independent iff the joint PMF factors into the product of marginals:
> $$p_{X_1, \dots, X_n}(k_1, \dots, k_n) = \prod_{i=1}^n p_{X_i}(k_i)$$

**Proof (for $n=3$):**
Suppose $p(k_1, k_2, k_3) = h_1(k_1)h_2(k_2)h_3(k_3)$ where $\sum h_i(k) = 1$.
The marginal $p_1(k_1)$ is:
$$p_1(k_1) = \sum_{k_2, k_3} p(k_1, k_2, k_3) = h_1(k_1) \left(\sum_{k_2} h_2(k_2)\right) \left(\sum_{k_3} h_3(k_3)\right) = h_1(k_1) \cdot 1 \cdot 1 = h_1(k_1)$$
Thus, the joint PMF factors into the product of its marginals.

---

## Independent Geometric RVs in a Bernoulli Process
Let $X_1, X_2, \dots$ be i.i.d. $\text{Ber}(p)$.
* $Y_1$: Index of the 1st heads ($Y_1 \sim \text{Geo}(p)$).
* $Y_2$: Distance (gap) between the 1st and 2nd heads.
* $Y_k$: Gap between the $(k-1)$-th and $k$-th heads.

**Claim:** $Y_1, \dots, Y_n$ are independent.
The event $\{Y_1=k_1, \dots, Y_n=k_n\}$ corresponds to a sequence of $n$ blocks of [T...TH]:
$$P(Y_1=k_1, \dots, Y_n=k_n) = \underbrace{(1-p)^{k_1-1}p}_{h_1(k_1)} \times \dots \times \underbrace{(1-p)^{k_n-1}p}_{h_n(k_n)}$$
Since the joint PMF factors into valid Geometric PMFs, the $Y_i$ are i.i.d. $\text{Geo}(p)$.

> [!tip] Useful Identity
> $$P(Y_1 \ge k) = \sum_{j=k}^\infty p(1-p)^{j-1} = (1-p)^{k-1}$$
> *(Equivalently, the probability that the first $k-1$ tosses are all tails).*

---

## Conditional PMFs
> [!definition] 
> If $P(X=k) > 0$, the **conditional PMF** of $Y$ given $X=k$ is:
> $$p_{Y|X=k}(j) = \frac{P(X=k, Y=j)}{P(X=k)}$$
> Consequently: $p_{X,Y}(k, j) = p_{Y|X=k}(j) p_X(k)$.

### Example: Binomial to Hypergeometric
Let $X$ be total heads in $n$ tosses with prob $p$ ($X \sim \text{Bin}(n, p)$).
Let $Y$ be total heads in the first $M$ tosses ($M \le n$).
For $0 \le j \le M$ and $0 \le k \le n$:

**Joint PMF:**
Using independence of the first $M$ and last $n-M$ tosses:
$$P(X=k, Y=j) = P(Y=j, X-Y=k-j) = P(Y=j)P(X-Y=k-j)$$
$$= \binom{M}{j}p^j(1-p)^{M-j} \binom{n-M}{k-j}p^{k-j}(1-p)^{(n-M)-(k-j)}$$
$$= \binom{M}{j}\binom{n-M}{k-j} p^k (1-p)^{n-k}$$

**Conditional PMF:**
$$p_{Y|X=k}(j) = \frac{\binom{M}{j}\binom{n-M}{k-j} p^k (1-p)^{n-k}}{\binom{n}{k} p^k (1-p)^{n-k}} = \frac{\binom{M}{j}\binom{n-M}{k-j}}{\binom{n}{k}}$$
This is the **Hypergeometric Distribution**.
*Intuition:* Given there are $k$ total successes, the probability that $j$ of them occurred in the first $M$ trials depends only on the number of ways to arrange the successes, not the probability $p$.
# Continuous Random Variables

> [!definition] 
> A random variable $X$ is **discrete** if its range $X(\Omega)$ is finite or countable.
> A random variable $X$ is **continuous** if there exists a function $f: \mathbb{R} \to [0, \infty)$ such that for all $a \le b$:
> $$P(a \le X \le b) = \int_a^b f(x) \, dx$$
> The function $f$ is called the **Probability Density Function (PDF)** of $X$.

### Properties of the PDF
1. **Point Probability:** $P(X = x) = \int_x^x f(t) \, dt = 0$.
2. **Total Probability:** $P(-\infty < X < \infty) = 1 = \int_{-\infty}^{\infty} f(x) \, dx$.
3. **Density Logic:** If $f$ is continuous at $x$:
   $$f(x) = \lim_{\epsilon \to 0^+} \frac{1}{2\epsilon} \int_{x-\epsilon}^{x+\epsilon} f(y) \, dy = \lim_{\epsilon \to 0^+} \frac{1}{2\epsilon} P(x-\epsilon \le X \le x+\epsilon)$$

> [!canvas] Sketch: PDF Area
> (A smooth curve $f(x)$ with a shaded region between $x-\epsilon$ and $x+\epsilon$. The area of the shaded slice represents the probability, with the height at the center being $f(x)$.)

---

## Construction of Continuous RVs

### 1. Base-2 Representation
Consider an infinite sequence $X_1, X_2, \dots$ of i.i.d. $\text{Ber}(1/2)$ random variables. Define:
$$Z = \sum_{k=1}^\infty X_k 2^{-k} = 0.X_1X_2X_3 \dots \text{ (in base 2)}$$

* $P(1/2 \le Z \le 1) = P(X_1 = 1) = 1/2$
* $P(1/2 < Z \le 3/4) = P(X_1 = 1, X_2 = 0) = 1/4$

For any $a, b \in [0, 1]$ of the form $j/2^n$:
$$P(a \le X \le b) = b - a = \int_a^b 1 \, dx$$
This defines the **Uniform([0, 1])** distribution with PDF:
$$f_Z(x) = \begin{cases} 1 & \text{if } x \in [0, 1] \\ 0 & \text{otherwise} \end{cases}$$

### 2. General PDF Construction
**Goal:** Find a probability space $(\Omega, P)$ and $X: \Omega \to \mathbb{R}$ such that $X$ has a given PDF $f$.
* Let $\Omega = \mathbb{R}$.
* Let $P(A) = \int_A f(x) \, dx$.
* By the properties of the integral, $(\Omega, P)$ is a valid probability space.
* Define $X(w) = w$.
Then:
$$P(a \le X \le b) = P(\{w \in \mathbb{R} : a \le X(w) \le b\}) = P([a, b]) = \int_a^b f(x) \, dx$$

---

## Common Continuous Distributions

1. **Uniform($[a, b]$):**
   $$f_X(x) = \begin{cases} \frac{1}{b-a} & \text{if } x \in [a, b] \\ 0 & \text{else} \end{cases}$$

2. **Exponential($\lambda$):**
   $$f_X(x) = \begin{cases} \lambda e^{-\lambda x} & \text{if } x > 0 \\ 0 & \text{else} \end{cases}$$

3. **Normal / Gaussian ($N(\mu, \sigma^2)$):**
   With mean $\mu$ and standard deviation $\sigma > 0$:
   $$f_X(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

---

## Proof: The Gaussian Integral
We want to show that the Gaussian PDF integrates to 1. Let:
$$I = \int_{-\infty}^{\infty} f_X(x) \, dx$$
Consider $I^2$ (treating $X$ and $Y$ as independent):
$$I^2 = \int_{-\infty}^{\infty} f(x) \, dx \int_{-\infty}^{\infty} f(y) \, dy = \iint_{\mathbb{R}^2} f(x)f(y) \, dx \, dy$$
Using the Normal PDF (simplified with $\mu=0, \sigma=1$ for translation invariance):
$$I^2 = \frac{1}{2\pi\sigma^2} \iint_{\mathbb{R}^2} e^{-\frac{1}{2\sigma^2}(x^2+y^2)} \, dx \, dy$$

### Switch to Polar Coordinates
Let $x = r\cos\theta, y = r\sin\theta$. This provides a bijection between $(r, \theta) \in (0, \infty) \times [0, 2\pi)$ and $\mathbb{R}^2 \setminus \{(0,0)\}$.
**Jacobian Matrix:**
$$J = \det \begin{bmatrix} \frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} \\ \frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta} \end{bmatrix} = \det \begin{bmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{bmatrix}$$
$$J = r\cos^2\theta + r\sin^2\theta = r$$

**Integration:**
$$I^2 = \frac{1}{2\pi\sigma^2} \int_0^{2\pi} \int_0^{\infty} e^{-\frac{1}{2\sigma^2}r^2} r \, dr \, d\theta$$
Let $u = \frac{1}{2\sigma^2}r^2 \implies du = \frac{1}{\sigma^2}r \, dr$:
$$I^2 = \frac{1}{2\pi} \int_0^{2\pi} \int_0^{\infty} e^{-u} \, du \, d\theta$$
Since $\int_0^{\infty} e^{-u} \, du = 1$:
$$I^2 = \frac{1}{2\pi} \int_0^{2\pi} (1) \, d\theta = \frac{2\pi}{2\pi} = 1$$
**Conclusion:** The Gaussian is integrable and equal to 1.
# Cumulative Distribution Functions (CDF)

> [!definition] 
> The **Cumulative Distribution Function (CDF)** of any random variable $X$ is defined as:
> $$F_X(x) = P(X \le x)$$

### Fundamental Properties
1. **Monotonicity:** $F(s) \le F(t)$ if $s \le t$.
2. **Asymptotes:** * $\lim_{t \to \infty} F(t) = 1$
   * $\lim_{t \to -\infty} F(t) = 0$
3. **Right-Continuity:** Limits exist from the right: $\lim_{u \to t^+} F(u) = F(t)$.

> [!canvas] Sketch: CDF of Poisson
> (A step function starting at $e^{-\lambda}$ for $x=0$, with open circles on the left and closed circles on the right of each step, showing right-continuity.)

---

## Relation to PDF
For a continuous random variable $X$ with PDF $f$:
$$F_X(t) = \int_{-\infty}^t f(x) \, dx$$

By the **Fundamental Theorem of Calculus (FTOC)**, if $f$ is continuous at $t$:
$$f(t) = \frac{d}{dt} F_X(t)$$

### Point Probabilities in Continuous RVs
For any continuous RV where the CDF is differentiable:
Let $\epsilon > 0$. 
$$P(X=a) \le P(a-\epsilon \le X \le a) = F(a) - F(a-\epsilon)$$
Taking the limit as $\epsilon \to 0$:
$$P(X=a) \le F_X(a) - F_X(a) = 0 \implies P(X=a) = 0$$

> [!tip] 
> For continuous variables, $P(a \le X \le b) = P(a < X \le b) = F_X(b) - F_X(a)$.

---

## Transformations of Random Variables (The CDF Method)

When you have a random variable $X$ and define a new variable $Y = g(X)$, the most reliable way to find the PDF of $Y$ is to first find its CDF.

### Example 1: Square of a Uniform RV
Let $X \sim \text{Unif}([0, 1])$ and $Y = X^2$. Find the PDF of $Y$.

1. **Find the CDF of $Y$:** For $t \in (0, 1)$:
   $$P(Y \le t) = P(X^2 \le t) = P(X \le \sqrt{t}) = F_X(\sqrt{t})$$
2. **Differentiate to find the PDF:**
   Since $F_X(x) = x$ for $x \in [0, 1]$:
   $$f_Y(t) = \frac{d}{dt} F_X(\sqrt{t}) = F'_X(\sqrt{t}) \cdot \frac{d}{dt}(\sqrt{t})$$
   $$f_Y(t) = 1 \cdot \frac{1}{2\sqrt{t}} = \frac{1}{2\sqrt{t}} \quad \text{for } t \in (0, 1)$$

### Example 2: Negative Log of a Uniform RV
Find the law of $Z = -\log(X)$ where $X \sim \text{Unif}([0, 1])$.

1. **CDF Calculation:**
   $$P(Z \le z) = P(-\log(X) \le z) = P(\log(X) \ge -z) = P(X \ge e^{-z})$$
   $$F_Z(t) = 1 - P(X < e^{-t}) = 1 - F_X(e^{-t})$$
2. **PDF Calculation:**
   Let $V(t) = e^{-t}$. Then $F_Z(t) = 1 - F_X(V(t))$.
   $$f_Z(t) = \frac{d}{dt} [1 - F_X(V(t))] = -F'_X(V(t)) \cdot V'(t)$$
   Since $F'_X(V(t)) = 1$ (for $V(t) \in [0, 1]$) and $V'(t) = -e^{-t}$:
   $$f_Z(t) = -1 \cdot (-e^{-t}) = e^{-t}$$
3. **Determine Support:**
   $V(t) \in [0, 1] \implies e^{-t} \le 1 \implies t \ge 0$.

**Conclusion:** $Z \sim \text{Exp}(1)$.

# Transformations & Joint Distributions

## General Transformation Rule
**Proposition:** Let $X$ be a continuous RV. Let $u: \mathbb{R} \to \mathbb{R}$ be a function that is either strictly increasing or strictly decreasing on the support of $X$ (so the inverse is well-defined). If $u$ is also differentiable except for finitely many points, then $Z = u(X)$ is continuous with PDF:
$$f_Z(z) = f_X(v(z)) \cdot |v'(z)|$$
where $v$ is the inverse of $u$.

> [!info] 
> The $|v'(z)|$ term (absolute value of the derivative of the inverse) ensures the PDF remains non-negative, which is necessary when dealing with decreasing functions.

> [!canvas] Sketch: Density Transformation
> (Diagram showing a density $f_X$ being mapped through $u$ to $f_Z$. The area must be preserved; because the width of the interval changes by the derivative, we divide by the derivative of the transformation—or multiply by the derivative of the inverse—to correct the area).

---

## Transformation Examples

### 1. Scaling an Exponential RV
Let $X \sim \text{Exp}(\lambda)$ and $Z = \alpha X$ for $\alpha > 0$.
* $u(x) = \alpha x \implies v(z) = \frac{z}{\alpha} \implies v'(z) = \frac{1}{\alpha}$
$$f_Z(z) = f_X\left(\frac{z}{\alpha}\right) \cdot \frac{1}{\alpha} = \frac{\lambda}{\alpha} e^{-\lambda \frac{z}{\alpha}} \quad \text{for } z \ge 0$$
**Result:** $Z \sim \text{Exp}\left(\frac{\lambda}{\alpha}\right)$.

### 2. Absolute Value of a Normal RV
Let $X \sim N(0, \sigma^2)$ and $Z = |X|$. 
*Note: $u(x) = |x|$ is not strictly monotonic on the support of $X$.*
$$F_Z(t) = P(|X| \le t) = P(-t \le X \le t) = F_X(t) - F_X(-t)$$
Differentiating gives:
$$f_Z(t) = f_X(t) + f_X(-t)$$
Since the Normal PDF is symmetric about 0, $f_X(-t) = f_X(t)$:
$$f_Z(t) = 2f_X(t) \quad \text{for } t > 0$$

### 3. Linear Transformation of a Normal RV
**Exercise:** If $X \sim N(\mu, \sigma^2)$, then $Y = aX + b \sim N(a\mu + b, a^2\sigma^2)$.
*(To be proven later).*

---

## Pathological / Mixed Distributions
Some distributions have a continuous CDF but are not differentiable everywhere.
**Example:** $X_i \sim \text{Ber}(1/2)$ i.i.d.
$$Z = \sum_{i=1}^\infty (2X_i) 3^{-i}$$
$Z$ lives in the **Cantor Set**. This distribution has a continuous CDF but it is not differentiable (it has no PDF in the standard sense).

---

## Joint Probability Density Functions
We say $(X_1, X_2, \dots, X_n)$ is a **jointly continuous** random vector if there exists a function $f: \mathbb{R}^n \to [0, \infty)$ such that for any "nice" set $A \subseteq \mathbb{R}^n$:
$$P((X_1, \dots, X_n) \in A) = \iint \dots \int_A f(x_1, \dots, x_n) \, dx_1 \dots dx_n$$

**Consequences:**
1. Total integral must equal 1: $\int_{\mathbb{R}^n} f = 1$.
2. **Marginalization:** Given a joint PDF $f(x_1, \dots, x_n)$, the marginal PDF of $X_1$ is:
$$f_{X_1}(x_1) = \int_{\mathbb{R}^{n-1}} f(x_1, \dots, x_n) \, dx_2 \dots dx_n$$

---

## Example: Uniform Distribution on a Disk
Let $(X, Y)$ be distributed uniformly on the unit disk $D = \{ (x, y) : x^2 + y^2 \le 1 \}$.
The joint PDF is $f(x, y) = \frac{1}{\pi}$ inside the disk and 0 otherwise.

**Find the marginal PDF of $X$:**
For a fixed $x \in [-1, 1]$, $Y$ ranges from $-\sqrt{1-x^2}$ to $\sqrt{1-x^2}$.
$$f_X(x) = \int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}} \frac{1}{\pi} \, dy = \frac{2\sqrt{1-x^2}}{\pi}$$

> [!canvas] Sketch: Disk Marginal
> (Circle with a vertical slice at $x$. The length of this slice represents the "density" of $X$ at that point).

# Independence, Conditional PDFs, and Random Vectors

## Independence of Continuous RVs
> [!definition] 
> Jointly continuous RVs $X_1, \dots, X_n$ with joint PDF $f$ are **independent** if:
> $$f(x_1, \dots, x_n) = f_1(x_1)f_2(x_2)\dots f_n(x_n)$$
> where each $f_i$ is the marginal PDF of $X_i$.

**Consequence:** For any sets $B_1, \dots, B_n \in \mathbb{R}$:
$$P(X_1 \in B_1, \dots, X_n \in B_n) = P(X_1 \in B_1)P(X_2 \in B_2)\dots P(X_n \in B_n)$$

### Factorization Theorem
If the joint PDF can be factored into functions of individual variables, they are independent.
i.e., if $f(x_1, \dots, x_n) = h_1(x_1)h_2(x_2)\dots h_n(x_n)$, then $X_i$ are independent.
* **Proof Gist:** Let $C_i = \int_{-\infty}^{\infty} h_i(x) \, dx$. We can normalize each function by setting $\tilde{h}_i(x) = \frac{h_i(x)}{C_i}$, which then equals the marginal PDF $f_i(x)$.

---

## Example: Uniform Independence
1.  **Independent Case:** If $(X, Y) \sim \text{Unif}([0, 1] \times [0, 1])$, then $X \perp Y$.
2.  **Dependent Case:** If $(X, Y) \sim \text{Unif}(D)$ where $D$ is a disk or a triangle, $X$ and $Y$ are **dependent** because the joint PDF cannot be factored into two separate cases (the support of $Y$ depends on $X$).

---

## Conditional PDFs
> [!definition] 
> The **conditional PDF** of $Y$ given $X=x$ is:
> $$f_{Y|X=x}(y) = \frac{f_{X,Y}(x, y)}{f_X(x)} \quad \text{if } f_X(x) > 0$$

**Intuition:**
$$P(y-\epsilon \le Y \le y+\epsilon | X \in [x-\epsilon, x+\epsilon]) = \frac{\int_{x-\epsilon}^{x+\epsilon} \int_{y-\epsilon}^{y+\epsilon} f_{X,Y} \, ds \, dt}{\int_{x-\epsilon}^{x+\epsilon} f_X(s) \, ds} \approx \frac{(2\epsilon)^2 f_{X,Y}(x, y)}{(2\epsilon) f_X(x)} = 2\epsilon f_{Y|X=x}(y)$$

### Law of Total Probability (Continuous Version)
For any set $A \in \mathbb{R}^2$:
$$P((X, Y) \in A) = \int_{-\infty}^{\infty} f_X(x) P((X, Y) \in A | X=x) \, dx$$
Where $P((X, Y) \in A | X=x) = \int_{\{y: (x,y) \in A\}} f_{Y|X=x}(y) \, dy$.

---

## Transforming Random Vectors
**Theorem:** Let $X = (X_1, \dots, X_n)$ be a random vector with joint PDF $f_X$. Let $Y = u(X)$ where $u: \mathbb{R}^n \to \mathbb{R}^n$ is smooth, differentiable, and injective (1-to-1). Let $v = u^{-1}$ be the inverse function. 
The joint PDF of $Y$ is:
$$f_Y(y) = f_X(v(y)) | \det J_v(y) |$$
where $J_v(y)$ is the **Jacobian matrix** of the inverse function $v$.

### Case 1: Sum of Two RVs ($Z = X + Y$)
To find the PDF of $Z$, we use a dummy variable $W = X$.
1.  Transformation: $u(x, y) = (x+y, x) = (z, w)$.
2.  Inverse: $v(z, w) = (w, z-w) = (x, y)$.
3.  Jacobian of $v$: $J_v(z, w) = \begin{bmatrix} 0 & 1 \\ 1 & -1 \end{bmatrix} \implies | \det J | = 1$.
4.  Joint PDF: $f_{Z,W}(z, w) = f_{X,Y}(w, z-w)$.
5.  Marginal: $f_Z(z) = \int_{-\infty}^{\infty} f_{X,Y}(w, z-w) \, dw$.

> [!important] Convolution
> If $X \perp Y$, then $f_Z(z) = \int_{-\infty}^{\infty} f_X(w) f_Y(z-w) \, dw = (f_X * f_Y)(z)$.

### Case 2: Product of Two RVs ($Z = XY$)
Let $W = X$. Inverse: $x=w, y=z/w$.
Jacobian $J_v(z, w) = \begin{bmatrix} 0 & 1 \\ 1/w & -z/w^2 \end{bmatrix} \implies | \det J | = |1/w|$.
$$f_Z(z) = \int_{-\infty}^{\infty} f_{X,Y}(w, z/w) \left| \frac{1}{w} \right| \, dw$$

---

## Gamma Random Variables
> [!definition] 
> We say $X \sim \Gamma(n, \lambda)$ if:
> $$f_X(x) = \frac{\lambda^n x^{n-1} e^{-\lambda x}}{(n-1)!} \quad \text{for } x > 0$$

### Sum of i.i.d. Exponentials
**Proposition:** If $X_1, \dots, X_n \sim \text{Exp}(\lambda)$ are i.i.d., then $Z = \sum_{i=1}^n X_i \sim \Gamma(n, \lambda)$.

**Proof (by induction on $n$):**
* Base Case ($n=1$): $\Gamma(1, \lambda) = \lambda e^{-\lambda x} = \text{Exp}(\lambda)$.
* Inductive Step: Assume $W = \sum_{i=1}^{n-1} X_i \sim \Gamma(n-1, \lambda)$. Let $Z = W + X_n$.
Using convolution:
$$f_Z(z) = \int_0^z f_W(w) f_{X_n}(z-w) \, dw = \int_0^z \frac{\lambda^{n-1} w^{n-2} e^{-\lambda w}}{(n-2)!} \cdot \lambda e^{-\lambda(z-w)} \, dw$$
Factor out terms not dependent on $w$:
$$= \frac{\lambda^n e^{-\lambda z}}{(n-2)!} \int_0^z w^{n-2} \, dw = \frac{\lambda^n e^{-\lambda z}}{(n-2)!} \left[ \frac{w^{n-1}}{n-1} \right]_0^z = \frac{\lambda^n e^{-\lambda z} z^{n-1}}{(n-1)!}$$
# Expectation & Linearity of Expectation

## Expectation for Discrete RVs
> [!definition] 
> For a discrete random variable $X$, we define the **expectation** as:
> $$E[X] = \sum_{k \in \mathbb{R}} k \cdot p_X(k)$$
> This holds provided the sum is **absolutely convergent**, i.e., $\sum |k| p_X(k) < \infty$.

### Frequentist Perspective
If $X$ has finite support $\{k_1, k_2, \dots, k_n\}$:
$$E[X] = \sum_{k=1}^n k P(X=k) \approx \sum_k k \cdot \frac{\text{# of times } X=k}{\text{# of experiments}}$$
$$= \frac{\sum (\text{# of } X=k) \cdot k}{\text{# of experiments}} \implies \text{Long run average of } X \text{ as you repeat experiments.}$$

*Note: $E[X]$ depends only on the **law** of $X$.*

### Discrete Examples
1. **Bernoulli:** $X \sim \text{Ber}(p)$
   $$E[X] = 0(1-p) + 1(p) = p$$
   *Note: $E[X]$ does not have to be in the support of $X$.*

2. **Binomial:** $X \sim \text{Bin}(n, p)$
   $$E[X] = \sum_{k=0}^n k \binom{n}{k} p^k (1-p)^{n-k} = \sum_{k=1}^n k \frac{n!}{k!(n-k)!} p^k (1-p)^{n-k}$$
   Using the identity $k \binom{n}{k} = n \binom{n-1}{k-1}$:
   $$= n \sum_{k=1}^n \binom{n-1}{k-1} p^k (1-p)^{n-k} = np \sum_{j=0}^{n-1} \binom{n-1}{j} p^j (1-p)^{n-1-j}$$
   Since the sum of the PMF for $\text{Bin}(n-1, p)$ is 1:
   $$E[X] = np$$

3. **Geometric:** $X \sim \text{Geo}(p)$
   $$E[X] = \sum_{k=1}^\infty k(1-p)^{k-1}p = p \sum_{k=1}^\infty k(1-p)^{k-1}$$
   Using the power series $f(x) = \sum_{k=0}^\infty x^k = \frac{1}{1-x} \implies f'(x) = \sum_{k=1}^\infty kx^{k-1} = \frac{1}{(1-x)^2}$:
   $$E[X] = p \cdot \frac{1}{(1-(1-p))^2} = \frac{p}{p^2} = \frac{1}{p}$$

4. **Poisson:** $X \sim \text{Poisson}(\lambda)$
   $$E[X] = \sum_{k=0}^\infty k \frac{e^{-\lambda} \lambda^k}{k!} = e^{-\lambda} \sum_{k=1}^\infty \frac{\lambda^k}{(k-1)!} = \lambda e^{-\lambda} \sum_{j=0}^\infty \frac{\lambda^j}{j!} = \lambda e^{-\lambda} e^\lambda = \lambda$$

---

## Expectation for Continuous RVs
> [!definition] 
> If $X$ is a continuous RV, then:
> $$E[X] = \int_{-\infty}^{\infty} x f_X(x) \, dx$$
> provided $\int |x| f_X(x) \, dx < \infty$.

### Continuous Examples
1. **Uniform:** $X \sim \text{Unif}(a, b)$
   $$E[X] = \int_a^b x \cdot \frac{1}{b-a} \, dx = \frac{1}{b-a} \cdot \frac{1}{2} x^2 \Big|_a^b = \frac{b^2 - a^2}{2(b-a)} = \frac{a+b}{2}$$

2. **Exponential:** $X \sim \text{Exp}(\lambda)$
   $$E[X] = \int_0^\infty x \lambda e^{-\lambda x} \, dx = \lambda \left[ \frac{x}{-\lambda} e^{-\lambda x} - \frac{1}{\lambda^2} e^{-\lambda x} \right]_0^\infty = \lambda \left( 0 - (0 - \frac{1}{\lambda^2}) \right) = \frac{1}{\lambda}$$

3. **Cauchy:** $f_X(x) = \frac{1}{\pi(x^2 + 1)}$
   $$E[X] = \int_{-\infty}^\infty \frac{x}{\pi(x^2 + 1)} \, dx$$
   The integral is **not absolutely convergent** because $|x|/x^2 \sim 1/x$, which diverges. 
   **Intuition:** The distribution is "too heavy-tailed." Even though it is symmetric around 0, the limit $\lim_{a, b \to \infty} \int_{-a}^b$ depends on the rates at which $a$ and $b$ approach infinity. Thus, $E[X]$ does not exist.

4. **Normal:** $X \sim N(\mu, \sigma^2)$
   $$E[X] = \int_{-\infty}^\infty x \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \, dx$$
   Let $w = x - \mu$:
   $$= \int_{-\infty}^\infty (w + \mu) \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{w^2}{2\sigma^2}} \, dw$$
   $$= \underbrace{\int_{-\infty}^\infty w \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{w^2}{2\sigma^2}} \, dw}_{0 \text{ (Odd function)}} + \mu \underbrace{\int_{-\infty}^\infty \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{w^2}{2\sigma^2}} \, dw}_{1 \text{ (Valid PDF)}}$$
   $$E[X] = \mu$$

---

## Law of the Unconscious Statistician (LOTUS)
**Question:** How do we find $E[u(X)]$ without first finding the PDF/PMF of $u(X)$?

> [!proposition] 
> If $X_1, \dots, X_n$ are discrete RVs and $Y = u(X_1, \dots, X_n)$, then:
> $$E[u(X)] = \sum_{x_1, \dots, x_n} u(x_1, \dots, x_n) p_{X_1, \dots, X_n}(x_1, \dots, x_n)$$
> For the continuous case:
> $$E[u(X)] = \int_{\mathbb{R}^n} u(x_1, \dots, x_n) f_{X_1, \dots, X_n}(x_1, \dots, x_n) \, dx_1 \dots dx_n$$

### Proof (Discrete Case)
$$E[Y] = \sum_y y P(Y=y) = \sum_y y \sum_{x: u(x)=y} P(X=x)$$
$$= \sum_y \sum_{x: u(x)=y} u(x) P(X=x) = \sum_{x} u(x) P(X=x)$$
The sum over all $x$ is the same as partitioning the sum by their output $y$ and then summing over all possible $y$.

---

## Linearity of Expectation
> [!proposition] 
> Let $X_1, \dots, X_n$ be random variables. For any $a_i \in \mathbb{R}$:
> $$E[a_0 + a_1 X_1 + \dots + a_n X_n] = a_0 + a_1 E[X_1] + \dots + a_n E[X_n]$$
> **Crucially:** The random variables do **NOT** have to be independent. All you need is the existence of the individual expectations.

### Proof (Discrete $n=2$ Case)
$$E[a_0 + a_1 X_1 + a_2 X_2] = \sum_{x_1, x_2} (a_0 + a_1 x_1 + a_2 x_2) p_{X_1, X_2}(x_1, x_2)$$
$$= a_0 \sum p + a_1 \sum x_1 p_{X_1, X_2} + a_2 \sum x_2 p_{X_1, X_2}$$
Using marginalization ($\sum_{x_2} p_{X_1, X_2} = p_{X_1}$):
$$= a_0 + a_1 \sum_{x_1} x_1 p_{X_1}(x_1) + a_2 \sum_{x_2} x_2 p_{X_2}(x_2) = a_0 + a_1 E[X_1] + a_2 E[X_2]$$

### Example: Binomial Expectation (Indicator Trick)
Let $X \sim \text{Bin}(n, p)$. We can view $X$ as a sum of $n$ Bernoulli trials.
Define the **Indicator Random Variable** for the $i$-th trial:
$$1_{A_i} = \begin{cases} 1 & \text{if } i\text{-th flip is heads} \\ 0 & \text{else} \end{cases}$$
$1_{A_i} \sim \text{Ber}(p)$, so $E[1_{A_i}] = p$.
Then $X = \sum_{i=1}^n 1_{A_i}$. By Linearity:
$$E[X] = E\left[\sum_{i=1}^n 1_{A_i}\right] = \sum_{i=1}^n E[1_{A_i}] = \sum_{i=1}^n p = np$$
# Indicators and Advanced Expectation

### Gamma Distribution Expectation
Using the property that a Gamma random variable is the sum of $n$ i.i.d. Exponentials:
If $X \sim \Gamma(n, \lambda)$, then $X \sim \sum_{i=1}^n Y_i$ where $Y_i \sim \text{Exp}(\lambda)$.
$$E[X] = \sum_{i=1}^n E[Y_i] = n E[Y_1] = \frac{n}{\lambda}$$

---

## The Indicator Method
For an event $A \subseteq \Omega$, the **Indicator Random Variable** $1_A$ is defined as:
$$1_A(\omega) = \begin{cases} 1 & \text{if } \omega \in A \\ 0 & \text{else} \end{cases}$$

**Properties:**
* $1_A \sim \text{Ber}(P(A))$
* $E[1_A] = P(A)$
* $1_{A \cap B} = 1_A 1_B$
* $1_{A \cup B} = 1_A + 1_B - 1_{A \cap B}$ (Relates to the Inclusion-Exclusion principle)

---

## Example: The Mailbox Problem
**Problem:** Place $n$ letters into $n$ mailboxes randomly such that every box contains exactly one letter. What is the expected number of correctly delivered letters?

Let $X$ be the number of correct deliveries.
Let $A_i$ be the event that letter $i$ goes to box $i$.
$X = \sum_{i=1}^n 1_{A_i}$

By Linearity of Expectation:
$$E[X] = \sum_{i=1}^n P(A_i) = n \cdot \left(\frac{1}{n}\right) = 1$$
> [!check] Result
> On average, you expect exactly 1 letter to go to the correct box, regardless of $n$.

---

## Example: Balls into Bins
**Problem:** $n$ balls are dropped into $n$ bins uniformly and independently. Let $X$ be the number of empty bins.

Let $1_i$ be the indicator that bin $i$ is empty.
$X = \sum_{i=1}^n 1_i$

For a bin to be empty, all $n$ balls must "miss" it.
$P(1_i = 1) = \left(1 - \frac{1}{n}\right)^n$

$$E[X] = \sum_{i=1}^n P(1_i = 1) = n \left(1 - \frac{1}{n}\right)^n$$
**Asymptotic behavior:** For large $n$, $\left(1 - \frac{1}{n}\right)^n \to e^{-1}$.
$$E[X] \approx \frac{n}{e}$$

---

## Example: Runs of Heads
**Problem:** Toss a fair coin $n$ times. Let $X$ be the number of "runs" of heads (a sequence of consecutive heads).
*e.g., HHHTHTHHT contains 3 runs.*

Define indicators $A_i$ for $i=1 \dots n$:
* $A_1$: First flip is heads. $P(A_1) = p$
* $A_i$ (for $i > 1$): The $i$-th flip starts a new run. This happens if the $i$-th flip is $H$ and the $(i-1)$-th flip was $T$.
$$P(A_i) = P(i\text{-th is } H \cap (i-1)\text{-th is } T) = p(1-p)$$

$$E[X] = P(A_1) + \sum_{i=2}^n P(A_i) = p + (n-1)p(1-p)$$

---

## Expectation of Independent RVs

> [!theory] Proposition
> If $X_1, \dots, X_n$ are independent random variables, then:
> $$E\left[\prod_{i=1}^n X_i\right] = \prod_{i=1}^n E[X_i]$$

**Remark:** Independence is invariant under transformations. If $X_i$ are independent, then $g_i(X_i)$ are also independent.
**Remark (Indicators):** If $X_1 = 1_A$ and $X_2 = 1_B$, then $X_1 X_2 = 1_{A \cap B}$.
* $E[X_1 X_2] = P(A \cap B)$
* $E[X_1]E[X_2] = P(A)P(B)$
* Independence of $A$ and $B$ is equivalent to $E[X_1 X_2] = E[X_1]E[X_2]$.

### Proof (Discrete Case)
Assume $X_i$ have PMFs $p_i$.
$$E[X_1 \dots X_n] = \sum_{x_1 \dots x_n} (x_1 \dots x_n) P(X_1=x_1, \dots, X_n=x_n)$$
By independence:
$$= \sum_{x_1} \dots \sum_{x_n} (x_1 p_1(x_1)) \dots (x_n p_n(x_n))$$
$$= \left(\sum_{x_1} x_1 p_1(x_1)\right) \dots \left(\sum_{x_n} x_n p_n(x_n)\right) = E[X_1] \dots E[X_n]$$
# Advanced Expectation, Variance & Covariance

## Tail Integral (Layer-Cake Formula)
> [!theory] Proposition
> If $X$ is a non-negative random variable ($X \ge 0$):
> 1. If $X$ is continuous: $E[X] = \int_0^\infty P(X > t) \, dt$
> 2. If $X$ is discrete (taking values in $\mathbb{Z}^{\ge 0}$): $E[X] = \sum_{k=0}^\infty P(X > k)$

**Example: Exponential Distribution**
Let $X \sim \text{Exp}(\lambda)$. We know $P(X > t) = e^{-\lambda t}$.
$$E[X] = \int_0^\infty e^{-\lambda t} \, dt = \left[ -\frac{1}{\lambda} e^{-\lambda t} \right]_0^\infty = \frac{1}{\lambda}$$

**Proof Idea (using Fubini's Theorem):**
Represent $X$ as an integral of an indicator: $X(\omega) = \int_0^\infty 1_{\{X(\omega) > t\}} \, dt$.
$$E[X] = E\left[ \int_0^\infty 1_{\{X > t\}} \, dt \right] = \int_0^\infty E[1_{\{X > t\}}] \, dt = \int_0^\infty P(X > t) \, dt$$
*Basically, we are changing the order of integration/expectation.*

---

## Random Vectors & Conditional Expectation

### Mean of a Random Vector
For $X = (X_1, \dots, X_n) \in \mathbb{R}^n$, we define:
$$E X = (E[X_1], \dots, E[X_n]) \in \mathbb{R}^n$$
**Property:** For an $m \times n$ matrix $A$ and vector $M \in \mathbb{R}^m$:
$$E[M + AX] = M + A E[X]$$

### Conditional Expectation
> [!definition] 
> 1. **Discrete:** $E[Y|X=x] = \sum_y y P(Y=y | X=x)$
> 2. **Continuous:** $E[Y|X=x] = \int_{-\infty}^\infty y f_{Y|X=x}(y) \, dy$

**As a Random Variable:**
Define $g(x) = E[Y|X=x]$. Then $E[Y|X] = g(X)$ is itself a random variable.
*Intuition:* $E[Y|X]$ is the "best guess" of $Y$ given only the information in $X$.

> [!theory] The Tower Property
> $$E[E[Y|X]] = E[Y]$$
> **Proof (Discrete):**
> $\sum_x E[Y|X=x] P(X=x) = \sum_x \left( \sum_y y \frac{P(Y=y, X=x)}{P(X=x)} \right) P(X=x)$
> $= \sum_x \sum_y y P(Y=y, X=x) = \sum_y y P(Y=y) = E[Y]$

### Properties
* **Taking out what is known:** $E[h(X)Y | X] = h(X) E[Y|X]$
* **Independence:** If $X \perp Y$, then $E[Y|X] = E[Y]$.

---

## Variance of a Random Variable
> [!definition] 
> The **Variance** of $X$ measures the expected square distance from its mean:
> $$\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$$
> *Note: $\text{Var}(X) \ge 0$ always.*

### Proof of the Identity:
$E[(X - E[X])^2] = E[X^2 - 2X E[X] + (E[X])^2]$
$= E[X^2] - 2(E[X])E[X] + (E[X])^2 = E[X^2] - (E[X])^2$

### Variance Examples
1. **Bernoulli($p$):** $E[X]=p, E[X^2]=p \implies \text{Var}(X) = p - p^2 = p(1-p)$
2. **Uniform($a, b$):** $E[X^2] = \frac{b^3-a^3}{3(b-a)} \implies \text{Var}(X) = \frac{(b-a)^2}{12}$
3. **Exponential($\lambda$):** $E[X^2] = 2/\lambda^2 \implies \text{Var}(X) = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}$
4. **Geometric($p$):**
   Using $E[X(X-1)] = \sum k(k-1)(1-p)^{k-1}p = \frac{2(1-p)}{p^2}$:
   $E[X^2] = E[X(X-1)] + E[X] = \frac{2(1-p)}{p^2} + \frac{1}{p}$
   $\text{Var}(X) = \frac{1-p}{p^2}$

---

## Covariance
**Note:** $\text{Var}(bX + c) = b^2 \text{Var}(X)$. Variance is **not** linear.

> [!definition] 
> The **Covariance** of $X$ and $Y$ is:
> $$\text{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$$
> *Note: $\text{Cov}(X, X) = \text{Var}(X)$.*

### Bilinearity of Covariance
If $U = \sum a_i X_i$ and $V = \sum b_j Y_j$:
$$\text{Cov}(U, V) = \sum_i \sum_j a_i b_j \text{Cov}(X_i, Y_j)$$
*Covariance is a **bilinear** function.*
# Covariance Properties & Fundamental Inequalities

## Bilinearity of Covariance
**Proof (by Linearity of Expectation):**
Let $U = \sum a_i X_i$ and $V = \sum b_j Y_j$.
$$E[UV] = E\left[ \left(\sum a_i X_i\right) \left(\sum b_j Y_j\right) \right] = \sum_{i=1}^n \sum_{j=1}^m a_i b_j E[X_i Y_j]$$
Since $E[U] = \sum a_i E[X_i]$ and $E[V] = \sum b_j E[Y_j]$, we have:
$$E[U]E[V] = \sum_i \sum_j a_i b_j E[X_i]E[Y_j]$$
Thus:
$$\text{Cov}(U, V) = E[UV] - E[U]E[V] = \sum_i \sum_j a_i b_j \text{Cov}(X_i, Y_j)$$

> [!important] Remark
> $\text{Cov}(X, Y) = \text{Cov}(Y, X)$ (Symmetry).

---

## Inequalities of Expectation

### 1. Monotonicity
If $X$ is a random variable such that $X \ge 0$ (meaning $X(\omega) \ge 0$ for all $\omega \in \Omega$):
$$E[X] \ge 0$$
* **Proof (Discrete):** $E[X] = \sum_{x \ge 0} x P(X=x) \ge 0$.
* **Proof (Continuous):** $E[X] = \int_0^\infty x f_x(x) \, dx \ge 0$.

**Corollary:** If $X \ge Y$ almost surely, then $E[X - Y] \ge 0 \implies E[X] \ge E[Y]$.

### 2. Moment Inequalities
* **Observation:** Since $|X| \ge X$ and $|X| \ge -X$, monotonicity implies $E[|X|] \ge E[X]$ and $E[|X|] \ge -E[X]$. Thus:
$$|E[X]| \le E[|X|]$$
* **Variance Bound:** Since $\text{Var}(X) \ge 0 \implies E[X^2] - (E[X])^2 \ge 0$:
$$(E[X])^2 \le E[X^2] \implies |E[X]| \le \sqrt{E[X^2]}$$

### 3. Generalization (Lyapunov's Inequality)
For any $k \ge 1$:
$$|E[X]| \le (E[|X|^k])^{1/k}$$
* **Proof Sketch:** For $y \ge 0$, use the bound $y \le \frac{y^k}{k} + 1 - \frac{1}{k}$.

---

## Tower Property Example: Poisson Thinning
**Problem:** Let $Z \sim \text{Poisson}(\lambda)$. Given $Z=z$, let $X \sim \text{Bin}(z, p)$. Find $E[X]$.

Using the **Tower Property**:
$$E[X] = E[E[X|Z]]$$
We know the expectation of a Binomial $\text{Bin}(z, p)$ is $zp$.
$$E[X|Z=z] = zp \implies E[X|Z] = Zp$$
Then:
$$E[X] = E[Zp] = p E[Z] = p\lambda$$

> [!note] 
> If $X \perp Z$, then $E[X|Z] = E[X]$. The Tower Property holds for all random variables.

---

## Cauchy-Schwarz Inequality
**Proposition:** For any two random variables $X$ and $Y$:
$$|E[XY]| \le \sqrt{E[X^2] E[Y^2]}$$

**Proof:**
1. Assume $E[X^2] = 1$ and $E[Y^2] = 1$.
   Since $(|X|-|Y|)^2 \ge 0 \implies |XY| \le \frac{X^2+Y^2}{2}$.
   $E[|XY|] \le \frac{E[X^2] + E[Y^2]}{2} = 1$.
2. For general $X, Y$, define normalized variables:
   $U = \frac{X}{\sqrt{E[X^2]}}$ and $V = \frac{Y}{\sqrt{E[Y^2]}}$.
   Applying the result from step 1: $E[UV] \le 1$.
   $$\frac{E[XY]}{\sqrt{E[X^2]E[Y^2]}} \le 1 \implies E[XY] \le \sqrt{E[X^2]E[Y^2]}$$

**Remark (Indicators):** If $X=1_A$ and $Y=1_B$:
$$P(A \cap B) \le \sqrt{P(A)P(B)}$$
Equality occurs when the events are identical or multiples of each other.

---

## Markov’s Inequality
> [!theory] Proposition
> Let $X$ be a non-negative random variable ($X \ge 0$). For any $t > 0$:
> $$P(X \ge t) \le \frac{E[X]}{t}$$

**Proof:**
Define the indicator $1_{\{X \ge t\}}$.
* If $\omega \in \{X \ge t\}$, then $X(\omega)/t \ge 1 = 1_{\{X \ge t\}}$.
* If $\omega \notin \{X \ge t\}$, then $X(\omega)/t \ge 0 = 1_{\{X \ge t\}}$ (since $X \ge 0$).
In all cases: $\frac{X}{t} \ge 1_{\{X \ge t\}}$.
By monotonicity:
$$E\left[\frac{X}{t}\right] \ge E[1_{\{X \ge t\}}] = P(X \ge t)$$
$$\frac{E[X]}{t} \ge P(X \ge t)$$
# Chebyshev’s Inequality & Indicators for Variance

## Example: Mailbox Problem Comparison
Recall for the mailbox problem: $E[X] = 1$.
By **Markov’s Inequality**: $P(X \ge k) \le \frac{E[X]}{k} = \frac{1}{k}$.

* **Comparison:** For $X = n$ (all correct), Markov says $P(X=n) \le 1/n$. 
  The actual probability is $P(X=n) = 1/n!$.
* **Insight:** Markov is quite "loose" for large values of $t$, but it is a robust bound for small $t$ or when you only know the first moment.

---

## Chebyshev’s Inequality
> [!theory] Theorem
> For any random variable $X$ and any $t > 0$:
> $$P(|X - E[X]| \ge t) \le \frac{\text{Var}(X)}{t^2}$$

### Interpretation
The probability that $X$ deviates from its mean by more than $t$ falls off at least as fast as $1/t^2$. This is much stronger than Markov, but it requires knowing the **second moment** (Variance).

### Proof
Since $t \ge 0$:
$$P(|X - E[X]| \ge t) = P(|X - E[X]|^2 \ge t^2)$$
Apply **Markov’s Inequality** to the non-negative RV $Y = |X - E[X]|^2$:
$$P(Y \ge t^2) \le \frac{E[Y]}{t^2} = \frac{E[|X - E[X]|^2]}{t^2} = \frac{\text{Var}(X)}{t^2}$$

### The Standard Deviation Version
Let $s = \sqrt{\text{Var}(X)}$ (Standard Deviation). For any $L > 0$, set $t = Ls$:
$$P(|X - E[X]| \ge Ls) \le \frac{\text{Var}(X)}{(Ls)^2} = \frac{1}{L^2}$$
*i.e., the probability $X$ deviates from its mean by $L$ standard deviations is $\le 1/L^2$.*

---

## Method of Indicator RVs for Variance
Calculating the variance of a sum $X = \sum_{i=1}^n 1_{A_i}$ is more complex than expectation because of cross-terms.
$$\text{Var}(X) = \text{Cov}(X, X) = \text{Cov}\left(\sum_{i=1}^n 1_{A_i}, \sum_{j=1}^n 1_{A_j}\right) = \sum_{i=1}^n \sum_{j=1}^n \text{Cov}(1_{A_i}, 1_{A_j})$$

### Example: Number of Heads Runs
**Problem:** $n$ fair coin flips. $X = \text{number of H-runs}$.
Indicators: $1_{A_1} = \{1\text{st is } H\}$, $1_{A_i} = \{i\text{-th is } H, (i-1)\text{-th is } T\}$.
$E[X] = \frac{1}{2} + \frac{n-1}{4}$.

**Variance Calculation:**
We need $\text{Cov}(1_{A_i}, 1_{A_j}) = P(A_i \cap A_j) - P(A_i)P(A_j)$.
1.  **If $|i-j| > 1$:** The events depend on disjoint flips, so they are independent. $\text{Cov} = 0$.
2.  **If $|i-j| = 1$ (Adjacent):** For example, $A_i$ and $A_{i+1}$. Both cannot start a run simultaneously because $A_i$ requires the $i$-th flip to be $H$ and $A_{i+1}$ requires the $i$-th flip to be $T$.
    $$P(A_i \cap A_{i+1}) = 0 \implies \text{Cov}(1_{A_i}, 1_{A_{i+1}}) = 0 - P(A_i)P(A_j)$$
3.  **If $i=j$:** $\text{Cov}(1_{A_i}, 1_{A_i}) = \text{Var}(1_{A_i}) = P(A_i)(1 - P(A_i))$.

---

## Summary Table: Probability Inequalities

| Name | Statement | Condition |
| :--- | :--- | :--- |
| **Monotonicity** | $X \le Y \implies E[X] \le E[Y]$ | - |
| **R-th Moment** | $|E[X]| \le (E[|X|^k])^{1/k}$ | $k \ge 1, E[|X|^k] < \infty$ |
| **Cauchy-Schwarz** | $|E[XY]| \le \sqrt{E[X^2] E[Y^2]}$ | $E[X^2], E[Y^2] < \infty$ |
| **Markov** | $P(X \ge t) \le \frac{E[X]}{t}$ | $X \ge 0, t > 0, E[X] < \infty$ |
| **Chebyshev** | $P(|X - E[X]| \ge t) \le \frac{\text{Var}(X)}{t^2}$ | $\text{Var}(X) < \infty$ |

---

## Practical Example: 1 Million Coin Flips
Let $X$ be the number of heads in $1,000,000$ flips.
* $E[X] = 500,000$
* $\text{Var}(X) = \sum \text{Var}(1_{A_i}) = n p(1-p) = 10^6 \cdot (1/4) = 250,000$
  *(Since flips are independent, all covariances are zero).*

**Chebyshev Bound:**
What is the probability $X$ is off by more than $5,000$?
$$P(|X - 500,000| \ge 5,000) \le \frac{250,000}{5,000^2} = \frac{250,000}{25,000,000} = \frac{1}{100} = 1\%$$
**Markov Bound (for comparison):**
$$P(X \ge 505,000) \le \frac{500,000}{505,000} \approx 99\%$$
*Markov is almost useless here, whereas Chebyshev gives a very tight 1% bound.*

# Convergence of Random Variables & LLN

## Convergence in Probability
> [!definition] 
> We say a sequence of random variables $X_1, X_2, \dots$ **converges in probability** to a constant $c \in \mathbb{R}$ (written $X_n \xrightarrow{P} c$) if for every $\epsilon > 0$:
> $$\lim_{n \to \infty} P(|X_n - c| > \epsilon) = 0$$

### Example: Proportion of Heads
Let $X_n = \frac{\text{# of heads in } n \text{ flips}}{n}$ for fair coin flips.
* $E[X_n] = 1/2$
* $\text{Var}(X_n) = \frac{1}{n^2} \text{Var}(\sum 1_{A_i}) = \frac{1}{n^2} (n \cdot \frac{1}{4}) = \frac{1}{4n}$

By **Chebyshev's Inequality**:
$$0 \le P(|X_n - 1/2| \ge \epsilon) \le \frac{\text{Var}(X_n)}{\epsilon^2} = \frac{1}{4n\epsilon^2}$$
As $n \to \infty$, the RHS $\to 0$. By the **Squeeze Theorem**:
$$X_n \xrightarrow{P} 1/2$$

> [!danger] Counterexample: $X_n \xrightarrow{P} c \not\implies E[X_n] \to c$
> **Question:** Is it true that if $X_n \xrightarrow{P} c$, then $E[X_n] \to c$?
> **NO.** Consider $X_n$ defined as:
> * $X_n = n^2$ with probability $1/n$
> * $X_n = 0$ with probability $1 - 1/n$
> 
> Here, $P(|X_n - 0| > \epsilon) = P(X_n = n^2) = 1/n \to 0$. So $X_n \xrightarrow{P} 0$.
> However, $E[X_n] = n^2(1/n) + 0(1 - 1/n) = n$.
> As $n \to \infty$, $E[X_n] \to \infty$.

---

## The Second Moment Method
> [!theory] Theorem
> Let $(X_n)_{n=1}^\infty$ be a sequence of RVs such that:
> 1. $E[X_n] \to c$ as $n \to \infty$
> 2. $\text{Var}(X_n) \to 0$ as $n \to \infty$
>
> Then $X_n \xrightarrow{P} c$.

**Proof:**
Using the identity $E[(X_n - c)^2] = \text{Var}(X_n) + (E[X_n] - c)^2$.
By assumptions (1) and (2), $E[(X_n - c)^2] \to 0 + 0 = 0$.
Applying **Markov's Inequality** to the squared difference:
$$P(|X_n - c| > \epsilon) = P(|X_n - c|^2 > \epsilon^2) \le \frac{E[(X_n - c)^2]}{\epsilon^2} \xrightarrow{n \to \infty} 0$$

---

## The Weak Law of Large Numbers (WLLN)
> [!theory] Theorem
> Let $X_1, X_2, \dots$ be i.i.d. random variables with finite expectation $\mu$ and finite variance $\sigma^2$. Then:
> $$\frac{\sum_{k=1}^n X_k}{n} \xrightarrow{P} \mu$$

**Proof (using Second Moment Method):**
Let $Z_n = \frac{1}{n} \sum X_k$.
1. **Expectation:** $E[Z_n] = \frac{1}{n} \sum E[X_k] = \frac{n\mu}{n} = \mu$.
2. **Variance:** Since $X_k$ are independent, covariances are zero:
   $\text{Var}(Z_n) = \frac{1}{n^2} \sum \text{Var}(X_k) = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n} \to 0$.
By the Second Moment Method, $Z_n \xrightarrow{P} \mu$.

**Remarks:**
* Finite variance is not strictly necessary for the WLLN, but it makes the proof much simpler.
* **Strong Law of Large Numbers (SLLN):** Replaces "convergence in probability" with "**almost sure convergence**."

---

## Applied Examples

### 1. Balls into Bins (Empty Bins)
Let $X_n$ be the number of empty bins when $n$ balls are thrown into $n$ bins.
We previously found $E[X_n] = n(1 - 1/n)^n \approx n/e$.
It can be shown (via the Second Moment Method) that the variance of the proportion $\text{Var}(X_n/n) \to 0$.
$$\frac{X_n}{n} \xrightarrow{P} \frac{1}{e}$$

### 2. Number of Heads Runs
Let $X_n$ be the number of heads runs in $n$ fair flips.
$E[X_n] = p + (n-1)p(1-p)$.
$$\implies E\left[\frac{X_n}{n}\right] \to p(1-p)$$
For the variance $\text{Var}(X_n)$, we consider indicators $1_{A_k}$.
* If $|i - j| \ge 2$, then $1_{A_i} \perp 1_{A_j} \implies \text{Cov} = 0$.
* Only adjacent terms have non-zero covariance. 
Since there are only $O(n)$ non-zero covariance terms, $\text{Var}(X_n) = O(n)$.
Thus, $\text{Var}(X_n/n) = \frac{O(n)}{n^2} \to 0$.
**Result:** $\frac{X_n}{n} \xrightarrow{P} p(1-p)$.

# Convergence in Distribution & The Central Limit Theorem

## Convergence in Distribution (Convergence in Law)
> [!definition] 
> Let $X_1, X_2, \dots$ be random variables and $X$ be a random variable. We say $X_n$ **converges in distribution** to $X$ (written $X_n \xrightarrow{d} X$) if:
> $$\lim_{n \to \infty} F_{X_n}(t) = F_X(t)$$
> for all $t \in \mathbb{R}$ such that $F_X$ is continuous at $t$.

### Remarks
1. **Dependencies:** Convergence in distribution depends only on the laws ($F_{X_n}, F_X$), not the underlying sample space.
2. **Continuity Case:** If $F_X$ is continuous everywhere (like a Normal distribution), then we require convergence for all $t$.
3. **Probability Bounds:** If $X_n \xrightarrow{d} X$ and $F_X$ is continuous, then for any $a, b \in \mathbb{R}$:
   $$P(a \le X_n \le b) \xrightarrow{n \to \infty} P(a \le X \le b) = F_X(b) - F_X(a)$$

---

## Examples & Counterexamples

### 1. Binomial to Poisson
We previously showed that if $X_n \sim \text{Bin}(n, \lambda/n)$, then for each $k$:
$$P(X_n = k) \to e^{-\lambda} \frac{\lambda^k}{k!}$$
This implies $X_n \xrightarrow{d} \text{Poisson}(\lambda)$.

### 2. The $t=0$ Discontinuity
Let $X_n \sim N(0, 1/n^2)$. As $n \to \infty$, the mass "squashes" toward 0.
$X_n \xrightarrow{P} 0$, so we expect $X_n \xrightarrow{d} X$ where $P(X=0) = 1$.
* **CDF of $X_n$ at 0:** $F_{X_n}(0) = 1/2$ for all $n$.
* **CDF of limit $X$:** $F_X(t) = 0$ if $t < 0$ and $F_X(t) = 1$ if $t \ge 0$.
Note that $\lim F_{X_n}(0) = 1/2$, but $F_X(0) = 1$. 
**Why this is okay:** $t=0$ is a point of **discontinuity** for $F_X$, so the definition doesn't require convergence there.

> [!canvas] Sketch: Squashing Gaussian
> (A very tall, thin Gaussian centered at 0. Show an arrow indicating it getting thinner as $n \to \infty$, turning into a vertical line at $x=0$.)

---

## The Central Limit Theorem (CLT)
> [!theory] Theorem
> Let $X_1, X_2, \dots$ be i.i.d. random variables with $E[X_i] = \mu$ and $\text{Var}(X_i) = \sigma^2 < \infty$. Let $S_n = \sum_{i=1}^n X_i$. Then:
> $$\frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0, 1)$$

### Moments of the Normalized Sum
Let $Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}}$.
1. **Expectation:** $E[Z_n] = \frac{E[S_n] - n\mu}{\sigma\sqrt{n}} = \frac{n\mu - n\mu}{\dots} = 0$.
2. **Variance:** $\text{Var}(Z_n) = \frac{1}{\sigma^2 n} \text{Var}(S_n) = \frac{1}{\sigma^2 n} (n\sigma^2) = 1$.

*Note: While WLLN says the average $\frac{S_n}{n}$ converges to a point $\mu$, the CLT tells us the **shape** of the fluctuations around that point (after scaling by $\sqrt{n}$) is always Gaussian.*

> [!canvas] Sketch: CLT Distribution
> (Draw a standard Normal curve centered at 0. Label the peak as the result of the "normalized sum" of any i.i.d. variables, regardless of their original distribution.)

---

## Smooth Test Functions & Convergence
**Proposition:** $Y_n \xrightarrow{d} Y$ if and only if $E[h(Y_n)] \to E[h(Y)]$ for all $h \in C_b^\infty$ (functions that are infinitely differentiable and bounded, with bounded derivatives).

**Remark:** The function $h(x) = x$ is NOT in $C_b^\infty$ because it is not bounded. This is why convergence in distribution does not strictly imply convergence of expectations.

### Lemma: Construction of a Smooth Step
To relate the "smooth function" definition to the "CDF" definition, we use functions like:
$$g(x) = \begin{cases} e^{-1/x} & \text{if } x > 0 \\ 0 & \text{if } x \le 0 \end{cases}$$
By using combinations of such functions, we can create "smooth" versions of indicators $1_{(-\infty, t]}$ to sandwich the CDF and prove the equivalence.
# Asymptotic Theory: Convergence in Law & CLT Proof

## Convergence in Distribution (Convergence in Law)
> [!definition] 
> Let $X_1, X_2, \dots$ and $X$ be random variables. We say $X_n$ **converges in distribution** to $X$ ($X_n \xrightarrow{d} X$) if:
> $$\lim_{n \to \infty} F_{X_n}(t) = F_X(t)$$
> for all $t \in \mathbb{R}$ where $F_X$ is continuous.

### Remarks
1. **Law Only:** Convergence in distribution depends only on the CDFs, not on whether the variables are defined on the same sample space.
2. **Probability of Intervals:** If $X_n \xrightarrow{d} X$ and $F_X$ is continuous, then for any $a, b \in \mathbb{R}$:
   $$P(a \le X_n \le b) \to P(a \le X \le b) = F_X(b) - F_X(a)$$

### Examples
* **Binomial to Poisson:** $X_n \sim \text{Bin}(n, \lambda/n) \xrightarrow{d} \text{Pois}(\lambda)$.
* **Squashing Gaussian:** If $X_n \sim N(0, 1/n^2)$, then $X_n \xrightarrow{P} 0$. Let $X \equiv 0$. The limit $F_X(t)$ is $0$ for $t < 0$ and $1$ for $t \ge 0$. Note that $F_{X_n}(0) = 1/2 \not\to F_X(0) = 1$, but this is allowed because $t=0$ is a discontinuity point of $F_X$.

> [!canvas] Sketch: Squashing Density
> (A Gaussian curve centered at 0 that gets narrower and taller as $n$ increases, eventually becoming a vertical line "spike" at $x=0$).

---

## The Central Limit Theorem (CLT)
> [!theory] Theorem
> Let $X_1, X_2, \dots$ be i.i.d. random variables with mean $\mu$ and variance $\sigma^2 < \infty$. Let $S_n = \sum_{i=1}^n X_i$. Then:
> $$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0, 1)$$

**Moments of $Z_n$:**
1. $E[Z_n] = \frac{E[S_n] - n\mu}{\sigma\sqrt{n}} = 0$
2. $\text{Var}(Z_n) = \frac{1}{\sigma^2 n} \text{Var}(S_n) = \frac{n\sigma^2}{\sigma^2 n} = 1$

> [!canvas] Sketch: $S_n$ Distribution
> (A distribution for $S_n$ centered at $n\mu$. As $n$ increases, the peak moves to the right and spreads out, but the *normalized* version $Z_n$ always settles into the standard Bell Curve).

---

## Smooth Test Functions & Convergence
**Proposition:** $Y_n \xrightarrow{d} Y$ if and only if $E[h(Y_n)] \to E[h(Y)]$ for all $h \in C_b^\infty$ (bounded, infinitely differentiable functions with bounded derivatives).

### Proof Sketch (Sandwiching the CDF)
To relate $E[h(Y)]$ back to the CDF $F_Y(t)$, we construct a "smooth step function."
Let $g(x) = e^{-1/x}$ for $x > 0$ and $0$ otherwise.
We can use $g(x)$ to build a function $H_{s,t}(y)$ that is:
* $1$ for $y \le s$
* $0$ for $y \ge t$
* Smoothly decreasing in between.

Then $1_{(-\infty, s]} \le H_{s,t} \le 1_{(-\infty, t]}$. Taking expectations:
$$F_{Y_n}(s) \le E[H_{s,t}(Y_n)] \le F_{Y_n}(t)$$
By taking limits and using the Squeeze Theorem, we show that convergence of expectations of smooth functions implies convergence of the CDF.

---

# Asymptotic Theory: Convergence & The CLT Proof

## Convergence in Distribution (Convergence in Law)
> [!definition] 
> Let $X_1, X_2, \dots$ be a sequence of RVs and $X$ be an RV. We say $X_n \xrightarrow{d} X$ if:
> $$\lim_{n \to \infty} F_{X_n}(t) = F_X(t)$$
> for all $t \in \mathbb{R}$ such that $F_X$ is continuous at $t$.

**Remarks:**
1. Convergence in distribution depends only on the laws ($F_{X_n}, F_X$).
2. **Most Common Case:** If $F_X$ is continuous everywhere, then $X_n \xrightarrow{d} X$ iff $F_{X_n}(t) \to F_X(t)$ for all $t$.
3. If $X_n \xrightarrow{d} X$ and $F_X$ is continuous, then $P(a \le X_n \le b) \xrightarrow{n \to \infty} P(a \le X \le b)$ for any $a, b \in \mathbb{R}$.

### Examples
* **Binomial to Poisson:** If $X_n \sim \text{Bin}(n, \lambda/n)$, then $X_n \xrightarrow{d} \text{Pois}(\lambda)$.
* **Squashing Gaussian:** Let $X_n \sim N(0, 1/n^2)$. As $n \to \infty$, $X_n \xrightarrow{P} 0$. Let $X \equiv 0$.
  * $F_{X_n}(t) = \int_{-\infty}^t f_{X_n}(s) \, ds$.
  * If $t < 0$, $F_{X_n}(t) \to 0$. If $t > 0$, $F_{X_n}(t) \to 1$.
  * At $t=0$, $F_{X_n}(0) = 1/2$.
  * $F_X(t) = \begin{cases} 0 & t < 0 \\ 1 & t \ge 0 \end{cases}$.
  * Since $t=0$ is a discontinuity point, the fact that $1/2 \neq 1$ does not prevent $X_n \xrightarrow{d} X$.

---

## The Central Limit Theorem (CLT)
> [!theory] Theorem
> Let $X_1, X_2, \dots$ be i.i.d. RVs with mean $\mu = E[X_1]$ and variance $\sigma^2 = \text{Var}(X_1) < \infty$. Let $S_n = \sum_{i=1}^n X_i$. Then:
> $$T_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0, 1)$$

**Moments of $T_n$:**
1. $E[T_n] = E\left[\frac{S_n - n\mu}{\sigma\sqrt{n}}\right] = 0$.
2. $\text{Var}(T_n) = \text{Var}\left[\frac{S_n - n\mu}{\sigma\sqrt{n}}\right] = \frac{1}{\sigma^2 n} \text{Var}(S_n) = \frac{1}{\sigma^2 n} (n\sigma^2) = 1$.

> [!canvas] Sketch: Normalized Sum
> (A distribution for $S_n$ centered at $n\mu$. As $n$ grows, the distribution becomes a very sharp "spike" relative to the scale of $n$, but when centered and scaled by $\sqrt{n}$, it always converges to the Standard Normal bell curve.)

---

# Detailed Proof: The Central Limit Theorem (Lindeberg Swap)

## 1. Smooth Test Functions

We use smooth functions to bridge the gap to the CDF.

Define $g(x) = \begin{cases} e^{-1/x} & x > 0 \\ 0 & x \le 0 \end{cases} \in C_b^\infty$.

For any $-\infty < a < b < \infty$, define $\theta_{a,b}(x) = g(x-a)g(b-x)$.

- Note: If $g(x) < 0$, then $g(x)=0$.
    
    Define $C_{a,b} = \int_a^b \theta_{a,b}(x) \, dx$.
    
    Define $h_{a,b}(x) = \frac{\theta_{a,b}(x)}{C_{a,b}}$.
    
    Define $H_{a,b}(x) = \int_{-\infty}^x h_{a,b}(y) \, dy$.
    
    _(This is an integral of a non-negative function, creating a smooth step)._
    

### Proposition Proof (Sandwiching)

Assume $E[h(Y_n)] \to E[h(Y)]$ for all $h \in C_b^\infty$.

Define the indicator $1_{(-\infty, t]}(y) = \begin{cases} 1 & y \le t \\ 0 & \text{else} \end{cases}$.

Note that $P(Y_n \le t) = E[1_{(-\infty, t]}(Y_n)] = F_{Y_n}(t)$.

Let $s < t$. Then:

$$11_{(-\infty, s]}(Y) \le 1 - H_{s,t}(Y) \le 11_{(-\infty, t]}(Y)$$

Taking expectations:

$$F_{Y_n}(s) \le E[1 - H_{s,t}(Y_n)] \le F_{Y_n}(t)$$

As $n \to \infty$:

$$\limsup F_{Y_n}(s) \le E[1 - H_{s,t}(Y)] \le \liminf F_{Y_n}(t)$$

If $F_Y$ is continuous at $t$, take $s \to t^-$:

Since $F_{Y_n}(t) \ge F_Y(t)$ and $\limsup F_{Y_n}(t) \le F_Y(t)$, we conclude $F_{Y_n}(t) \to F_Y(t)$.

$$\implies Y_n \xrightarrow{d} Y$$

---

## 2. Theorem: Lindeberg CLT

Let $X_1, X_2, \dots$ be i.i.d. RVs with $\mu = E[X_1]$, $\sigma^2 = \text{Var}(X_1)$. Let $Z \sim N(0, 1)$.

Set $S_n = \sum_{i=1}^n X_i$ and $T_n = \frac{S_n - n\mu}{\sigma\sqrt{n}}$.

**Assumption:** $E[|X - \mu|^3] < \infty$.

Then for every $h \in C_b^\infty$ such that $|h'''(x)| \le C < \infty$:

$$0 \le |E[h(T_n)] - E[h(Z)]| \le \frac{C}{\sigma^3\sqrt{n}} \left( E[|X_i - \mu|^3] + E[|Z|^3] \right)$$

And $T_n \xrightarrow{d} Z$.

---

## 3. Proof of Inequality (*)

Define $Y_i = \frac{X_i - \mu}{\sigma\sqrt{n}}$. So $T_n = \sum_{i=1}^n Y_i$.

- $Y_1, Y_2, \dots$ are i.i.d. with mean 0 and variance $1/n$.
    
- Let $Z_1, Z_2, \dots, Z_n$ be i.i.d. $N(0, 1/n)$.
    
- Then $Z = Z_1 + Z_2 + \dots + Z_n \sim N(0, 1)$.
    

**The Hybrid Sequence ($A_i$):**

- $A_0 = Z_1 + Z_2 + \dots + Z_n = Z$
    
- $A_1 = Y_1 + Z_2 + \dots + Z_n$
    
- $A_i = Y_1 + \dots + Y_i + Z_{i+1} + \dots + Z_n$
    
- $A_n = Y_1 + \dots + Y_n = T_n$
    

**Telescoping Sum:**

$$h(T_n) - h(Z) = \sum_{i=1}^n [h(A_i) - h(A_{i-1})]$$

Let $B_i = \sum_{j < i} Y_j + \sum_{j > i} Z_j$.

Then $A_i = B_i + Y_i$ and $A_{i-1} = B_i + Z_i$.

**Taylor Approximation:**

By Taylor's theorem, for some small error $R_i$:

$$h(B_i + Y_i) = h(B_i) + h'(B_i)Y_i + \frac{1}{2}h''(B_i)Y_i^2 + R_i$$

where $|R_i| \le \frac{C}{6} |Y_i|^3$ (where $C$ bounds $h'''$).

Taking expectations, and noting that $B_i$ is independent of $Y_i$:

$$E[h(A_i)] = E[h(B_i)] + E[h'(B_i)]E[Y_i] + \frac{1}{2}E[h''(B_i)]E[Y_i^2] + E[R_i]$$

Since $E[Y_i] = 0$ and $E[Y_i^2] = 1/n$:

$$E[h(A_i)] = E[h(B_i)] + 0 + \frac{1}{2n}E[h''(B_i)] + E[R_i]$$

Similarly for $A_{i-1}$ (using $Z_i$):

$$E[h(A_{i-1})] = E[h(B_i)] + 0 + \frac{1}{2n}E[h''(B_i)] + E[\tilde{R}_i]$$

**Difference of Hybrids:**

$$|E[h(A_i)] - E[h(A_{i-1})]| = |E[R_i] - E[\tilde{R}_i]| \le \frac{C}{6} \left( E[|Y_i|^3] + E[|Z_i|^3] \right)$$

Substituting $Y_i = \frac{X_i-\mu}{\sigma\sqrt{n}}$ and $Z_i \sim N(0, 1/n)$:

$$= \frac{C}{6} \left( \left(\frac{1}{\sigma\sqrt{n}}\right)^3 E[|X_i-\mu|^3] + \left(\frac{1}{\sqrt{n}}\right)^3 E[|Z|^3] \right)$$

**Total Bound:**

$$|E[h(T_n)] - E[h(Z)]| \le \sum_{i=1}^n \frac{C}{6 n^{3/2}} \left( \frac{E[|X-\mu|^3]}{\sigma^3} + E[|Z|^3] \right)$$

$$= \frac{C}{6\sqrt{n}} \left( \frac{E[|X-\mu|^3]}{\sigma^3} + E[|Z|^3] \right) \xrightarrow{n \to \infty} 0$$
---

## Applying the CLT
1. Identify i.i.d. RVs $X_1, X_2, \dots$
2. Construct $T_n$ by centering and normalizing (ensure $E[T_n]=0, \text{Var}(T_n)=1$).
3. Approximate: $P(a \le T_n \le b) \approx \Phi(b) - \Phi(a)$.

# Applying the Central Limit Theorem: Normalization Guide

The Central Limit Theorem (CLT) allows us to approximate the distribution of a sum or average of i.i.d. variables using the Standard Normal distribution $N(0, 1)$.

## 1. The Normalization Formulas
Let $X_1, X_2, \dots, X_n$ be i.i.d. random variables with mean $\mu$ and variance $\sigma^2$.

### For the Total Sum ($S_n$)
To find the probability of the total sum $S_n = \sum_{i=1}^n X_i$:
$$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0, 1)$$
* **Centering:** Subtract the expected total ($n\mu$).
* **Scaling:** Divide by the total standard deviation ($\sigma\sqrt{n}$).

### For the Sample Mean ($\bar{X}_n$)
To find the probability of the average $\bar{X}_n = \frac{S_n}{n}$:
$$Z_n = \frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0, 1)$$
* **Centering:** Subtract the population mean ($\mu$).
* **Scaling:** Divide by the "Standard Error" ($\sigma/\sqrt{n}$).

---

## 2. Step-by-Step Procedure
When asked to find $P(a \le S_n \le b)$:

1.  **Extract Parameters:** Identify $n$, $\mu = E[X_i]$, and $\sigma = \sqrt{\text{Var}(X_i)}$.
2.  **Standardize the Bounds:** Apply the normalization to every part of the inequality:
    $$P\left( \frac{a - n\mu}{\sigma\sqrt{n}} \le \frac{S_n - n\mu}{\sigma\sqrt{n}} \le \frac{b - n\mu}{\sigma\sqrt{n}} \right)$$
3.  **Map to $Z$:** Substitute the standardized sum with the variable $Z \sim N(0, 1)$:
    $$P(z_{low} \le Z \le z_{high})$$
4.  **Evaluate:** Use the Standard Normal CDF ($\Phi$):
    $$\Phi(z_{high}) - \Phi(z_{low})$$

---

## 3. Important Nuance: Continuity Correction
When $X_i$ are **discrete** (integers) but being approximated by a **continuous** curve, adjust the bounds by $\pm 0.5$ to improve accuracy:

* For $P(S_n \le k)$, use: $P\left(Z \le \frac{k + 0.5 - n\mu}{\sigma\sqrt{n}}\right)$
* For $P(S_n \ge k)$, use: $P\left(Z \ge \frac{k - 0.5 - n\mu}{\sigma\sqrt{n}}\right)$

---

## 4. Summary Table

| Metric | Target | Centering | Scaling Factor |
| :--- | :--- | :--- | :--- |
| **Sum** | $S_n$ | $n\mu$ | $\sigma\sqrt{n}$ |
| **Mean** | $\bar{X}_n$ | $\mu$ | $\sigma/\sqrt{n}$ |
# Tower Property & Markov Chains

## Tower Property with Discrete RVs
> [!theory] Law of Total Expectation
> If $X$ is a discrete random variable with PMF $p_X$, then:
> $$E[E[Y|X]] = \sum_x E[Y|X=x] p_X(x)$$
> For the continuous case:
> $$E[E[Y|X]] = \int_{\mathbb{R}} E[Y|X=x] f_X(x) \, dx = E[Y]$$

**Interpretation:** $E[Y|X]$ is a random variable that takes the value $E[Y|X=x]$ with probability $P(X=x)$.

---

## Example: The Coupon Collector Problem
**Problem:** There are $n$ types of coupons. At each time step, you collect a coupon chosen uniformly at random from the $n$ types. Let $T_n$ be the time taken to collect at least one of each type. What is $E[T_n]$?

**Method:**
Define $X_i$ as the time between collecting the $(i-1)$-th new coupon and the $i$-th new coupon.
$$T_n = X_1 + X_2 + \dots + X_n$$

When you have $i-1$ unique coupons, the probability of getting a *new* one is:
$$p_i = \frac{n - (i-1)}{n}$$
Since we wait for a success with probability $p_i$, $X_i$ follows a **Geometric Distribution**:
$$X_i \sim \text{Geo}\left(\frac{n-i+1}{n}\right) \implies E[X_i] = \frac{n}{n-i+1}$$

**Calculating Expectation:**
$$E[T_n] = \sum_{i=1}^n E[X_i] = \sum_{i=1}^n \frac{n}{n-i+1} = n \left( \frac{1}{n} + \frac{1}{n-1} + \dots + 1 \right)$$
$$E[T_n] = n \sum_{k=1}^n \frac{1}{k} \approx n \ln n$$

---

## Finite State Space Markov Chains
> [!definition] 
> Let $S = \{1, 2, \dots, N\}$ be the **state space**. An $S$-valued sequence of random variables $X_0, X_1, X_2, \dots$ is a **Markov Chain** if for all $x_0, x_1, \dots, x_n \in S$:
> $$P(X_n = x_n | X_0 = x_0, \dots, X_{n-1} = x_{n-1}) = P(X_n = x_n | X_{n-1} = x_{n-1})$$
> *Intuition: The future depends only on the present, not the past.*

### Example: 2-State Chain
$S = \{1, 2\}$
* If $X_{n-1} = 2$, then $X_n = 1$ with probability 1.
* If $X_{n-1} = 1$, then $X_n = 1$ with probability $1/2$ and $X_n = 2$ with probability $1/2$.

> [!canvas] Sketch: State Transition Diagram
> (Node 1 has a self-loop of 1/2 and an edge to Node 2 of 1/2. Node 2 has an edge to Node 1 of probability 1.)

---

## Transition Probabilities & Stochastic Matrices
A Markov Chain is **time-homogeneous** if $P(X_n = y | X_{n-1} = x)$ does not depend on $n$.
We define the **Transition Matrix** $P = (P_{x,y})_{x,y \in S}$ where:
$$P_{x,y} = P(X_n = y | X_{n-1} = x)$$

**Properties of $P$:**
1. $P_{x,y} \in [0, 1]$ (Non-negative).
2. $\sum_{y \in S} P_{x,y} = 1$ (Rows sum to 1). This is called a **stochastic matrix**.

---

## Chapman-Kolmogorov Formula
Let $P_{x,y}^{(n)} = P(X_n = y | X_0 = x)$ be the $n$-step transition probability.

> [!theory] Theorem
> $P^{(n)} = P^n$
> The $n$-step transition matrix is the $n$-th power of the 1-step transition matrix.

**Proof (by induction/matrix multiplication):**
Consider the path $x_0, x_1, \dots, x_n$:
$$P(X_0=x_0, \dots, X_n=x_n) = P(X_0=x_0) \prod_{i=1}^n P(X_i=x_i | X_{i-1}=x_{i-1})$$
By the Law of Total Probability:
$$P(X_n=y | X_0=x) = \sum_{x_1, \dots, x_{n-1}} P_{x,x_1} P_{x_1,x_2} \dots P_{x_{n-1},y}$$
This sum is exactly the definition of the $(x, y)$ entry of the matrix power $P^n$.

---

## Invariant Distributions
> [!definition] 
> A **probability distribution** on $S$ is a set of values $(\mu_x)_{x \in S}$ s.t. $\mu_x \ge 0$ and $\sum \mu_x = 1$. We treat $\mu$ as a **row vector**.

> [!definition] 
> A distribution $\pi$ is an **invariant (stationary) distribution** if:
> $$\pi P = \pi$$
> i.e., $\pi$ is a **left eigenvector** of $P$ with eigenvalue 1.

### Example: Solving for $\pi$
For $P = \begin{pmatrix} 1/2 & 1/2 \\ 1 & 0 \end{pmatrix}$:
Solve $\begin{pmatrix} \mu_1 & \mu_2 \end{pmatrix} \begin{pmatrix} 1/2 & 1/2 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} \mu_1 & \mu_2 \end{pmatrix}$
1. $\frac{1}{2}\mu_1 + \mu_2 = \mu_1 \implies \frac{1}{2}\mu_1 = \mu_2$
2. $\mu_1 + \mu_2 = 1$
Substituting: $\mu_1 + \frac{1}{2}\mu_1 = 1 \implies \frac{3}{2}\mu_1 = 1 \implies \mu_1 = 2/3, \mu_2 = 1/3$.
**Stationary Distribution:** $\pi = (2/3, 1/3)$.

> [!warning] 
> Not every chain converges to its invariant distribution. 
> **Counterexample:** $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$. 
> $\pi = (1/2, 1/2)$ is invariant, but if you start at state 1, you cycle $1 \to 2 \to 1 \to 2$, so $P^n$ does not converge.

# Advanced Expectation & Markov Chains

## Tower Property (Law of Total Expectation)
> [!theory] 
> If $X$ is a discrete random variable with PMF $p_x$, then for any random variable $Y$:
> $$E[E[Y|X]] = \sum_x E[Y|X=x] p_X(x) = E[Y]$$
> For the continuous case:
> $$E[E[Y|X]] = \int_{\mathbb{R}} E[Y|X=x] f_X(x) \, dx = E[Y]$$

**Interpretation:** $E[Y|X]$ is a random variable that is a function of $X$. It takes the value $E[Y|X=x]$ with probability $p_X(x)$.

---

## The Coupon Collector Problem
**Problem:** There are $n$ types of coupons. At each step, you collect a coupon chosen uniformly at random. Let $T_n$ be the time to collect all $n$ types.

**Calculation:**
Define $X_i$ as the time elapsed between collecting the $(i-1)$-th new coupon and the $i$-th new coupon.
$$T_n = X_1 + X_2 + \dots + X_n$$
When you have $i-1$ types, the probability of getting a new one is $p_i = \frac{n - (i-1)}{n}$.
Since each $X_i \sim \text{Geo}(p_i)$:
$$E[X_i] = \frac{1}{p_i} = \frac{n}{n-i+1}$$
$$E[T_n] = \sum_{i=1}^n \frac{n}{n-i+1} = n \sum_{k=1}^n \frac{1}{k} \approx n \ln n$$

> [!note] 
> The Central Limit Theorem (CLT) does **not** work well for extreme values here. While $T_n$ converges in probability, its behavior for large $n$ is more nuanced.

---

## Finite State Space Markov Chains (DTMC)
> [!definition] 
> Let $S = \{1, 2, \dots, N\}$ be the state space. A sequence of random variables $X_0, X_1, \dots$ is a **Markov Chain** if:
> $$P(X_n = x_n | X_0 = x_0, \dots, X_{n-1} = x_{n-1}) = P(X_n = x_n | X_{n-1} = x_{n-1})$$
> *The "Memoryless" Property: The future depends only on the present.*

### Transition Probabilities
A chain is **time-homogeneous** if $P(X_n = y | X_{n-1} = x)$ is independent of $n$.
We define the **Transition Matrix** $P = (P_{x,y})$ where $P_{x,y} = P(X_n = y | X_{n-1} = x)$.

**Stochastic Matrix Properties:**
1. $P_{x,y} \ge 0$
2. $\sum_{y \in S} P_{x,y} = 1$ (Rows sum to 1).

---

## Chapman-Kolmogorov Formula
Let $P_{x,y}^{(n)} = P(X_n = y | X_0 = x)$.

> [!theory] Theorem
> $$P^{(n)} = P^n$$
> The $n$-step transition matrix is the $n$-th power of the 1-step transition matrix.

**Proof Sketch:**
By the Law of Total Probability, we sum over all possible intermediate paths:
$$P(X_n = y | X_0 = x) = \sum_{x_1, \dots, x_{n-1}} P_{x,x_1} P_{x_1,x_2} \dots P_{x_{n-1},y}$$
This is exactly the definition of matrix multiplication for $(P^n)_{x,y}$.

---

## Invariant Distributions
> [!definition] 
> A distribution $\mu$ (row vector) is **invariant** (stationary) if:
> $$\mu P = \mu$$
> i.e., $\mu$ is a **left eigenvector** of $P$ with eigenvalue $\lambda = 1$.

**Convergence and Cycles:**
If $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, the chain is periodic. While an invariant distribution exists ($\mu = [1/2, 1/2]$), the chain $P^n$ does not converge because it oscillates.

---

## Irreducibility & Ergodicity
> [!definition] 
> A Markov Chain is **irreducible** if for every $x, y \in S$, there exists $n$ such that $P_{x,y}^n > 0$ (you can get from any state to any other state).

**The Ergodic Theorem:**
If a Markov Chain is irreducible, then:
$$\frac{1}{n} \sum_{k=0}^{n-1} 1_{\{X_k = x\}} \xrightarrow{n \to \infty} \mu_x$$
The long-run proportion of time spent in state $x$ converges to the invariant measure $\mu_x$.

---

## PageRank & The Doeblin Condition
In the PageRank model, the state space $S$ consists of all websites.
* **Transition Matrix $Q$:** $Q_{x,y} = 1/k_x$ if $x$ has a link to $y$.
* **The Problem:** $Q$ might not be irreducible or aperiodic.
* **The Fix (Damping Factor):** Introduce $\alpha \in (0, 1)$ and define:
  $$P = \alpha Q + (1-\alpha) \frac{1}{n} \mathbb{1}\mathbb{1}^T$$
  This ensures the matrix is **strictly positive**, making the chain irreducible and aperiodic.

**Convergence Rate:**
By the **Perron-Frobenius Theorem**, for this constructed $P$, the second largest eigenvalue $|\lambda_2| \le \alpha$. This guarantees that the power iteration $\tilde{\mu} P^n$ converges exponentially fast to the unique invariant distribution $\mu$.
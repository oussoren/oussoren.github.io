+++
author = "max"
title = "Linear Algebra Notes"
date = "2024-12-19"
description = "My collection of linear algebra related thoughts and lessons"
math = true
tags = ["math", "programming"]
+++

# Chapter Notes

### Quick Overview
Given that this is linear algebra, I will be focusing on linear subspaces, which can be defined as the span, or the
amount of space covered by, a finite collection of vectors. These subspaces will lie in $\mathbf{R}^n$, or the space of
all n-dimensional vectors(with n coordinates). Linear subspaces will be represented by $\mathsf{V}$. The n-tuples of
vectors which define these subspaces will be represented by the following:
$\vec{v}_n=\begin{bmatrix}
\vec{v}_1 \\\\
\vdots \\\\
\vec{v}_n
\end{bmatrix}$



## Chapter 1: Vectors

### Vector Overview
Vectors can represent a very wide variety of things from physical direction and magnitude to collections of numerical
data. In other words, vectors are typically thought of as representing a particular direction, but they don't always
have to denote movement or incremental distance along coordinate axis. 

This is especially true for problems in data science where there are large collections of numerical data that would be easier to work with if put into vector form.
For example, say we wanted to keep track of the precipitation amount each day at Stanford over the course of a year. 
We could organize this data into a 365-vector:
$\mathbf{P}=\begin{bmatrix}
P_1 \\\\
P_2 \\\\
\vdots \\\\
P_{365}
\end{bmatrix}$
We have a general idea for defining vectors but provided below is a more concrete definition which clarifies what I meant by 
a "365-vector".

**Definition 1.1.2:**
For a whole number n, an n-vector is a list of n real numbers. We denote by $\mathbf{R}^n$ the collection of all possible n-vectors.

Additionally, we can introduce the idea of a scalar, which can be understood by the following definition provided below.

**Definition 1.1.4:**
To distinguish ordinary real numbers from vectors, the word scalar refers to a real number.

So we know what vectors and scalars are but what can we do with them? How can we manipulate and combine them?

**Definition 1.3.1:**
The sum $\vec{v}$ + $\vec{w}$ of two vectors is defined precisely when $\vec{v}$ and $\vec{w}$ are n-vectors for
the same n. In that case, we define their sum by the rule:$\begin{bmatrix}
\vec{v}_1 \\\\
\vdots \\\\
\vec{v}_n
\end{bmatrix}$ + $\begin{bmatrix}
\vec{w}_1 \\\\
\vdots \\\\
\vec{w}_n
\end{bmatrix}$ = $\begin{bmatrix}
\vec{v}_1 + \vec{w}_1 \\\\
\vdots \\\\
\vec{v}_n + \vec{w}_n
\end{bmatrix}$

**Definition 1.3.2** 
We multiply a scalar c against an n-vector v = $\vec{v}_n=\begin{bmatrix}
\vec{v}_1 \\\\
\vdots \\\\
\vec{v}_n
\end{bmatrix}$ by the rule $c\vec{v}_n=\begin{bmatrix}
c\vec{v}_1 \\\\
\vdots \\\\
c\vec{v}_n
\end{bmatrix}$.

**Definition 1.3.4** 
A linear combination of two n-vectors $\vec{v}$, w is an n-vector $a\vec{v}$ + $b\vec{w}$ for scalars a, b. More generally,
a linear combination of k such n-vectors $ v_1, v_2,...,v_k$ is $a_1v_1 + a_2v_2 + ··· + a _kv_k $ for scalars
$a_1, a_2, . . . , a_k.$

Linear combinations, or vector addition can be interpreted through a parallelogram rule. This is a nice geometric
interpretation of vector addition which showcases the commutative property of vector addition. Below I have provided an
image which nicely visualizes this parallelogram rule:

**Convex Linear Combinations:**
These Linear combinations involve two n-vectors $\vec{v}$ and $\vec{w}$. This linear combination of these vectors can be written in the
form $(1 − t)\vec{v} + t\vec{w} = \vec{v} + t(\vec{w} − \vec{v})$ with $0 ≤ t ≤ 1$. This adds to $\vec{v}$ a portion(given by t) of the displacement $\vec{w}$ − $\vec{v}$ from $\vec{v}$
to w. For $\mathbf{R}^2$ and $\mathbf{R}^3$ it can be interpreted as being a point on the line segment between the tips of $\vec{v}$ and
$\vec{w}$; e.g., it is $\vec{v}$ when t = 0, it is the midpoint when t = 1/2, and it is $\vec{w}$ when t = 1.

Here's an image to help visualize how t changes the influence each vector has on the linear combination:
![Convex Linear Combination](/static/images/Conv_lin_combo.png)

For any n-vectors 
$v_1 , . . . , v_k$ , a convex combination of them means a linear combination $t_1v_1 + ··· + t_kv_k$ for which all $t_j≥0$ and the 
sum of the coefficients is equal to 1; that is, $t_1 + ··· + t_k =1$. When the k coefficients are all equal, which is to say
every $t_j$ is equal to 1/k, this is the centroid of the k vectors. It's essentially just the average of the k vectors. 
Working in $\mathbf{R}^2$, a convex combination where not all coefficients are equal is a point inside the polygon with
vertices given by the $v_j$’s, with its distance to each $v_j$ weighted by the corresponding coefficient. 
If all coefficients are equal, it is the “center of mass” of the polygon defined by the vectors.

This is better interpreted by images, so take a look at this awesome screenshot from my textbook :)
![More Convex Linear Combination](/static/images/Conv_lin_combo2.png)

**Vector Algebra:**
As I stated earlier vector addition follows the commutative law. That is $\vec{v} + \vec{w} = \vec{w} + \vec{v}$. This is, at least
in my eyes, trivial so I do not feel the need to justify this law. This applies to all Rn(Latex) and applies to the
addition of more than just 2 vectors(associativity).

**Definition 1.6.1** The length or magnitude of an n-vector $\vec{v}$ = $\vec{v}_n=\begin{bmatrix}
\vec{v}_1 \\\\
\vdots \\\\
\vec{v}_n
\end{bmatrix}$, denoted ∥$\vec{v}$∥, is the number
$∥ v ∥ = \sqrt{v_1^2 + v_2^2 + · · · + v_n^2} ≥ 0$.
Note that the length is a scalar, and ∥$-\vec{v}$∥ = ∥$\vec{v}$∥ (in accordance with the visualization of $-\vec{v}$ as “a
copy of $\vec{v}$ pointing in the opposite direction”) because signs disappear when squaring each $-\vec{v}_j$ .
If c is any scalar then ∥$c\vec{v}$∥ = |c|∥$\vec{v}$∥ (i.e., if we multiply a vector by c then the length scales by
the factor |c|). For example, (−5)$\vec{v}$ has length 5∥$\vec{v}$∥.
(In other references, you may see ∥$\vec{v}$∥ called the “norm” of $\vec{v}$.)

**Definition 1.6.4:** 
The distance between two n-vectors $\vec{x}$, $\vec{y}$ is defined to be $∥\vec{x} − \vec{y}∥$.
(This will soon be visualized as the familiar notion of distance between tips of arrows for n = 2, 3. In general, it also
equals $∥\vec{y} − \vec{x}∥$ since $y − x = −(x − y)$ and any vector has the same length as its negative, so the order of subtraction doesn’t matter.


**Definition 1.7.1:** 
The zero vector in $\mathbf{R}^2$ is $0 = \begin{bmatrix}
0 \\\\
\vdots \\\\
0
\end{bmatrix}$, and a unit vector is a vector pointing in the same direction as $\vec{v}$ with length one, found using the
following: $\vec{u}=\frac{\vec{v}}{∥\vec{v}∥}$.
Always ∥$\vec{v}$∥ ≥ 0, and $∥\vec{v}∥ = 0$ precisely when $\vec{v}$ = 0.

Include here some worked examples

## Chapter 2

From here on we will see my lack of time become...apparent in terms of the quantity of notes produced. However, I will
try to make up for that with quality :).

### Vector Geometry and Correlation Coefficients

In this section I will cover how the dot product can be used to develop a geometric understanding for $\mathbf{R}^n$.
I will start by discussing the dot product in $\mathbf{R}^2$ & $\mathbf{R}^3$, then I will generalize to n > 3. 

**Definition 2.1.1:**
In $\mathbf{R}^2$ the angle between two vectors: $a=(a_1, a_2)$ & $b=(b_1, b_2)$ can be related by $\cos(\theta)=\frac{a_1b_1+a_2b_2}{||a||||b||}$


This may seem strange, but it is actually just a re-arranged form of the law of cosines. Imagine a triangle formed by
the vectors $a$, $b$, and $(a-b)$. We will refer to $a$ as side $A$, $b$ as side $B$, and $(a-b)$ as side $C$. The law
of cosines says $C^2=A^2+B^2-2AB\cos(\theta)$. We can rearrange this to $\cos(\theta)=\frac{A^2+B^2-C^2}{2AB}$. Putting
the numerator and denominator in terms of the vector form gives us $\cos(\theta)=\frac{(a_1^2+a_2^2)+(b_1^2+b_2^2)-((a_1-b_1)^2+(a_2-b_2)^2)}{2||a||||b||}$
This simplifies out to the result above. This method of finding the angle between two vectors can be generalized to n dimensions by the dot product.

**Definition 2.1.6:**
Consider n-vectors $\vec{x}=\begin{bmatrix}
\vec{x}_1 \\\\
\vdots \\\\
\vec{x}_n
\end{bmatrix}$ & $\vec{y}=\begin{bmatrix}
\vec{y}_1 \\\\
\vdots \\\\
\vec{y}_n
\end{bmatrix}$.

(i) The *dot product* of x and y is defined to be the scalar: $x \cdot y=x_1y_1+x_2y_2+...+x_ny_n=\sum_{i=1}^{n} x_iy_i$
(The dot product is only defined if the two vectors are n-vectors for the same value of n.)

(ii) The angle $\theta$ between two nonzero n-vectors x, y is defined by the formula: $\cos(\theta)=\frac{x \cdot y}{||x||||y||}$ With 0° ≤ $\theta$ ≤ 180°

(iii) When $x \cdot y=0$, x and y are perpendicular/orthogonal

Here's an image to help visualize:
![Dot Product](/static/images/Dot_product.png)

Some properties of the dot product naturally follow:

$v \cdot v= v_1^2+v_2^2+...+v_n^2=||v||^2\geq 0$ with equality exactly at when **v**=0

**Cauchy-Schwarz Inequality:**  $|x \cdot y|\leq||x||||y||$

This results from looking at the other helpful formulation of the dot product: $x \cdot y=\cos(\theta)||x||||y||$. As we
can see, if we take the absolute value, the cosine in the formula will only ever give values $0\leq\cos(\theta)\leq1$
therefore the dot product will always be capped by the magnitude of the first vector multiplied by the magnitude of the
second(when cosine is at 0).

**Theorem 2.2.1**: For any n-vectors v, w, $w_1$, $w_2$, the following hold:

(i) $v \cdot w=w \cdot v$

(ii) $v \cdot v=||v||^2$(already referenced above)

(iii) $v \cdot (cw) = c(v \cdot w)$ for any scalar c, and $v \cdot (w_1+w_2)=v \cdot w_1 + v \cdot w_2$

(iii') Combining both rules in (iii), for any scalars c_1, c_2 we have $v \cdot (c_1w_1 + c_2w_2)=c_1(v \cdot w_1) + c_2(v \cdot w_2)$

These can be generalized to larger n: $v \cdot w=\sum_{i=1}^{n}v_iw_i=w \cdot v=\sum_{i=1}^{n}w_iv_i$

Here's an example of using the dot product with larger n:
![Dot Product for Larger n](/static/images/Dot_product3.png)

**Correlation Coefficients:**
Given data points $(x_1,y_1),(x_2,y_2),...(x_n,y_n)$, it is often useful to find a line of best fit for the data. But to
determine whether it is even worth finding a best fit line, it is useful to see if there is a linear relationship
between the $x_i$'s and the $y_i$'s. The correlation coefficient, *r*, measures such linear relation.

**Definition 2.2.3:**
Consider a set of n data points $(x_1,y_1),(x_2,y_2),...(x_n,y_n)$. $X=\begin{bmatrix}
\vec{x}_1 \\\\
\vdots \\\\
\vec{x}_n
\end{bmatrix}$, $Y=\begin{bmatrix}
\vec{y}_1 \\\\
\vdots \\\\
\vec{y}_n
\end{bmatrix}$
The correlation coefficient between the $x_i$'s and the $y_i$'s is the cosine of the angle between x and y: or $r=\frac{X \cdot Y}{||X||||Y||}$

Some examples of correlation coefficients:
![Correlation Coefficients](/static/images/Correl_coeff.png)

Add examples and a few other things

## Chapter 3

### Planes

In this section I will discuss planes in $\mathbf{R}^3$. In particular, I will discuss the different descriptions of
planes, the transition between different forms of writing an equation for a plane, determine if points lie on the same
side or different sides of a plane, and interpreting the parametric form in terms of displacement vectors from a point
on the plane.

**Definition 3.1.1:**
The collection of points (x, y, z) in $\mathbf{R}^3$ satisfying an equation of the form $ax+by+cz=d$ is known as a plane.
At least one of the constants a, b, or c must be non-zero. 

**Equational Form:**
$\large ax+by+cz=d$ 

-This form describes the set of all x, y, and z that lie on the plane. It will also be useful in
determining whether 2 or more points are on the same side of a plane.

**Parametric Form:**
$\large \begin{bmatrix}
p_1 \\\\
p_2 \\\\
p_3
\end{bmatrix} + t\begin{bmatrix}
v_1 \\\\
v_2 \\\\
v_3
\end{bmatrix} + t'\begin{bmatrix}
w_1 \\\\
w_2 \\\\
w_3
\end{bmatrix}$ 

-This form describes the set of all points on the plane as the linear combination of some initial point, P, lying on the
plane, with two independently-scaled vectors v and w which describe two directions on the plane. *Note that these 
vectors do not have to be perpendicular, since the set of all linearly independent vectors span the entire plane that
they lie on.*

![parametric form](/static/images/Parametric_plane.png)

**Point and Normal Vector Form:**
$\large P=\begin{bmatrix}
p_1 \\\\
p_2 \\\\
p_3
\end{bmatrix}$ and $\large n=\begin{bmatrix}
n_1 \\\\
n_2 \\\\
n_3
\end{bmatrix}$

![normal plane](/static/images/Normal-plane.png)

-This isn't a complete form on it's own, rather it is actually the basis for the equational form of a plane, but it is
helpful to visualize the plane in terms of the normal vector and the point which define the set of all other points on
the plane. In-fact for the equational form the coefficients a, b, and c are all determined by the normal vector n where
$(n_1, n_2, n_3)$ represent a, b, and c respectively. Finally, d is found by plugging in point P for x, y, and z and 
evaluating the result. *Note that the vectors used must not be scalar multiples of each other.*

**Other Ways the Information to Form a Plane Might be Given:**
Sometimes the information necessary to form a plane might be given by three points P, Q, R. Two find an equation for a plane 
with this information, all that is necessary is to pick some initial point, say P(will also serve as initial point for 
parametric form), then find the direction vectors from P to Q and P to R. After, you can either take the parametric path
by organizing $\vec{PQ}$ and $\vec{PR}$ and using the initial point P to reach the form $P + t\vec{PQ} + t'\vec{PR}$, or
you can take the equational/normal form by finding the normal vector $n$. $n$ can be found by creating an arbitrary 
vector $\vec{n}=\begin{bmatrix}
n_1 \\\\
n_2 \\\\
n_3
\end{bmatrix}$ and setting up a system of equations that modeled by the dot product of it with each vector(making sure
to set the dot product to zero. By doing so, values of $n_1, n_2, and n_3$ can be found which, when dotted with each 
vector is zero, therefore proving that $\vec{n}$ is orthogonal to the plane. Then using $n_1, n_2, and n_3$ for a, b, 
and c, we can find the equational form after plugging in the initial point P for x, y, and z.

Additionally, you may be provided with the normal vector of the plane, and you may be asked to find the parametric form
of the plane. To do this, write the equational form of the plane then restrict either x or y or z to be zero, then set 
one of the others to be 1, then evaluate what the last variable must be to lie on the plane. Repeat to obtain a third
point then create the directional vectors necessary to write the parametric form of the equation. *We should make sure
that the coefficient of that third variable solved at the end is not 0.*

**Describing a Line in Parametric Form:**
A line in parametric form can be expressed through a vector, $p$, which specifies a point the line originates from, and  
a scaled vector $tv$. We can visualize this scaled vector as the actual line, where each segment is made up of a 
different scalar t, and the entire line is made up by the set of all scalars t.

This form can help us understand the equational form of planes. With a manipulation of variables we can express the 
plane as z in terms of x and y, then we can fix x or y. Visualizing the set of same-sloped lines created when fixing one
of these variables and evaluating the expression at various values of the fixed variable will result in a plane becoming
clear. However, there are multiple non-planar surfaces that can create such a set of lines when performing this process,
therefore we must make a distinction. The lines created by these planes will have the same slope, and the rate by which
their height varies at a linear rate.

![Equational Form Justification](/static/images/Plane_cross.png)

Add examples and images

## Chapter 4

### Span, Subspaces, and Dimension
When given a set of n-vectors in Rn, oftentimes it is useful to look at the space that could be covered by the set of
all linear combinations of those vectors. This space is defined as the span of those n-vectors. For example given a 
plane in R3 passing through *0*=(0, 0, 0). We want to mathematically express the idea that the plane is flat with 2 
degrees of freedom. By choosing two vectors v & w that do not lie on a common line through *0* we can map out every 
point in the plane as a combination of scalar multiples of the vectors v and w. In other words, plane: $P = {all 
vectors of the form av + bw, for scalars a, b}$. If any n n-vectors happen to be scalar multiples of each other, they 
are defined as being linearly dependent and thus, they lay on the same line with span defined by a scalar multiplied by
the direction vector of the line.

![span](/static/images/Span1.png)

**Definition 4.1.3:**
The *span* of vectors $v_1, ...,v_k$ in Rn is the collection of all vectors in Rn that one can obtain from $v1, ..., vk$
by repeatedly using addition and scalar multiplication. In symbols:$span(v_1, ...,v_k)=${all*n*-vectors *x* of the form 
$c_1v_1+...+c_kv_k$} where $c_1, ...,c_k$ are arbitrary scalars.

In R3, for k=2 and nonzero $v_1$, $v_2$ not multiples of each other, this recovers the parametric form of a plane 
through P = 0. In general, the span of a collection of finitely many n-vectors is the collection of all the n-vectors 
one can reach from those given n-vectors by forming linear combinations in every possible way.

![More span](/static/images/Span2.png)

The span of two nonzero n-vectors that are not scalar multiples of each other should be visualized as a plane through *0*
in Rn(assuming n is not 1). With larger Rn and larger sets of vectors we will discuss visualizing/understanding their 
span.

The set of vectors in Rn perpendicular to any fixed nonzero vector in Rn is a span of n-1 nonzero n-vectors. As we know 
in R3 the set of vectors perpendicular to a 3-vector is the span of 2 3-vectors(a plane).

![Even more span visualization](/static/images/Span3.png)

A line in R2 or R3 passing through *0* and a plane in R3 passing through *0* each arise a span of one or two vectors.
But lines and planes not passing through *0* are not a span of any collection of vectors since the span of any collection
of n-vectors always contains 0, by setting all coefficients $c_1, ..., c_k$ in Definition 4.1.3 to be 0.

If V is the span of some finite collection of vectors in Rn then there are generally many different sets of vectors that
have the same span.

Add in example discussing the 4-vectors that amre perpendicular to another vector

**Definition 4.1.7:**
A *linear subspace* of Rn is a subset of Rn that is the span of a finite collection of vectors in Rn. If V is a linear 
subspace of Rn, a spanning set for V is a collection of n-vectors v1, ..., vk whose span equals V.

**Affine Subspaces:**
Sometimes a line or plane will not pass through the origin, and we will want to discuss the space which the composite 
vectors describe. We define such a space as an *affine subspace* although the concept is surprisingly less practical than
linear subspaces.

**Proposition 4.1.11:**
If V is a linear subspace in Rn, then for any vectors $x_1, ..., x_m$ lying in $V$ and scalars $a_1,...,a_m$ the linear 
combination $a_1x_1+...+a_mx_m$ also lies in V. What follows is that in order to check if a set is a linear subspace, we
must make sure it satisfies the conditions of a linear subspace: all cV and V+W make up the set.

To determine if some equation represents a linear subspace what I need to do is find some points/vectors (x,y,z) that
satisfy the conditions of the equation then verify whether they: contain the zero vector;  can be scaled and still
satisfy the equation, and can be added and still satisfy the equation

Include example 4.1.13
Namely explain why they first rewrite the perpendicularity equations in terms of three variables then explain how that 
relates to the span of vectors that are perpendicular to the two vectors. Answer: the perpendicular vector we solved for
represents the linear combination of three scaled vectors with scalars x_2, x_4, and x_5 which makle up all the normal
vectors to the other two vectors.

**Example Problem:** Consider the set W of all vectors in c that are perpendicular to both $\begin{bmatrix}
1 \\\\
1 \\\\
0 \\\\
-1 \\\\
2
\end{bmatrix}$ and $\begin{bmatrix}
0 \\\\
2 \\\\
3 \\\\
1 \\\\
-1
\end{bmatrix}$.

We will now find three explicit 5-vectors $v_1, v_2, v_3$ so that *W* = span($v_1, v_2, v_3$), and in particular W is 
a linear subspace of $\mathbf{R}^5$. *(This phenomenon is not specific to W; it works for perpendicularity against any 
finite collection of vectors in any $\mathbf{R}^n$. This can be explained by relating the algebra and geometry of linear
algebra: showing that the solution to any such system of conditions is a span of a finite set of vectors.)* Now we write
out the two perpendicularity requirements in terms of dot products. Namely, a vector $\begin{bmatrix}
x_1 \\\\
x_2 \\\\
x_3 \\\\
x_4 \\\\
x_5
\end{bmatrix}$ in $\mathbf{R}^5$ lies in *W* precisely when it satisfies the two "perpendicularity equations"
$$x_1 + x_2 - x_4 + 2x_5 = 0, 2x_2 + 3x_3 + x_4 - x_5 = 0$$.
We can rewrite these two equations as expressing two of the variables in terms of the others (with no further 
constraints in these other variables), say $x_1, x_3$ in terms of $x_2, x_4, x_5$: the pair of equations equivalently 
says
$$x_1=-x_2+x_4-2x_5, x_3=-(2/3)x_2-(1/3)x_4+(1/3)x_5$$.
Since there are no restrictions at all on $x_2, x_4, x_5$, W is the collection of vectors of the form $\begin{bmatrix}
-x_2 + x_4 - 2x_5 \\\\
x_2 \\\\
-(2/3)x_2 - (1/3)x_4 + (1/3)x_5 \\\\
x_4 \\\\
x_5
\end{bmatrix}$ for arbitrary scalars $x_2, x_4, x_5$. This vector can be expressed in the form of a linear combination 
by separating out the parts involving each $x_2, x_4, x_5$ separately: $\begin{bmatrix}
-x_2 \\\\
x_2 \\\\
-(2/3)x_2 \\\\
0 \\\\
0
\end{bmatrix}$ + $\begin{bmatrix}
x_4 \\\\
0 \\\\
-(1/3)x_4 \\\\
x_4 \\\\
0
\end{bmatrix}$ + $\begin{bmatrix}
-2x_5 \\\\
0 \\\\
(1/3)x_5 \\\\
0 \\\\
x_5
\end{bmatrix}$ =  $x_2\begin{bmatrix}
-1 \\\\
1 \\\\
-(2/3) \\\\
0 \\\\
0
\end{bmatrix}$ + $x_4\begin{bmatrix}
1 \\\\
0 \\\\
-(1/3) \\\\
1 \\\\
0
\end{bmatrix}$ + $x_5\begin{bmatrix}
-2 \\\\
0 \\\\
(1/3) \\\\
0 \\\\
1
\end{bmatrix}$.

In other words, W is the span of vectors $v_1=\begin{bmatrix}
-1 \\\\
1 \\\\
-(2/3) \\\\
0 \\\\
0
\end{bmatrix}$, $v_2=\begin{bmatrix}
1 \\\\
0 \\\\
-(1/3) \\\\
1 \\\\
0
\end{bmatrix}$, $v_3=\begin{bmatrix}
-2 \\\\
0 \\\\
(1/3) \\\\
0 \\\\
1
\end{bmatrix}$.

Now we will move on to discussing dimension. A good way of understanding the dimension of something is to consider the 
collection P4 of all polynomials of degree at most 4. Such a polynomial has the form $ax^4+bx^3+cx^2+dx+e$ where all 
constants can be any real numbers. This description involves 5 independent choices(a,b,c,d,e). Essentially this means P4
is 5 dimensional since it can be defined by 5 numbers. Informally, the "dimension" of an object X tells us how many 
different numbers are needed to locate a point in X.

Now with this general idea we can better articulate this to be less ambiguous and more useful. We will do this by 
focusing on the case of a linear subspace V of Rn, where vector algebra will provide a way to make that informal idea
precise. The "dimension" of V will be, intuitively, the number of independent directions in V. In other words, it will 
tell us how many numbers we need in order to specify a vector v in V.

**Definition 4.2.4:**
Let V be a nonzero linear subspace of some Rn. The dimension of V, denoted as dim(v), is defined to be the smallest 
number of vectors needed to span V. We define dim({0})=0.

**Theorem 4.2.5:**
For $k\geq 2$, consider a collection $v_1,...,v_k$ of vectors spanning a linear subspace V in Rn. We have dim(V)=k 
precisely when there is no redundancy, or when each $v_i$ is not a linear combination of the others(removing one destroys the spanning property).
Equivalently, dim(V)<k precisely when "there is redundancy": some $v_i$ is a linear combination of the others, or in other words
removing it will not affect the span.

**Theorem 4.2.8:**
If V and W are linear subspaces of Rn with W contained in V(every vector in W also belongs to V) then dim(W)$\leq$dim(V)

**Dimension Criterion:**
Span of two vectors: a subspace span(u,v) has dimension 2 if u and v are not collinear.
Span of three vectors: a subspace *V* = span(u,v,w) has dimension three except when:
-all vectors are collinear. Then dim(V)=1.
-two of the three vectors are collinear. Then dim(V)=2.
-None of the vectors are collinear, but one of them is a linear combination of the two others. Then dim(V)=2.


## Chapter 5

### Basis and orthogonality

**Definition 5.1.1:**
A basis of a subspace V of Rn is a spanning set of V that has exactly k=dim(V) n-vectors. i.e. a spanning set with as
few vectors as possible in it.

Since a linear subspace has many spanning sets, it has many bases. For example, if {u,v,w} is a basis of V, then so is 
{-u,2v,v+W}, BUT NOT {2u,-v+w} since it has only 2 n-vectors defining 3-space--NOR IS {-u,2v,u-4v} since its vectors do 
not include w. Also, any set of 4 3-vectors in this example would not be considered a basis because it is not the least 
number of vectors necessary to define the linear subspace.

To see if any given set of k n-vectors has $dim(v) <$ span$(v_1,v_2, ..., v_k)$ we can simply pick one $v_i$ and pick
arbitrary scalars $c_1, ...,c_k$ not including $c_i$ then we can set $v_i$ equal to the linear combination of the other
scaled vectors to set up a system of equations. With this system of equations we can find the potential linear 
combinations that result in vector $v_i$ proving that $dim(v) <$ span$(v_1,v_2, ..., v_k)$. If the set of k n-vectors is
a basis for *V*, then there will be no such set of scalars which result in a linear combination that equals $v_i$. Later
on we will find a way to remove redundancy for a spanning set for a linear subspace *V* of Rn, but for now this is all
we have lol. The next type of spanning set for any linear subspace *V* is always guaranteed to be a basis of *V*.

**Definition 5.2.1:**
A collection of vectors $v_1,v_2, ..., v_k$ in Rn is called orthogonal if $v_i\cdot{v_j}=0$ whenever *i* is not equal to
*j*. I.e. all the vectors are perpendicular to one another.

**Theorem 5.2.2:**
If $v_1,v_2, ..., v_k$ is an orthogonal collection of *nonzero* vectors in Rn then it is a basis for span($v_1,v_2, ..., v_k$).
In particular, span($v_1,v_2, ..., v_k$) Then has dimension *k*, and we call $v_1,v_2, ..., v_k$ an *orthogonal basis* 
for its span. *(A single nonzero vector is always an orthogonal basis for its span)*

The span of a collection of *k* vectors in Rn has dimension of at most *k*. By theorem 5.2.2, orthogonality is a useful way to guarantee that *k* given nonzero n-vectors have a *k*-dimensional span.

Include example 5.2.4

**Theorem 5.2.5:**
Every nonzero linear subspace of Rn has an orthogonal basis. There is an especially convenient type of orthogonal basis
for every type of orthogonal basis for a nonzero linear subspace of Rn included in definition 5.2.6

**Definition 5.2.6:**
A collection of vectors $v_1,v_2, ..., v_k$ in Rn is called *orthonormal* if they are orthogonal to each other and in 
addition they are all unit vectors; that is $v_i\cdot{v_i}=1$ for all *i* (ensuring $||v_i||=\sqrt{v_i\cdot{v_i}}=\sqrt{1}=1$ for all *i*).

Any orthonormal collection of vectors is a basis of its span, by theorem 5.2.2.

It is worth noting that it is not always useful to try and solve a system of equations to find the dimension of some set
of vectors spanning *V* to see if they are a basis. In those cases where there are many unknowns and many equations, it 
may be more useful to simply check if the vectors are orthogonal.

**Theorem 5.3.6(Fourier Formula):**
For any orthogonal collection of nonzero vectors $v_1,v_2, ..., v_k$ in Rn and vector v in their span, 
$$v=\sum_{i=1}^k(\frac{v\cdot{v_i}}{v_i\cdot{v_i}}v_i$$
In particular, if the $v_i$'s are all unit vectors (so $v_i\cdot{v_i}=1$ for all *i*) then $v=\sum_{i=1}^k(v\cdot{v_i}v_i$.

This is basically just a nice formula for finding what linear combination of basis vectors gives another specific vector
within the span of the basis vectors.

![Fourier's Justification](/static/images/Fourier_justif.png)

**Example 5.3.8:**
Consider the explicit orthogonal basis ${w_1, w_2, w_3}$ for the linear subspace $V=span(v_1,v_2,v_3)$ in $\mathbf{R}^5$
with explicit $v_i$'s provided below. 

![Example 5.3.8.1](/static/images/5.3.8.1.png)

![Example 5.3.8.2](/static/images/5.3.8.2.png)
*(Note that in this case the orthogonal basis of $w_i$'s is given, we will learn how to solve later*

Applying the Fourier formula for the orthogonal basis ${w_1,w_2,w_3}$ of *V*, for 
each $v \in V$ we have $$v=\sum_{i=1}^3(\frac{(v\cdot{w_i})}{(w_i\cdot{w_i})})w_i=(\frac{(v\cdot{w_1})}{15})w_1+\frac{v\cdot{w_2}}{75}w_2+\frac{v\cdot{w_3}{64575}w_3$$
since the denominators in the final expression are just the dot product evaluations $w_1 \cdot{w_1}=15$, $w_2 \cdot{w_2}=75$, $w_3 \cdot{w_3}=64575$.

Consider the vector $v=2v_1-v_2+v_3=\begin{bmatrix}
2 \\\\
0 \\\\
6 \\\\
4 \\\\
2 
\end{bmatrix} - \begin{bmatrix}
1 \\\\
1 \\\\
2 \\\\
0 \\\\
3 
\end{bmatrix} + \begin{bmatrix}
0 \\\\
3 \\\\
0 \\\\
2 \\\\
1 
\end{bmatrix} = \begin{bmatrix}
1 \\\\
2 \\\\
4 \\\\
6 \\\\
0 
\end{bmatrix}$ in $V$. Since ${w_1,w_2,w_3}$ is a basis of *V*, we know that there is some expression of the form $v=c_1w_1+c_2w_2+c_3w_3$
for unknown scalars $c_1,c_2,c_3$. These scalars can be solved for using a brute-force system of equations:
$$\begin{bmatrix}
1 \\\\
2 \\\\
4 \\\\
6 \\\\
0 
\end{bmatrix}=v=c_1w_1+c_2w_2+c_3w_3=c_1\begin{bmatrix}
1 \\\\
0 \\\\
3 \\\\
2 \\\\
1 
\end{bmatrix} + c_2\begin{bmatrix}
1 \\\\
3 \\\\
0 \\\\
-4 \\\\
7
\end{bmatrix} + c_3\begin{bmatrix}
-33 \\\\
201 \\\\
-75 \\\\
132 \\\\
-6 
\end{bmatrix} = \begin{bmatrix}
c_1 + c_2 - 33c_3 \\\\
3c_2 + 201c_3 \\\\
3c_1-75c_3 \\\\
2c_1-4c_2+132c_3 \\\\
c_1 + 7c_2 - 6c_3 
\end{bmatrix}$$
However we already know that this would take a lot of time and effort. We can get around this by computing dot products
with fourier's formula for our specific vector *v*. To carry this out, we use the explicit descriptions of *v* and the $w_i$'s to compute
$v\cdot{w_1}=25$, $v\cdot{w_2}=-17$, $v\cdot{w_3}=861$, so fourier's formula would give: $$v=\frac{25}{15}w_1-\frac{17}{75}w_2 + \frac{861}{64575}w_3=\frac{5}{3}w_1-\frac{17}{75}w_2+\frac{1}{75}w_3$$


## Chapter 6

### Projections

Here we will look at what methods we can use to find either a) the projection of a point onto a line in terms of the 
scaled direction vector of the line, or b) the projection of a point onto a general linear subspace V in terms of 
a linear combination of scaled basis vectors.

We will begin with the more simple case: projecting a point onto a linear subspace of one dimension(a line). We will do
this in two ways, one of which makes use of vector algebra, and the other which looks at the geometry of such a 
projection. 

All of these projections will rely on finding some orthogonal vector in the linear subspace that is closest to the point
which we can express as a combination of the basis vectors.

Say we have line L, and we want to find the projection of point x onto line L. Also imagine that line L has direction 
vector w. The closest point on line L to x can then be expressed in terms of some scaled vector cw. The vector formed 
between the point x and cw expressed by (x-cw) is minimal(in length) and has the property that it is orthogonal to every
vector in line L. This is an idea that can be generalized to Rn. 

![Projection onto line](/static/images/Projection.png)

**Algebraic Method:**
We look for a scalar c for which x-cw is orthogonal to every vector in L. The points of L=span(w) are those of the form
aw for scalars a, so we seek c making $(x-cw)\cdot{aw}=0$ for every scalar a. The dot product has the property 
$(x-cw)\cdot{(aw)}=a((x-cw)\cdot{w})$, so actually all we need to do is make sure that $(x-cw)\cdot{w}=0$. We can rewrite
this dot product as $0=(x-cw)\cdot{w}=x\cdot{w}-(cw)\cdot{w}$. This can further be rearranged as $c(w\cdot{w})=x\cdot{w}$.
Since w is not a zero vector, we can rearrange into the final form: $c=\frac{x\cdot{w}}{w\cdot{w}}$. This is all to find
the scalar that minimizes the distance between the linear subspace and the point, but we can go further and express it 
as a vector to make a more comprehensible output in terms of some vector *v*. $$v=\frac{x\cdot{w}}{w\cdot{w}}w$$

**Geometric Method:**
I will not go too into depth since this method cannot be generalized to larger Rn(which is what we really care about). 
Essentially it revolves around making an acute angle $\theta$ between line L and the vector describing point x and
using the alternative way of describing the dot product in terms of cosine and the magnitude of the two vectors to find
that the projection can be expressed as: $(||x||cos{\theta})\frac{w}{||w||}$.

**Proposition 6.1.1:**
Let $L=span(w)={cw : c \in R}$ be a 1-dimensional linear subspace of Rn(so w is not equal to 0), a "line". Choose any 
point $x \in \mathbf{R}^n$. There is exactly one point in L closest to x, and it is given by the scalar multiple 
$$\frac{x\cdot{w}}{w\cdot{w}}w$$
of w. This is called "the projection of x into span(w)"; we denote it by the symbol $Proj_{w}(x)$.

We can find a faster way to project multiple points onto one line. The key observation in doing so is that the formula
for the $Proj_{w}(x)$ behaves well for any linear combination of n-vectors $x_1, x_2, ..., x_k$: the projection of a 
linear combination of all the $x_i$'s is equal to the corresponding linear combination of the projections.

**Example 6.1.4:**
Sometimes it is useful(much more so in subsequent sections) to express a projection onto a vector which is a 
linear combination. Right below here I have included an interesting property that arises out of the linear properties of
the dot product. Basically it just shows us that we can split up a projection into a combination of projections onto 
separate vectors.
![Example 6.1.4](/static/images/Lin_combo_proj.png)

Now we will move onto projecting onto a general subspace. Essentially we will just be finding the point in a linear 
subspace V of Rn nearest to a chose $x\in\mathbf{R}^n$, which we denote as $Proj_{V}(x) \in V$. This nearest point to x 
will be, as mentioned earlier computed as a sum of projections onto x into lines through 0 in V arising from an 
orthogonal basis of V.

![Linear Subspace Projection](/static/images/Lin_subspace_proj.png)

Essentially we need to find some vector $v$ that can be expressed as some linear combination of the other orthogonal basis
vectors. Dotting this vector $v$ with $x-Proj_{V}(x)$(this is also perpendicular to everything in V) will yield 0, and we
will be able to prove that this vector is indeed the closest vector to the point x. 

**Theorem 6.2.1:**
(Orthogonal Projection theorem version I) For any $x\in\mathbf{R}^n$ and linear subspace *V* of $\mathbf{R}^n$, there is
a unique *v* in *V* closest to x. (In symbols, $||x-v||<||x-v'||$ for all $v'$ in *V* with $v'\neq{v}$). This *v* is
called the *Projection of x onto V*, and is denoted $Proj_{v}(x)$. The projection $Proj_{v}(x)$ is also the only vector
$v \in V$ with the property that the displacement $x-v$ is perpendicular to *V*.
If *V* is nonzero then for any orthogonal basis $v_1, v_2, ..., v_k$ of *V* we have 
$$Proj_{V}(x)=Proj_{v_1}(x)+Proj_{v_2}(x)+...+Proj_{v_k}(x)$$,
where $Proj_{v_i}(x)=((x\cdot{v_i})/(v_{i}\cdot{v_i}))v_i$. 

(For $x\in V$ we have $Proj_{V}(x)=x$--the point in *V* closest
to x is itself.)

It may seem confusing that the basis must be orthogonal for this formula to hold true, afterall we have proved that for 
linearly independent vectors, we can represent any vector in their span by some linear combination of those vectors. 
This is still true, but the issue is that when we are projecting onto two non-orthogonal vectors, there will be 
redundancy in the projections. Imagine two very close vectors v and w representing some linear subspace *V*, when we 
take the projection of some point x onto *V*, these projections will basically be the same if they are very close. So 
when it comes to adding these projections to find the vector *y* that represents x's projection, we will be way off due 
to the overlap which v and w shared. Thus, it is essential that we always ensure that we have an orthogonal basis when 
projecting onto some linear subspace as it will ensure there is zero redundancy in the projections.


**Theorem 6.2.4(Orthogonal Projection Theorem, Version II):**
(Orthogonal Projection Theorem, Version II). 
If *V* is a linear subspace of $\mathbf{R}^n$ then every vector $x\in \mathbf{R}^n$ can be uniquely expressed as a sum 
$$x=v+v'$$
with $v\in V$ and $v'$ orthogonal to everything in *V*. Explicitly, $$v=Proj_{V}(x)$$ and $$v'=x-Proj_{v}(x)$$.

^ My preferred way of looking at this theorem.

**How to find an orthogonal basis for $V\in \mathbf{R}^n$:**
We know how to find a projection onto a general subspace *V*, but to do so we must have an orthogonal basis for the 
linear subspace *V*. This will be addressed in chapter 19 and 20 using the Gram-Schmidt process and some matrix algebra.

Maybe include proof 6.3

## Chapter 7

### Applications of Projections in $\mathbf{R}^n$: orthogonal bases of planes and linear regression

So far we have found a formula for projection to a linear subspace of $\mathbf{R}^n$ using an orthogonal basis of the 
linear subspace, but we can also go the other way and use projections to find an orthogonal basis for a linear subspace.

**Theorem 7.1.1:**
Suppose $x$, $y$ $\in \mathbf{R}^n$ are nonzero, and not scalar multiples of each other. The vectors *y* and $x'=x-Proj_{y}(x)$
constitute an orthogonal basis of span(x,y).

![Error Measurement](/static/images/Lin_regression_error.png) 

**Fitting a function to data:**
Essentially we want to find the function $f(x) = mx + b$ that "best fits" n data points $(x_1,y_1),...,(x_n,y_n)$. 
We just want to make some $f(x_i)$ to be as close as possible to $y_i$ for *i*. The error: $error_i=y_i-(mx_i+b)$
measures in absolute value how close the line $y=mx+b$ is vertically to $(x_i,y_i)$. Since we are arbitrarily measuring
the "best fit" we can square the *error* for each *i* and find the sum of errors of the set (x, y). $\sum_{i=1}^n(y_i-(mx_i+b))^2$.

**Example 7.3.2**
![Example 7.3.2](/static/images/7.3.2.png)

**General 7.3:**
Here is the general method. Suppose we are given n data points $(x_i, y_i)$ that do not lie on a common vertical line. 
To find the best line $y=mx+b$, do the following.
(i)Assemble the given data into two n-vectors
$$X=\begin{bmatrix}
x_1 \\\\
\vdots \\\\
x_n
\end{bmatrix}$$ & $$Y=\begin{bmatrix}
y_1 \\\\
\vdots \\\\
y_n
\end{bmatrix}$$. Also let *1* be the n-vector all of whose entries are equal to 1

(ii) For $W=span(X,1)$, we will compute $Proj_w(Y)$ as a linear combination of $mX+b$*1* of *X* and *1*; those 
coefficients are exactly the coefficients of the best line $y=mx+b$.

(iii) To compute $Proj_W(Y)$, use the orthogonal basis *1* and $\hat{X}=X-Proj_1(X)$ for *W*. Explicitly 
$$\hat{X}=\begin{bmatrix}
x_1-\bar{x} \\\\
\vdots \\\\
x_n-\bar{x}
\end{bmatrix}$$ and so $Proj_{W}(Y)$=$(\frac{Y\cdot{\hat{X}}}{\hat{X}\cdot{\hat{X}}})(\hat{X})$ + $\bar{y}1$ $=$ $(\frac{Y\cdot{\hat{X}}}{\hat{X}\cdot{\hat{X}}})(X-\bar{x}1)+\bar{y}1$

If we imagine minimizing this error between the data points given by the vector *Y* and the line of best fit defined by 
*mX+b* in terms of $\mathbf{R}^n$, then we can interpret this formula as finding the 
projection(point of minimal distance between it and linear subspace V) of *Y* onto the linear subspace defined
by *X* and *1*. Here is an image to help:
![Linear Regression Formula Justification](/static/images/Linear_regression_justif.png)


Whenever $\bar{x}=0$ we have $\hat{X}=X$.

if $\bar{x}=0$ then $Proj_{W}(Y)=(\frac{Y\cdot{X}}{X\cdot{X}})X+\bar{y}1$, so $m=(\frac{Y\cdot{X}}{X\cdot{X}})$ and $b=\bar{y}$ whenever $\bar{x}=0$.
*Only when $\bar{x}=0$!!!!*



**Finding the distance between two lines:**
Let $l_1$ be the line in $\mathbf{R}^3$ that is parallel to $v=\begin{bmatrix}
2 \\\\
3 \\\\
4 
\end{bmatrix}$ and goes through $a=\begin{bmatrix}
1 \\\\
0 \\\\
0
\end{bmatrix}$, and let $l_2$ be the line in $\mathbf{R}^3$ that is parallel to $v=\begin{bmatrix}
4 \\\\
3 \\\\
2 
\end{bmatrix}$ and goes through $b=\begin{bmatrix}
0 \\\\
1 \\\\
0 
\end{bmatrix}$. What is the closest distance between $l_1$ and $l_2$?

Here is an image to help with illustration:
![7.4](/static/images/Dist_btw_lines2.png)

To solve this problem, we can express the solution as finding a closest point to a plane(projection). The parametric 
form of lines in space gives $l_1$ consists of the points of the form $a+tv$ for an arbitrary scalar $t$, and $l_2$ 
consists of the points of the form $b+t'w$ for an arbitrary scalar $t'$. The distance between any two points on the 
lines can be provided by $||(a+tv)-(b+t'w)||$. We look for $t$ and $t'$ that minimize this distance.

Instead of trying to arbitrarily search for a scalar that minimizes the distance between these lines, we can instead 
re-write the form for the distance between any two points in the line as: $(a+tv)-(b+t'w)=(a-b)-(t'w-tv)$, which we can 
interpret as the distance between the vector/point $a-b$ and the vector $t'w-tv$. Varying $t$ and $t'$ gives thew span 
of the vectors $v$ and $w$. This now offers us the alternative geometric interpretation of the problem included below:
![7.4.2](/static/images/Dist_btw_lines1.png)

We can clean up this to produce a more familiar image of a projection onto a linear subspace *V*:
![7.4.3](/static/images/Dist_btw_lines3.png)

I personally would not have arrived at this creative reinterpretation of the problem, but now we can see the intuition 
behind this reinterpretation.

Step 1: We want to use a projection onto a linear subspace to minimize the distance between the point and the linear 
subspace *V* defined by the span of vectors *v* and *w*
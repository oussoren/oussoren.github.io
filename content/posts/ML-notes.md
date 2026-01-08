+++
title = "Machine Learning Notes"
date = "2026-01-05"
draft = false
math = true
tags = ["linear algebra", "programming", "python", "probability", "math"]
+++

# Overview
Here are my notes for CS229, a graduate class in Machine Learning.

# Supervised Learning

The thing that distinguishes supervised learning from other machine learning is the fact that there are labels associated
with our features.

## Regression

In regression we introduce a model that describes a relationship between our features and our outputs. f(x) -- our model
describes the expected relationship between x and y. In regression our model for a specific training point will output
$f(x_i)$. We will also have the actual value for that training point $x_i$, $y_i$. We consider the difference between our
model and the output, we call it epsilon i. Our expectation for this error, will be normally distributed with mean 0.

### House Example
Suppose you have a dataset of information about houses. For simplicity's sake, say our data for each house is just 
the square footage, and our label or output is the price of our output. For this example we have a linear regression model
where $f(x)= w_0 + w_1x, and y_i = w_0 + w_1x_i + \epsilon_i$. In order to choose the line that best fits our data, we will
consider the residual sum of squares(sum of square differences between our prediction and the label), and we choose the
parameters w_0 and w_1 that minimize the cost (our RSS). $min(w_0,w1)\sum_{i=1}^{N}(y_i - [w_0 + w_1x_i])^2$.

### Polynomial regression:
Our data doesn't look like a simple linear relationship when we plot it. We assume the model is as such,
$y_i = w_0*1 + w_1x_i + w_2x_i^2 + ... + w_px_i^p + \epsilon_i$.

### Generic Featurized Linear Regression:
$y_i = w_0*1 + w_1h_1(x_i) + w_2h_2(x_i) + ... + w_ph_p(x_i) + \epsilon_i$. Where h(x) is some function of our feature.
i.e. h(x)=log(beds) * log(baths) where x is now a vector and beds and baths are features.
There is an easier way to write the generic model, which instead of writing $\sum_{j=0}^{D-(num features)}w_jh_j(x_i) + \epsilon_i = w\cdot{h(x_i)} + \epsilon_i$

*inputs v. features*

Suppose we have a table of observations where our ith row is observation i and our jth column is feature j. We are given a set
of inputs, but we can choose our features -- essentially manipulations (h(x)). This feature is a specific transformation of that raw data designed to make the relationship with the output ($y$) easier for a linear model to see.

### Matrix Notation
For observaiton i,
$y_i = \sum_{j=0}^Dw_jh_j(x_i) + \epsilon_i$.
We need to do this over every training point. Suppose our dataset is actually a matrix where the ith row is training point
i. Call this matrix $H$. Thus, our vector of observations, y, can be represented as such,
$y = H(w) + \epsilon$. Where these variables are vectors and $H$ represents the linear transformation of our observations/features.

### Some notes about feature generation
If you have no idea what the relationship is, you can just throw in every possible combination and let the math sort it out. This is called Polynomial Expansion.If you have two inputs, $x_1$ and $x_2$, you can "engineer" a massive list of features:$h_1(x) = x_1$
$h_2(x) = x_2$
$h_3(x) = x_1^2$
$h_4(x) = x_2^2$
$h_5(x) = x_1 \cdot x_2$ (This is an interaction term, capturing how two features affect each other).
In Deep Learning what happens is we just use the chain rule to look at how our individual features are affecting our estimate, we pick the one that is affecting the estimate the most, and we perform a chain rule to see how the weights in this feature need to be changed to produce the most likely results.
We will dive into this later though.


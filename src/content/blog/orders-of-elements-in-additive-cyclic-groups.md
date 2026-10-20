---
title: 'How Many Additions Return to Zero? The Order of Elements in Cyclic Groups'
description: 'A mathematical note on modular addition, the gcd and lcm formulas for element order, residue cycles, generators, and a reproducible Python verification.'
pubDate: '2026-10-21'
tags:
  - Group Theory
  - Abstract Algebra
  - Number Theory
  - Mathematics
  - Python
  - Computational Mathematics
draft: false
---

*By Md Arif Hossain*

*This article develops the LCM-first and residue-wheel approach that I explored during my undergraduate studies, with expanded examples, proofs, and computational verification.*

**[Read the complete mathematics paper (PDF)](/papers/orders-in-additive-cyclic-groups.pdf)**

## 1. A simple question in modular arithmetic

Consider the integers modulo $10$:

$$
\mathbb Z_{10}=\{[0],[1],[2],\ldots,[9]\}.
$$

Addition takes place modulo $10$. For example, $[7]+[6]=[3]$ because $13\equiv3\pmod {10}$. Now choose an element, such as $[4]$, and repeatedly add it to itself. Starting from $[0]$, the sequence is

$$
[0]\to[4]\to[8]\to[2]\to[6]\to[0].
$$

After five additions, we are back at zero. Five is therefore the **order** of $[4]$ in the additive group $\mathbb Z_{10}$.

Why five, rather than ten? Why does adding $[1]$ take ten steps while adding $[5]$ takes only two? The answer involves a useful relationship between cyclic groups, divisibility, the greatest common divisor, and the least common multiple.

I approached this problem in my undergraduate mathematics work by starting with a simple question: what is the *first multiple of a chosen step size* that is also a multiple of the modulus? The answer is the least common multiple. I then drew repeated additions as jumps on a circular **residue wheel**, using the picture to count how many jumps it took to return to zero. The wheel diagrams helped me connect the first-common-multiple calculation to the number of steps needed to return to zero.

## 2. Groups and element order

A group is a set equipped with an associative operation, an identity, and an inverse for each element; it is also closed under the operation. The group $\mathbb Z_n$ consists of the residue classes $[0],\ldots,[n-1]$ with addition modulo $n$. Its identity is $[0]$.

The order of $[a]$ in $\mathbb Z_n$ is the least positive integer $k$ such that

$$
k[a]=[0].
$$

Since $k[a]=[ka]$, this is equivalent to the congruence

$$
ka\equiv0\pmod n,
$$

or, in the language of divisibility,

$$
n\mid ka.
$$

This restatement is the key step: **finding an element's order means finding the smallest positive multiplier of $a$ that is divisible by $n$**.

## 3. My starting point: the least common multiple

When I first explored the problem, I did not begin by calculating a greatest common divisor. I started with the integer sums before they were reduced modulo $n$:

$$
a,2a,3a,4a,\ldots.
$$

The residue returns to zero at the first positive step $k$ for which $ka$ is divisible by $n$. But $ka$ is already a multiple of $a$, so that first unreduced total must be the **least positive common multiple of $a$ and $n$**.

Therefore, for $1\le a<n$,

$$
\boxed{\operatorname{ord}_n([a])=\frac{\operatorname{lcm}(a,n)}{a}.}
$$

For example, choose $a=4$ and $n=10$. The multiples of $4$ begin $4,8,12,16,20$, and the multiples of $10$ begin $10,20$. Their first shared number is $20$, so the return time is

$$
\operatorname{ord}_{10}([4])=\frac{\operatorname{lcm}(4,10)}4=\frac{20}{4}=5.
$$

Those five steps are precisely the wheel positions:

$$
[0]\to[4]\to[8]\to[2]\to[6]\to[0].
$$

This is why the LCM expression and the wheel setup belong together: **the first common multiple gives the unreduced distance traveled, and dividing by the step size counts the jumps**.

### The formal proof

Let $L=\operatorname{lcm}(a,n)$. Any return to the identity means $ka\equiv0\pmod n$; hence $ka$ is simultaneously divisible by $a$ and by $n$. Its least positive possible value is $L$, attained at $k=L/a$. No smaller positive $k$ can work, because it would give a positive common multiple smaller than $L$. This proves the formula.

The familiar greatest-common-divisor formula follows from

$$
\gcd(a,n)\operatorname{lcm}(a,n)=an:
$$

$$
\boxed{\operatorname{ord}_n([a])=\frac{n}{\gcd(a,n)}.}
$$

For the zero element $[0]$, the order is $1$. The LCM quotient is only stated for $a>0$; the gcd formula also covers the zero case.

### What was independently mine, and what was already known?

My starting point was to **calculate the return time using an LCM and then represent those additions on a residue wheel**. The same formula appears in established algebra and number theory; for example, an [earlier mathematical discussion](https://math.stackexchange.com/questions/1021526/find-and-prove-a-formula-for-the-order-of-an-element-k-in-mathbb-z-n) also derives the LCM expression. The wheel makes the first return easy to see and connects the calculation to the orbit structure.

## 4. What the residue wheel tells us

For a fixed $a$, imagine drawing an arrow from every residue $[r]$ to $[r+a]$ in $\mathbb Z_n$. The result is a directed graph. Since every addition has an inverse—subtracting the same residue—each vertex has exactly one outgoing and one incoming arrow. The graph therefore breaks into cycles.

For example, with $n=10$ and $a=4$ we obtain

$$
[0]\to[4]\to[8]\to[2]\to[6]\to[0]
$$

and also

$$
[1]\to[5]\to[9]\to[3]\to[7]\to[1].
$$

There are **two cycles, each containing five residues**. That is not a coincidence:

$$
\begin{aligned}
\text{number of cycles}&=\gcd(a,n),\\
\text{length of each cycle}&=\frac{n}{\gcd(a,n)}.
\end{aligned}
$$

For $a=4$ and $n=10$, the gcd is $2$, so there are two cycles of length $5$.

Why does this follow? From any starting point $[r]$, returning to that point after $k$ steps means

$$
[r+ka]=[r],
$$

or $ka\equiv0\pmod n$. That is exactly the same condition used in the proof of the element-order formula. Every cycle therefore has length $n/\gcd(a,n)$, and the remaining count follows because there are $n$ residues in total.

This is a more rigorous interpretation of the circular and spiral drawings in my original manuscript: the drawings represent **modular translation orbits**.

A similar comparison works in $\mathbb Z_{12}$. If we add $[3]$, then the gcd is $\gcd(3,12)=3$, so the residue wheel splits into three cycles of length $4$:

$$
[0]\to[3]\to[6]\to[9]\to[0],\qquad
[1]\to[4]\to[7]\to[10]\to[1],\qquad
[2]\to[5]\to[8]\to[11]\to[2].
$$

If instead we add $[4]$, then $\gcd(4,12)=4$, so the wheel splits into four cycles of length $3$:

$$
[0]\to[4]\to[8]\to[0],\quad
[1]\to[5]\to[9]\to[1],\quad
[2]\to[6]\to[10]\to[2],\quad
[3]\to[7]\to[11]\to[3].
$$

These wheel decompositions are exactly the visual form of the theorem: the gcd gives the number of cycles, and the order gives the length of each cycle.

## 5. More wheel setups

Because the wheel representation is central to the way I first understood the problem, it is worth looking at several more examples.

### Wheel setup in $\mathbb Z_8$

- **Step size $[2]$**: the wheel splits into two cycles,

$$
[0]\to[2]\to[4]\to[6]\to[0]
$$

and

$$
[1]\to[3]\to[5]\to[7]\to[1].
$$

Here $\gcd(2,8)=2$, so there are two cycles, each of length $4$. Therefore

$$
\operatorname{ord}_8([2])=4.
$$

- **Step size $[3]$**: the wheel becomes one single cycle,

$$
[0]\to[3]\to[6]\to[1]\to[4]\to[7]\to[2]\to[5]\to[0].
$$

Since $\gcd(3,8)=1$, the residue $[3]$ is a generator and has order $8$.

### Wheel setup in $\mathbb Z_7$

If we add $[2]$ repeatedly in $\mathbb Z_7$, we obtain

$$
[0]\to[2]\to[4]\to[6]\to[1]\to[3]\to[5]\to[0].
$$

Again the gcd is $1$, so the wheel is a single cycle of length $7$. This is typical for nonzero residues modulo a prime.

### Wheel setup in $\mathbb Z_9$

If we add $[6]$ in $\mathbb Z_9$, then $\gcd(6,9)=3$, and the wheel breaks into three 3-cycles:

$$
[0]\to[6]\to[3]\to[0],
$$

$$
[1]\to[7]\to[4]\to[1],
$$

$$
[2]\to[8]\to[5]\to[2].
$$

This makes the general rule visible:

$$
\text{number of cycles}=\gcd(a,n),\qquad \text{cycle length}=\frac{n}{\gcd(a,n)}.
$$

The wheel setup therefore does more than illustrate a few examples. It gives a consistent geometric language for reading off the subgroup generated by $[a]$, the order of the element, and the way the residue classes are partitioned.

## 5. Which residues generate the entire group?

The subgroup generated by $[a]$ consists of all residues encountered by repeated addition:

$$
\langle[a]\rangle=\{[0],[a],[2a],\ldots\}.
$$

Its size equals the order of $[a]$:

$$
|\langle[a]\rangle|=\frac{n}{\gcd(a,n)}.
$$

Consequently, $[a]$ generates *every* residue class in $\mathbb Z_n$ exactly when

$$
\gcd(a,n)=1.
$$

These residues are called the generators of the cyclic group. For $\mathbb Z_{10}$, the generators are $[1]$, $[3]$, $[7]$, and $[9]$. Each has order $10$.

A related observation concerns prime moduli. If $p$ is prime, every nonzero residue in $\mathbb Z_p$ has order $p$, since every integer $1\le a<p$ is relatively prime to $p$. Conversely, if $n$ is composite, any nontrivial divisor $a$ produces an element whose order is smaller than $n$.

Therefore, for $n>1$,

$$
n\text{ is prime}\quad\Longleftrightarrow\quad
\operatorname{ord}_n([a])=n\text{ for every }1\le a<n.
$$

The condition thus gives another way to recognize why the generators are precisely the residues relatively prime to the modulus.

## 7. How many elements have a particular order?

In $\mathbb Z_{12}$, possible element orders are exactly the positive divisors of $12$. The wheel setups above already exhibit two of these: $[3]$ has order $4$, while $[4]$ has order $3$. The additional wheel examples in $\mathbb Z_8$, $\mathbb Z_7$, and $\mathbb Z_9$ show the same structural rule in several different settings. More generally, the possible orders are

$$
1,2,3,4,6,12.
$$

In fact, for every divisor $m\mid n$, the number of elements in $\mathbb Z_n$ with order exactly $m$ is

$$
\boxed{\varphi(m)},
$$

where $\varphi$ is Euler's totient function. This follows from the gcd formula: an element has order $m$ precisely when its representative has gcd $n/m$ with $n$, and there are exactly $\varphi(m)$ such representatives.

For $\mathbb Z_{12}$ the counts are:

| Element order $m$ | Number of elements |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 4 | 2 |
| 6 | 2 |
| 12 | 4 |

The total is $12$, illustrating the classical identity

$$
\sum_{m\mid n}\varphi(m)=n.
$$

In particular, the number of generators of $\mathbb Z_n$ is $\varphi(n)$.

## 8. A connection with the Chinese remainder theorem

Suppose $n=uv$ and $u,v$ are relatively prime. The Chinese remainder theorem identifies residue classes modulo $n$ with pairs of residue classes modulo $u$ and $v$:

$$
\mathbb Z_{uv}\cong\mathbb Z_u\times\mathbb Z_v.
$$

Under this identification, a repeated addition returns to the identity only when *both* coordinates return to their respective identities. Therefore

$$
\operatorname{ord}_{uv}([a])
=\operatorname{lcm}\bigl(\operatorname{ord}_u([a]),
\operatorname{ord}_v([a])\bigr).
$$

For example, $60=3\cdot4\cdot5$. The element $[9]$ has projected orders $1$, $4$, and $5$, giving

$$
\operatorname{ord}_{60}([9])=\operatorname{lcm}(1,4,5)=20.
$$

The gcd formula agrees: $60/\gcd(9,60)=60/3=20$.

This connection makes the order problem especially useful in algebra and elementary number theory, where a large modulus can often be understood through smaller coprime moduli.

## 9. Verifying the formula with Python

My earlier manuscript included a program based on the least common multiple and printed the orders of the residues modulo $100$. For this revision, I used two independent computations:

1. The formula $n/\gcd(a,n)$.
2. Directly adding $a$ modulo $n$ until the residue returns to zero.

A minimal implementation is:

```python
from math import gcd

def order_formula(a, n):
    return n // gcd(a, n)

def order_by_repetition(a, n):
    residue = 0
    for steps in range(1, n + 1):
        residue = (residue + a) % n
        if residue == 0:
            return steps
    raise AssertionError("Unexpected failure")
```

The accompanying reproducibility script checks every pair $(a,n)$ with $2\le n\le500$ and $0\le a<n$. It also checks the cycle count and cycle length for modular translation, as well as the totient distribution of element orders.

**Result: all 125,249 element–modulus pairs passed the checks.**

These finite computations agree with the divisibility proof given above.

For large $n$, the gcd formula is much more efficient than testing consecutive additions, because the Euclidean algorithm computes a gcd using a number of arithmetic operations logarithmic in the input magnitude.

## 10. Closing observations

The question—how many additions are needed to return to zero?—led me first to the least common multiple and then to its standard gcd equivalent:

$$
\operatorname{ord}_n([a])=\frac{\operatorname{lcm}(a,n)}{a}=\frac{n}{\gcd(a,n)},\qquad 1\le a<n.
$$

Viewed arithmetically, the LCM is the first shared multiple of the step size and the modulus. Dividing by the step size counts the jumps taken. Viewed geometrically, those jumps trace a directed orbit on a residue wheel, with the first return to zero marking the element's order. Viewed algebraically, the orbit is the cyclic subgroup generated by the chosen residue.

The LCM calculation and wheel representation are two views of the same mathematical process. The first identifies the smallest common multiple; the second shows the associated sequence of residues and its return to zero. Together they provide an intuitive route from modular arithmetic to the structure of finite cyclic groups.

## References

1. Clapham, C., and Nicholson, J. (2014). *The Concise Oxford Dictionary of Mathematics*, 5th ed. Oxford University Press.
2. Finston, D. R., and Morandi, P. J. (2014). *Abstract Algebra: Structure and Application*. Springer/Birkhäuser. [DOI: 10.1007/978-3-319-04498-9](https://doi.org/10.1007/978-3-319-04498-9).
3. Gallian, J. A. (2021). *Contemporary Abstract Algebra*, 10th ed. Chapman and Hall/CRC.
4. Hardy, G. H., and Wright, E. M. (1979). *An Introduction to the Theory of Numbers*, 5th ed. Oxford University Press.

*The manuscript PDF presents full theorem/proof formatting and the complete verification code is supplied separately in the accompanying download package.*

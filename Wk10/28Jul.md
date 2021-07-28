# Computational Linguistics (CL3.101)
## Summer 2021, IIIT Hyderabad
## 28 July, Wednesday (Lecture 27) – Syntax 8

Taught by Prof. Radhika Mamidi

## Semantics (contd.)
### Paninian Dependency Parsing (contd.)
Consider the sentence _I prefer the morning flight through Denver._ Here, the verb _prefer_ forms the root of the sentence. _I_ (with the relation `nsubj`) and _flight_ (with the relation `dobj`) are its dependents. Similarly, _the_ (`det`), _morning_ (`nmod`) and _Denver_ (`nmod`) are dependent on _flight_.  

### Tree-Adjoining Grammar
TAGs focus on exocentric relations (in contrast to rewrite grammars like PSG which handle endocentric relations better).  

Rules in a TAG are trees with a special leaf node called the foot node, anchored to a word. There are two kinds of trees: initial (representing basic valency relations) and auxiliary (allowing for recursion).  

Formally, a TAG is a 5-tuple $G = (\Sigma, NT, I, A, S)$. $\Sigma$ is a terminal alphabet and $NT$ is the set of variables. $I$ is a finite set of finite, initial trees; $A$ is a finite set of finite, auxiliary trees. $S$ is a special non-terminal symbol.  

The trees in $I \cup A$ are called elementary trees. Trees are combined by adjunction and substitution. Initial trees are elementary trees whose leaves are labelled with non-terminal or terminal categories, while auxiliary trees are those with a designated foot node.  

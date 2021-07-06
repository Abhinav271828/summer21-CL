# Computational Linguistics (CL3.101)
## Summer 2021, IIIT Hyderabad
## 06 July, Tuesday (Lecture 18) – Syntax 2

Taught by Prof. Radhika Mamidi

## Basics of Syntax (contd.)
### Chunks
Prasing at the chunk level is also known as shallow parsing.  
In order to test if a phrase is a constituent, there are three tests:

* substitution: if a single word can replace a string of words in a sentence, the string of words is a constituent.
* coordination: if a string of words can be joined to another string of words using _and_, they are constituents.
* question-fragments: if a string of words can be made into the answer of a question, it is a constituent.

### Representation
Constituents can be represented by using brackets; for example, [$_S$ [$_{NP}$ the man] [$_{VP}$ hit the dog]].

A clearer representation is using trees.

### Augmented Transition Network
An ATN is a formalism on which a syntactic parser is based. They look at transitions between each of the constituents of a sentence.

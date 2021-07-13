---
author: Abhinav S Menon
title: CL Seminar 1
subtitle: Pattern-Based Context-Free Grammars for Machine Translation
theme: Dresden
---

# Overview
* Context-Free Grammars
* Pattern-Based CFGs
* The Translation Algorithm
* Features and Agreement
* An Example

# Context-Free Grammars
Context-Free Grammars (CFGs) are a common formalism for describing the syntax of natural (and programming) languages. For example,  

$\mathbb{S \to NP \; VP}$  
$\mathbb{NP \to A \; N}$  
$\mathbb{VP \to V \; NP}$  
$\mathbb{N} \to \mathtt{cat \; | \; dog \; | \; mouse}$  
$\mathbb{A} \to \mathtt{the \; | \; a}$  
$\mathbb{V} \to \mathtt{chased \; | \; hugged}$  

# Pattern-Based CFGs: Patterns
Pattern-Based CFGs or PCFGs consist of a set of patterns – analogous to the set of rules that make up a CFG.  

Each pattern describes how to translate a certain type of phrase from the source to the target language.  

An example pattern is  

$\mathbb{NP}_1 \; [\mathtt{miss}]\mathbb{V}_2 \; \mathbb{NP}_3 \gets \mathbb{S}_2$  
$\mathbb{S}_2 \to \mathbb{NP}_3 \; [\mathtt{manquer}]\mathbb{V}_2 \; \mathtt{à} \; \mathbb{NP}_1$

# Pattern-Based CFGs: Skeletons
The two rules (one in the source language and one in the target language) that make up the pattern are called its _skeleton_.  

For example, the skeleton of the example above

$\mathbb{NP}_1 \; [\mathtt{miss}]\mathbb{V}_2 \; \mathbb{NP}_3 \gets \mathbb{S}_2$  
$\mathbb{S}_2 \to \mathbb{NP}_3 \; [\mathtt{manquer}]\mathbb{V}_2 \; \mathtt{à} \; \mathbb{NP}_1$  

is

$\mathbb{NP} \; \mathbb{V} \; \mathbb{NP} \gets \mathbb{S}$  
$\mathbb{S} \to \mathbb{NP} \; \mathbb{V} \; \mathtt{à} \; \mathbb{NP}$  

# Pattern-Based CFGs: Constraints
$\mathbb{NP}_1 \; [\mathtt{miss}]\mathbb{V}_2 \; \mathbb{NP}_3 \gets \mathbb{S}_2$  
$\mathbb{S}_2 \to \mathbb{NP}_3 \; [\mathtt{manquer}]\mathbb{V}_2 \; \mathtt{à} \; \mathbb{NP}_1$  

There are two types of constraints in the above pattern:

* Link constraints (subscripts): specifying the correlation between the constituents of each part.
* Head constraints (enclosed in $[\;]$): specifying lexeme- or phrase-level conditions on the applicability of the pattern.

The latter makes it possible to translate phrases that are constructed differently in the target language, as in the above example.  

# The Translation Algorithm: Essentials
The basic algorithm consists of three simple steps:

* Parse the input using the source language CFG skeletons.
* Propagate link and head constraints from the source to the target language and build a target language derivation sequence.
* Generate the output using the target sequence.

# The Translation Algorithm: Parsing
Parsing of CFGs is a well-studied area. Many algorithms are known for this task – we will consider the one described in Earley (1970).

This algorithm consists of stepping through the input string one at a time, and trying to parse the upcoming symbols given the incomplete parses until the current point.  

It generates all possible derivations for the input string (sometimes called a _parse forest_) in the given CFG.

# The Translation Algorithm: Priorities
Under some conditions, it is very easy for the number of target skeletons to increase exponentially for the same number of source skeletons.  

Therefore, when two or more patterns share the same source skeleton, we must decide which pattern is more likely to yield a correct translation.

# The Translation Algorithm: Priorities
The priority order is as follows:

* Prefer a pattern with more head constraints (a more _specific_ pattern).
* Prefer a pattern with more terminal symbols.
* Prefer the shortest derivation sequence.

These preferences can be expressed as numeric _costs_ for patterns.

# Features and Agreement
The constraints can be extended to lay restrictions on the features of words or phrases as well, to increase its descriptive power.  

For example, in French, pronouns as direct objects come _before_ the verb. This can be expressed as

$\mathbb{V}_1 \; \mathbb{NP}_2 \gets \mathbb{VP}_1\{\mathtt{+OBJ}\}$  
$\mathbb{VP}_1\{\mathtt{+OBJ}\} \to \mathbb{NP}_2\{\mathtt{+PRO}\} \; \mathbb{V}_1$  

# Integration of Bilingual Corpora
Given a bilingual corpus, we can translate all the sentences and compare them.  

If the translation is correct, nothing needs to be done.  

If there was a derivation sequence that resulted in an incorrect translation, use the vocabulary as head constraints.  

If there was no paired derivation sequence, add specific patterns for idioms or collocations (if any).  

# An Example
$\mathbb{NP}_1 \; \mathbb{VP}_1 \gets \mathbb{S}_1$  
$\mathbb{S}_1 \to \mathbb{NP}_1 \; \mathbb{VP}_1$  

$\mathbb{VP}_1 \; \mathbb{ADVP}_2 \gets \mathbb{VP}_1$  
$\mathbb{VP}_1 \; \to \mathbb{VP}_1 \; \mathbb{ADVP}_2$

$[\mathtt{know}]\mathbb{VP}_1\{\mathtt{+OBJ}\} \; \mathtt{well} \gets \mathbb{VP}_1$  
$\mathbb{VP}_1 \to [\mathtt{connaître}]\mathbb{VP}_1\{\mathtt{+OBJ}\} \; \mathtt{bien}$  

$\mathbb{V}_1 \; \mathbb{NP}_2 \gets \mathbb{VP}_1\{\mathtt{+OBJ}\}$  
$\mathbb{VP}_1\{\mathtt{+OBJ}\} \to \mathbb{V}_1 \; \mathbb{NP}_2\{\mathtt{-PRO}\}$  

$\mathbb{V}_1 \; \mathbb{NP}_2 \gets \mathbb{VP}_1\{\mathtt{+OBJ}\}$  
$\mathbb{VP}_1\{\mathtt{+OBJ}\} \to \mathbb{NP}_2\{\mathtt{+PRO}\} \; \mathbb{V}_1$  

# An Example
$\mathtt{he} \gets \mathbb{NP}\{\mathtt{+PRO+NOMI+3RD+SG}\}$  
$\mathbb{NP}\{\mathtt{+PRO+NOMI+3RD+SG}\} \to \mathtt{il}$  

$\mathtt{me} \gets \mathbb{NP}\{\mathtt{+PRO+CAUS-3RD+SG}\}$  
$\mathbb{NP}\{\mathtt{+PRO+CAUS-3RD+SG}\} \to \mathtt{me}$  

$\mathtt{knows} \gets \mathbb{V}\{\mathtt{+FIN+3SG}\}$  
$\mathbb{V}\{\mathtt{+FIN+3SG}\} \to \mathtt{sait}$  

$\mathtt{knows} \gets \mathbb{V}\{\mathtt{+FIN+3SG}\}$  
$\mathbb{V}\{\mathtt{+FIN+3SG}\} \to \mathtt{connait}$  

$\mathtt{well} \gets \mathbb{ADVP}$  
$\mathbb{ADVP} \to \mathtt{bien}$  

$\mathtt{well} \gets \mathbb{ADVP}$  
$\mathbb{ADVP} \to \mathtt{beaucoup}$

# An Example
According to these rules, the sentence `He knows me well` is parsed.  

| Fragment | Translation |
| ---: | :--- |
| $\mathtt{He \; knows \; me \; well}$ | $\mathbb{S}$ |
| $\mathtt{He}$ | $\mathtt{il}$ |
| $\mathtt{knows \; me \; well}$ | $\mathbb{VP}$ |
| $\mathtt{well}$ | $\mathtt{bien}$ |
| $\mathtt{knows \; me}$ | $\mathbb{VP}$ |
| $\mathtt{knows}$ | $\mathtt{connait}$ |
| $\mathtt{me}$ | $\mathtt{me}$ |

We get the correct output: `Il me connait bien`.

# References
Takeda, Koichi. "Pattern-based context-free grammars for machine translation." arXiv preprint cmp-lg/9607011 (1996).

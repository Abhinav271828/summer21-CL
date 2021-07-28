# Computational Linguistics (CL3.101)
## Summer 2021, IIIT Hyderabad
## 27 July, Tuesday (Lecture 26) – Syntax 7

Taught by Prof. Radhika Mamidi

## Semantics (contd.)
### Thematic Roles
A thematic role is the semantic relationship between a predicate and an argument of a sentence. For example,

* agent: deliberately performs the action (***Bill** ate his soup quietly.*)
* experiencer: receives sensory or emotional input  (***Jennifer** could smell the lilies.*)
* theme: the recipient of an action that does not change its state (*Bill gave Mary **a gift**.*)
* beneficiary: for whom the action is performed (*Bill gave **Mary** a gift*.)
* patient: undergoes action and has state changed (*The falling rocks crushed **the car***.)
* instrument: used to carry out the action (*Jamie cut the ribbon **with a pair of scissors**.*)
* cause/force: mindlessly performs the action (***An avalanche** destroyed the temple.*)
* location: where the action occurs (*Johnny and Linda played **in the park**.*)
* goal: what the action is directed towards (*The caravan went **towards the oasis**.*)
* source: where the action originated (*The rocket was launched **from Central Command**.*)
* result: the end product of an event (*Mary baked a **cake**.*)
* content: the content/proposition of a propositional event (*Mary said, **"I will bake a cake."***)

Thematic roles remain the same in paraphrased sentences. They have been associated with cases, but this morpho-syntactic marking of thematic roles is now usually denied (as many languages do not mark thematic roles homomorphically).  

In a sentence, aach thematic role is assigned to a single noun phrase and each noun phrase has a unique role; this is called bi-uniqueness and is a proposed universal priniciple of grammar.  

Thematic roles also separate dummy (pleonastic) noun phrases from those with meaning.

### Paninian Dependency Parsing
Computational Paninian Grammar (CPG) is quite suited for analysis of Indian languages.  

Thematic roles are called kAraka in CPG. Some of the various relations are kartA, karma, karaNa, saMpradAna, apAdAna and adhikaraNa.  

Consider the sentence _rAma rotI KAtA hE_. Here, *rAma* is k1 (kartA), and *rotI* k2 (karma), with respect to the verb *KAtA hE*.  

There are two important notions in the Paninian grammatical tradition: AkAMkRA (expectation; the roles that a verb requires as its arguments) and yogyatA (eligibility; the possibility that a certain noun can fill a certain thematic role).

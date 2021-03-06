# Computational Linguistics (CL3.101)
## Summer 2021, IIIT Hyderabad
## Assignment 3, Part 4

## Notation
The start state in all FSTs is marked $S_0$. The state which one reaches after getting the root is called $R$. States with a double outline are accepting states.  

On each arc, the notation followed is `input : output`. For example, `fut : vuM` indicates that in the future tense, the suffix -vuM is to be added.  

By convention, ε denotes an empty or null affix.  

The various short forms used are:

* `hab`: habitual (aspect)
* `perf`: perfective (aspect)
* `sim`: simple (aspect)
* `cont`: continuous/progressive (aspect)
* `imp`: imperative (mood)
* `as`: assertive (mood)
* `pot`: potential (mood)
* `ob`: obligative (mood)
* `past`: past (tense)
* `pres`: present (tense)
* `fut`: future (tense)

## Grammar
In total, 18 verb forms are generated by each of the FSTs. First, the aspect is taken, then the mood and finally the tense. The forms generated are:

* Habitual Aspect
    - Past Tense
    - Present Tense
    - Future Tense
* Perfective Aspect
    - Past Tense
    - Present Tense
    - Future Tense
* Simple Aspect
    - Imperative Mood
    - Assertive Mood
        - Past Tense
        - Present Tense
        - Future Tense
    - Potential Mood
        - Past Tense
        - Present Tense
    - Obligative Mood
        - Past Tense
        - Present Tense
        - Future Tense
* Continuous Aspect
    - Potential Mood
    - Assertive Mood
        - Past Tense
        - Present Tense

Malayalam does not inflect for GNP; therefore only TAM inflections are given.

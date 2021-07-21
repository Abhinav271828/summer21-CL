# Computational Linguistics (CL3.101)
## Summer 2021, IIIT Hyderabad
## Assignment 3, Part 3(a)

## Notation
The FSA has been divided into four distinct "levels"; level 0 parses numbers, level 1 parses the ordinal superscript, level 2 parses the months and level 3 parses the years.

For brevity's sake, the months' full names are not written; rather, two-letter codes are used. These are:
| Month | Code |
| :--: | :--: |
| January | `JA` |
| February | `FE` |
| March | `MR` |
| April | `AP` |
| May | `MY` |
| June | `JU` |
| July | `JL` |
| August | `AU` |
| September | `SE` |
| October | `OC` |
| November | `NO` |
| December | `DE` |

It is assumed that the months form a sequence `JA, FE, MR, AP, MY, JU, JL, AU, SE, OC, NO, DE`.

On the transition arcs, two notations are used:

* commas `,` to indicate any one of a set; for example, `JA, MR, MY` means "January", "March" or "May".
* square brackets `[ ]` to indicate any one of a subsequence; for example, `[4-7]` means "4", "5", "6" or "7" and `[JU-JL]` means either "June" or "July".

## Assumptions
It is assumed that transition arcs can have strings on them. In case two different outgoing arcs have the same first character, the second character is to be checked, *i.e.*, the transition is greedy. For example, the state $S_0$ has outgoing arcs `2` and `21`; therefore if the next symbol is `2`, then the symbol after that is to be read. If this is `1`, then `21` is followed; else, `2` should be followed.

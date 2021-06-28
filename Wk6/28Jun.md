# Computational Linguistics (CL3.101)
## Summer 2021, IIIT Hyderabad
## 28 June, Monday (Lecture 14) – Morph Analysis 6

Taught by Prof. Radhika Mamidi

## Paradigm Based Morphological Analysers
### Paradigm Table
A paradigm table represents the inflected forms of a particular lexeme.  
We use add-delete rules to indicate the change in words. For example, `play[0,3,ing]` means we delete 0, add 3 characters which are 'ing' – this gives us `playing`. Similarly, `eat[3,3,ate]` means we delete 3, add 3 characters which are 'ate' – this gives us `ate`.

    shake shake   shake[0,0,0]
    shake shakes  shake[0,1,s]
    shake shaking shake[1,3,ing]
    shake shook   shake[3,3,ook]
    shake shaken  shake[0,1,n]
    
    make make   make[0,0,0]
    make makes  make[0,1,s]
    make making make[1,3,ing]
    make made   make[2,2,de]
    make made   make[2,2,de]

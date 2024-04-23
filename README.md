# UD-treebank-Romanian
### UD_Romanian_SMSL (Romanian Social Media Sexist Language)
### Summary
+ Genre: Social Media
+ Corpus size: 210 samples
+ The Romanian Social Media Sexist Language UD treebank (called UD_RoSMSL) is a reference treebank in UD format for Romanian sexist language.
#### Tasks
- [x] Annotation of 210 samples (source: git: [CoRoSeOf](https://github.com/DianaHoefels/CoRoSeOf) - paper:  [CoRoSeOf - An Annotated Corpus of Romanian Sexist and Offensive Tweets](https://aclanthology.org/2022.lrec-1.243/))
- [x] Added two deprel labels non-existing in the Romanian language, i.e, *vocative:mention* and *discourse:emo*,  which results in Syntax errors: 182(*** FAILED *** with 182 errors)
- [x] Without the new labels validation is successful :tada:
- [ ] Adding the new Unknown DEPREL label in the documentation upon submission:
- Unknown DEPREL label: 'vocative:mention'
- Unknown DEPREL label: 'discourse:emo'

### Statistics of UD_RoSMSL
- Tree count:  **210**

##### POS TAGS
- Number of unique POS tags: **17**
- Unique POS tags: ['ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'DET', 'INTJ', 'NOUN', 'NUM', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X']
##### Relations
- Number of unique dependency relations: **47** (+ 2 new ) out of 52 relations currently permitted in Romanian language 
- - Unique deprels: ['acl', 'advcl', 'advcl:tcl', 'advmod', 'advmod:tmod', 'amod', 'appos', 'aux', 'aux:pass', 'case', 'cc', 'cc:preconj', 'ccomp', 'ccomp:pmod', 'compound', 'conj', 'cop', 'csubj', 'dep', 'det', 'discourse', 'discourse:emo', 'expl', 'expl:pass', 'expl:poss', 'expl:pv', 'fixed', 'flat', 'goeswith', 'iobj', 'list', 'mark', 'nmod', 'nsubj', 'nsubj:pass', 'nummod', 'obj', 'obl', 'obl:agent', 'obl:pmod', 'obl:tmod', 'orphan', 'parataxis', 'punct', 'reparandum', 'root', 'vocative', 'vocative:mention', 'xcomp']

##### Tokenization and Word Segmentation

- This corpus contains **210** sentences
- Total number of tokens: **4417**
- Total number of unique tokens: **1692**

##### Mispellings
- Total number of misspelled words: **451** (documented in the misc column with the CorrectForm)
 
### Data Splits

The treebank will be divided into three parts: 
- 12.5% for the test set (ro-ud-smsl-test.conllu)
- 12.5% for the development set (ro-ud-smsl-dev.conllu)
- 75% for the training set (ro-ud-smsl-train.conllu)

The split will be done done randomly. The corpus has been divided into documents containing instances of sexist language found in social media, from Twitter.  

### Language Family

+ Language: Romanian (code: ro) 
+ Language family: Indo-European

                    - Italic
                      - Latino-Faliscan
                            - Romance
                              - Eastern Romance
                                - Daco-Romance
                                    - Romanian


&copy;

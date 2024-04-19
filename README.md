# UD-treebank-Romanian
### UD_RoSMSL (Romanian Social Media Sexist Language)
### Summary
+ Genre: Social Media
+ Corpus size: 210 samples
+ The Romanian Social Media Sexist Language UD treebank (called UD_RoSMSL) is a reference treebank in UD format for Romanian sexist language.
#### Tasks
- [x] Annotation of 210 samples (source: git: [CoRoSeOf](https://github.com/DianaHoefels/CoRoSeOf) - paper:  [CoRoSeOf - An Annotated Corpus of Romanian Sexist and Offensive Tweets](https://aclanthology.org/2022.lrec-1.243/))
- [x] Added two deprel labels non-existing in the Romanian language, i.e, *vocative:mention* and *discourse:emo*,  which results in Syntax errors: 182(*** FAILED *** with 182 errors)
- [x] Without the new labels upon validation, validation is successful :tada:
- [ ] Adding the new Unknown DEPREL label in the documentation upon submission:
- Unknown DEPREL label: 'vocative:mention'
- Unknown DEPREL label: 'discourse:emo'
      
### Data Splits

The treebank will be divided into three parts: 
- 12.5% for the test set (ro-ud-smsl-test.conllu)
- 12.5% for the development set (ro-ud-smsl-dev.conllu)
- 75% for the training set (ro-ud-smsl-train.conllu)

The split will be done done randomly. The corpus has been divided into documents containing instances of sexist language found in social media, from Twitter.  

### Basic Statistics

- Tree count:  210
- Word count:  
- Token count: 
- Dep. relations: 
- POS tags: 
- Category=value feature pairs:

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

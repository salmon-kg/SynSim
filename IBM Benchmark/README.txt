# IBM Split and Rephrase 2019

## Overview
This repository contains data to the paper "Small but Mighty: New Benchmarks for Split and Rephrase". 

## Structure
`/benchmarks` contain the data of our proposed benchmarks.

`/judgements` contain the raw and aggregated human judgements of model performances from Amazon Mechanical Turk.

## Citation
If you use our work, please cite
@inproceedings{zhang-etal-2020-small,
    title = "Small but Mighty: New Benchmarks for Split and Rephrase",
    author = "Zhang, Li  and
      Zhu, Huaiyu  and
      Brahma, Siddhartha  and
      Li, Yunyao",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.emnlp-main.91",
    doi = "10.18653/v1/2020.emnlp-main.91",
    pages = "1198--1205",
    abstract = "Split and Rephrase is a text simplification task of rewriting a complex sentence into simpler ones. As a relatively new task, it is paramount to ensure the soundness of its evaluation benchmark and metric. We find that the widely used benchmark dataset universally contains easily exploitable syntactic cues caused by its automatic generation process. Taking advantage of such cues, we show that even a simple rule-based model can perform on par with the state-of-the-art model. To remedy such limitations, we collect and release two crowdsourced benchmark datasets. We not only make sure that they contain significantly more diverse syntax, but also carefully control for their quality according to a well-defined set of criteria. While no satisfactory automatic metric exists, we apply fine-grained manual evaluation based on these criteria using crowdsourcing, showing that our datasets better represent the task and are significantly more challenging for the models.",
}
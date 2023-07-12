<h1 align="center">
  SynSim
</h1>
# SynSim: Syntactic Complexity Identification and Simplification Through GPT
 # Summary
 Text simplification is one of the domains in Natural Language Processing (NLP) that offers an opportunity to understand the text in a simplified manner for exploration. However, it is always hard to understand and retrieve knowledge from unstructured text, which is usually in the form of compound and complex sentences. There are state-of-the-art neural network-based methods to simplify the sentences for improved readability while replacing words with plain English substitutes and summarising the sentences and paragraphs. In the Knowledge Graph (KG) creation process from unstructured text, summarising long sentences and substituting words is undesirable since this may lead to information loss. In this work, we propose a controlled simplification approach based on OpenAI, which transform a compound and complex sentence into a simple set of sentence. This simplification process retains the original wording and involves syntactic rewriting of the sentence. The paper also introduces an algorithm to identify and measure a sentence’s syntactic complexity (SC), followed by reduction through a controlled syntactic simplification process.

<h4 align="center">
  Syntactic Simplification Process for Split & Rephrase
  <img align="center"  src="https://github.com/sallmanm/SynSim/blob/main/tree.png" alt="...">
</h4>
<h4 align="center">
  <img align="center"  src="https://github.com/sallmanm/SynSim/blob/main/snr.png" alt="...">
</h4>
## Evaluation
<h2 align="center">
  Syntactic Complexity Identification 
  <img align="center"  src="https://github.com/sallmanm/SynSim/blob/main/perf-sc.png" alt="...">
</h2>

<h2 align="center">
  Re-Annotated dataset Statistics with Comparison
  <img align="center"  src="https://github.com/sallmanm/SynSim/blob/main/perf-synsim.png" alt="...">
</h2>


 ## IBM Benchmark:
 This folder contains the following files:  
       - README.txt : Information about the original benchmark dataset.  
       - benchmark.tsv : Original Benchmark Dataset of "Split & Rephrase" for sentence Simplification.  

 ## Re-Annotated Benchmark:
 This folder contains the re-annotated dataset by GPT in ReAnnotated_Benchmark.csv file.

# Other Python Files:
  syntactic_Complexity.py: Contains the implemented Algorithm for syntactic complexity measurement. It uses both Part-of-Speech-Based and Dependency_Based syntactic structures of the sentences.  
  Similarity-Check.py : It computes the similarity of a simplified sentence set against the original text.


# Citation:

If you use this work, please cite:  

@ARTICLE{2023arXiv230407774S,  
       author = {{Salman}, Muhammad and {Haller}, Armin and {Rodrìguez Mèndez}, Sergio J.},  
        title = "{Syntactic Complexity Identification, Measurement, and Reduction Through Controlled Syntactic Simplification}",  
      journal = {arXiv e-prints},  
     keywords = {Computer Science - Computation and Language, Computer Science - Information Retrieval},  
         year = 2023,  
        month = apr,  
          eid = {arXiv:2304.07774},  
        pages = {arXiv:2304.07774},  
          doi = {10.48550/arXiv.2304.07774},  
archivePrefix = {arXiv},  
       eprint = {2304.07774},  
 primaryClass = {cs.CL},  
       adsurl = {https://ui.adsabs.harvard.edu/abs/2023arXiv230407774S},   
}


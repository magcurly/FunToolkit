# Grabing Lineage Information from NCBI Taxonomy Browser

## Introduction

This is a script to get Lineage information from NCBI Taxonomy Browser.
It had been divided into two parts. First, I defined a class called **tax_object**.
It contains some Information we need in further studies, including the taxonomy id, the parent tax id, the name, the lineage information and the rank of a taxon.
Of cause, other information can also be added if necessary.  
The second part is to grab information from NCBI.
Thanks to the simple code of the NCBI website, I only need to decode the html code and find sitable matches using regular expression (library: re).
I recommend to use txid as key word to search, while I provide two ways to get the information, the taxon's name and the taxon's txid.
The reason is that it's really easy to meet ambiguity when searching by name, for example, the class of Actinobacteria and the phylum of Actinobacteria.

## Opinions

It's really simple for everyone to use web crawler to get information, especially when you need to deal with thousands of samples.

***Life is short. Python is good.***
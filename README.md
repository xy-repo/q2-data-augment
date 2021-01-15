## q2-data-augment: QIIME2 plugin for data augmentation using rarefaction (Rarefy for Augment)

Data augmentation is a very useful and widely used method in data science (see: https://en.wikipedia.org/wiki/Data_augmentation). Especially, it can increase the sample size of the training set for machine learning models.

Rarefaction can be used as an effective and trustable method for data augmentation, given the following reasons:
* Essentially, biological sample collection and sequencing are random sampling processes, which capture microbes from an unknown population. Rarefaction is just another random sampling process, 
which can also be seen as sampling certain reads from the same population, just the same as biological sample collection and sequencing.
* Under the hypothesis that "rarefaction" = "biological sample collection and sequencing", each iteration of rarefaction on a sequencing sample in fact generates a new sequencing sub-sample. 
This new sub-sample contains a subset of reads of the original sample, and come from the same population that the original sample belongs to.
* Some preliminary results show using rarefaction for data augmentation can significantly the results of machine learning classification (unpublished results).

This method, named Rarefy for Augment, is very simple. Run random rarefaction *N* times. Each time, rename the samples and corresponding metadata and concatenate them with the previous two files. Finally, the sample size can be enlarged *N* times.

## Installing
```
conda activate qiime2-2020.11
pip install git+https://github.com/yxia0125/q2-data-augment.git
```
Type "qiime data-augment" to test if the installation is successful.

## Uninstalling
```
pip uninstall q2-data-augment
```

## Using
```
qiime data-augment augment --i-table raw_table.qza 
                           --m-raw-metadata-file raw_metadata.tsv 
                           --p-sampling-depth 2000 
                           --p-augment-times 10
                           --p-output-path-metadata augmented_meta.tsv  
                           --o-augmented-table augmented_table.qza 
```                      
"raw_table.qza" and "raw_metadata.tsv" are the input raw feature table and metadata; --p-sampling-depth --> the rarefaction depth; --p-augment-times set to 10 means repeating 
rarefaction 10 times (i.e., enlarge sample 10 times); "augmented_table.qza" is the augmented feature table, its sample size is 10 times larger than "raw_table.qza", and new rarefed samples end with "*_X*" (X represents the *i*_th rarefaction); "augmented_meta.tsv" is the augmented metadata that has matching sample names in "augmented_table.qza".

Note: Only need to augment the training set.

## Citing 
If you are interested to use this method, please include the following citation:

*Yao Xia, q2-data-augment: QIIME2 plugin for data augmentation using rarefaction (Rarefy for Augment), (2021), GitHub repository, https://github.com/yxia0125/q2-repeat-rarefy.*






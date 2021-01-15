# ----------------------------------------------------------------------------
# Copyright (c) 2021, Yao Xia.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import biom
import numpy as np
import pandas as pd
import qiime2

def augment(table: biom.Table, sampling_depth: int, augment_times: int, output_path_metadata: str,
        raw_metadata: qiime2.Metadata, with_replacement: bool = False, rarefy_start: bool = True) -> biom.Table:

    metadata = raw_metadata.to_dataframe()
    metadata = metadata.sort_index()

    all_df = table.to_dataframe().sort_index().sort_index(axis=1)
    ## change sorted table back to biom
    table = biom.Table(all_df.values, all_df.index.to_list(), all_df.columns.to_list())

    zero_df = all_df[all_df==0].fillna(0)
    zero_table = biom.Table(zero_df.values, zero_df.index.to_list(), zero_df.columns.to_list())

    sub_table = table.subsample(sampling_depth, axis='sample', by_id=False,
            with_replacement=with_replacement)

    if rarefy_start == True:
        output_table = zero_table.merge(sub_table)
    else:
        output_table = table

    output_metadata = metadata

    for i in range(augment_times):
        num = i+1
        sub_table = table.subsample(sampling_depth, axis='sample', by_id=False,
              with_replacement=with_replacement)
        sub_df = sub_table.to_dataframe().sort_index().sort_index(axis=1)

        ## rename
        sub_df_names = sub_df.columns.to_list()
        sub_df_names_added = [x + '_' + str(num) for x in sub_df_names]

        sub_df.columns = sub_df_names_added
        sub_table = biom.Table(sub_df.values, sub_df.index.to_list(), sub_df.columns.to_list())
        output_table = output_table.merge(sub_table)

        metadata_names = metadata.index.to_list()
        metadata_names_added = [x + '_' + str(num) for x in metadata_names]

        tmp_metadata = metadata.copy()
        tmp_metadata.index = metadata_names_added
        print(output_metadata)
        output_metadata = pd.concat((output_metadata, tmp_metadata))

    output_metadata.index.name = 'sample-id'
    output_metadata = qiime2.metadata.Metadata(output_metadata)
    output_metadata.save(output_path_metadata)

    if output_table.is_empty():
        raise ValueError('The output table contains no features.')

    return output_table

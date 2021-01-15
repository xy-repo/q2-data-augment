# ----------------------------------------------------------------------------
# Copyright (c) 2016-2020, Yao Xia.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import (Plugin, Int, Float, Range, Metadata, Str, Bool,
                           Choices, MetadataColumn, Categorical, List,
                           Citations, TypeMatch)

from ._utils import augment
from q2_types.feature_table import (FeatureTable, Frequency)

citations = Citations.load('citations.bib', package='q2_data_augment')

plugin = Plugin(
    name='q2-data-augment',
    version='1.0',
    website='https://github.com/yxia0125/q2_data_augment',
    package='q2_data_augment',
    short_description=('Data augmentation'),
    description=('This is a QIIME 2 plugin for data augmentation.'),
    citations = Citations.load('citations.bib', package='q2_data_augment')
)

plugin.methods.register_function(
    function = augment,
    inputs={'table': FeatureTable[Frequency]},
    parameters={'sampling_depth': Int % Range(1, None),
                'with_replacement': Bool,
                'augment_times': Int % Range(1, None),
                'raw_metadata':Metadata,
                'output_path_metadata': Str,
                'rarefy_start': Bool},
    outputs=[('augmented_table', FeatureTable[Frequency])],
    input_descriptions={'table': 'The raw feature table to be augmented.'},
    parameter_descriptions={
        'sampling_depth': ('The total frequency that each sample should be '
                           'rarefied to. Samples where the sum of frequencies '
                           'is less than the sampling depth will be not be '
                           'included in the resulting table unless '
                           'subsampling is performed with replacement.'),
        'with_replacement': ('Rarefy with replacement by sampling from the '
                             'multinomial distribution instead of rarefying '
                             'without replacement.'),
        'augment_times': ('Augment data N times. For example, setting to 10, '
                          'means augmenting 10 times'),
        'raw_metadata': ('Input raw metadata.'),
        'output_path_metadata': ('Output meatadata that matches the augmented feature table.'),
        'rarefy_start': ('True: rarefy the original feature table, False: do not rarefy the '
                        'original feature table.'),
    },
    output_descriptions={'augmented_table': 'The resulting augmented feature table.'},
    name=('Augmented table'),
    description=("Augment feature table"),
    citations = [citations['Xia2021']])

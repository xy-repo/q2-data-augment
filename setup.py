# ----------------------------------------------------------------------------
# Copyright (c) 2016-2020, Yao XIa.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name="q2-data-augment",
    version='1.0',
    packages=find_packages(),
    author="Yao Xia",
    author_email="xiayao0125@outlook.com",
    url="https://github.com/yxia0125/q2-data-augment",
    license="BSD-3-Clause",
    description="qiime 2 plugin for data augmentation",
    entry_points={
        "qiime2.plugins":
        ["q2-data-augment=q2_data_augment.plugin_setup:plugin"]
    },
    zip_safe=False,
    package_data={'q2_data_augment':['citations.bib']}
)

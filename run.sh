#!/usr/bin/env bash

# This script compiles an FST using foma, which is used to transduce
# a list of UR into their SR. 
# Then it evaluates the output of the FST and displays the errors on screen.
# The evaluation script prints in red where the FST SR is different from
# the ground truth.
#
# Author: Salvador Medina

UR_PATH=UR.lst
SR_PATH=SR.lst
FOMA_SCRIPT_PATH=somali.xfst
FST_PATH=somali.fst
FST_OUTPUT_PATH=somali_xfst.out

foma -l ${FOMA_SCRIPT_PATH}
flookup -i ${FST_PATH} < ${UR_PATH} > ${FST_OUTPUT_PATH}
python3 -u eval_sr.py -fo ${FST_OUTPUT_PATH} -gt ${SR_PATH}
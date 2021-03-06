# Foma FST Evaluation

This script compiles an FST using foma, which is used to transduce
a list of underlying representations (UR) into their surface representations (SR). 
Then it evaluates the output of the FST and displays the errors on screen.
The evaluation script prints the segment of the SR in red from the first character where the FST output and the ground truth are different.

### Installation

The evaluation script is written in Python3 and only requires to install the `colorama` package. You can install it via `pip`:

```
pip install colorama
```

### Instructions

To run this evaluation code you need to:

1. Fill the `somali.xfst` with your classes, rules, regex, etc.. Please make sure to keep the *save to disk* and *exit* lines at the end untouched.
2. Add the list of URs in `UR.lst`
3. Add the list of SRs we obtained from the data in `SR.lst`. This must be in the same order as the UR in `UR.lst`.
4. Run the evaluations script `run.sh`

**NOTE:** `UR.lst` and `SR.lst` just have 4 entries to illustrate the order in which they should be inserted. You can put all of the SR from the data in `SR.lst` and the URs that you came up with in `UR.lst`

### Usage

This script should run without a problem on Mac or Linux. 

You can either run the script by giving the proper execution permits through `chmod +x run.sh` and calling it through `./run.sh`, or by calling it through `bash run.sh`.


### Output

After runnig the script you will have two ouput files and the results printed on screen. The output files are:
1. `somali.fst`: the compiled FST
1. `somali_xfst.out` the output of running `somali.xfst` with `UR.lst` as input

The columns printed out from left to right are: UR, SR, FST OUTPUT. It should look like the following:

![screenshot](imgs/screenshot.png)

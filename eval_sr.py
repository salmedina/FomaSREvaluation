import argparse
import sys
from colorama import Fore, Style


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fo', '--fst-out-path', type=str,
                        help='Path to the FST output path')
    parser.add_argument('-gt', '--gt-path', type=str,
                        help='Path to the file with the ground truth of the surface representations')
    return parser.parse_args()


def get_eq_pos(root, word):
    '''Returns the position in the string until which both strings are equal'''
    pos = -1
    for idx in range(min(len(root), len(word))):
        if root[idx] == word[idx]:
            pos = idx
        else:
            break
    return pos


def main(opts):
    ur_list, sr_fst_list = zip(*[line.strip().split('\t') for line in open(opts.fst_out_path, 'r') if line.strip() != ''])
    sr_gt_list = [line.strip() for line in open(opts.gt_path, 'r')]
    
    if len(sr_fst_list) == 0:
        print('WARNING: Empty output from FST')
        sys.exit(0)
    
    if len(sr_fst_list) != len(sr_gt_list):
        print(f'ERROR: The length of the output and ground truth do not match.')
        sys.exit(-1)
    
    ur_header = 'UR'
    gt_header = 'SR-GT'
    pred_header = 'SR-FST'
    print('')
    print(f'{Fore.BLUE}{ur_header:15}{gt_header:15}{pred_header}{Style.RESET_ALL}')
    for ur, sr_pred, sr_gt in zip(ur_list, sr_fst_list, sr_gt_list):
        eq_pos = get_eq_pos(sr_pred, sr_gt) + 1
        print(f'{ur:15}{sr_gt:15}{Fore.GREEN}{sr_pred[:eq_pos]}{Style.RESET_ALL}{Fore.RED}{sr_pred[eq_pos:]}{Style.RESET_ALL}')
    print('')
    
    
if __name__ == '__main__':
    opts = parse_args()
    main(opts)
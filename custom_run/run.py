
import argparse
import sys
sys.path.insert(0, '..')

from osnma.receiver.receiver import OSNMAReceiver
from osnma.receiver.input_sbf import SBF


parser = argparse.ArgumentParser(description='Runs OSNMAlib against the provided SBF file that contains the block '
                                             'GALRawINAV.')
parser.add_argument('sbf_file', metavar='file', type=str, default='current_config.sbf', nargs='?',
                    help='name of the SBF file.')
args = parser.parse_args()


def sbf_current_config():
    config_dict = {
        'scenario_path': args.sbf_file,
        'exec_path': '.',
        'pubk_name': 'OSNMA_PublicKey.xml',
        'merkle_name': 'OSNMA_MerkleTree.xml'
    }

    input_module = SBF(config_dict['scenario_path'])
    osnma_r = OSNMAReceiver(input_module, config_dict)

    osnma_r.start()


if __name__ == "__main__":

    print(f"Running file {args.sbf_file}")
    sbf_current_config()

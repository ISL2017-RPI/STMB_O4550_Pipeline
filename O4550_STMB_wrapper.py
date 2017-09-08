import sys
import numpy as np
import STMB_O4550

def STMB(data_file, target_file):
    my_STMB = STMB_O4550.initialize()
    feat = my_STMB.STMB_primitive_O4550(data_file, target_file)
    return feat


if __name__ == "__main__":
    data = sys.argv[1]
    target = sys.argv[2]
    selected_feature = np.array(STMB(data, target), dtype=np.int16)
    np.savetxt('Features_O4550_STMB.csv', selected_feature, delimiter=',')
    print selected_feature
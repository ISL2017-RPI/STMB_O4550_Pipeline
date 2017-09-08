FROM keyi/python2-mcr2017a-rpi-isl

COPY STMB_O4550/ ./STMB_O4550
COPY O4550_STMB_wrapper.py ./
COPY setup.py ./
COPY trainData.csv ./
COPY trainTargets.csv ./

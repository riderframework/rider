#!/bin/sh

./clean.sh
rm -f .coverage

#real tests
cd real
./test_real.sh
cp .coverage ../.coverage.real
cd ..
#

#coverage
coverage combine


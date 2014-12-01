#!/bin/sh

./clean.sh
rm -f .coverage

#real tests
cd real
./test_real.sh

#
coverage combine
coverage report
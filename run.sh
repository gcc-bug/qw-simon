> test.log
echo "isq 模拟运行 simon结果:" >> test.log
~/isqc_/isqc simulate ~/isqc_/isq/simon.so --shots 1000 >> test.log
echo "求解方程:" >> test.log
python simon/simons_algorithm.py 1 5 3 >> test.log
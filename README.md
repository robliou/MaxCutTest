# MaxCutTest
 Repository for various testing methods for MaxCut problem:

<h2> Overview </h2>
<h3>Test metrics</h3>
<br>
 100 nodes
 <br>
 edge density 10%, 30%, 50%, 70%, 90%
 <br><br>
 500 nodes
 <br>
 edge density 10%, 30%, 50%, 70%, 90%
<br>
<h3>Test methods</h3>
<h4>D-wave </h4>
Simulated annealing using the D-wave ``neal`` package<br>
all test files under `dwave_sa' folder

[Repository](https://github.com/dwavesystems/dwave-neal)

<br> 
<h4>Kaiwu </h4>
Kaiwu CIM- simulator and Kaiwu Simulated Annealing  
all test files under `kaiwu' folder

<h4> Scipy dual anneal </h4>
all test files under `other_methods' folder

[Repository]([https://github.com/dwavesystems/dwave-nea](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.dual_annealing.html)
<h4> Proprietary simulated annealing algorithm </h4>
all test files under `other_methods' folder


 <h2>Instructions</h2>

 ``pip install numpy matplotlib itertools neal kaiwu``
 (Note: kaiwu is not publicly available)

 then

 Go to desired test folder
 Type ``python 'testfile name``

i.e. 
``cd dwave_sa``<br>
``python simulated_annealing_100_10.py``
<br>
or
<br>
``cd kaiwu`` <br>
``python run_test_500_30_SA.py``
<br>
or
<br>
``cd other_methods``<br>
``python simulated_annealing_own_algo_100_30.py``

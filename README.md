# MaxCutTest
 Repository for various testing methods for MaxCut problem:

<h2> Overview </h2>
<h3>Test metrics</h3>
<br>
 nodes: 100
 <br>
 edge density: 10%, 30%, 50%, 70%, 90%
 <br><br>
 nodes: 500
 <br>
 edge density: 10%, 30%, 50%, 70%, 90%
<br>
<h3>Test methods</h3>
<h4>D-wave </h4>
Simulated annealing using the D-wave ``neal`` package<br>
all test files under `dwave_sa' folder

[Repository](https://github.com/dwavesystems/dwave-neal)

<br> 
<h4>Kaiwu </h4>
Kaiwu CIM- simulator and Kaiwu Simulated Annealing  <br>
all test files under `kaiwu' folder

<h4> Scipy dual anneal </h4>
all test files under `other_methods' folder<br>

[Repository](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.dual_annealing.html)
<h4> Proprietary simulated annealing algorithm </h4>
all test files under `other_methods' folder


 <h2>Instructions</h2>

 ``pip install numpy matplotlib itertools neal kaiwu`` <br>
 <em> (Note: kaiwu is not publicly available)</em>
<br>
 then
<br>
 1)Go to desired test folder <br>
 2) Type ``python *testfile_ name`` <br>
<br>
i.e. <br><br> 
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

# MaxCutTest
 Repository for various testing methods for MaxCut problem:

<h2> Overview </h2>
<h3>Test metrics</h3>
<br>
 100 nodes
 <br>
 edge density 10%, 30%, 50%, 70%, 90%
 <br>
 500 nodes
 <br>
 edge density 10%, 30%, 50%, 70%, 90%
<br>
<h3>D-wave </h3>
Simulated annealing using the D-wave ``neal`` package

[Repository](https://github.com/dwavesystems/dwave-neal)

<br> 
<h3>Kaiwu </h3>
Kaiwu CIM and Kaiwu SA  

<h3> Scipy dual anneal </h3>

<h3> Proprietary simulated annealing </h3>


 <h2>Instructions</h2>h2>

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

# MaxCutTest
 Repository for various testing methods for MaxCut problem:

<h2> Overview </h2>
<h3>Test metrics</h3>

 100 nodes
 edge density 10%, 30%, 50%, 70%, 90%
 500 nodes
 edge density 10%, 30%, 50%, 70%, 90%

<h3>Dwave </h3>
Simulated annealing using the ``neal`` package, Kaiwu CIM, Kaiwu simulated annealing, scipy- dual anneal, and proprietary simulated annealing solutions. 

[Repository](https://github.com/dwavesystems/dwave-neal) 
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
cd dwave_sa
python simulated_annealing_100_10.py

or

cd kaiwu
python run_test_500_30_SA.py

or

cd other_methods
python simulated_annealing_own_algo_100_30.py

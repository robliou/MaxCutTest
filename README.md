# MaxCutTest
 Repository for various testing methods for MaxCut problem:

<h2> Overview </h2>
<h3>Test metrics</h3>
<br>
 
 
 nodes: <b>100</b>
 <br>
 edge density: <b>10%, 30%, 50%, 70%, 90%</b>
 <br><br>
 nodes: <b>500</b>
 <br>
 edge density: <b>10%, 30%, 50%, 70%, 90%</b>
 
<br>
  
<h3>Test methods</h3>
<h4>D-wave </h4>
Simulated annealing using the D-wave <code>neal</code> package<br>
<em>all test files under `dwave_sa' folder</em> 

[Repository](https://github.com/dwavesystems/dwave-neal)

<br> 
<h4>Kaiwu </h4>
Kaiwu CIM- simulator and Kaiwu Simulated Annealing  <br>
<em>all test files under `kaiwu' folder</em> 

<h4> Scipy dual anneal </h4>
<em> all test files under `other_methods' folder</em> 

[Repository](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.dual_annealing.html)
<h4> Proprietary simulated annealing algorithm </h4>
<em> all test files under `other_methods' folder</em> 

 <h2>Instructions</h2>
<h5>Install requirements</h5>
 <code>pip install numpy matplotlib itertools neal kaiwu</code>code> <br><br>
 <em> (Note: kaiwu is not publicly available)</em>
<br><br>
 then
<br><br>
 1)Go to desired test folder <br>
 2) Type <code>python *testfile_ name</code>code> <br>
<br>
i.e. <br><br> 
<code>cd dwave_sa</code>code>br>
<code>python simulated_annealing_100_10.py</code>
<br><br>
or
<br><br>
<code>cd kaiwu</code>code> <br>
<code>python run_test_500_30_SA.py</code>code>
<br><br>
or
<br><br>
<code>cd other_methods</code>code><br>
<code>python simulated_annealing_own_algo_100_30.py</code>code>

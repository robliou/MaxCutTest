# MaxCutTest
 Repository for various testing methods for MaxCut problem:

<h2> Overview </h2>
<h3>Test metrics</h3>
 
 
 <b>nodes:</b> 100
 <br>
 <b>edge density:</b> 10%, 30%, 50%, 70%, 90%
 <br><br>
 <b>nodes:</b> 500
 <br>
 <b>edge density:</b> 10%, 30%, 50%, 70%, 90%
 
 
<h2>Test methods</h2>
<h3>D-wave </h3>
Simulated annealing using the D-wave <code>neal</code> package<br>
<em>all test files under `dwave_sa' folder</em> 
<br>
[Repository](https://github.com/dwavesystems/dwave-neal)

<h3>Kaiwu </h3>
Kaiwu CIM- simulator and Kaiwu Simulated Annealing  <br>
<em>all test files under `kaiwu' folder</em> 

<h3> Scipy dual anneal </h3>
<em> all test files under `other_methods' folder</em> 
<br>
[Repository](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.dual_annealing.html)
<h3> Proprietary simulated annealing algorithm </h3>
<em> all test files under `other_methods' folder</em> 

 <h2>Instructions</h2>
 1) <b>Clone this folder</b>
 <br><br>
 2)  <b>Install required packages </b>
 <br><br>
 <code>pip install numpy matplotlib itertools neal kaiwu</code> <br><br>
 <em> (Note: kaiwu is not publicly available)</em>
<br><br>
 3) <b>Launch test files</b>
<br>
 a) Go to desired test folder <br>
 b) Type <code>python </code> and then the test file name <br>
<br>
i.e. <br><br> 
<code>cd dwave_sa</code><br>
<code>python simulated_annealing_100_10.py</code>
<br><br>
or
<br><br>
<code>cd kaiwu</code><br>
<code>python run_test_500_30_SA.py</code>
<br><br>
or
<br><br>
<code>cd other_methods</code><br>
<code>python simulated_annealing_own_algo_100_30.py</code>

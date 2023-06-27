# MaxCutTest
 MaxCut 问题的各种测试方法的存储库 (Repository for various testing methods for MaxCut problem)

<h2> 概述 Overview </h2>
<h3>测试指标 Test metrics</h3>
 
 
 <b>顶点 nodes:</b> 100
 <br>
 <b>边缘密度 edge density:</b> 10%, 30%, 50%, 70%, 90%
 <br><br>
 <b>顶点 nodes:</b> 500
 <br>
 <b>边缘密度 edge density:</b> 10%, 30%, 50%, 70%, 90%
 
 
<h2>测试方法Test methods</h2>
<h3>D-wave </h3>
Simulated annealing using the D-wave <code>neal</code> package<br>
<em>所有测试文件在`dwave_sa' 文件夹下 all test files under `dwave_sa' folder</em> 
<br>
[Repository](https://github.com/dwavesystems/dwave-neal)

<h3>Kaiwu </h3>
Kaiwu CIM- simulator and Kaiwu Simulated Annealing  <br>
<em>所有测试文件在‘Kaiwu'文件夹下 all test files under `kaiwu' folder</em> 

<h3> Scipy dual anneal </h3>
<em> 所有测试文件在‘other_methods'文件夹下 all test files under `other_methods' folder</em> 
<br>
[Repository](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.dual_annealing.html)
<h3> Proprietary simulated annealing algorithm </h3>
<em> 所有测试文件在‘other_methods'文件夹下 all test files under `other_methods' folder</em> 

 <h2>指示Instructions</h2>
 <h4>克隆此文件夹Clone this folder</h4>
   <code>git clone</code>  

<h4>安装所需的包 Install required packages </h4>
  <code>pip install numpy matplotlib itertools neal kaiwu</code> <br><br>
 <em> (注：kaiwu不公开 Note: kaiwu is not publicly available)</em>
  <h4>启动测试文件 Launch test files</h4>
  a) 转到所需的测试文件夹 Go to desired test folder <br>
 b) 输入 <code>python </code>，然后输入测试文件名 Type <code>python </code> and then the test file name <br>
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

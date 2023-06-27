# MaxCutTest

MaxCut 问题的各种测试方法的存储库 (Repository for various testing methods for MaxCut problem)

<h2> 概述  </h2>
<h3>测试指标 Test metrics</h3>
 
 
 <b>顶点 nodes:</b> 100
 <br>
 <b>边缘密度 edge density:</b> 10%, 30%, 50%, 70%, 90%
 <br><br>
 <b>顶点 nodes:</b> 500
 <br>
 <b>边缘密度 edge density:</b> 10%, 30%, 50%, 70%, 90%
 
 
<h2>测试方法 </h2>
<h3>D-wave </h3>
Simulated annealing using the D-wave <code>neal</code> package<br>
<em>所有测试文件在`dwave_sa' 文件夹下   </em> 
<br><br>
存储库:<br>
(https://github.com/dwavesystems/dwave-neal)

<h3>Kaiwu </h3>
Kaiwu CIM- simulator and Kaiwu simulated annealing  <br>
<em>所有测试文件在‘Kaiwu'文件夹下  </em>

<h3> Scipy dual anneal 算法</h3>
<em> 所有测试文件在‘other_methods'文件夹下  </em> 
<br><br>
存储库:<br>
(https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.dual_annealing.html)
<h3> 专有 simulated annealing 算法 </h3>
 开发了一种模拟退火算法，无需使用任何算法软件包.<br> 注意，对于每个测试用例 (iterations)，必须手动设置迭代次数和冷却速率(cooldown rate).<br>
<em> 所有测试文件在‘other_methods'文件夹下  </em>

 <h2>指示 </h2>
 <h4>克隆此文件夹 Clone this folder</h4>
   <code>git clone</code>

<h4>安装所需的包 Install dependencies</h4>
  <code>pip install numpy matplotlib itertools neal kaiwu</code> <br><br>
 <em> (注：kaiwu不公开）</em>
  <h4>启动测试文件 Launch test files </h4>
  a) 转到所需的测试文件夹   <br> <br>
 b) 输入 <code>python </code>，然后输入测试文件名  <br>
<br>
比如: <br><br> 
<code>cd dwave_sa</code><br> <br>
<code>python simulated_annealing_100_10.py</code>
<br><br>
或:
<br><br>
<code>cd kaiwu</code><br> <br>
<code>python run_test_500_30_SA.py</code>
<br><br>
或:
<br><br>
<code>cd other_methods</code><br> <br>
<code>python simulated_annealing_own_algo_100_30.py</code>

Link to the problem:
(https://www.codechef.com/problems/SPC2025Q2)

Ved and Varun are both members of Shaastra’s CnL team this year. While they are equally skilled in programming, they differ in height. Ved’s height is K, and Varun’s height is P.

Both want to watch a movie in OAT from outside the gate, without entering. There are N chairs available outside OAT, each with a height represented as Ai​. These chairs can be stacked on top of each other to create a platform, allowing them to stand on it for a better view of the movie.

Tej, the OAT security officer, gives all the chairs to Varun, except for one - the tallest chair, which is given to Ved.

Now, Tej wants to know who will have a better view of the movie. If Ved has a better view, print "Ved". If Varun has a better view, print "Varun". If both have the same view, print "Equal".

* Note : A person is said to have a better view if they can get a better combined height by stacking their chairs and standing on top of them.

Input Format:
* The first line of input will contain a single integer T, denoting the number of test cases.
* Each test case consists of multiple lines of input.
* The first line of each test case contains three space-separated integers N, K and P - the number of chairs, Ved's height and Varun's height
* The next line contains N space-separated integers - A1,A2,...,AN.

Output Format:
* For each test case, output "Ved "if Ved will have a better view, "Varun "if Varun will have a better view, or "Equal" if both will have the same view.
* Each character of the strings can be printed in upper or lower case. VED, ved and vEd will all be accepted.

Constraints:
* 1≤T≤100
* 1≤N≤100
* 1≤K,P≤10^4
* 1≤Ai≤100

Sample 1:

* Input:
4
2 4 2
1 3
6 10 6
6 1 4 5 7 8
4 10 6
1 2 7 5
3 2 4
1 1 4

* Output:
Ved
Varun
Ved
Equal

Explanation:

* Test Case 1 : Varun gets all chairs except the maximum one, so he gets chair with height 1. Ved gets chair of height 3.

The combined height of Ved becomes 4+3=7, and Varun's is 2+1=3.

* Test Case 3 : Ved's combined height becomes 10+7=17, while Varun's is 6+1+2+5=14.
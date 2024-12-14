Link to the problem:
(https://www.codechef.com/problems/SPC2025)

Ved claims to be a pro at programming, but his friend Varun disagrees. To settle the debate, they decided to seek advice from their mentor. The mentor proposed a simple challenge:

Ved must write a program containing N lines of code. When the code is compiled, the compiler will indicate how many of those lines have errors, denoted as M. Based on the results:

* If errors are present in at least half of the total lines, Ved will be labeled as a NEWBIE.
* Otherwise, he will be called a PRO

After compiling Ved's code, the compiler reported errors in M lines. Determine Ved's skill category based on this evaluation.

Input Format:

* The input contains two space-separated integers N and M — the number of lines of code written by Ved and the number of lines of code containing errors, respectively.

Output Format:

* Output PRO if Ved is pro, else output NEWBIE.

* It is allowed to print each character in either case.pro,pRo,PRo will all be accepted.

Constraints:

* 1≤N≤1000
* 1≤M≤1000
* M≤N

Sample 1:

* Input: 10 6

* Output: NEWBIE

* Explanation:
There were 10 lines and Ved has errors in 6 of them. Since 6≥5, where 5 is half of 10, Ved is a newbie due to having errors in at least half the lines.

Sample 2:
* Input: 9 4

* Output: PRO

* Explanation:
Half of 9 is 4.5. Ved has errors in less than half the lines, thus he is a pro.

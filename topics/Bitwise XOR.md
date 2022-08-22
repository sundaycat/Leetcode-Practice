# Overview 

+ **XOR 定义**

                            |  A  |   B |  A XOR B  |
                            |:---:|:---:|:---------:|
                            |  0  |  0  |     0     |
                            |  0  |  1  |     1     |
                            |  1  |  0  |     1     |
                            |  1  |  1  |     0     |

+ **XOR 性质** 
    <br>
    1. Taking XOR of a number with itself returns 0. Ex: `29 ^ 29 = 0`
    2. Taking XOR of a number with 0 returns the same number. Ex: `1 ^ 0 = 1`
    3.  XOR is Associative & Commutative, which means:<br>
        + `(a ^ b) ^ c = a ^ (b ^ c)`
        + `a ^ b = b ^ a`

---
#### problem set 1

+ [268. Missing Number][1]
+ [136. Single Number][2]
+ [260. Single Number III][3]
+ [1009. Complement of Base 10 Integer][4]
+ [832. Flipping an Image][5]


[1]: https://leetcode.com/problems/missing-number/
[2]: https://leetcode.com/problems/single-number/
[3]: https://leetcode.com/problems/single-number-iii/
[4]: https://leetcode.com/problems/complement-of-base-10-integer/
[5]: https://leetcode.com/problems/flipping-an-image/
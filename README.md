# graduationCeremony
Assignment for Impact Analytics:

Solutions: 
Method 1:=> Brute Force:

1) Here we are calculating every permutation of a string based on 
starting where the student will be absent for 0 days till N days.
2) This is stored in a set and then checked accordingly for the ways to attend and in those ways to attend, we are checking if he's absent on last day that is graduation day.
3) If absent then the count is taken as number of days to miss ceremony

Method 2:=> Optimised solution

1) Here iterative approach is followed by using dynamic programming.
2) dp[i][j] = you attended i day and missed j consecutive days
3) For 0 days you cant attend or nor miss so dp[0][0] = 1, since there's only one way of doing it
4) We have taken four state for each row because either you can miss 0 day, 1 day,  2 day or 3 day.
5) Now for first day if we miss  0 consecutive days, 
we should sum all values for 0th days. 
That will be total number of ways to attend on day1.
6) that's why dp[i][0] = no ways to attend i day if you dont miss any day. It will be same as dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
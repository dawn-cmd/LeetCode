cmake_minimum_required(VERSION 3.24)
project(Leetcode)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(.idea)

add_executable(Leetcode
        .idea/.gitignore
        .idea/Leetcode.iml
        .idea/modules.xml
        .idea/vcs.xml
        .idea/workspace.xml
        "10. Regular Expression Matching.py"
        1001GridIllumination.py
        "101. Symmetric Tree.py"
        "102. Binary Tree Level Order Traversal.py"
        1020NumberofEnclaves.py
        "1021. Remove Outermost Parentheses.py"
        1034ColoringABorder.py
        1036EscapeaLargeMaze.py
        "104. Maximum Depth of Binary Tree.py"
        "105. Construct Binary Tree from Preorder and Inorder Traversal.py"
        "1073. Adding Two Negabinary Numbers.py"
        "1089. Duplicate Zeros.py"
        "11. ʢ���ˮ������.py"
        "1108. Defanging an IP Address.py"
        "114. Flatten Binary Tree to Linked List.py"
        1189MaximumNumberofBalloons.py
        1190ReverseSubstringsBetweenEachPairofParentheses.py
        "12. ����ת��������.py"
        "1206. Design Skiplist.py"
        "121. Best Time to Buy and Sell Stock.py"
        1219PathwithMaximumGold.py
        1220CountVowelsPermutation.py
        "124. Binary Tree Maximum Path Sum.py"
        "1260. Shift 2D Grid.py"
        "128. Longest Consecutive Sequence.py"
        "13. ��������ת����.py"
        "1305. ���ö����������е�����Ԫ��.py"
        1342NumberofStepstoReduceaNumbertoZero.py
        1345JumpGameIV.py
        "136. Single Number.py"
        "138. Copy List with Random Pointer.py"
        1380LuckyNumbersinaMatrix.py
        "139. Word Break.py"
        "14. Longest Common Prefix.py"
        1405LongestHappyString.py
        "141. Linked List Cycle.py"
        1414FindtheMinimumNumberofFibonacciNumbersWhoseSumIsK.py
        "142. Linked List Cycle II.py"
        1447SimplifiedFractions.py
        "146 LRU Cache.cpp"
        "146. LRU Cache.py"
        "148. Sort List.py"
        "15. 3Sum.py"
        "152. Maximum Product Subarray.py"
        "155. Min Stack.py"
        "16 3Sum Closest.cpp"
        "160. Intersection of Two Linked Lists.py"
        1609EvenOddTree.py
        "1658 Minimum Operations to Reduce X to Zero.cpp"
        "1663 Smallest String With A Given Numeric Value.cpp"
        "1664 Ways to Make a Fair Array.cpp"
        1688CountofMatchesinTournament.py
        "169. Majority Element.py"
        "1691. Maximum Height by Stacking Cuboids.py"
        "1694. Reformat Phone Number.py"
        "17. Letter Combinations of a Phone Number.py"
        "1703 Minimum Adjacent Swaps for K Consecutive Ones.cpp"
        1716CalculateMoneyinLeetcodeBank.py
        1719NumberOfWaysToReconstructATree.py
        "172. �׳˺����.py"
        1725NumberOfRectanglesThatCanFormTheLargestSquare.py
        1748SumofUniqueElements.py
        "1750 Minimum Length of String After Deleting Similar.cpp"
        "1754 Largest Merge Of Two Strings.cpp"
        "1759 Count Number of Homogenous Substrings.cpp"
        1763LongestNiceSubstring.py
        "1764 Form Array by Concatenating Subarrays of Another Array.cpp"
        "1768. Merge Strings Alternately.py"
        "1779. Find Nearest Point That Has the Same X or Y.cpp"
        "1785 Minimum Elements to Add to Form a Given Sum.cpp"
        "1790. Check if One String Swap Can Make Strings Equal.py"
        1791FindCenterofStarGraph.py
        "1796. Second Largest Digit in a String.py"
        "1799 Maximize Score After N Operations.cpp"
        "1801 Number of Orders in the Backlog.cpp"
        "1803 Count Pairs With XOR in a Range.cpp"
        "1806 Minimum Number of Operations to Reinitialize a Permutation.cpp"
        "1807 Evaluate the Bracket Pairs of a String.cpp"
        "1813 Sentence Similarity III.cpp"
        "1814 Count Nice Pairs in an Array.cpp"
        "1817 Finding the Users Active Minutes.cpp"
        "1819 Number of Different Subsequences GCDs.cpp"
        "1825 Finding MK Average.cpp"
        "1827 Minimum Operations to Make the Array Increasing.cpp"
        "1828 Queries on Number of Points Inside a Circle.cpp"
        "19. Remove Nth Node From End of List.py"
        "1945 Sum of Digits of String After Convert.cpp"
        "1971 Find if Path Exists in Graph.cpp"
        "198. House Robber.py"
        1984MinimumDifferenceBetweenHighestandLowestofKScores.py
        1994TheNumberofGoodSubsets.py
        1996TheNumberofWeakCharactersintheGame.py
        "20. Valid Parentheses.py"
        "200. Number of Islands.py"
        2000ReversePrefixofWord.py
        2006CountNumberofPairsWithAbsoluteDifferenceK.py
        "2027 Minimum Moves to Convert String.cpp"
        "2028. �ҳ�ȱʧ�Ĺ۲�����.py"
        "2032 Two Out of Three.cpp"
        "2037 Minimum Number of Moves to Seat Everyone.cpp"
        "2038. �������������ɫ����ͬ��ɾ����ǰ��ɫ.py"
        "2039. ������е�ʱ��.py"
        "2042 Check if Numbers Are Ascending in a Sentence.cpp"
        "2043. ��������ϵͳ.py"
        "2044. ͳ�ư�λ���ܵõ����ֵ���Ӽ���Ŀ.py"
        "2049. ͳ����߷ֵĽڵ���Ŀ.py"
        "2055. ����֮�������.py"
        "206. Reverse Linked List.py"
        "207. Course Schedule.py"
        "208. Implement Trie (Prefix Tree).py"
        "21. Merge Two Sorted Lists.py"
        "2100. �ʺϴ�����е�����.py"
        "2104. �����鷶Χ��.py"
        "215. Kth Largest Element in an Array.py"
        "2180 Count Integers With Even Digit Sum.cpp"
        "2185 Counting Words With a Given Prefix.cpp"
        219ContainsDuplicateII.py
        "22. Generate Parentheses.py"
        "221. Maximal Square.py"
        "226. Invert Binary Tree.py"
        "2283 Check if Number Has Equal Digit Count and Digit Value.cpp"
        "2293 Min Max Game.cpp"
        "2299 Strong Password Checker II.cpp"
        "23. Merge k Sorted Lists.py"
        "2303 Calculate Amount Paid in Taxes.cpp"
        "234. Palindrome Linked List.py"
        "2351 First Letter to Appear Twice.cpp"
        "236. Lowest Common Ancestor of a Binary Tree.py"
        "238. Product of Array Except Self.py"
        "239. Sliding Window Maximum.py"
        "24. Swap Nodes in Pairs.py"
        "240. Search a 2D Matrix II.py"
        "25 Reverse Nodes in k-Group.cpp"
        "258. ��λ���.py"
        "279. Perfect Squares.py"
        "283. Move Zeroes.py"
        "287. Find the Duplicate Number.py"
        "297. Serialize and Deserialize Binary Tree.py"
        2AddTwoNumbers.py
        "300. Longest Increasing Subsequence.py"
        "301. Remove Invalid Parentheses.py"
        306AdditiveNumber.py
        "307. ����ͼ��� - ������޸�.py"
        "309. Best Time to Buy and Sell Stock with Cooldown.py"
        "31. Next Permutation.py"
        "312. Burst Balloons.py"
        "32. Longest Valid Parentheses.py"
        "322. Coin Change.py"
        334IncreasingTripletSubsequence.py
        "337. House Robber III.py"
        "34. Find First and Last Position of Element in Sorted Array.py"
        "347. Top K Frequent Elements.py"
        "386. �ֵ�������.py"
        "39. Combination Sum.py"
        "393. UTF-8 ������֤.py"
        "394. Decode String.py"
        "396. ��ת����.py"
        "398. ���������.py"
        "399 Evaluate Division (disjoint-set).cpp"
        "399 Evaluate Division.cpp"
        3LongestSubstringWithoutRepeatingCharacters.py
        "4. Ѱ�����������������λ��.py"
        400nth-digit.cpp
        "406. Queue Reconstruction by Height.py"
        "42. Trapping Rain Water.py"
        "429. N �����Ĳ������.py"
        "433. ��С����仯.py"
        "440. �ֵ���ĵ�KС����.py"
        "442. �������ظ�������.py"
        "449. ���л��ͷ����л�����������.py"
        "46. Permutations.py"
        "462. �����ƶ�����ʹ����Ԫ����� II.py"
        "467. Unique Substrings in Wraparound String.py"
        "468. Validate IP Address.py"
        "498. Diagonal Traverse.py"
        "5. ������Ӵ�.py"
        "504. �߽�����.py"
        "513. Find Bottom Left Tree Value.py"
        "521. ��������� ��.py"
        "522. Longest Uncommon Subsequence II.py"
        "53. Maximum Subarray.py"
        539MinimumTimeDifference.py
        540SingleElementinaSortedArray.py
        "55. Jump Game.py"
        "553 Optimal Division.py"
        "56. Merge Intervals.py"
        "564. Ѱ������Ļ�����.py"
        "587. ��װդ��.py"
        "589. N ������ǰ�����.py"
        "590. N �����ĺ������.py"
        "593. Valid Square.py"
        "599. �����б����С�����ܺ�.py"
        "6. Z ���α任.py"
        "606. ���ݶ����������ַ���.py"
        "62. Unique Paths.py"
        630CourseScheduleIII.py
        "64. Minimum Path Sum.py"
        "653. ����֮�� IV - ���� BST.py"
        "661. ͼƬƽ����.py"
        "682. �������.py"
        688KnightProbabilityinChessboard.py
        "699. Falling Squares.py"
        "7. ������ת.py"
        "70. Climbing Stairs.py"
        "713. �˻�С�� K ��������.py"
        7171-bitand2-bitCharacters.py
        "719. Find K-th Smallest Pair Distance.py"
        "72. Edit Distance.py"
        "720. �ʵ�����ĵ���.py"
        "728. �Գ���.py"
        "744. Ѱ�ұ�Ŀ����ĸ�����С��ĸ.py"
        747LargestNumberAtLeastTwiceofOthers.py
        748ShortestCompletingWord.py
        "75. Sort Colors.py"
        "753 Cracking the Safe.cpp"
        "754. Reach a Number.py"
        "76. Minimum Window Substring.py"
        "762. �����Ʊ�ʾ��������������λ.py"
        "78. Subsets.py"
        "79. Word Search.py"
        "796. ��ת�ַ���.py"
        "8. �ַ���ת������ (atoi).py"
        "804. ΨһĦ��˹�����.py"
        "806. д�ַ�����Ҫ������.py"
        "812. ������������.py"
        "816. Ambiguous Coordinates.py"
        "824. ɽ��������.py"
        838PushDominoes.py
        "84. Largest Rectangle in Histogram.py"
        "86. Partition List.py"
        "868. �����Ƽ��.py"
        "883. ��ά����ͶӰ���.py"
        884UncommonWordsfromTwoSentences.py
        "904. Fruit Into Baskets.py"
        "905. ����ż��������.py"
        "908. ��С��ֵ I.py"
        917ReverseOnlyLetters.py
        "92. ��ת���� II.py"
        "929. Unique Email Addresses.py"
        "933. ������������.py"
        "94. Binary Tree Inorder Traversal.py"
        "942. �����ַ���ƥ��.py"
        "944. ɾ������.py"
        "953. ��֤������ʵ�.py"
        "96. Unique Binary Search Trees.py"
        "965. ��ֵ������.py"
        969PancakeSorting.py
        "98. Validate Binary Search Tree.py"
        tempCodeRunnerFile.py
        "��ָ Offer 51. �����е������.py"
        "������ 01.05. һ�α༭.py"
        "������ 17.11. Find Closest LCCI.py")

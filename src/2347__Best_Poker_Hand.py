from typing import List

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        """
        Given a list of card ranks and suits, returns the best possible hand.
        Possible hands are: Flush, Three of a Kind, Pair, and High Card.

        Args:
        - ranks: a list of integers representing the rank of each card.
          Each integer should be between 2 and 14 (inclusive).
        - suits: a list of strings representing the suit of each card.
          Each string should be one of "C", "D", "H", or "S" (case insensitive).

        Returns:
        A string representing the best possible hand, one of: "Flush", "Three of a Kind", "Pair", or "High Card".
        """
        # Check if all cards have the same suit (i.e., Flush)
        def is_flush():
            suit = suits[0]
            for s in suits:
                if s != suit:
                    return False
            return True

        if is_flush():
            return "Flush"

        # Sort the list of ranks in ascending order
        ranks.sort()

        # Find the maximum number of cards with the same rank
        cnt = 1
        max_cnt = 1
        for i in range(1, len(ranks)):
            if ranks[i] == ranks[i-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

        # Determine the best possible hand based on the maximum number of cards with the same rank
        if max_cnt >= 3:
            return "Three of a Kind"
        elif max_cnt == 2:
            return "Pair"
        else:
            return "High Card"

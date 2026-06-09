# ==========================================
# LC 217 - Contains Duplicate
# ==========================================
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ==========================================
# LC 121 - Best Time to Buy and Sell Stock
# ==========================================
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit
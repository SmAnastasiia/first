""" Module for return average value of numbers"""
def calculate_average(nums):
    """
    :param nums: list of numbers
    :return: average number
    """
    total = sum(nums)
    count = len(nums)
    average = total / count

    return average

numbers = [10, 15, 20]
result = calculate_average(numbers)
print("The average is:", result)

function arrayPairSum(nums: number[]): number {
  nums.sort();
  let result = 0;

  for (let i = 0; i < nums.length; i++) {
    if (i % 2 === 0) {
      result += nums[i];
    }
  }

  return result;
};

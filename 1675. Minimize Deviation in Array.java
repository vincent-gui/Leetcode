class Solution {
     public int minimumDeviation(int[] nums) {
        PriorityQueue<Integer> heap = new PriorityQueue<>((o1, o2) -> o2 - o1); // 主要这个不要加大括号
        int minium = Integer.MAX_VALUE;
        for (int num : nums){
            if(num % 2 != 0){
                num *= 2;
            }
            heap.add(num);
            minium = Math.min(minium, num);
        }

        int minDeviation = Integer.MAX_VALUE;
        while(!heap.isEmpty()){
            int curr = heap.poll();
            minDeviation = Math.min(minDeviation, curr - minium);
            if (curr % 2 == 0){
                minium = Math.min(minium, curr / 2);
                heap.add(curr / 2);
            }else{
                break;
            }

        }

        return minDeviation;
    }

   
}
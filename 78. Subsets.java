class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        if(nums.length == 0){
            return ans;
        }
        
        dfs(nums, 0, new ArrayList<Integer>(), ans);
        return ans;
    }
    
    public void dfs(int[] nums, int idx, ArrayList<Integer> tmp,  List<List<Integer>> ans){
        ans.add(new ArrayList<Integer>(tmp)); //这里需要新建一个arrayList
        for (int i = idx; i < nums.length; i++){
            tmp.add(nums[i]);
            dfs(nums, i+1, tmp, ans);
            tmp.remove(tmp.size() - 1);
        }
    }
}
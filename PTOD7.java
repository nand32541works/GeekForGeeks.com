//Please copy this code

class Solution {
    int countPairs(int arr[], int target) {
        int count = 0;
        Map<Integer,Integer> map = new HashMap<>();
        for(int i : arr){
            int complement = target-i;
            if(map.containsKey(complement)){
                count += map.get(complement);
            }
            map.put(i,map.getOrDefault(i,0)+1);
        }
        return count;
    }
}

class Solution {
    public int startStation(int[] gas, int[] cost) {
        ArrayList<Integer> available = new ArrayList<>();
        for(int k=0; k<2;k++){
            for(int i=0;i<gas.length;i++){
                available.add(gas[i]-cost[i]);
            }
        }
        int total =0, length=0;
        for(int i=0;i<available.size();i++){
            total += available.get(i);
            if(total<0){
                total = 0;
                length = 0;
            } 
            else{
                length += 1;
            }
            if(length==gas.length) {
                return i - gas.length + 1;
            }
        }
        return -1;        
    }
}

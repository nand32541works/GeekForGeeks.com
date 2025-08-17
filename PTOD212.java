class Solution {
    public void rearrange(int[] arr, int x) {
        Map<Integer,Integer> map = new HashMap<>();
        for(int i : arr){
            map.put(i,Math.abs(x-i));
        }
        List<Integer> list = new ArrayList<>();
        for(int i : arr) list.add(i);
        Collections.sort(list,(a,b)-> Integer.compare(map.get(a),map.get(b)));
        for(int i =0;i<arr.length;i++){
            arr[i] = list.get(i);
        }
    }
}

class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> a=new ArrayList<String> ();
        int t=0;
        for(int i=1;i<=n && t<target.length;i++){
            if (target[t]==i){
                t++;
                a.add("Push");
            }
            else{
                a.add("Push");
                a.add("Pop");
            }
        }return a;
    }
}

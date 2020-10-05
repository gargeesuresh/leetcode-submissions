class Solution {
    public String makeGood(String s) {
        if (isGood(s)<0)return s;
        else{
            while(isGood(s)>=0){
                if(s.length()==2){return "";}
                int k=isGood(s);
                s=s.substring(0,k)+s.substring(k+2);
            }
            return s;
        }
    }
    public int isGood(String s){
       
        for(int i=0;i<=s.length()-2;i++){
            int a=(int) s.charAt(i);
            int b=(int) s.charAt(i+1);
            if (a-32==b||b-32==a){
                return i;
            }
        }
        return -1;
    }
}

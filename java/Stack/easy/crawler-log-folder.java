class Solution {
    public int minOperations(String[] logs) {
        int c=0;
        for(String str: logs){
            if (str.charAt(1)=='/'){c+=0;}
            else if(str.charAt(1)=='.'){
                if(c==0){c+=0;}
                else{c--;}
            }
            else{
                c++;
            }
        }
    return c;
    }
}

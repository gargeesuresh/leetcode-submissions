class Solution {
    public String removeOuterParentheses(String S) {
        int sum=0;
        StringBuilder a=new StringBuilder();
        char[] s=S.toCharArray();
        for(int i=0;i<s.length;i++){
            if((s[i]=='('&&sum++>0)||(s[i]==')'&&--sum>0)){
                a.append(s[i]);
            }
        }
        return a.toString();
    }
}

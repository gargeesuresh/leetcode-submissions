class Solution {
    public String removeDuplicates(String S) {
       StringBuilder a=new StringBuilder();
        a.append(S);
        for(int i=0;i<S.length() && i!=S.length()-1;i++){
            if (a.charAt(i)==a.charAt(i+1))
            {a.deleteCharAt(i);
            a.deleteCharAt(i+1);                 
            }
        }
        if(S==a.toString()){return S;}
        return removeDuplicates(a.toString());
    }
}

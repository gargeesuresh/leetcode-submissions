class Solution {
    public boolean backspaceCompare(String S, String T) {
        return build(S).equals(build(T));
    }
    public String build(String S){
        Stack<Character> stack=new Stack<Character>();
        for(char c: S.toCharArray()){
            if(c!='#')
                stack.push(c);
            else if(!stack.empty())
                stack.pop();
        }
        return String.valueOf(stack);
        
    }




}




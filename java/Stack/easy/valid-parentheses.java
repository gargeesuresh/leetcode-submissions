class Solution {
    public boolean isValid(String s) {
        char[] S=s.toCharArray();
        Stack<Character> a=new <Character>Stack();
        for(char c:S){
            
            if(c==']'){
                if(a.isEmpty()){return false;}
                else{
                    if(a.peek()=='[')
                    {
                        a.pop();
                    }
                    else{return false;}
                }
            }
            else if(c=='}'){
                if(a.isEmpty()){return false;}
                else{
                    if(a.peek()=='{')
                    {
                        a.pop();
                    }
                    else{return false;}
                }
            }
            else if(c==')'){
                if(a.isEmpty()){return false;}
                else{
                    if(a.peek()=='(')
                    {
                        a.pop();
                    }
                    else{return false;}
                }
            }
            else{a.push(c);}
        
        
        
        }
        if(a.isEmpty()){return true;}
    return false;
    }
}

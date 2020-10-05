class Solution {

    public int calPoints(String[] ops) {
        int peek;
        Stack<Integer> s=new <Integer>Stack();
        for(String i:ops){
            if(i.equals("D")){
                s.push(s.peek()*2);
            }
            else if(i.equals("C")){
                s.pop();
            }
            else if(i.equals("+")){
                int m,l=s.pop();
                m=l; l+=s.peek();
                s.push(m);
                s.push(l);
            }
            else{
                int k=Integer.valueOf(i);
                s.push(k);
            }
        }
       int k=0;
        while(!s.isEmpty()){
            k+=s.pop();
        }
        return k;
        
    }
}

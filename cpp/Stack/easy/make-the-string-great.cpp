class Solution {
public:
    string makeGood(string s) {
        stack<char> st;
        for(auto i : s) {
            if(st.empty()) {
                st.push(i);
            } else {
                if(i >= 'A' && i <= 'Z' && st.top() >= 'a' && st.top() <= 'z' && tolower(i) == st.top()) {
                    st.pop();
                } else if(i >= 'a' && i <= 'z' && st.top() >= 'A' && st.top() <= 'Z' && tolower(st.top()) == i) {
                    st.pop();
                } else {
                    st.push(i);
                }
            }
        }
        string ans = "";
        while(!st.empty()) {
            ans += (st.top());
            st.pop();
        }
        return string(ans.rbegin(), ans.rend());
    }
};

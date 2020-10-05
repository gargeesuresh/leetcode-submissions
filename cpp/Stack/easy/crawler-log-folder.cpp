class Solution {
public:
    int minOperations(vector<string>& logs) {
        int curr = 0;
        for(auto i : logs) {
            if(i == "./") {
                // do nothing
            } else if(i[0] == '.') {
                curr--;
            } else {
                curr++;
            }
            curr = max(curr, 0);
        }
        return curr;
    }
};

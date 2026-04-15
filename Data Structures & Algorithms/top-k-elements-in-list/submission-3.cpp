class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int> mp;
        priority_queue<pair<int,int>> pq;
        vector<int> ans;
        for(int i = 0;i<nums.size();i++){
            mp[nums[i]]++;
        }

        for (auto it : mp) {
    pq.push({it.second, it.first});
}

        while(k){
            int topEle = pq.top().second;
            ans.push_back(topEle);
            pq.pop();
            k--;
        }

        return ans;
    }
};

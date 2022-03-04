vector<int> mergeSortedArrays(vector<int>& nums1, vector<int>& nums2){
    vector<int> merged;
    merged.reserve(nums1.size() + nums2.size());
    int i1 = 0, i2 = 0;
    while(i1 != nums1.size() || i2 != nums2.size()){
        // edge case
        if(i1 == nums1.size()){
            merged.push_back(nums2[i2]);
            i2++;
            continue;
        }else if (i2 == nums2.size()){
            merged.push_back(nums1[i1]);
            i1++;
            continue;
        }
        
        if(nums1[i1] < nums2[i2]){
            merged.push_back(nums1[i1]);
            i1++;
        }else{
            merged.push_back(nums2[i2]);
            i2++;
        }
    }

    return merged;
}

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> merged(mergeSortedArrays(nums1, nums2));
        int size = merged.size();
        if(size % 2 == 0){
            return (double)(merged[size/2 - 1] + merged[size/2]) / 2;
        }else{
            return merged[size/2];
        }
    }
};
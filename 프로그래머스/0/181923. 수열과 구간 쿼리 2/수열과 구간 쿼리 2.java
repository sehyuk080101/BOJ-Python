class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        
        for (int i = 0; i < queries.length; i++) {
            int least = 1000000;
            boolean tf = true;
            
            for (int j = queries[i][0]; j <= queries[i][1]; j++) {
                if (arr[j] > queries[i][2] && arr[j] < least) {
                    least = arr[j];
                    tf = false;
                }
            }
            
            if (tf) {
                least = -1;
            }
            
            answer[i] = least;
        }
        
        return answer;
    }
}
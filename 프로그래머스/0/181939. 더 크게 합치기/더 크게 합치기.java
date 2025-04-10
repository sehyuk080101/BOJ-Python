class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        if (Integer.parseInt(b + "" + a) > Integer.parseInt(a + "" + b)) {
            answer = Integer.parseInt(b + "" + a);
        } else {
            answer = Integer.parseInt(a + "" + b);
        }
        
        return answer;
    }
}
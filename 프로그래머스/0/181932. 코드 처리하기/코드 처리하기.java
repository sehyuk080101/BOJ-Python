class Solution {
    public String solution(String code) {
        int mode = 0;
        String answer = "";
        
        for (int i = 0; i < code.length(); i++) {
            if (code.charAt(i) == '1') {
                if (mode == 0) {
                    mode++;
                } else {
                    mode--;
                }
            } else {
                if (mode == 0) {
                    if (i % 2 == 0) {
                        answer += code.charAt(i);
                    }
                } else {
                    if (i % 2 == 1) {
                        answer += code.charAt(i);
                    }
                }
            }
        }
        
        if (answer == "") {
            return "EMPTY";
        }
        
        return answer;
    }
}
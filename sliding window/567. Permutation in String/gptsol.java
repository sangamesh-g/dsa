class Solution {
    public boolean checkInclusion(String patternString, String searchString) {

        // If pattern is bigger → impossible
        if (patternString.length() > searchString.length()) {
            return false;
        }

        // Frequency arrays for pattern and current window
        int[] patternFrequency = new int[26];
        int[] windowFrequency = new int[26];

        // Fill frequency for pattern
        for (int i = 0; i < patternString.length(); i++) {
            patternFrequency[patternString.charAt(i) - 'a']++;
            windowFrequency[searchString.charAt(i) - 'a']++;
        }

        // Count how many characters match initially
        int matches = 0;
        for (int i = 0; i < 26; i++) {
            if (patternFrequency[i] == windowFrequency[i]) {
                matches++;
            }
        }

        int leftPointer = 0;

        // Slide the window
        for (int rightPointer = patternString.length(); rightPointer < searchString.length(); rightPointer++) {

            // If all 26 match → valid permutation found
            if (matches == 26) {
                return true;
            }

            // Add new character to window
            int indexOfNewChar = searchString.charAt(rightPointer) - 'a';
            windowFrequency[indexOfNewChar]++;

            // Update matches after adding
            if (windowFrequency[indexOfNewChar] == patternFrequency[indexOfNewChar]) {
                matches++;
            } else if (windowFrequency[indexOfNewChar] == patternFrequency[indexOfNewChar] + 1) {
                matches--;
            }

            // Remove left character from window
            int indexOfLeftChar = searchString.charAt(leftPointer) - 'a';
            windowFrequency[indexOfLeftChar]--;

            // Update matches after removing
            if (windowFrequency[indexOfLeftChar] == patternFrequency[indexOfLeftChar]) {
                matches++;
            } else if (windowFrequency[indexOfLeftChar] == patternFrequency[indexOfLeftChar] - 1) {
                matches--;
            }

            leftPointer++;
        }

        // Final check
        return matches == 26;
    }
}
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def boundarycheck(mode, index, limit):
            if mode == 'central' and ((index-limit) < 0 or (index+limit) > (len(s)-1)):
                return False
            if mode == 'axial' and ((index-limit) < 0 or (index+limit-1) > (len(s)-1)):
                return False
            return True

        def central_symmetry(index):
            limit = 1
            while boundarycheck('central', index, limit) and s[index-limit] == s[index+limit]:
                limit += 1
            return limit - 1

        def axial_symmetry(index):
            limit = 1
            while boundarycheck('axial', index, limit) and s[index-limit] == s[index+limit-1]:
                limit += 1
            return limit - 1

        lp_substring = ''
        for index, value in enumerate(s):
            central_limit = central_symmetry(index)
            if (2*central_limit + 1) > len(lp_substring):
                lp_substring = s[index-central_limit:index+central_limit+1]

            axial_limit = axial_symmetry(index)
            if (2 * axial_limit) > len(lp_substring):
                lp_substring = s[index-axial_limit:index+axial_limit]

        return lp_substring

    def manacher(self, s: str) -> str:
        ss = '^#' + '#'.join(s) + '#$'
        p = [0] * len(ss)
        maxright = center = 0
        lp_substring = ''
        for i in range(1, len(ss)-1):
            if  i < maxright:
                p[i] = min(p[2*center - i], maxright - i)
            while ss[i - p[i] - 1] == ss[i + p[i] + 1]:
                p[i] += 1
            if i + p[i] > maxright:
                maxright = i + p[i]
                center = i
            if p[i] > len(lp_substring):
                lp_substring = ss[i - p[i]:i + p[i] + 1].replace('#', '')
        return lp_substring

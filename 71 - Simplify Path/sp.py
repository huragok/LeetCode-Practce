class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        directories = path.split('/')[1:]
        directories_out = []
        for directory in directories:
            if directory == "..": # The previous directory
                if len(directories_out) > 0:
                    directories_out.pop()
            elif directory != "." and directory != "": # Not current directory
                directories_out.append(directory)
            # print(directories_out) 
        return '/'+str.join('/', directories_out)
        
if __name__ == "__main__":
    path = "/a/./b/../../c/"
    print(Solution().simplifyPath(path))

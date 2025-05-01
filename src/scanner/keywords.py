class KeywordChecker:

    
    def __init__(self, keywords=None):
        """Initialize with a list of keywords to search for."""
        keyword_list = ["show", "me", "sus"]
        self.keywords = keyword_list
    


    def set_keywords(self, keywords):
        """Set or update the keywords to search for."""
        self.keywords = keywords
    


    def check_file(self, filepath):
        """
        Check each line of a file for the presence of keywords.
        Returns a dictionary with line numbers and matched keywords.
        """
        results = {}
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    matches = []
                    for keyword in self.keywords:
                        if keyword.lower() in line.lower():
                            matches.append(keyword)
                    
                    if matches:
                        results[line_num] = matches
            
            
            return results
        
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
    
    def check_file_count(self, filepath):
        """
        Count the total occurrences of each keyword in the file.
        Returns a dictionary with keywords and their counts.
        """
        keyword_counts = {keyword: 0 for keyword in self.keywords}
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                for line in file:
                    for keyword in self.keywords:
                        keyword_counts[keyword] += line.lower().count(keyword.lower())
            
            return keyword_counts
        
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
        



if __name__ == "__main__":
    checker = KeywordChecker()
    

    

    

    print(checker.check_file("testfile.txt"))




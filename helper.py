from html.parser import HTMLParser
from dataclasses import dataclass, field
from typing import List

@dataclass
class Parser(HTMLParser):
    start_tags:List[str] = field(default_factory=list)
    end_tags:List[str] = field(default_factory=list)
    all_data:List[str] = field(default_factory=list)
    comments:List[str] = field(default_factory=list)
    
    def __post_init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    # method to append the start tag to the list start_tags.
    def handle_starttag(self, tag, attrs):
        self.start_tags.append(tag)
        # method to append the end tag to the list end_tags.
    def handle_endtag(self, tag):
        self.end_tags.append(tag)
    # method to append the data between the tags to the list all_data.
    def handle_data(self, data):
        self.all_data.append(data)
    # method to append the comment to the list comments.
    def handle_comment(self, data):
        self.comments.append(data)
    
if __name__ == "__main__":
    start_tags = []
    end_tags = []
    all_data = []
    comments = []
    # Creating an instance of our class.
    parser = Parser()
    # Poviding the input.
    parser.feed('<html><title>Desserts</title><body><p>'
                'I am a fan of frozen yoghurt.</p><'
                '/body><!--My first webpage--></html>')
    print("start tags:", start_tags)
    print("end tags:", end_tags)
    print("data:", all_data)
    print("comments", comments)
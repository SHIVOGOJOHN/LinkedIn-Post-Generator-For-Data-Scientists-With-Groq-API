import json

def process_posts(raw_file_path, processed_file_path=r"C:\Users\A\.vscode\Neural Networks\Data\raw_post1.json"):
    enriched_posts=[]
    # Open and read the raw JSON file with UTF-8 encoding
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        print(posts)
        for post in posts:
            metadata=extract_metadata(post['text'])
            post_wit_metadata= post  | metadata
            enriched_posts.append(post_wit_metadata)
            post={'text': 'abc','engagement':345}
            metadata={'line_count':10,'language':'English','tags':['Mental health','Motivation']} 

    for epost in enriched_posts:
        print(epost)        

def extract_metadata(post):
    return{
        'line_count':10,
        'language':'English',
        'tags':['Mental health','Motivation']
    }           
        
       
if __name__ == "__main__":
    process_posts(r"C:\Users\A\Desktop\reformatted_json1.json", r"C:\Users\A\.vscode\Neural Networks\Data\raw_post1.json")

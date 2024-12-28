from summarizer import WebSummarizer

def main():
    summarizer = WebSummarizer()
    url = "https://www.chimpavision.com/"  # Replace with your URL
    summary = summarizer.summarize_website(url)
    print("Summary:", summary)

if __name__ == "__main__":
    main()
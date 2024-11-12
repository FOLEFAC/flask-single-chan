from playwright.sync_api import Playwright, sync_playwright
import time

def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        print(" i was here 0")
        page = browser.new_page()
        print("i was here 1")
        page.goto("https://youtubetranscript.com/?v=u4wV0-31oI0", timeout=120000)  # Replace with your target URL
        print("i was here 2")
        time.sleep(20)
        # Locate the element by its ID
        element = page.locator("#demo")  # Replace "element_id" with the actual ID
        print("i was here 3")

        # iframe = page.query_selector("iframe").first
        # print(iframe)
        # #iframe = page.locator("iframe[name='vidembed']")
        
        # if iframe:
        #     # Switch to the first iframe context
        #     page.wait_for_selector("iframe")
        #     page.frame_locator("iframe").locator("body").wait_for()
        #     page.frame(iframe).wait_for_load_state()

        #     # Get all text content from the first iframe
        #     text_content = page.frame(iframe).evaluate('''
        #         () => {
        #             const text = [];
        #             const nodes = document.body.childNodes;
        #             for (let i = 0; i < nodes.length; i++) {
        #                 if (nodes[i].nodeType === Node.TEXT_NODE) {
        #                     text.push(nodes[i].textContent);
        #                 }
        #             }
        #             return text.join(' ');
        #         }
        #     ''')

        # print(text_content)
        # Extract all text from the element
        all_text = element.inner_text()
        print("the text is ", all_text)
        browser.close()

if __name__ == "__main__":
    main()

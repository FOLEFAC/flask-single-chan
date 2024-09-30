import grequests
import time

time_init = time.time()
urls = [f"https://flask-single-chan.onrender.com/extract?neuralearn-{i}" for i in range(10)]#200
    
rs = (grequests.get(u) for u in urls)

responses = grequests.map(rs)
print(time.time()-time_init)

# Process the responses
for response in responses:
    if response.status_code == 200:
        data = response.json()
        print(data)
        # Process the data here
    else:
        print(f"Request failed with status code: {response.status_code}")


# async def make_request(url):
#     print("i was here ")
#     response = await asyncio.to_thread(requests.get, url)
#     print(url)
#     return response.json()

# async def main():
#     #urls = [f"http://0.0.0.0:5100/extract?neuralearn-{i}" for i in range(100)]
#     urls = [f"https://flask-single-chan.onrender.com/extract?neuralearn-{i}" for i in range(1)]#200
    
#     tasks = [make_request(url) for url in urls]

#     results = await asyncio.gather(*tasks)
#     print(results)

# if __name__ == "__main__":
#     asyncio.run(main())
import new_file
async def run():
    data = await scrape_properties(
            ["https://www.zillow.com/homedetails/1625-E-13th-St-APT-3K-Brooklyn-NY-11229/245001606_zpid/"]
        )
    print(json.dumps(data, indent=2))
if __name__ == "__main__":
    asyncio.run(run())